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
from src.categories import Course


def write_subscription(account_obj, course_obj):
    try:
        if isinstance(account_obj, Account) and isinstance(course_obj, Course):
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
        if isinstance(obj, Account):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT course FROM raave_subscription WHERE subscriber = ?", (obj.account_id,))
            result = c.fetchall()
            if result:
                subscription_data = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                bool_true.extend(subscription_data)
                return bool_true
            else:
                conn.close()
                e = 'No subscribed courses found for the specified account.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        elif isinstance(obj, Course):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT subscriber FROM raave_subscription WHERE subscriber = ?", (obj.course_id,))
            result = c.fetchall()
            if result:
                subscription_data = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                bool_true.extend(subscription_data)
                return bool_true
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
        c.execute('''SELECT c.course_id, cat.owner, cat.name, cat.description, c.department, c.course, c.section,
                     strftime('%Y-%m-%d %H:%M', c.start_date) AS start_date,
                     strftime('%Y-%m-%d %H:%M', c.end_date) AS end_date
                     FROM raave_course AS c 
                     JOIN raave_category AS cat ON c.course_id = cat.category_id
                     WHERE cat.category_type = 1 AND cat.visibility = 0;''')
        result = c.fetchall()
        bool_true = [True]
        if result:
            subscribable_data = [list(t) for t in result]
            conn.close()
            bool_true.extend(subscribable_data)
            return bool_true
        else:
            conn.close()
            e = 'No subscribed courses found for the specified account.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]
