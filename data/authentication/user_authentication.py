"""
@RW
"""

import sqlite3

from src.accounts import Account
from data.log.error_log import logger
from data.tables import db_path


def user_login(account_obj):
    try:
        if isinstance(account_obj, Account):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT account_id FROM raave_account WHERE username = ? AND password = ?''',
                      (account_obj.username, account_obj.password))
            result = c.fetchall()
            if result:
                account_data_id = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                bool_true.extend(account_data_id)
                return bool_true
            else:
                conn.close()
                return [False, 'Account not found.']
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]
