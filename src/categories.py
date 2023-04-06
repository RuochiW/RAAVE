#Author: Anandita Gupta
#Contents: Category and Category controller class

#from category_data_controller import *
from data.data_controller import category_data_controller

class Category:
    """The category class contains a layout of the information pertaining to a category.
    """
    
    category_id = int() 
    category_type = int() 
    visibility = int() 
    name = str() 
    description = str()
    owner = str() 

    def __init__(self, category_id=None, category_type=None, owner=None,
                  name=None, visibility=None, description=None):
        self.setCategoryId(category_id)
        self.setCategoryType(category_type)
        self.setOwner(owner)
        self.setName(name)
        self.setVisibility(visibility)
        self.setDescription(description)


    def __str__(self):
        """Formated output for the Category object, it will print each attribute line by line.""" 
        return f"category_id: {self.category_id},\n category_type: {self.category_type},\n visibility: {self.visibility},\n name: {self.name}, description: {self.description},\n owner: {self.owner}"

    
    def getCategoryId(self):
        return self.category_id
    
    #Likely will only be used for testing purposes
    def setCategoryId(self, category_id):
        if type(category_id) is not type(Category.category_id) and type(category_id) is not type(None):
            print("Error: category_id must be of type {}.\n".format(type(Category.event_id)))
        else:
            self.category_id = category_id


    def getCategoryType(self):
        return self.category_type

    def setCategoryType(self, category_type):
        if type(category_type) is not type(Category.category_type) and type(category_type) is not type(None):
            print("Error: category_type must be of type {}.\n".format(type(Category.category_type)))
        else:
            self.category_type = category_type

    def getVisibility(self):
        return self.visibility
    
    def setVisibility(self, visibility):
        if type(visibility) is not type(Category.visibility) and type(visibility) is not type(None):
            print("Error: visibility must be of type {}\n".format(type(Category.visibility)))
        else:
            self.visibility = visibility

    def getName(self):
        return self.name
    
    def setName(self, name):
        if type(name) is not type(Category.name) and type(name) is not type(None):
            print("Error: name must be of type {}.\n".format(type(Category.name)))
        else:
            self.name = name

    def getDescription(self):
        return self.description
    
    def setDescription(self, description):
        if type(description) is not type(Category.description) and type(description) is not type(None):
            print("Error: description must be of type {}.\n".format(type(Category.description)))
        else:
            self.description = description

    def getOwner(self):
        return self.owner
    
    def setOwner(self, owner):
        if type(owner) is not type(Category.owner) and type(owner) is not type(None):
            print("Error: owner must be of type {}.\n".format(type(Category.owner)))
        else:
            self.owner = owner


    def getAll(self):
        attributes = list()
        for i in dir(self):
            if not i.startswith('__') and not i.startswith('get') and not i.startswith('set'):
                attributes.append(i) 

        return attributes #in alphabetical order


class Course():
    category_id = int()
    course = int()
    department = str()
    start_date = str()
    end_date = str()
    section = int()

    def __init__(self, category_id = None, course = None, start_date = None, end_date = None, department = None, section = None):
        self.setCategoryID(category_id)
        self.setCourse(course)
        self.setDepartment(department)
        self.setStartDate(start_date)
        self.setEndDate(end_date)
        self.setSection(section)
        #super().__init__()

    def getCategoryID(self):
        return self.category_id
    
    def setCategoryID(self, category_id):
        if type(category_id) is not type(Course.category_id) and type(category_id) is not type(None):
            print("Error: category_id must be of type {}.\n".format(type(Course.category_id)))
        else:
            self.category_id = category_id

    def getCourse(self):
        return self.course
    
    def setCourse(self, course):
        if type(course) is not type(Course.course) and type(course) is not type(None):
            print("Error: course must be of type {}.\n".format(type(Course.course)))
        else:
            self.course = course

    def getStartDate(self):
        return self.start_date
    
    def setStartDate(self, start_date):
        if type(start_date) is not type(Course.start_date) and type(start_date) is not type(None):
            print("Error: start_date must be of type {}.\n".format(type(Course.start_date)))
        else:
            self.start_date = start_date
    
    def getEndDate(self):
        return self.end_date
    
    def setEndDate(self, end_date):
        if type(end_date) is not type(Course.end_date) and type(end_date) is not type(None):
            print("Error: end_date must be of type {}.\n".format(type(Course.end_date)))
        else:
            self.end_date = end_date

    def getDepartment(self):
        return self.department
    
    def setDepartment(self, department):
        if type(department) is not type(Course.department) and type(department) is not type(None):
            print("Error: department must be of type {}.\n".format(type(Course.weight)))
        else:
            self.department = department
    
    def getSection(self):
        return self.section
    
    def setSection(self, section):
        if type(section) is not type(Course.section) and type(section) is not type(None):
            print("Error: section must be of type {}.\n".format(type(Course.section)))
        else:
            self.section = section

class CategoryController(Category, Course):
    """Inherits from the Event Class. It controls the interactions between the frontend and 
    the database related to the creation, deletion, reading and writing of event objects"""

    def createCategory(self):
        c = Category()
        res = write_category(c)
        return res
        

        

    def updateCategory(self):
        """Until user interface input is complete, input will be drawn from the command line.
        This functions will update the values of an event in the database and return the status of the operation"""
        
        c = Category()

        """get all the updates user wants, initially just command line input"""
        update_list = getCategoryInput()

        """get all the attributes that are in the event that is being updated"""
        attributes = c.getAll()

        """Update all varialbles unless input value specified is none or empty string """
        for i in range(0, len(attributes)):
            if update_list[i] == '' or update_list[i] == None:
                continue
            
            c.__setattr__(attributes[i], update_list[i])

        res = write_category(c)
        return res

    
    def readCategory(self):
        id = input("Enter the category_id of the category you would like to read: ")
        id = int(id)
        c = Category(id)
        res = read_category(c)
        return res

    def deleteCategory(self):
        id = input("Enter the category_id of the category you would like to delete: ")
        id = int(id) 
        c = Category(id) #The other attributes will be defaulted to None
        res = read_category(c)
        return res
        

    def getAllNotifications(self):
        id = input("Enter the category_id of the category you would like to fetch all notifications for: ")
        id = int(id)
        c = Category(id)
        res = get_all_notifications(c)
        return res
    
    def getAllEvents(self):
        id = input("Enter the category_id of the category you would like to fetch all events for: ")
        id = int(id)
        c = Category(id)
        res = get_all_events(c)
        return res



    def getCategoryInput():
        """
        Helper function that gets user input for updating attribute value,
        likely to be replaced with html form input.
        """
        c = Category()
        
        source_attr = c.getAll() #getAll() returns a list of only the user defined attributes of a class
        updated_attr = list()
        
        #iterate through all attributes prompting for input for each then storing that input in a list
        for i in range(0, source_attr.__len__()):
        
            attr = input("Enter value for {}: ".format(source_attr[i]))

            if (type(c.__getattribute__(source_attr[i])) == type(int)):
                attr = int(attr)
            
            updated_attr.append(attr)
            
        return updated_attr