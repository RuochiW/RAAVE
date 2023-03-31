"""
@RW
"""

import sqlite3
import os

import accounts
import categories
import events
import notifications

db_path = 'raave.db'


def create_tables():
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''CREATE TABLE raave_account
                 (account_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  type INTEGER DEFAULT 1 NOT NULL,
                  username VARCHAR UNIQUE NOT NULL,
                  password VARCHAR NOT NULL,
                  first_name VARCHAR,
                  last_name VARCHAR,
                  email VARCHAR)''')

    data = [(2, 'johndoe', '1111aaAA', 'John', 'Doe', 'john.doe@example.com'),
            (1, 'jane_smith', '2222bbBB', 'Jane', 'Smith', 'jane.smith@example.com'),
            (1, 'bob_johnson', '3333ccCC', 'Bob', 'Johnson', 'bob.johnson@example.com')]
    c.executemany(
        "INSERT INTO raave_account (type, username, password, first_name, last_name, email) VALUES (?, ?, ?, ?, ?, ?)",
        data)

    c.execute('''CREATE TABLE raave_category
                 (category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  type INTEGER,
                  owner INTEGER,
                  name VARCHAR,
                  visibility INTEGER DEFAULT 0,
                  description VARCHAR,
                  FOREIGN KEY (owner) REFERENCES raave_account (account_id))''')

    data = [(1, 1, 'CSCI375', '375 etc, etc'),
            (1, 1, 'CSCI370', '370 etc, etc'),
            (3, 0, 'Gym', 'Gym plan etc, etc')]
    c.executemany("INSERT INTO raave_category (owner, type, name, description) VALUES (?, ?, ?, ?)", data)

    c.execute('''CREATE TABLE raave_course
                 (course_id INTEGER PRIMARY KEY UNIQUE,
                  department VARCHAR,
                  course INTEGER,
                  section INTEGER,
                  start_date DATE,
                  end_date DATE,
                  FOREIGN KEY (course_id) REFERENCES raave_category (category_id))''')

    data = [(1, 'CSCI', 375, 1, '2023-09-01', '2023-12-31'),
            (2, 'CSCI', 370, 2, '2023-09-01', '2023-12-31')]
    c.executemany('''INSERT INTO raave_course (categoryID, department, course, section, start_date, end_date) 
                     VALUES (?, ?, ?, ?, ?, ?)''', data)

    c.execute('''CREATE TABLE raave_subscription
                 (course INTEGER NOT NULL,
                  subscriber INTEGER NOT NULL,
                  FOREIGN KEY (course) REFERENCES raave_course (course_id),
                  FOREIGN KEY (subscriber) REFERENCES raave_account (account_id))''')

    data = [(1, 2),
            (2, 2),
            (1, 3)]
    c.executemany("INSERT INTO raave_subscription (course, subscriber) VALUES (?, ?)", data)

    c.execute('''CREATE TABLE raave_event
                 (event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  category INTEGER,
                  type INTEGER,
                  name VARCHAR,
                  start_date DATETIME,
                  end_date DATETIME,
                  visibility INTEGER DEFAULT 0,
                  FOREIGN KEY (category) REFERENCES raave_category (category_id))''')

    data = [(1, 2, 'A1', '2023-09-15 10:30:00', '2023-09-15 12:00:00'),
            (2, 2, 'A2', '2023-10-01 13:00:00', '2023-10-01 14:30:00'),
            (3, 1, 'Gmy Time', '2023-11-01 16:00:00', '2023-11-01 17:30:00')]
    c.executemany("INSERT INTO raave_event (category, type, name, start_date, end_date) VALUES (?, ?, ?, ?, ?)", data)

    c.execute('''CREATE TABLE raave_deliverable
                 (deliverable_id INTEGER PRIMARY KEY UNIQUE,
                  weight INTEGER,
                  time_estimate TIME,
                  time_spent TIME,
                  FOREIGN KEY (deliverable_id) REFERENCES raave_event (event_id))''')

    data = [(1, 10, '00:30:00', '00:25:00'),
            (2, 5, '01:00:00', '00:55:00')]
    c.executemany("INSERT INTO raave_deliverable (eventID, weight, time_estimate, time_spent) VALUES (?, ?, ?, ?)",
                  data)

    c.execute('''CREATE TABLE raave_notification
                 (notify_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  event INTEGER,
                  account INTEGER,
                  notify_date DATETIME,
                  info VARCHAR,
                  FOREIGN KEY (event) REFERENCES raave_event (event_id),
                  FOREIGN KEY (account) REFERENCES raave_account (account_id))''')

    data = [(1, 2, '2023-09-10 09:30:00', 'A1 is near etc, etc'),
            (2, 3, '2023-09-25 15:00:00', 'A2 is near etc, etc'),
            (3, 3, '2023-11-01 15:00:00', 'Gym time soon etc, etc')]
    c.executemany("INSERT INTO raave_notification (event, account, notify_date, info) VALUES (?, ?, ?, ?)", data)

    conn.commit()
    conn.close()


def write_account(account):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        # if account.accountID is None:
        if account.attributes[0] is None:
            c.execute('''INSERT INTO raave_account (type, username, password, first_name, last_name, email) 
                         VALUES (?, ?, ?, ?, ?, ?)''',
                      (
                          account.attributes[1], account.attributes[2], account.attributes[3], account.attributes[4],
                          account.attributes[5], account.attributes[6]
                          # account.type, account.username, account.password, account.firstName, account.lastName,
                          # account.email
                      ))
            # temp
            account_id = c.lastrowid
            return [True, account_id]
        else:
            c.execute('''UPDATE raave_account 
                         SET type=?, username=?, password=?, first_name=?, last_name=?, email=? 
                         WHERE account_id=?''',
                      (
                          account.attributes[1], account.attributes[2], account.attributes[3], account.attributes[4],
                          account.attributes[5], account.attributes[6], account.attributes[0]
                          # account.type, account.username, account.password, account.firstName, account.lastName,
                          # account.email, account.accountID
                      ))

        conn.commit()
        conn.close()

        return [True]
    except Exception as e:
        return [False, str(e)]


def read_account(account_id):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute('''SELECT type, username, first_name, last_name, email
                     FROM raave_account WHERE account_id = ?''', (account_id,))
        result = c.fetchone()

        if result:
            account_data = list(result)
            conn.close()
            return [True] + account_data
        else:
            conn.close()
            return [False, 'Account not found.']

    except Exception as e:
        return [False, str(e)]


def write_category(obj):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        if isinstance(obj, categories.Category):
            # if obj.categoryID is None:
            if obj.attributes[0] is None:
                c.execute('''INSERT INTO raave_category (type, owner, name, visibility, description) 
                             VALUES (?, ?, ?, ?, ?)''',
                          (
                              obj.attributes[1], obj.attributes[2], obj.attributes[3], obj.attributes[4],
                              obj.attributes[5]
                              # obj.type, obj.owner, obj.name, obj.visibility, obj.description
                          ))
                # temp
                category_id = c.lastrowid
                return [True, category_id]
            else:
                c.execute('''UPDATE raave_category SET type=?, owner=?, name=?, visibility=?, description=? 
                             WHERE category_id=?''',
                          (
                              obj.attributes[1], obj.attributes[2], obj.attributes[3], obj.attributes[4],
                              obj.attributes[5], obj.attributes[0]
                              # obj.type, obj.owner, obj.name, obj.visibility, obj.description, obj.categoryID
                          ))
        elif isinstance(obj, categories.Course):
            # if obj.categoryID is None:
            if obj.attributes[0] is None:
                c.execute('''INSERT INTO raave_course (department, course, section, start_date, end_date) 
                             VALUES (?, ?, ?, ?, ?)''',
                          (
                              obj.attributes[1], obj.attributes[2], obj.attributes[3], obj.attributes[4],
                              obj.attributes[5]
                              # obj.department, obj.course, obj.section, obj.startDate, obj.endDate
                          ))
            else:
                c.execute('''UPDATE raave_course SET department=?, course=?, section=?, start_date=?, end_date=? 
                             WHERE course_id=?''',
                          (
                              obj.attributes[1], obj.attributes[2], obj.attributes[3], obj.attributes[4],
                              obj.attributes[5], obj.attributes[0]
                              # obj.department, obj.course, obj.section, obj.startDate, obj.endDate, obj.categoryID
                          ))
        else:
            return [False, 'Invalid object type.']

        conn.commit()
        conn.close()

        return [True]

    except Exception as e:
        return [False, str(e)]


def read_category(category_id):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute('''SELECT type, owner, name, visibility, description 
                     FROM raave_category WHERE category_id = ?''', (category_id,))
        result = c.fetchone()

        if result:

            category_data = list(result)
            c.execute('''SELECT department, course, section, start_date, end_date 
                         FROM raave_course WHERE category_id = ?''', (category_id,))
            course_result = c.fetchone()

            if course_result:
                course_data = list(course_result)
                conn.close()
                return [True] + category_data + course_data
            else:
                conn.close()
                return [True] + category_data
        else:
            conn.close()
            return [False, 'Category not found.']

    except Exception as e:
        return [False, str(e)]


def read_all_category(account_id):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute('''SELECT category_id, name FROM raave_category WHERE owner = ?''', (account_id,))
        result = c.fetchall()

        if result:
            categories_data = [item for sublist in result for item in sublist]
            conn.close()
            return [True] + categories_data
        else:
            conn.close()
            return [False, 'No categories found for the specified account.']

    except Exception as e:
        return [False, str(e)]


def write_event(obj):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        if isinstance(obj, events.Event):
            # if obj.eventID is None:
            if obj.attributes[0] is None:
                c.execute('''INSERT INTO raave_event (category, type, name, start_date, end_date, visibility)
                             VALUES (?, ?, ?, ?, ?, ?)''',
                          (
                              obj.attributes[1], obj.attributes[2], obj.attributes[3], obj.attributes[4],
                              obj.attributes[5], obj.attributes[6]
                              # obj.categoryID, obj.type, obj.name, obj.startDate, obj.endDate, obj.visibility
                          ))
                # temp
                event_id = c.lastrowid
                return [True, event_id]
            else:
                c.execute('''UPDATE raave_event SET category=?, type=?, name=?, start_date=?, end_date=?, visibility=?
                             WHERE event_id=?''',
                          (
                              obj.attributes[1], obj.attributes[2], obj.attributes[3], obj.attributes[4],
                              obj.attributes[5], obj.attributes[6], obj.attributes[0]
                              # obj.categoryID, obj.type, obj.name, obj.startDate, obj.endDate, obj.visibility,
                              # obj.eventID
                          ))

        elif isinstance(obj, events.Deliverable):
            # if obj.eventID is None:
            if obj.attributes[0] is None:
                c.execute('''INSERT INTO raave_deliverable (weight, time_estimate, time_spent) 
                             VALUES (?, ?, ?)''',
                          (
                              obj.attributes[1], obj.attributes[2], obj.attributes[3]
                              # obj.weight, obj.timeEstimate, obj.timeSpent
                          ))
            else:
                c.execute('''UPDATE raave_deliverable SET weight=?, time_estimate=?, time_spent=? 
                             WHERE deliverable_id=?''',
                          (
                              obj.attributes[1], obj.attributes[2], obj.attributes[3], obj.attributes[0]
                              # obj.weight, obj.timeEstimate, obj.timeSpent, obj.eventID
                          ))

        else:
            return [False, 'Invalid object type.']

        conn.commit()
        conn.close()

        return [True]

    except Exception as e:
        return [False, str(e)]


def read_event(event_id):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute('''SELECT category, type, name, start_date, end_date, visibility 
                     FROM raave_event WHERE event_id = ?''', (event_id,))
        result = c.fetchone()

        if result:
            event_data = list(result)
            deliverable_id = event_data[0]

            c.execute('''SELECT weight, time_estimate, time_spent 
                         FROM raave_deliverable WHERE deliverable_id = ?''', (deliverable_id,))
            deliverable_result = c.fetchone()

            if deliverable_result:
                deliverable_data = list(deliverable_result)
                conn.close()
                return [True] + event_data + deliverable_data
            else:
                conn.close()
                return [True] + event_data
        else:
            conn.close()
            return [False, 'Event not found.']

    except Exception as e:
        return [False, str(e)]


def read_all_event(category_id):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute('''SELECT event_id, name, start_date, end_date, visibility 
                     FROM raave_event WHERE category = ?''', (category_id,))
        result = c.fetchall()

        if result:
            event_data = [item for sublist in result for item in sublist]
            conn.close()
            return [True] + event_data
        else:
            conn.close()
            return [False, 'No events found for the category.']

    except Exception as e:
        return [False, str(e)]


def write_notification(notification):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # if notification.notifyID is None:
        if notification.attributes[0] is None:
            c.execute('''INSERT INTO raave_notification (event, account, notify_date, info)
                         VALUES (?, ?, ?, ?)''',
                      (
                          notification.attributes[1], notification.attributes[2], notification.attributes[3],
                          notification.attributes[4]
                          # notification.eventID, notification.accountID, notification.notifyDate, notification.info
                      ))
            # temp
            notify_id = c.lastrowid
            return [True, notify_id]
        else:
            c.execute('''UPDATE raave_notification SET event=?, account=?, notify_date=?, info=? 
                         WHERE notify_id=?''',
                      (
                          notification.attributes[1], notification.attributes[2], notification.attributes[3],
                          notification.attributes[4], notification.attributes[0]
                          # notification.eventID, notification.accountID, notification.notifyDate, notification.info,
                          # notification.notifyID
                      ))

        conn.commit()
        conn.close()

        return [True]

    except Exception as e:
        return [False, str(e)]


def read_notification(notify_id):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute('''SELECT notify_id, event, account, notify_date, info 
                     FROM raave_notification WHERE notify_id = ?''', (notify_id,))
        result = c.fetchone()

        if result:
            notification_data = list(result)
            conn.close()
            return [True] + notification_data
        else:
            conn.close()
            return [False, 'Notification not found.']

    except Exception as e:
        return [False, str(e)]


def read_all_notification(event_id):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute('''SELECT notifyI_id FROM raave_notification
                     WHERE event = ?''', (event_id,))
        result = c.fetchall()

        if result:
            notify_data = [item for sublist in result for item in sublist]
            conn.close()
            return [True] + notify_data
        else:
            conn.close()
            return [False, 'No notifications found.']

    except Exception as e:
        return [False, str(e)]
