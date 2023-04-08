# Author: Anandita Gupta
# Contents: Category and Category controller class

"""
@Reference: Ethan
@Editor: RW
"""


# from category_data_controller import *


class Category:
    """The category class contains a layout of the information pertaining to a category.
    """

    category_id = int()
    category_type = int()
    visibility = int()
    name = str()
    description = str()
    owner = str()

    def __init__(self, category_id=None, category_type=None, owner=None, name=None, visibility=None, description=None):
        self.set_category_id(category_id)
        self.set_category_type(category_type)
        self.set_owner(owner)
        self.set_name(name)
        self.set_visibility(visibility)
        self.set_description(description)

    def __str__(self):
        """Formatted output for the Category object, it will print each attribute line by line."""
        return "category_id: {self.category_id},\n category_type: {self.category_type},\n visibility: {" \
               "self.visibility},\n name: {self.name}, description: {self.description},\n owner: {self.owner}"

    def get_category_id(self):
        return self.category_id

    # Likely will only be used for testing purposes
    def set_category_id(self, category_id):
        if not isinstance(category_id, type(Category.category_id)) and category_id is not None:
            print("Error: category_id must be of type {}.\n".format(type(Category.category_id)))
        else:
            self.category_id = category_id

    def get_category_type(self):
        return self.category_type

    def set_category_type(self, category_type):
        if not isinstance(category_type, type(Category.category_type)) and category_type is not None:
            print("Error: category_type must be of type {}.\n".format(type(Category.category_type)))
        else:
            self.category_type = category_type

    def get_visibility(self):
        return self.visibility

    def set_visibility(self, visibility):
        if not isinstance(visibility, type(Category.visibility)) and visibility is not None:
            print("Error: visibility must be of type {}\n".format(type(Category.visibility)))
        else:
            self.visibility = visibility

    def get_name(self):
        return self.name

    def set_name(self, name):
        if not isinstance(name, type(Category.name)) and name is not None:
            print("Error: name must be of type {}.\n".format(type(Category.name)))
        else:
            self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        if not isinstance(description, type(Category.description)) and description is not None:
            print("Error: description must be of type {}.\n".format(type(Category.description)))
        else:
            self.description = description

    def get_owner(self):
        return self.owner

    def set_owner(self, owner):
        if not isinstance(owner, type(Category.owner)) and owner is not None:
            print("Error: owner must be of type {}.\n".format(type(Category.owner)))
        else:
            self.owner = owner

    def get_all_category(self):
        attributes = list()
        for i in dir(self):
            if not i.startswith('__') and not i.startswith('get') and not i.startswith('set'):
                attributes.append(i)

        return attributes  # in alphabetical order


class Course:
    course_id = int()
    course = int()
    department = str()
    start_date = str()
    end_date = str()
    section = int()

    def __init__(self, course_id=None, course=None, start_date=None, end_date=None, department=None, section=None):
        self.set_course_id(course_id)
        self.set_course(course)
        self.set_department(department)
        self.set_start_date(start_date)
        self.set_end_date(end_date)
        self.set_section(section)
        # super().__init__()

    def get_course_id(self):
        return self.course_id

    def set_course_id(self, course_id):
        if not isinstance(course_id, type(Course.course_id)) and course_id is not None:
            print("Error: category_id must be of type {}.\n".format(type(Course.course_id)))
        else:
            self.course_id = course_id

    def get_course(self):
        return self.course

    def set_course(self, course):
        if not isinstance(course, type(Course.course)) and course is not None:
            print("Error: course must be of type {}.\n".format(type(Course.course)))
        else:
            self.course = course

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        if not isinstance(start_date, type(Course.start_date)) and start_date is not None:
            print("Error: start_date must be of type {}.\n".format(type(Course.start_date)))
        else:
            self.start_date = start_date

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        if not isinstance(end_date, type(Course.end_date)) and end_date is not None:
            print("Error: end_date must be of type {}.\n".format(type(Course.end_date)))
        else:
            self.end_date = end_date

    def get_department(self):
        return self.department

    def set_department(self, department):
        if not isinstance(department, type(Course.department)) and department is not None:
            print("Error: department must be of type {}.\n".format(type(Course.department)))
        else:
            self.department = department

    def get_section(self):
        return self.section

    def set_section(self, section):
        if not isinstance(section, type(Course.section)) and section is not None:
            print("Error: section must be of type {}.\n".format(type(Course.section)))
        else:
            self.section = section
