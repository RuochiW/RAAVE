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
            if attributes[0] is None:
                c.execute('''INSERT INTO raave_event (category, type, name, start_date, end_date, visibility)
                             VALUES (?, ?, ?, ?, ?, ?)''',
                          (attributes[1], attributes[2], attributes[3], attributes[4],
                           attributes[5], attributes[6]))

                event_id = c.lastrowid
                return [True, event_id]
            else:
                c.execute('''UPDATE raave_event SET category=?, type=?, name=?, start_date=?, end_date=?, visibility=?
                             WHERE event_id=?''',
                          (attributes[1], attributes[2], attributes[3], attributes[4],
                           attributes[5], attributes[6], attributes[0]))

        elif isinstance(obj, events.Deliverable):
            if attributes[0] is None:
                c.execute('''INSERT INTO raave_deliverable (weight, time_estimate, time_spent)
                             VALUES (?, ?, ?)''',
                          (attributes[1], attributes[2], attributes[3]))
            else:
                c.execute('''UPDATE raave_deliverable SET weight=?, time_estimate=?, time_spent=?
                             WHERE deliverable_id=?''',
                          (attributes[1], attributes[2], attributes[3], attributes[0]))

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
