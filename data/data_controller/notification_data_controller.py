"""
Author: Ruochi Wang
Date: April 8, 2023
Purpose: Provide a simple and consistent way to read and write database
License: MIT License
Dependencies: sqlite3

To install the required dependencies, run the following command:

pip install sqlite3

"""

import sqlite3

from data.log.error_log import logger
from data.tables import db_path
from src.accounts import Account
from src.events import Event
from src.notifications import Notification


def write_notification(notification_obj):
    try:
        if isinstance(notification_obj, Notification):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
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
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]


def read_notification(notification_obj):
    try:
        if isinstance(notification_obj, Notification):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT notify_id, event, account, strftime('%Y-%m-%d %H:%M', notify_date) AS notify_date,info 
                         FROM raave_notification
                         WHERE notify_id = ?''', (notification_obj.notify_id,))
            result = c.fetchall()
            if result:
                notification_data = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                bool_true.extend(notification_data)
                return bool_true
            else:
                conn.close()
                e = 'Notification not found.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]


def read_all_notification(obj):
    try:
        if isinstance(obj, Event):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT notify_id FROM raave_notification WHERE event = ?''', (obj.event_id,))
            result = c.fetchall()
            if result:
                notify_data = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                bool_true.extend(notify_data)
                return bool_true
            else:
                conn.close()
                e = 'No notifications found for the specified event.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        elif isinstance(obj, Account):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT notify_id FROM raave_notification WHERE account = ?''', (obj.account_id,))
            result = c.fetchall()
            if result:
                notify_data = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                bool_true.extend(notify_data)
                return bool_true
            else:
                conn.close()
                e = 'No notifications found for the specified account.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]
