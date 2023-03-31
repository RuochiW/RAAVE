#Author: Ethan
#Contents: Event base class and event controller class

from data import *

class Event:
    """The event class contains all the information pertaining to an event"""
    eventID = int()
    eType = int()
    visibility = int()
    name = str()
    date = str() #class diagram has this listed as time but that is not a built in type
    timeEstimate = int()
    weight = int()
    categoryID = int()
    startDate = str()
    endDate = str()


    
    def __init__(self, eventID = int(-1), eType = -1, 
                visibility = -1, name = "", date = "",
                timeEstimate = -1, weight = -1, categoryID = -1, startDate = "", endDate = ""):
        """The event constructor defaults to -1 for integers and "" for strings, otherwise 
            it sets paramters as specified        
        """
        self.setEventID(eventID)
        self.setEType(eType)
        self.setVisibility(visibility)
        self.setName(name)
        self.setDate(date)
        self.setTimeEstimate(timeEstimate)
        self.setWeight(weight)
        self.categoryID = categoryID
        self.startDate = startDate
        self.endDate = endDate

    def __str__(self): 
        return f"eventID: {self.eventID},\n eType: {self.eType},\n visibility: {self.visibility},\n name: {self.name},\n date: {self.date},\n timeEstimate: {self.timeEstimate},\n weight: {self.weight}"

    
    def getEventID(self):
        return self.eventID
    
    #Likely will only be used for testing purposes
    def setEventID(self, eventID):
        if type(eventID) is not type(Event.eventID):
            print("Error: eventID must be of type {}.\n".format(type(Event.eventID)))
        else:
            self.eventID = eventID


    def getEType(self):
        return self.eType

    def setEType(self, eType):
        if type(eType) is not type(Event.eType):
            print("Error: EType must be of type {}.\n".format(type(Event.eType)))
        else:
            self.eType = eType

    def getVisibility(self):
        return self.visibility
    
    def setVisibility(self, visibility):
        if type(visibility) is not type(Event.visibility):
            print("Error: visibility must be of type {}\n".format(type(Event.visibility)))
        else:
            self.visibility = visibility

    def getName(self):
        return self.name
    
    def setName(self, name):
        if type(name) is not type(Event.name):
            print("Error: name must be of type {}.\n".format(type(Event.name)))
        else:
            self.name = name

    def getDate(self):
        return self.date
    
    def setDate(self, date):
        if type(date) is not type(Event.date):
            print("Error: date must be of type {}.\n".format(type(Event.date)))
        else:
            self.date = date

    def getTimeEstimate(self):
        return self.timeEstimate
    
    def setTimeEstimate(self, timeEstimate):
        if type(timeEstimate) is not type(Event.timeEstimate):
            print("Error: timeEstimate must be of type {}.\n".format(type(Event.timeEstimate)))
        else:
            self.timeEstimate = timeEstimate

    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        if type(weight) is not type(Event.weight):
            print("Error: weight must be of type {}.\n".format(type(Event.weight)))
        else:
            self.weight = weight

    '''def getContent(self):
        return self.content
    
    def setContent(self, content):
        if type(content) is not type(Event.content):
            print("Error: content must be of type {}.\n".format(type(Event.content)))
        else:
            self.content = content'''

    def getAll(self):
        attributes = list()
        for i in dir(self):
            if not i.startswith('__') and not i.startswith('get') and not i.startswith('set'):
                attributes.append(i) #in alphabetical order

        return attributes


class EventController(Event):
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


        #data.writeEvent(event_obj)
        writeEvent(event_obj)

    
    def readEvent(self):
        id = input("Enter the eventID of the event you would like to read: ")
        #data.readEvent(id)
        readEvent(id)

    def deleteEvent(self):
        id = input("Enter the eventID of the event you would like to delete: ")
        id = int(id)
        #e = Event(id, None, None, None, None, None, None, None)
        e = Event(id, -1, -1, "", "", -1, -1, -1, "", "")
        
        #data.readEvent(e)
        readEvent(e)
        

    def getAllNotifications():
        pass


def getEventInput():
        """
        Helper function that gets user input for updating attribute value,
        likely to be replaced with html form input
        """
        e = Event()
        #e.__setattr__()

        updated_attr = list()
        source_attr = e.getAll() #getAll() returns a list of only the user defined attributes of a class
        
        #iterate through all attributes prompting for input for each then storing that input in a list
        for i in range(0, source_attr.__len__()):
            #src_attr = source_attr[i]
            attr = input("Enter value for {}: ".format(source_attr[i]))
            print(type(e.__getattribute__(source_attr[i])))

            if (type(e.__getattribute__(source_attr[i]) == type(int))):
                attr = int(attr)
            
            if(type(e.__getattribute__(source_attr[i]) == type(str))):
                #attribute is of type string
                attr = str(attr)

            updated_attr.append(attr)
            #print("\n----------\n\t Type of {}: {} \n \t Source Type: {} \n---------\n".format(source_attr[i], type(attr), type(e.__getattribute__(source_attr[i]))))
            
        return updated_attr


