"""
Author: Ruochi Wang
Date: April 8, 2023
Purpose: A script that logging the error
License: MIT License
Dependencies: sqlite3

To install the required dependencies, run the following command:

pip install sqlite3

"""

import sqlite3

from data.log.error_log import logger
from data.tables import db_path
from src.categories import Category
from src.events import Event, Deliverable


def write_event(obj):
    try:
        if isinstance(obj, Event):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            if obj.event_id is None:
                c.execute('''INSERT INTO raave_event (category,event_type, name, start_date, end_date, visibility)
                             VALUES (?, ?, ?, ?, ?, ?)''',
                          (obj.category, obj.event_type, obj.name, obj.start_date, obj.end_date, obj.visibility))
                conn.commit()
                event_id = c.lastrowid
                conn.close()
                return [True, event_id]
            else:
                c.execute('''UPDATE raave_event SET category=?, event_type=?, name=?, start_date=?, end_date=?,
                             visibility=? WHERE event_id=?''',
                          (obj.category, obj.event_type, obj.name, obj.start_date, obj.end_date, obj.visibility,
                           obj.event_id))
        elif isinstance(obj, Deliverable):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''INSERT OR REPLACE INTO raave_deliverable (deliverable_id, weight, time_estimate, time_spent) 
                         VALUES (?, ?, ?, ?)''',
                      (obj.deliverable_id, obj.weight, obj.time_estimate, obj.time_spent))
            conn.commit()
            conn.close()
            return [True]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]


def read_event(event_obj):
    try:
        if isinstance(event_obj, Event):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT category, event_type, name, strftime('%Y-%m-%d %H:%M', start_date) AS start_date,
                         strftime('%Y-%m-%d %H:%M', end_date) AS end_date, visibility
                         FROM raave_event WHERE event_id = ?''', (event_obj.event_id,))
            result = c.fetchall()
            if result:
                event_data = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                deliverable_id = event_data[0]
                c.execute('''SELECT weight, time_estimate, time_spent FROM raave_deliverable
                             WHERE deliverable_id = ?''', (deliverable_id,))
                deliverable_result = c.fetchall()
                if deliverable_result:
                    deliverable_data = [list(t) for t in deliverable_result]
                    conn.close()
                    bool_true.extend(event_data)
                    bool_true.extend(deliverable_data)
                    return bool_true
                else:
                    conn.close()
                    bool_true.extend(event_data)
                    return bool_true
            else:
                conn.close()
                e = 'Event not found.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]


def read_all_event(category_obj):
    try:
        if isinstance(category_obj, Category):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT event_id, name, strftime('%Y-%m-%d %H:%M', start_date) AS start_date,
                         strftime('%Y-%m-%d %H:%M', end_date) AS end_date, visibility
                         FROM raave_event WHERE category = ?''', (category_obj.category_id,))
            result = c.fetchall()
            if result:
                event_data = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                bool_true.extend(event_data)
                return bool_true
            else:
                conn.close()
                e = 'No events found for the category.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]
