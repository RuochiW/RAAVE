"""
@RW
"""

import sqlite3

from data.log.error_log import logger
from data.tables import db_path

from src import categories
from src import accounts


def write_subscription(account_obj, course_obj):
    try:
        if isinstance(account_obj, accounts.Account) and isinstance(course_obj, categories.Course):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("INSERT INTO raave_subscription (course, subscriber) VALUES (?, ?)",
                      (course_obj.course_id, account_obj.account_id))
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


def read_all_subscription(obj):
    try:
        if isinstance(obj, accounts.Account):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT course FROM raave_subscription WHERE subscriber = ?", (obj.account_id,))
            result = c.fetchone()
            if result:
                subscription_data = list(result)
                conn.close()
                return [True] + subscription_data
            else:
                conn.close()
                e = 'No subscribed courses found for the specified account.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        elif isinstance(obj, categories.Course):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT subscriber FROM raave_subscription WHERE subscriber = ?", (obj.course_id,))
            result = c.fetchone()
            if result:
                subscription_data = list(result)
                conn.close()
                return [True] + subscription_data
            else:
                conn.close()
                e = 'No subscriber account found for the specified course.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]


def read_all_subscribable():
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        # TODO
        c.execute("")
        result = c.fetchone()
        if result:
            # TODO
            # list of list subscribable course that user can subscribe
            """
            [[course_id, owner, name, description, department, course, section, start_date, end_date],
             [course_id, owner, name, description, department, course, section, start_date, end_date],
             [course_id, owner, name, description, department, course, section, start_date, end_date],
             [course_id, owner, name, description, department, course, section, start_date, end_date]]
            """
            subscribable_data = []
            conn.close()
            return [True] + subscribable_data
        else:
            conn.close()
            e = 'No subscribed courses found for the specified account.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]