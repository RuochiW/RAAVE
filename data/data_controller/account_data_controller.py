"""
Author: Ruochi Wang
Date: April 8, 2023
Purpose: Provide a simple and consistent way to read and write database
License: MIT License
Dependencies: sqlite3

To install the required dependencies, run the following command:

pip install sqlite3

"""

# Import the sqlite3 module for working with SQLite databases
import sqlite3

# Import the Account class from the src.accounts module
from src.accounts import Account

# Import the logger object from the data.log.error_log module
from data.log.error_log import logger

# Import the db_path variable from the data.tables module
from data.tables import db_path


def write_account(account_obj):
    """
    Writes an account object to the database.

    Args:
        account_obj: An Account object to write to the database.

    Returns:
        Success case: A list containing the boolean value True followed by the account data ID when new account created.
        [True]
        [True, [account id]]

        Fail case: A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception: If an error occurs during the database transaction.

    """

    # Attempt to write the account object to the database
    try:

        # Check if account_obj is an instance of the Account class
        if isinstance(account_obj, Account):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # If the account ID is not set, insert a new record
            if account_obj.account_id is None:

                # Execute a SQL query to insert the account object to database
                c.execute('''INSERT INTO raave_account (account_type, username, password, first_name, last_name, email)
                             VALUES (?, ?, ?, ?, ?, ?)''',
                          (account_obj.account_type, account_obj.username, account_obj.password, account_obj.first_name,
                           account_obj.last_name, account_obj.email))

                # Commit the changes to the database
                conn.commit()

                # Get the ID of the newly-inserted record
                account_id = c.lastrowid

                # Close the database connection
                conn.close()

                return [True, account_id]

            # If the account ID is set, update the existing record
            else:

                # Execute a SQL query to update the account object to database
                c.execute('''UPDATE raave_account
                             SET account_type=?, username=?, password=?, first_name=?, last_name=?, email=?
                             WHERE account_id=?''',
                          (account_obj.account_type, account_obj.username, account_obj.password, account_obj.first_name,
                           account_obj.last_name, account_obj.email, account_obj.account_id))
                # Commit the changes to the database
                conn.commit()

                # Close the database connection
                conn.close()

                return [True]

        # If account_obj is not an instance of the Account class
        else:

            # Log the error
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)

            return [False, e]

    # If any other exceptions occur, log an error and return a list indicating an error occurred
    except Exception as e:

        # Log the error
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
