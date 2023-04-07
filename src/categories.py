# Author: Anandita Gupta
# Contents: Category and Category controller class

# from category_data_controller import *
from data.data_controller.category_data_controller import write_category, read_category


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


def create_category():
    category = Category()
    result = write_category(category)
    return result


def create_course():
    course = Course()
    result = write_category(course)
    return result


def read_user_category():
    category_id = input("Enter the category_id of the category you would like to read: ")
    category_id = int(category_id)
    category = Category(category_id)
    result = read_category(category)
    return result


def delete_category():
    category_id = input("Enter the category_id of the category you would like to delete: ")
    category_id = int(category_id)
    category = Category(category_id)  # The other attributes will be defaulted to None
    result = write_category(category)
    return result


def get_category_input():
    """
    Helper function that gets user input for updating attribute value,
    likely to be replaced with html form input.
    """
    category = Category()

    source_attribute = category.get_all_category()
    # getAll() returns a list of only the user defined attributes of a class
    updated_attribute = list()

    # iterate through all attributes prompting for input for each then storing that input in a list
    for i in range(0, source_attribute.__len__()):

        attribute = input("Enter value for {}: ".format(source_attribute[i]))

        if type(category.__getattribute__(source_attribute[i])) == type(int):
            attribute = int(attribute)

        updated_attribute.append(attribute)

    return updated_attribute


def update_category():
    """Until user interface input is complete, input will be drawn from the command line.
    This functions will update the values of an event in the database and return the status of the operation"""

    category = Category()

    """get all the updates user wants, initially just command line input"""
    update_list = get_category_input()

    """get all the attributes that are in the event that is being updated"""
    attributes = category.get_all_category()

    """Update all variables unless input value specified is none or empty string """
    for i in range(0, len(attributes)):
        if update_list[i] == '' or update_list[i] is None:
            continue

        category.__setattr__(attributes[i], update_list[i])

    result = write_category(category)
    return result


class CategoryController:
    """Inherits from the Event Class. It controls the interactions between the frontend and 
    the database related to the creation, deletion, reading and writing of event objects"""
