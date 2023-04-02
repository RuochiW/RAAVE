#Author: Anandita Gupta
#Info: Categories Class and Categories Controller class

class Category:

    categoryID = int()
    type = int()
    eType = int()
    visibility = int()
    name = str()
    ownerID = int()
    departmentID = int()
    sectionID = int()

    def __init__(self, categoryID = -1, ctype = -1,
            visibility = -1, name = "", ownerID = -1,
             departmentID= -1, sectionID = -1):
        self.setCategoryID(categoryID)
        self.setType(type)
        self.setVisibility(visibility)
        self.setName(name)
        self.setOwnerID(ownerID)
        self.setDepartmentID(departmentID)
        self.setSectionID(sectionID)

    def __str__(self): 
        return f"categoryID: {self.categoryID},\n ctype: {self.ctype},\n visibility: {self.visibility},\n name: {self.name},\n ownerID: {self.ownerID},\n departmentID: {self.departmentID},\n sectionID: {self.sectionID}"
    
    def getCategoryID(self):
        return self.categoryID
        
    def setCategoryID(self, categoryID):
        if type(categoryID) is not type(Category.categoryID):
            print("Error: categoryID must be of type {}.\n".format(type(Category.categoryID)))
        else:
            self.categoryID = categoryID
    def getCType(self):
        return self.ctype

    def setCType(self, cType):
        if type(cType) is not type(Category.cType):
            print("Error: CType must be of type {}.\n".format(type(Category.cType)))
        else:
            self.cType = cType

    def getVisibility(self):
        return self.visibility
    
    def setVisibility(self,visibility)
        if type(visibility) is not visibility(Category.visibility)))
            print("Error: Type must be of type {}.\n".format(type(Category.visibility)))
        else:
            self.visibility=visibility

    def getName(self):
        return self.name

    def setName(self, name)
        if type(name) is not name(Category.name)))
            print("Error: Type must be of type {}.\n".format(type(Category.name)))
        else:
            self.name=name

    def getOwnerID(self):
        return self.ownerID

    def setOwnerID(self, ownerID):
        if type(ownerID) is not type(Category.ownerID):
            print("Error: ownerID must be of type {}.\n".format(type(Category.ownerID)))
        else:
            self.ownerID = ownerID

    def getDepartmentID(self):
        return self.departmentID

    def setDepartmentID(self, departmentID):
        if type(departmentID) is not type(Category.departmentID):
            print("Error: departmentID must be of type {}.\n".format(type(Category.departmentID)))
        else:
            self.departmentID = departmentID

    def getSectionID(self):
        return self.sectionID

    def setSectionID(self, sectionID):
        if type(sectionID) is not type(Category.sectionID):
            print("Error: sectionID must be of type {}.\n".format(type(Category.sectionID)))
        else:
            self.sectionID = sectionID
    
    def getAll(self):
        attributes = list()
        for i in dir(self):
            if not i.startswith('__') and not i.startswith('get') and not i.startswith('set'):
                attributes.append(i) #in alphabetical order

        return attributes

class CategoryController(Category):
    def createCategory():
        c = Category()

    def updateCategory(self, category_obj):
        c = Category()
        update_list = getCategoryInput()
        attributes = category_obj.getAll()

        for i in range(0, len(attributes)):
            if update_list[i] == '' or update_list[i] == None:
                continue
            category_obj.__setattr__(attributes[i], [update_list[i]])

    def readCategory():
        pass

    def deleteCategory():
        pass

    def getAllNotifications():
        pass

    def getCategoryInput():
        c = Category()
        updated_attr = list()
        source_attr = e.getAll()
    
    for i in range(0, source_attr.__len__()):
        attr = input("Enter value for {}: ".format(source_attr[i]))
        updated_attr.append(attr)
    
    return updated_attr