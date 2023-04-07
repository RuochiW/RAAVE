# Author: Anandita Gupta


from data.data_controller.category_data_controller import write_category, read_category
from src.categories import Category, Course


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
