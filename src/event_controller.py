"""
Author: Ethan
Contents: Event and deliverable base classes and event controller class
"""
# from event_data_controller import *

from data.data_controller.event_data_controller import write_event, read_event
from data.data_controller.notification_data_controller import read_all_notification
from src.events import Event, Deliverable


def create_event():
    """Initializes an empty Event Object and puts it into the database, returns
    the status of the write operation."""
    event = Event()
    result = write_event(event)
    return result


def update_event():
    """Until user interface input is complete, input will be drawn from the command line.
    This functions will update the values of an event in the database and return the status of the operation"""

    event = Event()

    # get all the updates user wants, initially just command line input
    update_list = get_event_input()

    # get all the attributes that are in the event that is being updated
    attributes = event.get_all_event()

    # Update all variables unless input value specified is none or empty string
    for i, attribute in enumerate(attributes):
        if update_list[i] == '' or update_list[i] is None:
            continue

        event.__setattr__(attributes[i], update_list[i])

    result = write_event(event)
    return result


def read_user_event():
    """Returns a list of event attributes with a given event_id if the operation is successful,
    otherwise returns the read operation status and an error message"""

    event_id = input("Enter the event_id of the event you would like to read: ")
    event_id = int(event_id)  # input() always returns a string, cast it to an integer
    event = Event(event_id)

    result = read_event(event)
    return result


def delete_event():
    """Will 'remove' an event from the database, or rather, replace all the table values with
    Null. If this operation is successful it will return a list with the status and the empty
    attributes, otherwise will return a list with the status and an error message."""
    event_id = input("Enter the event_id of the event you would like to delete: ")
    event_id = int(event_id)
    obj = Event(event_id)  # The other attributes will be defaulted to None

    result = write_event(obj)
    return result


def get_all_notifications():
    """Returns a list of all notifications for an event object if successful,
    otherwise returns a list with the status of the operation and an error message."""
    event_id = input(
        "Enter the event_id of the event you would like to fetch all notifications for: ")
    event_id = int(event_id)
    event = Event(event_id)
    result = read_all_notification(event)
    # defined within notification_data_controller.py
    return result


class EventController(Event, Deliverable):
    """Inherits from the Event Class. It controls the interactions between the frontend and
    the database related to the creation, deletion, reading and writing of event objects"""


def get_event_input():
    """
    Helper function that gets user input for updating attribute values,
    likely to be replaced with html form input.
    """
    event = Event()

    # get_all() returns a list of only the user defined attributes of a class
    source_attribute = event.get_all_event()
    updated_attribute = list()

    # iterate through all attributes prompting for input for each then storing that input in a list
    for i, source_attribute in enumerate(source_attribute):

        attribute = input(f"Enter value for {source_attribute[i]}: ")

        if type(event.__getattribute__(source_attribute[i])) == type(int):
            attribute = int(attribute)

        updated_attribute.append(attribute)

    return updated_attribute
