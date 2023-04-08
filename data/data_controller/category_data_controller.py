"""
@RW
"""

import sqlite3

from src.accounts import Account
from src.categories import Category, Course
from data.log.error_log import logger
from data.tables import db_path


def write_category(obj):
    try:
        if isinstance(obj, Category):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            if obj.category_id is None:
                c.execute('''INSERT INTO raave_category (category_type, owner, name, visibility, description)
                             VALUES (?, ?, ?, ?, ?)''',
                          (obj.category_type, obj.owner, obj.name, obj.visibility, obj.description))
                conn.commit()
                category_id = c.lastrowid
                conn.close()
                return [True, category_id]
            else:
                c.execute('''UPDATE raave_category SET category_type=?, owner=?, name=?, visibility=?, description=?
                             WHERE category_id=?''',
                          (obj.category_type, obj.owner, obj.name, obj.visibility, obj.description, obj.category_id))
        elif isinstance(obj, Course):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''INSERT OR REPLACE INTO raave_course (course_id, department, course, section, start_date, 
                         end_date) VALUES (?, ?, ?, ?, ?, ?)''',
                      (obj.course_id, obj.department, obj.course, obj.section, obj.start_date, obj.end_date))
            conn.commit()
            conn.close()
            return [True]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]


def read_category(category_obj):
    try:
        if isinstance(category_obj, Category):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT category_type, owner, name, visibility, description
                         FROM raave_category WHERE category_id = ?''', (category_obj.category_id,))
            result = c.fetchone()
            if result:
                category_data = list(result)
                course_id = category_data[0]
                c.execute('''SELECT department, course, section, start_date, end_date
                             FROM raave_course WHERE course_id = ?''', (course_id,))
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
                e = 'Category not found.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]


def read_all_category(account_obj):
    try:
        if isinstance(account_obj, Account):
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''SELECT category_id, name FROM raave_category WHERE owner = ?''', (account_obj.account_id,))
            result = c.fetchall()
            if result:
                categories_data = [list(t) for t in result]
                conn.close()
                return [True, categories_data]
            else:
                conn.close()
                e = 'No categories found for the specified account.'
                logger.error("An error occurred: %s", e)
                return [False, e]
        else:
            e = 'Invalid object type.'
            logger.error("An error occurred: %s", e)
            return [False, e]
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return [False, str(e)]
