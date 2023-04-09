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

# Import the Category and Course class from the src.accounts module
from src.categories import Category, Course

# Import the logger object from the data.log.error_log module
from data.log.error_log import logger

# Import the db_path variable from the data.tables module
from data.tables import db_path


def write_category(obj):
    """
    Writes a category or course object to the database.

    Args:
        obj: A Category or Course object to write to the database.

    Returns:
        Success case: A list containing the boolean value True and followed by the category ID when new account created.
        [True]
        [True, [account id]]

        Fail case: A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception: If an error occurs during the database transaction.

    """

    # Attempt to write the category object to the database
    try:

        # Check if obj is an instance of the Category class
        if isinstance(obj, Category):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # If the category ID is not set
            if obj.category_id is None:

                # Execute a SQL query to insert the category object to database
                c.execute('''INSERT INTO raave_category (category_type, owner, name, visibility, description)
                             VALUES (?, ?, ?, ?, ?)''',
                          (obj.category_type, obj.owner, obj.name, obj.visibility, obj.description))

                # Commit the changes to the database
                conn.commit()

                # Get the ID of the newly-inserted record
                category_id = c.lastrowid

                # Close the database connection
                conn.close()

                return [True, category_id]

            # If the category ID is set
            else:

                # Execute a SQL query to update the account object to database
                c.execute('''UPDATE raave_category SET category_type=?, owner=?, name=?, visibility=?, description=?
                             WHERE category_id=?''',
                          (obj.category_type, obj.owner, obj.name, obj.visibility, obj.description, obj.category_id))

                # Commit the changes to the database
                conn.commit()

                # Close the database connection
                conn.close()

                return [True]

        # Check if obj is an instance of the Course class
        elif isinstance(obj, Course):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to insert or replace the course object to database
            c.execute('''INSERT OR REPLACE INTO raave_course (course_id, department, course, section, start_date, 
                         end_date) VALUES (?, ?, ?, ?, ?, ?)''',
                      (obj.course_id, obj.department, obj.course, obj.section, obj.start_date, obj.end_date))

            # Commit the changes to the database
            conn.commit()

            # Close the database connection
            conn.close()

            return [True]

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


def read_category(category_obj):
    """
    Reads a category object from the database, along with its corresponding course object.

    Args:
        category_obj: An instance of the Category class containing the category id.

    Returns:
        Success case: A list containing the boolean value True followed by the category data and its corresponding
        course data if there is one.
        [True, [category_type, owner, name, visibility, description]]
        [True, [category_type, owner, name, visibility, description, department, course, section, start_date, end_date]]

        Fail case: A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception: If an error occurs during the database transaction or any other error.

    """

    # Attempt to read the category object from the database
    try:

        # Check if obj is an instance of the Category class
        if isinstance(category_obj, Category):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the category data to database
            c.execute('''SELECT category_type, owner, name, visibility, description
                         FROM raave_category WHERE category_id = ?''', (category_obj.category_id,))

            # Get the result of the query
            result = c.fetchall()

            # Check if the query returns any results
            if result:

                # Convert the tuples in the result to lists
                category_data = [list(t) for t in result]

                # Set the ID of course
                course_id = category_data[0]

                # Create a list containing True followed by the list of category data
                bool_true = [True]
                bool_true.extend(category_data)

                # Execute a SQL query to retrieve the course data to database
                c.execute('''SELECT department, course, section, strftime('%Y-%m-%d %H:%M', start_date) AS start_date,
                             strftime('%Y-%m-%d %H:%M', end_date) AS end_date
                             FROM raave_course WHERE course_id = ?''', (course_id,))

                # Get the result of the query
                course_result = c.fetchall()

                # Check if the query returns any results
                if course_result:

                    # Convert the tuples in the result to lists
                    course_data = [list(t) for t in course_result]

                    # Close the database connection
                    conn.close()

                    # Add list of course data
                    bool_true.extend(course_data)

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
                e = 'Category not found.'
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


def read_all_category(account_obj):
    """
    Reads all categories belonging to the account from the database.

    Args:
        account_obj: An instance of the Account class containing the account ID.

    Returns:
        Success case: A list containing the boolean value True followed by the categories' data.
        [True, [category ID, name], [category ID, name], [sublist], [...]]

        Fail case: A list containing the boolean value False followed by the error message.
        [False, [error message]]

    Raises:
        Exception: If an error occurs during the database transaction.

    """

    # Attempt to read the category object from the database
    try:

        # Check if account_obj is an instance of the Account class
        if isinstance(account_obj, Account):

            # Connect to the database and create a cursor object
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            # Execute a SQL query to retrieve the categories info to database
            c.execute('''SELECT category_id, name FROM raave_category WHERE owner = ?''', (account_obj.account_id,))

            # Get the result of the query
            result = c.fetchall()

            # Check if the query returns any results
            if result:

                # Convert the tuples in the result to lists
                categories_data = [list(t) for t in result]

                # Close the database connection
                conn.close()

                # Create a list containing True followed by the list of categories info
                bool_true = [True]
                bool_true.extend(categories_data)

                return bool_true

            # If the query returns no results
            else:

                # Close the database connection
                conn.close()

                # Log the error
                e = 'No categories found for the specified account.'
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
