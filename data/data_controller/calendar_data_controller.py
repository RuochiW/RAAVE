"""
@RW
"""

import sqlite3

from src.accounts import Account
from data.log.error_log import logger
from data.tables import db_path


def read_all_user_calendar(account_obj):
    try:
        if isinstance(account_obj, Account):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            # TODO
            c.execute("")
            result = c.fetchall()
            if result:
                # TODO
                # time ordered list of list event that user have access
                """
                [[event_id, category, event_type, name, start_date, end_date, visibility, weight, time_estimate, 
                time_spent],
                 [event_id, category, event_type, name, start_date, end_date, visibility],
                 [event_id, category, event_type, name, start_date, end_date, visibility],
                 [event_id, category, event_type, name, start_date, end_date, visibility, weight, time_estimate, 
                 time_spent]]
                """
                user_calendar_data = []
                conn.close()
                return [True] + user_calendar_data
            else:
                conn.close()
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


def read_all_user_period_calendar(account_obj, start_date, end_date):
    try:
        if isinstance(account_obj, Account):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            # TODO
            c.execute("", (start_date, end_date))
            result = c.fetchall()
            if result:
                # TODO
                # time ordered list of list event that user has in the period
                """
                [[event_id, category, event_type, name, start_date, end_date, visibility, weight, time_estimate, 
                time_spent],
                 [event_id, category, event_type, name, start_date, end_date, visibility],
                 [event_id, category, event_type, name, start_date, end_date, visibility],
                 [event_id, category, event_type, name, start_date, end_date, visibility, weight, time_estimate, 
                 time_spent]]
                """
                user_calendar_data = []
                conn.close()
                return [True] + user_calendar_data
            else:
                conn.close()
                e = 'No user calendars found for the account in the period.'
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
            # TODO
            c.execute("")
            result = c.fetchall()
            if result:
                # TODO
                # list of list of list event that user have access
                """
                [[[owner, category_type, name, description],
                  [event_id, event_type, name, start_date, end_date, visibility],
                  [event_id, event_type, name, start_date, end_date, visibility],
                  [event_id, event_type, name, start_date, end_date, visibility]],
                 [[owner, category_type, name, description],
                  [event_id, event_type, name, start_date, end_date, visibility],
                  [event_id, event_type, name, start_date, end_date, visibility],
                  [event_id, event_type, name, start_date, end_date, visibility]]]
                """
                user_category_calendar_data = []
                conn.close()
                return [True] + user_category_calendar_data
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
            # TODO
            c.execute("")
            result = c.fetchall()
            if result:
                # TODO
                # list of list of list deliverable that user have access
                """
               [[[course_id, owner, name, description, department, course, section, start_date, end_date],
                  [event_id, name, start_date, end_date, visibility, weight, time_estimate, time_spent],
                  [event_id, name, start_date, end_date, visibility, weight, time_estimate, time_spent],
                  [event_id, name, start_date, end_date, visibility, weight, time_estimate, time_spent]],
                 [[course_id, owner, name, description, department, course, section, start_date, end_date],
                  [event_id, name, start_date, end_date, visibility, weight, time_estimate, time_spent],
                  [event_id, name, start_date, end_date, visibility, weight, time_estimate, time_spent],
                  [event_id, name, start_date, end_date, visibility, weight, time_estimate, time_spent]]]
                """
                user_course_calendar_data = []
                conn.close()
                return [True] + user_course_calendar_data
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
