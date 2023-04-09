"""
Author: Ruochi Wang
Date: April 8, 2023
Purpose: Provide a simple and consistent way to read and write database
License: MIT License
Dependencies: sqlite3

To install the required dependencies, run the following command:

pip install sqlite3

"""

# Import the os module for get dir and file path
import os

# Import the sqlite3 module for working with SQLite databases
import sqlite3

# Import the clear_file function from the data.clear module
from data.clear import clear_file

# Get the directory path for the current module
dir_path = os.path.dirname(os.path.abspath(__file__))

# Define the path for the database file
db_path = os.path.join(dir_path, "../data/raave.db")


def reset_tables():
    # For testing use only
    """
    Reset database.

    Args:
        None.

    Returns:
        None.

    Raises:
        None.

    """

    # Clear database
    clear_tables()

    # Create tables in database
    create_tables()


def clear_tables():
    # For testing use only
    """
    Clear database file.

    Args:
        None.

    Returns:
        None.

    Raises:
        None.

    """

    # Clear the database file
    clear_file(db_path)


def create_tables():
    # For testing use only
    """
    Create tables in database.

    Args:
        None.

    Returns:
        None.

    Raises:
        None.

    """

    # Connect to the database and create a cursor object
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Execute a SQL query to create raave_account table in database

    c.execute('''CREATE TABLE raave_account
                 (account_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  account_type INTEGER DEFAULT 1 NOT NULL,
                  username VARCHAR UNIQUE NOT NULL,
                  password VARCHAR NOT NULL,
                  first_name VARCHAR,
                  last_name VARCHAR,
                  email VARCHAR)''')

    # Define a list of tuples that contains sample data
    data = [(2, 'johndoe', '1111aaAA', 'John', 'Doe', 'john.doe@example.com'),
            (1, 'jane_smith', '2222bbBB', 'Jane', 'Smith', 'jane.smith@example.com'),
            (1, 'bob_johnson', '3333ccCC', 'Bob', 'Johnson', 'bob.johnson@example.com')]

    # Insert the sample data into the raave_account table
    c.executemany('''INSERT INTO raave_account (account_type, username, password, first_name, last_name, email)
                     VALUES (?, ?, ?, ?, ?, ?)''', data)

    # Execute a SQL query to create raave_category table in database
    c.execute('''CREATE TABLE raave_category
                 (category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  category_type INTEGER,
                  owner INTEGER,
                  name VARCHAR,
                  visibility INTEGER DEFAULT 0,
                  description VARCHAR,
                  FOREIGN KEY (owner) REFERENCES raave_account (account_id))''')

    # Define a list of tuples that contains sample data
    data = [(1, 1, 'CSCI375', '375 etc, etc'),
            (1, 1, 'CSCI370', '370 etc, etc'),
            (1, 1, 'Gym', 'Gym etc, etc'),
            (3, 0, 'Gym', 'Gym plan etc, etc')]

    # Insert the sample data into the raave_account table
    c.executemany("INSERT INTO raave_category (owner, category_type, name, description) VALUES (?, ?, ?, ?)", data)

    # Execute a SQL query to create raave_course table in database
    c.execute('''CREATE TABLE raave_course
                 (course_id INTEGER PRIMARY KEY UNIQUE,
                  department VARCHAR,
                  course INTEGER,
                  section INTEGER,
                  start_date DATE,
                  end_date DATE,
                  FOREIGN KEY (course_id) REFERENCES raave_category (category_id))''')

    # Define a list of tuples that contains sample data
    data = [(1, 'CSCI', 375, 1, '2023-09-01', '2023-12-31'),
            (2, 'CSCI', 370, 2, '2023-09-01', '2023-12-31')]

    # Insert the sample data into the raave_account table
    c.executemany('''INSERT INTO raave_course (course_id, department, course, section, start_date, end_date)
                     VALUES (?, ?, ?, ?, ?, ?)''', data)

    # Execute a SQL query to create raave_subscription table in database
    c.execute('''CREATE TABLE raave_subscription
                 (course INTEGER NOT NULL,
                  subscriber INTEGER NOT NULL,
                  FOREIGN KEY (course) REFERENCES raave_course (course_id),
                  FOREIGN KEY (subscriber) REFERENCES raave_account (account_id))''')

    # Define a list of tuples that contains sample data
    data = [(1, 2),
            (2, 2),
            (1, 3)]

    # Insert the sample data into the raave_account table
    c.executemany("INSERT INTO raave_subscription (course, subscriber) VALUES (?, ?)", data)

    # Execute a SQL query to create raave_event table in database
    c.execute('''CREATE TABLE raave_event
                 (event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  category INTEGER,
                  event_type INTEGER,
                  name VARCHAR,
                  start_date DATETIME,
                  end_date DATETIME,
                  visibility INTEGER DEFAULT 0,
                  FOREIGN KEY (category) REFERENCES raave_category (category_id))''')

    # Define a list of tuples that contains sample data
    data = [(1, 2, 'A1', '2023-09-15 10:30:00', '2023-09-15 12:00:00'),
            (2, 2, 'A2', '2023-10-01 13:00:00', '2023-10-01 14:30:00'),
            (3, 1, 'Gmy Time', '2023-11-01 16:00:00', '2023-11-01 17:30:00')]

    # Insert the sample data into the raave_account table
    c.executemany('''INSERT INTO raave_event (category, event_type, name, start_date, end_date)
                     VALUES (?, ?, ?, ?, ?)''', data)

    # Execute a SQL query to create raave_deliverable table in database
    c.execute('''CREATE TABLE raave_deliverable
                 (deliverable_id INTEGER PRIMARY KEY UNIQUE,
                  weight INTEGER,
                  time_estimate TIME,
                  time_spent TIME,
                  FOREIGN KEY (deliverable_id) REFERENCES raave_event (event_id))''')

    # Define a list of tuples that contains sample data
    data = [(1, 10, '00:30:00', '00:25:00'),
            (2, 5, '01:00:00', '00:55:00')]

    # Insert the sample data into the raave_account table
    c.executemany(
        "INSERT INTO raave_deliverable (deliverable_id, weight, time_estimate, time_spent) VALUES (?, ?, ?, ?)",
        data)

    # Execute a SQL query to create raave_notification table in database
    c.execute('''CREATE TABLE raave_notification
                 (notify_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  event INTEGER,
                  account INTEGER,
                  notify_date DATETIME,
                  info VARCHAR,
                  FOREIGN KEY (event) REFERENCES raave_event (event_id),
                  FOREIGN KEY (account) REFERENCES raave_account (account_id))''')

    # Define a list of tuples that contains sample data
    data = [(1, 2, '2023-09-10 09:30:00', 'A1 is near etc, etc'),
            (2, 3, '2023-09-25 15:00:00', 'A2 is near etc, etc'),
            (3, 3, '2023-11-01 15:00:00', 'Gym time soon etc, etc')]

    # Insert the sample data into the raave_account table
    c.executemany("INSERT INTO raave_notification (event, account, notify_date, info) VALUES (?, ?, ?, ?)", data)

    conn.commit()
    conn.close()
