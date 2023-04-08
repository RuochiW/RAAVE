"""
@RW
"""

import sqlite3

from src.accounts import Account
from data.log.error_log import logger
from data.tables import db_path


def write_account(account_obj):
    try:
        if isinstance(account_obj, Account):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            if account_obj.account_id is None:
                c.execute('''INSERT INTO raave_account (account_type, username, password, first_name, last_name, email)
                             VALUES (?, ?, ?, ?, ?, ?)''',
                          (account_obj.account_type, account_obj.username, account_obj.password, account_obj.first_name,
                           account_obj.last_name, account_obj.email))
                conn.commit()
                account_id = c.lastrowid
                conn.close()
                return [True, account_id]
            else:
                c.execute('''UPDATE raave_account
                             SET account_type=?, username=?, password=?, first_name=?, last_name=?, email=?
                             WHERE account_id=?''',
                          (account_obj.account_type, account_obj.username, account_obj.password, account_obj.first_name,
                           account_obj.last_name, account_obj.email, account_obj.account_id))
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


def read_account(account_obj):
    try:
        if isinstance(account_obj, Account):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT account_type, username, first_name, last_name, email
                         FROM raave_account WHERE account_id = ?''', (account_obj.account_id,))
            result = c.fetchall()
            if result:
                account_data = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                bool_true.extend(account_data)
                return bool_true
            else:
                conn.close()
                e = 'Account not found.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]
