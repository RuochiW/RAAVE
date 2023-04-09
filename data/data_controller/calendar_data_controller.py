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


def read_all_user_calendar(account_obj):
    # Please use with care, I do not know exactly what is it returned

    """
        Reads all events from a user's calendar.

        Args:
            account_obj: An instance of the Account class containing the account ID.

        Returns:
            Success case:
            A list containing the boolean value True followed by sublist of events in the user's calendar.
            [True, [event1], [event2], [sublist], [...]]

            Fail case:
            A list containing the boolean value False followed by the error message.
            [False, [error message]]

        Raises:
            Exception:
            If an error occurs during the database transaction or any other error.

        """

    # Attempt to read all events from the user's calendar
    try:

        # Check if account_obj is an instance of the Account class
        if isinstance(account_obj, Account):

            # Read all events from the user's course calendar
            user_course_calendar = read_all_user_course_calendar(account_obj)

            # Read all events from the user's category calendar
            user_category_calendar = read_all_user_category_calendar(account_obj)

            # If both calendars are found
            if user_course_calendar[0] and user_category_calendar[0]:

                # Remove the boolean value from the beginning of each calendar list
                user_course_calendar.pop(0)
                user_category_calendar.pop(0)

                # Combine the two calendars into a single list of events
                user_calendar = user_course_calendar + user_category_calendar

                # Sort the events by start date
                user_calendar.sort(key=lambda event: event['start_date'])

                # Create a list containing True followed by sublist of events
                bool_true = [True]
                bool_true.extend(user_calendar)

                return bool_true

            # If no calendars are found
            else:

                # Log the error
                e = 'No user calendars found for the account.'
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


def read_all_user_category_calendar(account_obj):
    """
    Reads all events from a user's category calendar.

    Args:
        account_obj: An instance of the Account class containing the account ID.

    Returns:
        Success case:
        A list containing the boolean value True followed by sublist of events in the user's category calendar.
        [True, [event1], [event2], [sublist], [...]]

        Fail case:
        A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception:
        If an error occurs during the database transaction or any other error.

    """

    # Attempt to read all events from the user's calendar
    try:

        # Check if account_obj is an instance of the Account class
        if isinstance(account_obj, Account):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the account data from the database
            c.execute('''SELECT e.event_id, e.category, e.event_type, e.name, 
                         strftime('%Y-%m-%d %H:%M', e.start_date) AS start_date,
                         strftime('%Y-%m-%d %H:%M', e.end_date) AS end_date, e.visibility
                         FROM raave_event AS e
                         JOIN raave_category AS c ON e.category = c.category_id
                         WHERE c.owner = ?
                         ORDER BY e.start_date''', (account_obj.account_id,))

            # Get the result of the query
            result = c.fetchall()

            # Check if the query returns any results
            if result:

                # Convert the tuples in the result to lists
                user_category_calendar_data = [list(t) for t in result]

                # Close the database connection
                conn.close()

                # Create a list containing True followed by the list of account data
                bool_true = [True]
                bool_true.extend(user_category_calendar_data)

                return bool_true

            # If the query returns no results
            else:

                # Close the database connection
                conn.close()

                # Log the error
                e = 'No user category calendars found for the account.'
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


def read_all_user_course_calendar(account_obj):
    """
        Reads all events from a user's course calendar.

        Args:
            account_obj:
            An instance of the Account class containing the account ID.

        Returns:
            Success case:
            A list containing the boolean value True followed by sublist of deliverables in the user's course calendar.
            [True, [deliverable1], [deliverable1], [sublist], [...]]

            Fail case:
            A list containing the boolean value False followed by the error message.
            [False, [error message]]

        Raises:
            Exception: If an error occurs during the database transaction or any other error.

        """

    # Attempt to read all events from the user's calendar
    try:

        # Check if account_obj is an instance of the Account class
        if isinstance(account_obj, Account):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the account data from the database
            c.execute('''SELECT d.deliverable_id, r.course_id, e.event_type, e.name,
                         strftime('%Y-%m-%d %H:%M', e.start_date) AS start_date,
                         strftime('%Y-%m-%d %H:%M', e.end_date) AS end_date, 
                         e.visibility, d.weight, d.time_estimate, d.time_spent
                         FROM raave_event AS e
                         JOIN raave_category AS c ON e.category = c.category_id
                         JOIN raave_course AS r ON c.category_id = r.course_id
                         JOIN raave_subscription AS s ON r.course_id = s.course
                         JOIN raave_deliverable AS d ON e.event_id = d.deliverable_id
                         WHERE s.subscriber = ? AND e.visibility = 0
                         ORDER BY e.start_date''', (account_obj.account_id,))

            # Get the result of the query
            result = c.fetchall()

            # Check if the query returns any results
            if result:

                # Convert the tuples in the result to lists
                user_course_calendar_data = [list(t) for t in result]

                # Close the database connection
                conn.close()

                # Create a list containing True followed by the list of account data
                bool_true = [True]
                bool_true.extend(user_course_calendar_data)

                return bool_true

            # If the query returns no results
            else:

                # Close the database connection
                conn.close()

                # Log the error
                e = 'No user course calendars found for the account.'
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
