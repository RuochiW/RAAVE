"""
@RW
"""

import sqlite3

from data.log.error_log import logger
from data.tables import db_path

from src import accounts


def login(account_obj):
    try:
        if isinstance(account_obj, accounts.Account):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT account_id FROM raave_account WHERE username = ? AND password = ?''',
                      (account_obj.username, account_obj.password))
            result = c.fetchone()
            if result:
                account_id = list(result)
                conn.close()
                return [True] + account_id
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
