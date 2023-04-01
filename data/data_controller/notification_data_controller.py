"""
@RW
"""

import sqlite3

from data.tables import db_path

from src import notifications
from src import events
from src import accounts


def write_notification(notification_obj):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        if isinstance(notification_obj, notifications.Notification):
            if notification_obj.notify_id is None:
                c.execute('''INSERT INTO raave_notification (event, account, notify_date, info)
                             VALUES (?, ?, ?, ?)''',
                          (notification_obj.event, notification_obj.account, notification_obj.notify_date,
                           notification_obj.info))
                conn.commit()
                notify_id = c.lastrowid
                conn.close()
                return [True, notify_id]
            else:
                c.execute('''UPDATE raave_notification SET event=?, account=?, notify_date=?, info=?
                             WHERE notify_id=?''',
                          (notification_obj.event, notification_obj.account, notification_obj.notify_date,
                           notification_obj.info, notification_obj.notify_id))
            conn.commit()
            conn.close()
            return [True]
        else:
            conn.close()
            return [False, 'Invalid object type.']
    except Exception as e:
        return [False, str(e)]


def read_notification(notification_obj):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        if isinstance(notification_obj, notifications.Notification):
            c.execute('''SELECT notify_id, event, account, notify_date, info
                                 FROM raave_notification WHERE notify_id = ?''', (notification_obj.notify_id,))
            result = c.fetchone()
            if result:
                notification_data = list(result)
                conn.close()
                return [True] + notification_data
            else:
                conn.close()
                return [False, 'Notification not found.']
        else:
            conn.close()
            return [False, 'Invalid object type.']
    except Exception as e:
        return [False, str(e)]


def read_all_notification(obj):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        if isinstance(obj, events.Event):
            c.execute('''SELECT notify_id FROM raave_notification
                             WHERE event = ?''', (obj.event_id,))
            result = c.fetchall()
            if result:
                notify_data = [item for sublist in result for item in sublist]
                conn.close()
                return [True] + notify_data
            else:
                conn.close()
                return [False, 'No notifications found.']
        elif isinstance(obj, accounts.Account):
            c.execute('''SELECT notify_id FROM raave_notification
                                         WHERE account = ?''', (obj.account_id,))
            result = c.fetchall()
            if result:
                notify_data = [item for sublist in result for item in sublist]
                conn.close()
                return [True] + notify_data
            else:
                conn.close()
                return [False, 'No notifications found.']
        else:
            conn.close()
            return [False, 'Invalid object type.']
    except Exception as e:
        return [False, str(e)]
