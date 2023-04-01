#Author: Ethan
#Contents: Event base class and event controller class

from data import *


class Event:
    """The event class contains a layout of the information pertaining to an event. Conceptually it
    represents a simple task or event that is contained wthin a grouping, that is, the category class.
    """
    
    eventID = int()
    eType = int()
    visibility = int()
    name = str()
    date = str()
    timeEstimate = int()
    weight = int()
    categoryID = int()
    startDate = str()
    endDate = str()


    
    def __init__(self, eventID = None, eType = None, 
                visibility = None, name = None, date = None,
                timeEstimate = None, weight = None, 
                categoryID = None, startDate = None, endDate = None):
        """The event constructor defaults every attribute to None, otherwise 
            it sets paramters as specified.        
        """
        self.setEventID(eventID)
        self.setEType(eType)
        self.setVisibility(visibility)
        self.setName(name)
        self.setDate(date)
        self.setTimeEstimate(timeEstimate)
        self.setWeight(weight)
        self.setCategoryID(categoryID) 
        self.setStartDate(startDate)
        self.setEndDate(endDate)

    def __str__(self):
        """Formated output for the Event object, it will print each attribute line by line.""" 
        return f"eventID: {self.eventID},\n eType: {self.eType},\n visibility: {self.visibility},\n name: {self.name},\n date: {self.date},\n timeEstimate: {self.timeEstimate},\n weight: {self.weight}"

    
    def getEventID(self):
        return self.eventID
    
    #Likely will only be used for testing purposes
    def setEventID(self, eventID):
        if type(eventID) is not type(Event.eventID) and type(eventID) is not type(None):
            print("Error: eventID must be of type {}.\n".format(type(Event.eventID)))
        else:
            self.eventID = eventID


    def getEType(self):
        return self.eType

    def setEType(self, eType):
        if type(eType) is not type(Event.eType) and type(eType) is not type(None):
            print("Error: EType must be of type {}.\n".format(type(Event.eType)))
        else:
            self.eType = eType

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

    def getDate(self):
        return self.date
    
    def setDate(self, date):
        if type(date) is not type(Event.date) and type(date) is not type(None):
            print("Error: date must be of type {}.\n".format(type(Event.date)))
        else:
            self.date = date

    def getTimeEstimate(self):
        return self.timeEstimate
    
    def setTimeEstimate(self, timeEstimate):
        if type(timeEstimate) is not type(Event.timeEstimate) and type(timeEstimate) is not type(None):
            print("Error: timeEstimate must be of type {}.\n".format(type(Event.timeEstimate)))
        else:
            self.timeEstimate = timeEstimate

    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        if type(weight) is not type(Event.weight) and type(weight) is not type(None):
            print("Error: weight must be of type {}.\n".format(type(Event.weight)))
        else:
            self.weight = weight

    def getCategoryID(self):
        return self.categoryID
    
    def setCategoryID(self, categoryID):
        if type(categoryID) is not type(Event.categoryID) and type(categoryID) is not type(None):
            print("Error: categoryID must be of type {}.\n".format(type(Event.categoryID)))
        else:
            self.categoryID = categoryID

    def getStartDate(self):
        return self.startDate
    
    def setStartDate(self, startDate):
        if type(startDate) is not type(Event.startDate) and type(startDate) is not type(None):
            print("Error: startDate must be of type {}.\n".format(type(Event.startDate)))
        else:
            self.startDate = startDate

    def getEndDate(self):
        return self.endDate
    
    def setEndDate(self, endDate):
        if type(endDate) is not type(Event.endDate) and type(endDate) is not type(None):
            print("Error: endDate must be of type {}.\n".format(type(Event.endDate)))
        else:
            self.endDate = endDate

    def getAll(self):
        attributes = list()
        for i in dir(self):
            if not i.startswith('__') and not i.startswith('get') and not i.startswith('set'):
                attributes.append(i) 

        return attributes #in alphabetical order


class EventController(Event):
    """Inherits from the Event Class. It controls the interactions between the frontend and 
    the database related to the creation, deletion, reading and writing of event objects"""

    def createEvent():
        E = Event()

        #Since this will be creating a new event, it will be pulling data
        # from the user interface
        #So there will be some kind of interaction here pulling data from the webpage
        # Will need to call data conrollers to make db reflect the new event

        

    def updateEvent(self, event_obj):
        """Until user interface input is complete, input will be drawn from the command line.
        @param event_obj is the object that will be updated
        @return there are no returns as object is modified directory and then (once data controllers are ready) the updated object will be sent to the DB"""

        
        e = Event()

        """get all the updates user wants, initially just command line input"""
        update_list = getEventInput()

        """get all the attributes that are in the event that is being updated"""
        attributes = event_obj.getAll()

        """Update all varialbles unless input value specified is none or empty string """
        for i in range(0, len(attributes)):
            if update_list[i] == '' or update_list[i] == None:
                continue
            
            event_obj.__setattr__(attributes[i], update_list[i])

        writeEvent(event_obj)

    
    def readEvent(self):
        id = input("Enter the eventID of the event you would like to read: ")
        readEvent(id)

    def deleteEvent(self):
        id = input("Enter the eventID of the event you would like to delete: ")
        id = int(id)
        e = Event(id)
        
        readEvent(e)
        

    def getAllNotifications():
        pass


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

            if (type(e.__getattribute__(source_attr[i]) == type(int))):
                attr = int(attr)
            
            if(type(e.__getattribute__(source_attr[i]) == type(str))):
                attr = str(attr)

            updated_attr.append(attr)
            
        return updated_attr
