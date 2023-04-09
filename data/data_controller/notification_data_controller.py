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

# Import the Event class from the src.events module
from src.events import Event

# Import the Notification class from the src.notifications module
from src.notifications import Notification


def write_notification(notification_obj):
    """
    Writes a notification object to the database.

    Args:
        notification_obj: An Notification object to write to the database.

    Returns:
        Success case: A list containing the boolean value True and followed by the notify ID when new notification
        created.
        [True]
        [True, [notify ID]]

        Fail case: A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception: If an error occurs during the database transaction or any other error.

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
        notification_obj: An Notification object to write to the database.

    Returns:
        Success case: A list containing the boolean value True followed by the notification data.
        [True, [notify_id, event, account, notify_date, info]]

        Fail case: A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception: If an error occurs during the database transaction or any other error.

    """

    try:
        if isinstance(notification_obj, Notification):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT notify_id, event, account, strftime('%Y-%m-%d %H:%M', notify_date) AS notify_date,info 
                         FROM raave_notification
                         WHERE notify_id = ?''', (notification_obj.notify_id,))
            result = c.fetchall()
            if result:
                notification_data = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                bool_true.extend(notification_data)
                return bool_true
            else:
                conn.close()
                e = 'Notification not found.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]


def read_all_notification(obj):
    try:
        if isinstance(obj, Event):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT notify_id FROM raave_notification WHERE event = ?''', (obj.event_id,))
            result = c.fetchall()
            if result:
                notify_data = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                bool_true.extend(notify_data)
                return bool_true
            else:
                conn.close()
                e = 'No notifications found for the specified event.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        elif isinstance(obj, Account):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT notify_id FROM raave_notification WHERE account = ?''', (obj.account_id,))
            result = c.fetchall()
            if result:
                notify_data = [list(t) for t in result]
                conn.close()
                bool_true = [True]
                bool_true.extend(notify_data)
                return bool_true
            else:
                conn.close()
                e = 'No notifications found for the specified account.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]
