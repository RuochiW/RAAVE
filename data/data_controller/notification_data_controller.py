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

# Import the Event class from the src.events module
from src.events import Event

# Import the Notification class from the src.notifications module
from src.notifications import Notification


def write_notification(notification_obj):
    """
    Writes a notification object to the database.

    Args:
        notification_obj:
        An Notification object to write to the database.

    Returns:
        Success case:
        A list containing the boolean value True and followed by the notify ID when new notification created.
        [True]
        [True, [notify ID]]

        Fail case:
        A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception:
        If an error occurs during the database transaction or any other error.

    """

    # Attempt to write the notification object to the database
    try:

        # Check if notification_obj is an instance of the Notification class
        if isinstance(notification_obj, Notification):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # If the notify ID is not set
            if notification_obj.notify_id is None:

                # Execute a SQL query to insert the notification object to database
                c.execute('''INSERT INTO raave_notification (event, account, notify_date, info)
                             VALUES (?, ?, ?, ?)''',
                          (notification_obj.event, notification_obj.account, notification_obj.notify_date,
                           notification_obj.info))

                # Commit the changes to the database
                conn.commit()

                # Get the ID of the newly-inserted record
                notify_id = c.lastrowid

                # Close the database connection
                conn.close()

                return [True, notify_id]

            # If the account ID is set
            else:

                # Execute a SQL query to update the notification object to database
                c.execute('''UPDATE raave_notification SET event=?, account=?, notify_date=?, info=?
                             WHERE notify_id=?''',
                          (notification_obj.event, notification_obj.account, notification_obj.notify_date,
                           notification_obj.info, notification_obj.notify_id))

            # Commit the changes to the database
            conn.commit()

            # Close the database connection
            conn.close()

            return [True]

        # If notification_obj is not an instance of the Notification class
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


def read_notification(notification_obj):
    """
    Reads a notification object from the database.

    Args:
        notification_obj:
        An instance of the Notification class containing the notify ID.

    Returns:
        Success case:
        A list containing the boolean value True followed by the notification data.
        [True, [notify_id, event, account, notify_date, info]]

        Fail case:
        A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception:
        If an error occurs during the database transaction or any other error.

    """

    # Attempt to read the notification object from the database
    try:

        # Check if notification_obj is an instance of the Notification class
        if isinstance(notification_obj, Notification):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the notification data from the database
            c.execute('''SELECT notify_id, event, account, strftime('%Y-%m-%d %H:%M', notify_date) AS notify_date,info 
                         FROM raave_notification
                         WHERE notify_id = ?''', (notification_obj.notify_id,))

            # Get the result of the query
            result = c.fetchall()

            # Check if the query returns any results
            if result:

                # Convert the tuples in the result to lists
                notification_data = [list(t) for t in result]

                # Close the database connection
                conn.close()

                # Create a list containing True followed by the list of notification data
                bool_true = [True]
                bool_true.extend(notification_data)

                return bool_true

            # If the query returns no results
            else:

                # Close the database connection
                conn.close()

                # Log the error
                e = 'Notification not found.'
                logger.error("An error occurred: %s", e)

                return [False, e]

        # If notification_obj is not an instance of the nNotification class
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


def read_all_notification(obj):
    """
    Reads all notifications belonging to the account or event from the database.

    Args:
        obj:
        An instance of the Account class containing the account ID or Event class containing the event ID.

    Returns:
        Success case:
        A list containing the boolean value True followed by the notifications' notify ID.
        [True, [notify_id1, notify_id2, ...]]

        Fail case:
        A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception:
        If an error occurs during the database transaction or any other error.

    """

    # Attempt to read the category object from the database
    try:

        # Check if obj is an instance of the Event class
        if isinstance(obj, Event):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the notifications info to database
            c.execute('''SELECT notify_id FROM raave_notification WHERE event = ?''', (obj.event_id,))

            # Get the result of the query
            result = c.fetchall()

            # Check if the query returns any results
            if result:

                # Convert the tuples in the result to lists
                notify_data = [list(t) for t in result]

                # Close the database connection
                conn.close()

                # Create a list containing True followed by the list of notifications info
                bool_true = [True]
                bool_true.extend(notify_data)

                return bool_true

            # If the query returns no results
            else:

                # Close the database connection
                conn.close()

                # Log the error
                e = 'No notifications found for the specified event.'
                logger.error("An error occurred: %s", e)

                return [False, e]

        # Check if account_obj is an instance of the Account class
        elif isinstance(obj, Account):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the notifications info to database
            c.execute('''SELECT notify_id FROM raave_notification WHERE account = ?''', (obj.account_id,))
            result = c.fetchall()

            # Check if the query returns any results
            if result:

                # Convert the tuples in the result to lists
                notify_data = [list(t) for t in result]

                # Close the database connection
                conn.close()

                # Create a list containing True followed by the list of notifications info
                bool_true = [True]
                bool_true.extend(notify_data)

                return bool_true

            # If the query returns no results
            else:

                # Close the database connection
                conn.close()

                # Log the error
                e = 'No notifications found for the specified account.'
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
