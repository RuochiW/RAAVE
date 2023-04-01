"""
@RW
"""

import sqlite3

from data.tables import db_path

from src import categories


def write_category(obj):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        if isinstance(obj, categories.Category):
            if obj.category_id is None:
                c.execute('''INSERT INTO raave_category (type, owner, name, visibility, description)
                             VALUES (?, ?, ?, ?, ?)''',
                          (obj.type, obj.owner, obj.name, obj.visibility, obj.description))
                category_id = c.lastrowid
                conn.commit()
                conn.close()
                return [True, category_id]
            else:
                c.execute('''UPDATE raave_category SET type=?, owner=?, name=?, visibility=?, description=?
                             WHERE category_id=?''',
                          (obj.type, obj.owner, obj.name, obj.visibility, obj.description, obj.category_id))
        elif isinstance(obj, categories.Course):
            c.execute('''INSERT OR REPLACE INTO raave_course (course_id, department, course, section, start_date, 
                                     end_date) VALUES (?, ?, ?, ?, ?, ?)''',
                      (obj.course_id, obj.department, obj.course, obj.section, obj.start_date, obj.end_date))
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
                         FROM raave_course WHERE course_id = ?''', (category_id,))
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
