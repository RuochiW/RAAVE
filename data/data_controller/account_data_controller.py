"""
@RW
"""

import sqlite3

from data.tables import db_path

from src import accounts


def write_account(account):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        if account.attributes[0] is None:
            c.execute('''INSERT INTO raave_account (type, username, password, first_name, last_name, email)
                         VALUES (?, ?, ?, ?, ?, ?)''',
                      (account.attributes[1], account.attributes[2], account.attributes[3], account.attributes[4],
                       account.attributes[5], account.attributes[6]))

            account_id = c.lastrowid
            return [True, account_id]
        else:
            c.execute('''UPDATE raave_account
                         SET type=?, username=?, password=?, first_name=?, last_name=?, email=?
                         WHERE account_id=?''',
                      (account.attributes[1], account.attributes[2], account.attributes[3], account.attributes[4],
                       account.attributes[5], account.attributes[6], account.attributes[0]))

        conn.commit()
        conn.close()

        return [True]
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
