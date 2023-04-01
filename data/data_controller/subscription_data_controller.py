"""
@RW
"""

import sqlite3

from data.tables import db_path

from src import categories
from src import accounts


def write_subscription(account_obj, course_obj):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        if isinstance(account_obj, accounts.Account) and isinstance(course_obj, categories.Course):
            c.execute("INSERT INTO raave_subscription (course, subscriber) VALUES (?, ?)",
                      (course_obj.course_id, account_obj.account_id))
        else:
            conn.close()
            return [False, 'Invalid object category_type.']
        conn.commit()
        conn.close()
        return [True]
    except Exception as e:
        return [False, str(e)]


def read_all_subscription(obj):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        if isinstance(obj, accounts.Account):
            c.execute("SELECT course FROM raave_subscription WHERE subscriber = ?", (obj.account_id,))
            result = c.fetchone()
            if result:
                subscription_data = list(result)
                conn.close()
                return [True] + subscription_data
            else:
                conn.close()
                return [False, 'No subscribed courses found.']
        elif isinstance(obj, categories.Course):
            c.execute("SELECT subscriber FROM raave_subscription WHERE subscriber = ?", (obj.course_id,))
            result = c.fetchone()
            if result:
                subscription_data = list(result)
                conn.close()
                return [True] + subscription_data
            else:
                conn.close()
                return [False, 'No subscriber found.']
        else:
            conn.close()
            return [False, 'Invalid object category_type.']
    except Exception as e:
        return [False, str(e)]
