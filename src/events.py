"""
Author: Ethan
Contents: Event and deliverable base classes and event controller class
"""
#from event_data_controller import *

from data.data_controller.event_data_controller import write_event, read_event


class Event:
    """The event class contains a layout of the information pertaining to an event. 
    Conceptually it represents a simple task or event that is contained wthin 
    a grouping, that is, the category class.
    """

    event_id = int()
    event_type = int()
    visibility = int()
    name = str()
    category = int()
    start_date = str()
    end_date = str()

    def __init__(self, event_id=None, event_type=None,
                 visibility=None, name=None, category=None,
                 start_date=None, end_date=None):
        """The event constructor defaults every attribute to None, otherwise 
            it sets paramters as specified.        
        """
        self.set_event_id(event_id)
        self.set_event_type(event_type)
        self.set_visibility(visibility)
        self.set_name(name)
        self.set_category_id(category)
        self.set_start_date(start_date)
        self.set_end_date(end_date)

    def __str__(self):
        """Formated output for the Event object, it will print each attribute line by line."""
        return f'''event_id: {self.event_id},\n event_type: {self.event_type},\n
                    visibility: {self.visibility},\n name: {self.name}, 
                    Category: {self.category},\n Start Date: {self.start_date}, \n 
                    End Date: {self.end_date}'''

    def get_event_id(self):
        """Returns the value of the event_id attribute for an Event object"""
        return self.event_id


    def set_event_id(self, event_id):
        """Sets the value of the event_id attribute for an Event object using the event_id
        parameter and checks if it is an integer. If event_id is not an integer or None the
        attribute will not be updated."""
        if type(event_id) is not type(Event.event_id) and type(event_id) is not type(None):
            print(f"Error: event_id must be of type {type(Event.event_id)}.")
        else:
            self.event_id = event_id

    def get_event_type(self):
        """Returns the value of the event_type attribute for an Event object."""
        return self.event_type

    def set_event_type(self, event_type):
        """Sets the value of the event_type attribute for an Event object using the event_type
        parameter and checks if it is an integer. If event_type is not an integer or None then 
        the attribute will not be updated."""
        if type(event_type) is not type(Event.event_type) and type(event_type) is not type(None):
            print(f"Error: event_type must be of type {type(Event.event_type)}.")
        else:
            self.event_type = event_type

    def get_visibility(self):
        """Returns the value of the visibility attribute for an Event object."""
        return self.visibility

    def set_visibility(self, visibility):
        """Sets the value of the visibility attribute for an Event object using the visibility
        parameter and checks if it is an integer. If visibility is not a integer the attribute 
        will not be updated"""
        if type(visibility) is not type(Event.visibility) and type(visibility) is not type(None):
            print(f"Error: visibility must be of type {type(Event.visibility)}.")
        else:
            self.visibility = visibility

    def get_name(self):
        """Returns the value of the name attribute for an Event object."""
        return self.name

    def set_name(self, name):
        """Sets the value of the name attribute for an Event object using the name
        parameter and checks if it is an string. If name is not a string this function 
        will not update the attribute"""
        if type(name) is not type(Event.name) and type(name) is not type(None):
            print(f"Error: name must be of type {type(Event.name)}.")
        else:
            self.name = name

    def get_category_id(self):
        """Returns the value of the category attribute for an Event object."""
        return self.category

    def set_category_id(self, category):
        """Sets the value of the category attribute for an Event object using the category
        parameter and checks if it is an integer. If name is not a integer this function 
        will not update the attribute"""
        if type(category) is not type(Event.category) and type(category) is not type(None):
            print(f"Error: category must be of type {type(Event.category)}.")
        else:
            self.category = category

    def get_start_date(self):
        """Returns the value of the start_date attribute for an Event object."""
        return self.start_date

    def set_start_date(self, start_date):
        """Sets the value of the start_date attribute for an Event object using the start_date
        parameter and checks if it is an integer. If start_date is not a integer this function 
        will not update the attribute"""
        if type(start_date) is not type(Event.start_date) and type(start_date) is not type(None):
            print(f"Error: start_date must be of type {type(Event.start_date)}.")
        else:
            self.start_date = start_date

    def get_end_date(self):
        """Returns the value of the end_date attribute for an Event object."""
        return self.end_date

    def set_end_date(self, end_date):
        """Sets the value of the end_date attribute for an Event object using the end_date
        parameter and checks if it is an integer. If end_date is not a integer this function 
        will not update the attribute"""
        if type(end_date) is not type(Event.end_date) and type(end_date) is not type(None):
            print(f"Error: end_date must be of type {type(Event.end_date)}.")
        else:
            self.end_date = end_date

    def get_all(self):
        """Returns a list of all user defined attributes of the event class in alphabetical order."""
        attributes = list()
        for i in dir(self):
            if not i.startswith['__'] and not i.startswith['get'] and not i.startswith['set']:
                attributes.append(i)

        return attributes  # in alphabetical order


class Deliverable():
    """The Deliverable class contains a layout of the information pertaining to a deliverable. 
    Conceptually it represents a course assigment or any task a professor may want to put on a 
    course calendar that is also contained within a grouping, that is, the course class.
    """
    deliverable_id = int()
    weight = int()
    time_estimate = str()
    time_spent = str()

    def __init__(self, deliverable_id=None, weight=None, time_estimate=None, time_spent=None):
        self.set_deliverable_id(deliverable_id)
        self.set_weight(weight)
        self.set_time_estimate(time_estimate)
        self.set_time_spent(time_spent)

    def get_deliverable_id(self):
        """Returns the value of the deliverable_id attribute for a Deliverable object."""
        return self.deliverable_id

    def set_deliverable_id(self, deliverable_id):
        """Sets the value of the deliverable_id attribute for a Deliverable object using the deliverable_id
        parameter and checks if it is an integer. If deliverable_id is not a integer this function 
        will not update the attribute."""
        if type(deliverable_id) is not type(Deliverable.deliverable_id) and type(deliverable_id) is not type(None):
            print(f"Error: deliverable_id must be of type {type(Deliverable.deliverable_id)}.")
        else:
            self.deliverable_id = deliverable_id

    def get_time_estimate(self):
        """Returns the value of the time_estimate attribute for a Deliverable object."""
        return self.time_estimate

    def set_time_estimate(self, time_estimate):
        """Sets the value of the time_estimate attribute for a Deliverable object using the time_estimate
        parameter and checks if it is a string. If time_estimate is not a string this function 
        will not update the attribute."""
        if type(time_estimate) is not type(Deliverable.time_estimate) and type(time_estimate) is not type(None):
            print(f"Error: time_estimate must be of type {type(Deliverable.time_estimate)}.")
        else:
            self.time_estimate = time_estimate

    def get_time_spent(self):
        """Returns the value of the time_spent attribute for a Deliverable object."""
        return self.time_spent

    def set_time_spent(self, time_spent):
        """Sets the value of the time_spent attribute for a Deliverable object using the time_spent
        parameter and checks if it is an string. If time_spent is not a stirng this function 
        will not update the attribute."""
        if type(time_spent) is not type(Deliverable.time_spent) and type(time_spent) is not type(None):
            print(f"Error: time_spent must be of type {type(Deliverable.time_spent)}.")
        else:
            self.time_spent = time_spent

    def get_weight(self):
        """Returns the value of the weight attribute for a Deliverable object."""
        return self.weight

    def set_weight(self, weight):
        """Sets the value of the weight attribute for a Deliverable object using the weight
        parameter and checks if it is an integer. If weight is not an integer this function 
        will not update the attribute."""
        if type(weight) is not type(Deliverable.weight) and type(weight) is not type(None):
            print(f"Error: weight must be of type {type(Deliverable.weight)}.")
        else:
            self.weight = weight


class EventController(Event, Deliverable):
    """Inherits from the Event Class. It controls the interactions between the frontend and 
    the database related to the creation, deletion, reading and writing of event objects"""

    def create_event(self):
        """Initizlies an empty Event Object and and puts it into the database, returns 
        the status of the write operation."""
        e = Event()
        res = write_event(e)
        return res

    def update_event(self):
        """Until user interface input is complete, input will be drawn from the command line.
        This functions will update the values of an event in the database and return the status of the operation"""

        e = Event()

        #get all the updates user wants, initially just command line input
        update_list = get_event_input()

        #get all the attributes that are in the event that is being updated
        attributes = e.get_all()

        #Update all varialbles unless input value specified is none or empty string
        for i in enumerate(attributes, 0):
            if update_list[i] == '' or update_list[i] is None:
                continue

            e.__setattr__(attributes[i], update_list[i])

        res = write_event(e)
        return res

    def read_event(self):
        """Returns a list of event attributes with a given event_id if the operation is successful,
        otherwise returns the read opertaion status and an error message"""

        event_id = input("Enter the event_id of the event you would like to read: ")
        event_id = int(event_id) #input() always returns a string, cast it to an integer
        e = Event(event_id)

        res = read_event(e)
        return res

    def delete_event(self):
        """Will 'remove' an event from the database, or rather, replace all the table values with 
        Null. If this operation is successful it will return a list with the status and the empty 
        attributes, otherwise will return a list with the status and an error message."""
        event_id = input("Enter the event_id of the event you would like to delete: ")
        event_id = int(event_id)
        obj = Event(id)  # The other attributes will be defaulted to None

        res = write_event(obj)
        return res

    def getAllNotifications(self):
        """Returns a list of all notifications for an event object if successful, 
        otherwise returns a list with the status of the operation and an error message."""
        id = input(
            "Enter the event_id of the event you would like to fetch all notifications for: ")
        id = int(id)
        e = Event(id)
        res = read_all_notifications(e) #defined witin notification_data_controller.py
        return res


def get_event_input():
    """
    Helper function that gets user input for updating attribute values,
    likely to be replaced with html form input.
    """
    e = Event()

    # get_all() returns a list of only the user defined attributes of a class
    source_attr = e.get_all()
    updated_attr = list()

    # iterate through all attributes prompting for input for each then storing that input in a list
    for i in enumerate(source_attr, 0):

        attr = input(f"Enter value for {source_attr[i]}: ")

        if type(e.__getattribute__(source_attr[i])) == type(int):
            attr = int(attr)

        updated_attr.append(attr)

    return updated_attr
