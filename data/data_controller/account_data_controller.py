"""
@RW
"""

import sqlite3

from data.tables import db_path

from src import accounts


def write_account(account_obj):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        if isinstance(account_obj, accounts.Account):
            if account_obj.account_id is None:
                c.execute('''INSERT INTO raave_account (type, username, password, first_name, last_name, email)
                              VALUES (?, ?, ?, ?, ?, ?)''',
                          (account_obj.type, account_obj.username, account_obj.password, account_obj.first_name,
                           account_obj.last_name, account_obj.email))
                account_id = c.lastrowid
                conn.commit()
                conn.close()
                return [True, account_id]
            else:
                c.execute('''UPDATE raave_account
                              SET type=?, username=?, password=?, first_name=?, last_name=?, email=?
                              WHERE account_id=?''',
                          (account_obj.type, account_obj.username, account_obj.password, account_obj.first_name,
                           account_obj.last_name, account_obj.email, account_obj.account_id))
            conn.commit()
            conn.close()
            return [True]
        else:
            return [False, 'Invalid object type.']
    except Exception as e:
        return [False, str(e)]


def read_account(account_id):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('''SELECT type, username, first_name, last_name, email
                     FROM raave_account WHERE account_id = ?''', (account_id,))
        result = c.fetchone()
        if result:
            account_data = list(result)
            conn.close()
            return [True] + account_data
        else:
            conn.close()
            return [False, 'Account not found.']
    except Exception as e:
        return [False, str(e)]
