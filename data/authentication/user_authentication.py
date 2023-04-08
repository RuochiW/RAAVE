"""
Author: Ruochi Wang
Date: April 8, 2023
Purpose: A script that logging the error
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


def user_login(account_obj):
    """
    Login the user with the given account object.

    Args:
        account_obj (Account): An instance of the Account class containing the username and password.

    Returns:
        Success case: A list containing the boolean value True followed by the account data ID.
        [True, [account id]]

        Fail case: A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        None

    """

    try:

        # Check if account_obj is an instance of the Account class
        if isinstance(account_obj, Account):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the account ID for the given username and password
            c.execute('''SELECT account_id FROM raave_account WHERE username = ? AND password = ?''',
                      (account_obj.username, account_obj.password))

            # Fetch the results of the query
            result = c.fetchall()

            # If the query returns any results, create a list of account IDs and return it
            if result:

                # Create a list of account IDs from the results of the SQL query
                account_data_id = [list(t) for t in result]

                # Close the database connection
                conn.close()

                # Create a list containing True followed by the list of account IDs and return it
                bool_true = [True]
                bool_true.extend(account_data_id)

                return bool_true
            else:
                # If the query returns no results, return a list indicating that the account was not found

                # Close the database connection
                conn.close()

                return [False, 'Account not found.']
        else:
            # If account_obj is not an instance of the Account class
            # Log the error and return a list indicating an error occurred

            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)

            return [False, e]
    except Exception as e:
        # If any other exceptions occur, log an error and return a list indicating an error occurred

        logger.error("An error occurred: %s", str(e))

        return [False, str(e)]
