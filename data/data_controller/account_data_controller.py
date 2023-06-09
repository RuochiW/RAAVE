"""
Database Interaction

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
        Success case:
        A list containing the boolean value True and followed by the account ID when new account created.
        [True]
        [True, [account_id]]

        Fail case:
        A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception:
        If an error occurs during the database transaction or any other error.

    """

    # Attempt to write the account object to the database
    try:

        # Check if account_obj is an instance of the Account class
        if isinstance(account_obj, Account):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # If the account ID is not set
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

            # If the account ID is set
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

    # If any other exceptions occur
    except Exception as e:

        # Log the error
        logger.error("An error occurred: %s", str(e))

        return [False, str(e)]


def read_account(account_obj):
    """
    Reads an account object from the database.

    Args:
        account_obj:
        An instance of the Account class containing the account ID.

    Returns:
        Success case:
        A list containing the boolean value True followed by the account data.
        [True, [account_type, username, first_name, last_name, email]]

        Fail case:
        A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception:
        If an error occurs during the database transaction or any other error.

    """

    # Attempt to read the account object from the database
    try:

        # Check if account_obj is an instance of the Account class
        if isinstance(account_obj, Account):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the account data from the database
            c.execute('''SELECT account_type, username, first_name, last_name, email
                         FROM raave_account WHERE account_id = ?''', (account_obj.account_id,))

            # Get the result of the query
            result = c.fetchall()

            # Check if the query returns any results
            if result:

                # Convert the tuples in the result to lists
                account_data = [list(t) for t in result]

                # Close the database connection
                conn.close()

                # Create a list containing True followed by the list of account data
                bool_true = [True]
                bool_true.extend(account_data)

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
