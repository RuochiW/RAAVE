#Author: Ethan
#Contents: Event and deliverable base classes and event controller class

#from event_data_controller import *
from data.data_controller import event_data_controller

class Event:
    """The event class contains a layout of the information pertaining to an event. Conceptually it
    represents a simple task or event that is contained wthin a grouping, that is, the category class.
    """
    
    event_id = int() 
    event_type = int() 
    visibility = int() 
    name = str() 
    #date = str()
    #time_estimate = int()
    #weight = int()
    category = int() 
    start_date = str() 
    end_date = str() 


    
    def __init__(self, event_id = None, event_type = None, 
                visibility = None, name = None, category = None, 
                start_date = None, end_date = None):
        """The event constructor defaults every attribute to None, otherwise 
            it sets paramters as specified.        
        """
        self.setEventID(event_id)
        self.setEType(event_type)
        self.setVisibility(visibility)
        self.setName(name)
        self.setCategoryID(category) 
        self.setStartDate(start_date)
        self.setEndDate(end_date)

    def __str__(self):
        """Formated output for the Event object, it will print each attribute line by line.""" 
        return f"event_id: {self.event_id},\n event_type: {self.event_type},\n visibility: {self.visibility},\n name: {self.name}, Category: {self.category},\n Start Date: {self.start_date}, \n End Date: {self.end_date}"

    
    def getEventID(self):
        return self.event_id
    
    #Likely will only be used for testing purposes
    def setEventID(self, event_id):
        if type(event_id) is not type(Event.event_id) and type(event_id) is not type(None):
            print("Error: event_id must be of type {}.\n".format(type(Event.event_id)))
        else:
            self.event_id = event_id


    def getEType(self):
        return self.event_type

    def setEType(self, event_type):
        if type(event_type) is not type(Event.event_type) and type(event_type) is not type(None):
            print("Error: event_type must be of type {}.\n".format(type(Event.event_type)))
        else:
            self.event_type = event_type

    def getVisibility(self):
        return self.visibility
    
    def setVisibility(self, visibility):
        if type(visibility) is not type(Event.visibility) and type(visibility) is not type(None):
            print("Error: visibility must be of type {}\n".format(type(Event.visibility)))
        else:
            self.visibility = visibility

    def getName(self):
        return self.name
    
    def setName(self, name):
        if type(name) is not type(Event.name) and type(name) is not type(None):
            print("Error: name must be of type {}.\n".format(type(Event.name)))
        else:
            self.name = name

    def getCategoryID(self):
        return self.category
    
    def setCategoryID(self, category):
        if type(category) is not type(Event.category) and type(category) is not type(None):
            print("Error: category must be of type {}.\n".format(type(Event.category)))
        else:
            self.category = category

    def getStartDate(self):
        return self.start_date
    
    def setStartDate(self, start_date):
        if type(start_date) is not type(Event.start_date) and type(start_date) is not type(None):
            print("Error: start_date must be of type {}.\n".format(type(Event.start_date)))
        else:
            self.start_date = start_date

    def getEndDate(self):
        return self.end_date
    
    def setEndDate(self, end_date):
        if type(end_date) is not type(Event.end_date) and type(end_date) is not type(None):
            print("Error: end_date must be of type {}.\n".format(type(Event.end_date)))
        else:
            self.end_date = end_date

    def getAll(self):
        attributes = list()
        for i in dir(self):
            if not i.startswith('__') and not i.startswith('get') and not i.startswith('set'):
                attributes.append(i) 

        return attributes #in alphabetical order


class Deliverable():
    deliverable_id = int()
    weight = int()
    time_estimate = str()
    time_spent = str()

    def __init__(self, deliverable_id = None, weight = None, time_estimate = None, time_spent = None):
        self.setDeliverableID(deliverable_id)
        self.setWeight(weight)
        self.setTimeEstimate(time_estimate)
        self.setTimeSpent(time_spent)
        #super().__init__()

    def getDeliverableID(self):
        return self.deliverable_id
    
    def setDeliverableID(self, deliverable_id):
        if type(deliverable_id) is not type(Deliverable.deliverable_id) and type(deliverable_id) is not type(None):
            print("Error: deliverable_id must be of type {}.\n".format(type(Deliverable.deliverable_id)))
        else:
            self.deliverable_id = deliverable_id

    def getTimeEstimate(self):
        return self.time_estimate
    
    def setTimeEstimate(self, time_estimate):
        if type(time_estimate) is not type(Deliverable.time_estimate) and type(time_estimate) is not type(None):
            print("Error: time_estimate must be of type {}.\n".format(type(Deliverable.time_estimate)))
        else:
            self.time_estimate = time_estimate

    def getTimeSpent(self):
        return self.time_spent
    
    def setTimeSpent(self, time_spent):
        if type(time_spent) is not type(Deliverable.time_spent) and type(time_spent) is not type(None):
            print("Error: time_spent must be of type {}.\n".format(type(Deliverable.time_spent)))
        else:
            self.time_spent = time_spent

    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        if type(weight) is not type(Deliverable.weight) and type(weight) is not type(None):
            print("Error: weight must be of type {}.\n".format(type(Deliverable.weight)))
        else:
            self.weight = weight

class EventController(Event, Deliverable):
    """Inherits from the Event Class. It controls the interactions between the frontend and 
    the database related to the creation, deletion, reading and writing of event objects"""

    def createEvent(self):
        e = Event()
        res = write_event(e)
        return res
        

        

    def updateEvent(self):
        """Until user interface input is complete, input will be drawn from the command line.
        This functions will update the values of an event in the database and return the status of the operation"""
        
        e = Event()

        """get all the updates user wants, initially just command line input"""
        update_list = getEventInput()

        """get all the attributes that are in the event that is being updated"""
        attributes = e.getAll()

        """Update all varialbles unless input value specified is none or empty string """
        for i in range(0, len(attributes)):
            if update_list[i] == '' or update_list[i] == None:
                continue
            
            e.__setattr__(attributes[i], update_list[i])

        res = write_event(e)
        return res

    
    def readEvent(self):
        id = input("Enter the event_id of the event you would like to read: ")
        id = int(id)
        e = Event(id)
        
        res = read_event(e)
        return res

    def deleteEvent(self):
        id = input("Enter the event_id of the event you would like to delete: ")
        id = int(id) 
        e = Event(id) #The other attributes will be defaulted to None
        
        res = read_event(e)
        return res
        

    def getAllNotifications(self):
        id = input("Enter the event_id of the event you would like to fetch all notifications for: ")
        id = int(id)
        e = Event(id)
        res = get_all_notifications(e)
        return res


def getEventInput():
        """
        Helper function that gets user input for updating attribute value,
        likely to be replaced with html form input.
        """
        e = Event()
        
        source_attr = e.getAll() #getAll() returns a list of only the user defined attributes of a class
        updated_attr = list()
        
        #iterate through all attributes prompting for input for each then storing that input in a list
        for i in range(0, source_attr.__len__()):
        
            attr = input("Enter value for {}: ".format(source_attr[i]))

            if (type(e.__getattribute__(source_attr[i])) == type(int)):
                attr = int(attr)
            
            updated_attr.append(attr)
            
        return updated_attr
