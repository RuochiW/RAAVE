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

# Import the Category and Course class from the src.categories module
from src.categories import Category, Course

# Import the Event and Deliverable class from the src.events module
from src.events import Event, Deliverable

# Import the logger object from the data.log.error_log module
from data.log.error_log import logger

# Import the db_path variable from the data.tables module
from data.tables import db_path


def write_event(obj):
    """

    Writes an event or deliverable object to the database.

    Args:
        obj: A Event and Deliverable object to write to the database.

    Returns:
        Success case:
        A list containing the boolean value True and followed by the event ID when new event created.
        [True]
        [True, [event ID]]

        Fail case:
        A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception:
        If an error occurs during the database transaction.

    """

    # Attempt to write the event or deliverable object to the database
    try:

        # Check if obj is an instance of the Event class
        if isinstance(obj, Event):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # If the event ID is not set
            if obj.event_id is None:

                # Execute a SQL query to insert the event object to database
                c.execute('''INSERT INTO raave_event (category,event_type, name, start_date, end_date, visibility)
                             VALUES (?, ?, ?, ?, ?, ?)''',
                          (obj.category, obj.event_type, obj.name, obj.start_date, obj.end_date, obj.visibility))

                # Commit the changes to the database
                conn.commit()

                # Get the ID of the newly-inserted record
                event_id = c.lastrowid

                # Close the database connection
                conn.close()

                return [True, event_id]

            # If the event ID is set
            else:

                # Execute a SQL query to update the account object to database
                c.execute('''UPDATE raave_event SET category=?, event_type=?, name=?, start_date=?, end_date=?,
                             visibility=? WHERE event_id=?''',
                          (obj.category, obj.event_type, obj.name, obj.start_date, obj.end_date, obj.visibility,
                           obj.event_id))

                # Commit the changes to the database
                conn.commit()

                # Close the database connection
                conn.close()

                return [True]

        # Check if obj is an instance of the Course class
        elif isinstance(obj, Deliverable):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to insert or replace the deliverable object to database
            c.execute('''INSERT OR REPLACE INTO raave_deliverable (deliverable_id, weight, time_estimate, time_spent) 
                         VALUES (?, ?, ?, ?)''',
                      (obj.deliverable_id, obj.weight, obj.time_estimate, obj.time_spent))

            # Commit the changes to the database
            conn.commit()

            # Close the database connection
            conn.close()

            return [True]

        # If obj is not an instance of the Event and Deliverable class
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


def read_event(event_obj):
    """
    Reads a category object from the database, along with its corresponding course object.

    Args:
        event_obj:
        An instance of the Event class containing the event ID.

    Returns:
        Success case:
        A list containing the boolean value True followed by the event data and its corresponding deliverable data if
        there is one.
        [True, [category, event_type, name, start_date, end_date, visibility]]
        [True, [category, event_type, name, start_date, end_date, visibility, weight, time_estimate, time_spent]]

        Fail case:
        A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception:
        If an error occurs during the database transaction or any other error.

    """

    # Attempt to read the event or deliverable object to the database
    try:

        # Check if obj is an instance of the Event class
        if isinstance(event_obj, Event):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the event data to database
            c.execute('''SELECT category, event_type, name, strftime('%Y-%m-%d %H:%M', start_date) AS start_date,
                         strftime('%Y-%m-%d %H:%M', end_date) AS end_date, visibility
                         FROM raave_event WHERE event_id = ?''', (event_obj.event_id,))

            # Get the result of the query
            result = c.fetchall()

            # Check if the query returns any results
            if result:

                # Convert the tuples in the result to lists
                event_data = [list(t) for t in result]

                # Set the ID of deliverable
                deliverable_id = event_data[0]

                # Create a list containing True followed by the list of event data
                bool_true = [True]
                bool_true.extend(event_data)

                # Execute a SQL query to retrieve the course data to database
                c.execute('''SELECT weight, time_estimate, time_spent FROM raave_deliverable
                             WHERE deliverable_id = ?''', (deliverable_id,))

                # Get the result of the query
                deliverable_result = c.fetchall()

                # Check if the query returns any results
                if deliverable_result:

                    # Convert the tuples in the result to lists
                    deliverable_data = [list(t) for t in deliverable_result]

                    # Close the database connection
                    conn.close()

                    # Add list of course data
                    bool_true.extend(deliverable_data)

                    return bool_true

                # If the query returns no results
                else:

                    # Close the database connection
                    conn.close()

                    return bool_true

            # If the query returns no results
            else:

                # Close the database connection
                conn.close()

                # Log the error
                e = 'Event not found.'
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


def read_all_event(category_obj):
    """
    Reads all categories belonging to the account from the database.

    Args:
        category_obj:
        An instance of the Category class containing the category ID.

    Returns:
        Success case:
        A list containing the boolean value True followed by the categories' data.
        [True, [event_id, name, start_date, end_date, visibility], [event2], [sublist], [...]]

        Fail case:
        A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception:
        If an error occurs during the database transaction or any other error.

    """

    # Attempt to read the event object from the database
    try:

        # Check if account_obj is an instance of the Category class
        if isinstance(category_obj, Category):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the events info to database
            c.execute('''SELECT event_id, name, strftime('%Y-%m-%d %H:%M', start_date) AS start_date,
                         strftime('%Y-%m-%d %H:%M', end_date) AS end_date, visibility
                         FROM raave_event WHERE category = ?''', (category_obj.category_id,))

            # Get the result of the query
            result = c.fetchall()

            # Check if the query returns any results
            if result:

                # Convert the tuples in the result to lists
                event_data = [list(t) for t in result]

                # Close the database connection
                conn.close()

                # Create a list containing True followed by the list of events info
                bool_true = [True]
                bool_true.extend(event_data)

                return bool_true

            # If the query returns no results
            else:

                # Close the database connection
                conn.close()

                # Log the error
                e = 'No events found for the category.'
                logger.error("An error occurred: %s", e)

                return [False, e]

        # If category_obj is not an instance of the Category class
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
