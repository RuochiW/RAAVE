"""
User Authentication

Author: Ruochi Wang

Date: April 8, 2023

Purpose: Provide a simple and consistent way to login user by username and password

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
        account_obj:
        An instance of the Account class containing the username and password.

    Returns:
        Success case:
        A list containing the boolean value True followed by the account ID.
        [True, [account_id]]

        Fail case:
        A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception:
        If an error occurs during the database transaction or any other error.

    """

    # Attempt to read the account id from the database
    try:

        # Check if account_obj is an instance of the Account class
        if isinstance(account_obj, Account):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the account ID for the given username and password
            c.execute('''SELECT account_id FROM raave_account WHERE username = ? AND password = ?''',
                      (account_obj.username, account_obj.password))

            # Get the result of the query
            result = c.fetchall()

            # Check if the query returns any results
            if result:

                # Convert the tuples in the result to lists
                account_data_id = [list(t) for t in result]

                # Close the database connection
                conn.close()

                # Create a list containing True followed by the list of account ID
                bool_true = [True]
                bool_true.extend(account_data_id)

                return bool_true

            # If the query returns no results
            else:

                # Close the database connection
                conn.close()

                # Log the error
                e = 'Account not found.'
                logger.error("An error occurred: %s", e)

                return [False, e]

        # If account_obj is not an instance of the Account class
        else:

            # Log the error
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)

            return [False, e]

    # If any other exceptions occur
    except Exception as e:

        # Log the error
        logger.error("An error occurred: %s", str(e))

        return [False, str(e)]
