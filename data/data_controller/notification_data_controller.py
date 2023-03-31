"""
@RW
"""

import sqlite3

from data.tables import db_path

from src import notifications


def write_notification(notification_obj):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        if isinstance(notification_obj, notifications.Notification):
            attributes = dir(notification_obj)[25]
            if attributes[0] is None:
                c.execute('''INSERT INTO raave_notification (event, account, notify_date, info)
                             VALUES (?, ?, ?, ?)''',
                          (attributes[1], attributes[2], attributes[3],
                           attributes[4]))

                notify_id = c.lastrowid
                return [True, notify_id]
            else:
                c.execute('''UPDATE raave_notification SET event=?, account=?, notify_date=?, info=?
                             WHERE notify_id=?''',
                          (attributes[1], attributes[2], attributes[3],
                           attributes[4], attributes[0]))

            conn.commit()
            conn.close()

            return [True]
        else:
            return [False, 'Invalid object type.']

    except Exception as e:
        return [False, str(e)]


def read_notification(notify_id):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute('''SELECT notify_id, event, account, notify_date, info
                     FROM raave_notification WHERE notify_id = ?''', (notify_id,))
        result = c.fetchone()

        if result:
            notification_data = list(result)
            conn.close()
            return [True] + notification_data
        else:
            conn.close()
            return [False, 'Notification not found.']

    except Exception as e:
        return [False, str(e)]


def read_all_notification(event_id):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute('''SELECT notify_id FROM raave_notification
                     WHERE event = ?''', (event_id,))
        result = c.fetchall()

        if result:
            notify_data = [item for sublist in result for item in sublist]
            conn.close()
            return [True] + notify_data
        else:
            conn.close()
            return [False, 'No notifications found.']

    except Exception as e:
        return [False, str(e)]
