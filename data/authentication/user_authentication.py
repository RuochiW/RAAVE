"""
@RW
"""

import sqlite3

from data.tables import db_path

from src import accounts


def login(account_obj):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        if isinstance(account_obj, accounts.Account):
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
            conn.close()
            return [False, 'Invalid object type.']
    except Exception as e:
        return [False, str(e)]
