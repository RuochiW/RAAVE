"""
@RW
"""

import sqlite3

from src.accounts import Account
from data.log.error_log import logger
from data.tables import db_path


def read_all_user_calendar(account_obj):
    # Please use with care, I do not know exactly what is returned
    try:
        if isinstance(account_obj, Account):
            user_course_calendar = read_all_user_course_calendar(account_obj)
            user_category_calendar = read_all_user_category_calendar(account_obj)
            if user_course_calendar[0] and user_category_calendar[0]:
                user_course_calendar.pop(0)
                user_category_calendar.pop(0)
                user_calendar = user_course_calendar + user_category_calendar
                user_calendar.sort(key=lambda event: event['start_date'])
                bool_true = [True]
                return bool_true.extend(user_calendar)
            else:
                e = 'No user calendars found for the account.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]


def read_all_user_category_calendar(account_obj):
    try:
        if isinstance(account_obj, Account):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT e.event_id, e.category, e.event_type, e.name, e.start_date, e.end_date, e.visibility
                         FROM raave_event AS e
                         JOIN raave_category AS c ON e.category = c.category_id
                         WHERE c.owner = ?
                         ORDER BY e.start_date''', (account_obj.account_id,))
            result = c.fetchall()
            if result:
                user_category_calendar_data = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                return bool_true.extend(user_category_calendar_data)
            else:
                conn.close()
                e = 'No user category calendars found for the account.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]


def read_all_user_course_calendar(account_obj):
    try:
        if isinstance(account_obj, Account):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT d.deliverable_id, r.course_id, e.event_type, e.name, e.start_date, e.end_date, 
                         e.visibility, d.weight, d.time_estimate, d.time_spent
                         FROM raave_event AS e
                         JOIN raave_category AS c ON e.category = c.category_id
                         JOIN raave_course AS r ON c.category_id = r.course_id
                         JOIN raave_subscription AS s ON r.course_id = s.course
                         JOIN raave_deliverable AS d ON e.event_id = d.deliverable_id
                         WHERE s.subscriber = ? AND e.visibility = 0
                         ORDER BY e.start_date''', (account_obj.account_id,))
            result = c.fetchall()
            if result:
                user_course_calendar_data = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                return bool_true.extend(user_course_calendar_data)
            else:
                conn.close()
                e = 'No user course calendars found for the account.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]
