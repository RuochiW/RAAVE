"""
Author: Ethan
Contents: Event and deliverable base classes and event controller class
"""


# from event_data_controller import *


class Event:
    """The event class contains a layout of the information pertaining to an event. 
    Conceptually it represents a simple task or event that is contained thin
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
            it sets parameters as specified.
        """
        self.set_event_id(event_id)
        self.set_event_type(event_type)
        self.set_visibility(visibility)
        self.set_name(name)
        self.set_category_id(category)
        self.set_start_date(start_date)
        self.set_end_date(end_date)

    def __str__(self):
        """Formatted output for the Event object, it will print each attribute line by line."""
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
        if not isinstance(event_id, type(Event.event_id)) and event_id is not None:
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
        if not isinstance(event_type, type(Event.event_type)) and event_type is not None:
            print(f"Error: event_type must be of type {type(Event.event_type)}.")
        else:
            self.event_type = event_type

    def get_visibility(self):
        """Returns the value of the visibility attribute for an Event object."""
        return self.visibility

    def set_visibility(self, visibility):
        """Sets the value of the visibility attribute for an Event object using the visibility
        parameter and checks if it is an integer. If visibility is not an integer the attribute
        will not be updated"""
        if not isinstance(visibility, type(Event.visibility)) and visibility is not None:
            print(f"Error: visibility must be of type {type(Event.visibility)}.")
        else:
            self.visibility = visibility

    def get_name(self):
        """Returns the value of the name attribute for an Event object."""
        return self.name

    def set_name(self, name):
        """Sets the value of the name attribute for an Event object using the name
        parameter and checks if it is a string. If name is not a string this function
        will not update the attribute"""
        if not isinstance(name, type(Event.name)) and name is not None:
            print(f"Error: name must be of type {type(Event.name)}.")
        else:
            self.name = name

    def get_category_id(self):
        """Returns the value of the category attribute for an Event object."""
        return self.category

    def set_category_id(self, category):
        """Sets the value of the category attribute for an Event object using the category
        parameter and checks if it is an integer. If name is not an integer this function
        will not update the attribute"""
        if not isinstance(category, type(Event.category)) and category is not None:
            print(f"Error: category must be of type {type(Event.category)}.")
        else:
            self.category = category

    def get_start_date(self):
        """Returns the value of the start_date attribute for an Event object."""
        return self.start_date

    def set_start_date(self, start_date):
        """Sets the value of the start_date attribute for an Event object using the start_date
        parameter and checks if it is an integer. If start_date is not an integer this function
        will not update the attribute"""
        if not isinstance(start_date, type(Event.start_date)) and start_date is not None:
            print(f"Error: start_date must be of type {type(Event.start_date)}.")
        else:
            self.start_date = start_date

    def get_end_date(self):
        """Returns the value of the end_date attribute for an Event object."""
        return self.end_date

    def set_end_date(self, end_date):
        """Sets the value of the end_date attribute for an Event object using the end_date
        parameter and checks if it is an integer. If end_date is not an integer this function
        will not update the attribute"""
        if not isinstance(end_date, type(Event.end_date)) and end_date is not None:
            print(f"Error: end_date must be of type {type(Event.end_date)}.")
        else:
            self.end_date = end_date

    def get_all_event(self):
        """Returns a list of all user defined attributes of the event class in alphabetical order."""
        attributes = list()
        for i in dir(self):
            if not i.startswith('__') and not i.startswith('get') and not i.startswith('set'):
                attributes.append(i)

        return attributes  # in alphabetical order


class Deliverable:
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
        parameter and checks if it is an integer. If deliverable_id is not an integer this function
        will not update the attribute."""
        if not isinstance(deliverable_id, type(Deliverable.deliverable_id)) and deliverable_id is not None:
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
        if not isinstance(time_estimate, type(Deliverable.time_estimate)) and time_estimate is not None:
            print(f"Error: time_estimate must be of type {type(Deliverable.time_estimate)}.")
        else:
            self.time_estimate = time_estimate

    def get_time_spent(self):
        """Returns the value of the time_spent attribute for a Deliverable object."""
        return self.time_spent

    def set_time_spent(self, time_spent):
        """Sets the value of the time_spent attribute for a Deliverable object using the time_spent
        parameter and checks if it is a string. If time_spent is not a string this function
        will not update the attribute."""
        if not isinstance(time_spent, type(Deliverable.time_spent)) and time_spent is not None:
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
        if not isinstance(weight, type(Deliverable.weight)) and weight is not None:
            print(f"Error: weight must be of type {type(Deliverable.weight)}.")
        else:
            self.weight = weight
