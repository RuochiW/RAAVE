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

# Import the Course class from the src.categories module
from src.categories import Course


def write_subscription(account_obj, course_obj):
    """
    Writes subscription to the database.

    Args:
        account_obj: An instance of the Account class containing the account ID.
        course_obj: An instance of the Course class containing the course ID.

    Returns:
        Success case: A list containing the boolean value True.
        [True]

        Fail case: A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception: If an error occurs during the database transaction or any other error.

    """

    # Attempt to write the subscription to the database
    try:

        # Check if account_obj is an instance of the Account class and course_obj is an instance of the Course class
        if isinstance(account_obj, Account) and isinstance(course_obj, Course):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to insert or replace the subscription to database
            c.execute("INSERT OR REPLACE INTO raave_subscription (course, subscriber) VALUES (?, ?)",
                      (course_obj.course_id, account_obj.account_id))

            # Commit the changes to the database
            conn.commit()

            # Close the database connection
            conn.close()

            return [True]

        # If obj is not an instance of the Category or Course class
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


def read_all_subscription(obj):
    """
    Writes subscription to the database.

    Args:
        obj: An instance of the Account class containing the account ID or Course class containing the course ID.

    Returns:
        Success case: A list containing the boolean value True followed by the account ID or course ID.
        [True, [account_id1, account_id2, ...]]
        [True, [course_id1, course_id2, ...]]

        Fail case: A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception: If an error occurs during the database transaction or any other error.

    """

    # Attempt to read the subscription to the database
    try:

        # Check if account_obj is an instance of the Account class
        if isinstance(obj, Account):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the subscription data to database
            c.execute("SELECT course FROM raave_subscription WHERE subscriber = ?", (obj.account_id,))

            # Get the result of the query
            result = c.fetchall()

            # Check if the query returns any results
            if result:

                # Convert the tuples in the result to lists
                subscription_data = [list(t) for t in result]

                # Close the database connection
                conn.close()

                # Create a list containing True followed by the list of subscription data
                bool_true = [True]
                bool_true.extend(subscription_data)

                return bool_true

            else:

                # Close the database connection
                conn.close()

                # Log the error
                e = 'No subscribed courses found for the specified account.'
                logger.error("An error occurred: %s", e)

                return [False, e]

        # Check if course_obj is an instance of the Course class
        elif isinstance(obj, Course):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the subscription data to database
            c.execute("SELECT subscriber FROM raave_subscription WHERE subscriber = ?", (obj.course_id,))

            # Get the result of the query
            result = c.fetchall()

            # Check if the query returns any results
            if result:

                # Convert the tuples in the result to lists
                subscription_data = [list(t) for t in result]

                # Close the database connection
                conn.close()

                # Create a list containing True followed by the list of subscription data
                bool_true = [True]
                bool_true.extend(subscription_data)

                return bool_true
            else:

                # Close the database connection
                conn.close()

                # Log the error
                e = 'No subscriber account found for the specified course.'
                logger.error("An error occurred: %s", e)

                return [False, e]

        # If account_obj is not an instance of the Category or Course class
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


def read_all_subscribable():
    """
    Reads all subscribable course from the database.

    Args:
        None.

    Returns:
        Success case: A list containing the boolean value True followed by the course ID.
        [True, [course_id1, course_id2, ...]]

        Fail case: A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception: If an error occurs during the database transaction or any other error.

    """

    # Attempt to read the subscribable from the database
    try:

        # Connect to the database and create a cursor object
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # Execute a SQL query to retrieve the subscribable info to database
        c.execute('''SELECT c.course_id, cat.owner, cat.name, cat.description, c.department, c.course, c.section,
                     strftime('%Y-%m-%d %H:%M', c.start_date) AS start_date,
                     strftime('%Y-%m-%d %H:%M', c.end_date) AS end_date
                     FROM raave_course AS c 
                     JOIN raave_category AS cat ON c.course_id = cat.category_id
                     WHERE cat.category_type = 1 AND cat.visibility = 0;''')

        # Get the result of the query
        result = c.fetchall()

        # Check if the query returns any results
        if result:

            # Convert the tuples in the result to lists
            subscribable_data = [list(t) for t in result]

            # Close the database connection
            conn.close()

            # Create a list containing True followed by the list of subscribable info
            bool_true = [True]
            bool_true.extend(subscribable_data)

            return bool_true

        # If the query returns no results
        else:

            # Close the database connection
            conn.close()

            # Log the error
            e = 'No subscribed courses found for the specified account.'
            logger.error("An error occurred: %s", e)

            return [False, e]

    # If any other exceptions occur
    except Exception as e:

        # Log the error
        logger.error("An error occurred: %s", str(e))

        return [False, str(e)]
