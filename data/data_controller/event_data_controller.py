"""
@RW
"""

import sqlite3

from data.tables import db_path

from src import events


def write_event(obj):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        attributes = dir(obj)[25]
        if isinstance(obj, events.Event):
            if obj.event_id is None:
                c.execute('''INSERT INTO raave_event (category, type, name, start_date, end_date, visibility)
                             VALUES (?, ?, ?, ?, ?, ?)''',
                          (obj.category, obj.type, obj.name, obj.start_date, obj.end_date, obj.visibility))
                conn.commit()
                conn.close()
                event_id = c.lastrowid
                return [True, event_id]
            else:
                c.execute('''UPDATE raave_event SET category=?, type=?, name=?, start_date=?, end_date=?, visibility=?
                             WHERE event_id=?''',
                          (obj.category, obj.type, obj.name, obj.start_date, obj.end_date, obj.visibility,
                           obj.event_id))
        elif isinstance(obj, events.Deliverable):
            c.execute('''INSERT OR REPLACE INTO raave_deliverable (deliverable_id, weight, time_estimate, time_spent) 
                         VALUES (?, ?, ?, ?)''',
                      (obj.deliverable_id, obj.weight, obj.time_estimate, obj.time_spent))
        else:
            return [False, 'Invalid object type.']
        conn.commit()
        conn.close()
        return [True]
    except Exception as e:
        return [False, str(e)]


def read_event(event_id):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('''SELECT category, type, name, start_date, end_date, visibility
                     FROM raave_event WHERE event_id = ?''', (event_id,))
        result = c.fetchone()
        if result:
            event_data = list(result)
            deliverable_id = event_data[0]
            c.execute('''SELECT weight, time_estimate, time_spent
                         FROM raave_deliverable WHERE deliverable_id = ?''', (deliverable_id,))
            deliverable_result = c.fetchone()
            if deliverable_result:
                deliverable_data = list(deliverable_result)
                conn.close()
                return [True] + event_data + deliverable_data
            else:
                conn.close()
                return [True] + event_data
        else:
            conn.close()
            return [False, 'Event not found.']
    except Exception as e:
        return [False, str(e)]


def read_all_event(category_id):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('''SELECT event_id, name, start_date, end_date, visibility
                     FROM raave_event WHERE category = ?''', (category_id,))
        result = c.fetchall()
        if result:
            event_data = [item for sublist in result for item in sublist]
            conn.close()
            return [True] + event_data
        else:
            conn.close()
            return [False, 'No events found for the category.']
    except Exception as e:
        return [False, str(e)]
