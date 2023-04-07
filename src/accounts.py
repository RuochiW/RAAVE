# Written by Austin Shouli
# Contains Account and Account Controller Classes


import pydoc
import sys

from data.data_controller import account_data_controller
#from data.data_controller import category_data_controller
#from data.data_controller import subscription_data_controller


#Accounts Class
class Account:
  """
  A class to represent a user's account
  
  ...
  Attributes
  ----------
  account_id : int
      unique id for the account
  account_type : int
      account type - student, proffesor
  username : str
      unique account username
  password : str
      unique account password
  first_name : str
      user's first name
  last_name : str
      user's last name
  email : str
      user's email adddress

  Methods
  -------
  getaccount_id():
      returns the account_id field

  getaccount_type(self):
    returns the account_type field

  setaccount_type(self, account_type):
    sets the account_type field

  getUsername(self):
    returns the username field
  
  setUsername(self, uname):
   sets the username field

  getPassword(self):
    returns the password field

  setPassword(self, password):
    sets the password field

  getfirst_name(self):
   returns the first_name field

  setfirst_name(self, fname):
    sets the first_name field

  getlast_name(self):
    returns the last_name field

  setlast_name(self, lname): 
    sets the last_name field

  getEmail(self):
    returns the email field

  setEmail(self, email):
    sets the email field
  
  """
  account_id = int()
  account_type = int()
  username = str()
  password = str()
  first_name = str()
  last_name = str()
  email = str()

  def __init__(self, account_id = None, account_type = None, 
              username = "", password = "", 
              first_name = "",  last_name = "", email = ""):

      self.account_id = account_id
      self.account_type = account_type
      self.username = username
      self.password = password
      self.first_name = first_name
      self.last_name = last_name
      self.email = email


  def __str__(self): 
    return f"{self.last_name}, {self.first_name} [{self.account_id}]"


  def getaccount_id(self):
    return self.account_id


  def getaccount_type(self):
    return self.account_type

  def setaccount_type(self, account_type):
    self.account_type = account_type


  def getUsername(self):
    return self.username
  
  def setUsername(self, uname):
    self.username = uname


  def getPassword(self):
    return self.password

  def setPassword(self, password):
    self.password = password


  def getfirst_name(self):
    return self.first_name

  def setfirst_name(self, fname):
    self.first_name = fname


  def getlast_name(self):
    return self.last_name

  def setlast_name(self, lname): 
    self.last_name = lname


  def getEmail(self):
    return self.email

  def setEmail(self, email):
    self.email = email




#Account Controller
class AccountController: 
  """
  A controller class for account objects, in particular the activeUser object 
  which represents the currently logged in user in a session
  
  ...
  Attributes
  ----------
  activeUser : Account
      The currently logged in user

  Methods
  -------
  createAccount():
      creates a new account object and calls function to update the database

  updateAccount():
      updates the activeUser information and writes the new values to the database

  readAccount(): 
      calls the account_data_controller to read the database, and sets
      the activeUser to the returned values 

  deleteAccount():
      sets the active user to null (execpt for id) and then updates the
      database with the null values
  
  getAllCat():
      calls the database to get a list of all categories belonging to this user
      *note, requires categories.py functions that are not functioning

  getSubscriptions():
      calls the database to get a list of all categories the activeUser is subscribed to
      *note, requires categories.py functions that are not functioning
      
  """
  activeUser = Account()

  def __init__(self, activeUser = None): 

    self.acvtiveUser = activeUser

    
  #not needed. Use updateAccount instead
  def createAccount(aType, uname, passw, fname, lname, email):

    #first update 'active' account object
    AccountController.activeUser.setaccount_type(None)
    AccountController.activeUser.setUsername(uname)
    AccountController.activeUser.setPassword(passw)
    AccountController.activeUser.setfirst_name(fname)
    AccountController.activeUser.setlast_name(lname)
    AccountController.activeUser.setEmail(email)

    results = account_data_controller.write_account(AccountController.activeUser)

    #then call writeDB to update in DB
    if results[0] == False:

      print("Account was not updated in the databse. {}".format(results[1]))
      return -1

    else: 
      return 0



  def updateAccount(id, aType, uname, passw, fname, lname, email):

    #first update 'active' account object
    AccountController.activeUser.setaccount_type(aType)
    AccountController.activeUser.setUsername(uname)
    AccountController.activeUser.setPassword(passw)
    AccountController.activeUser.setfirst_name(fname)
    AccountController.activeUser.setlast_name(lname)
    AccountController.activeUser.setEmail(email)

    #then call writeDB to update in DB
    results = account_data_controller.write_account(AccountController.activeUser)

    if results[0] == False:

      print("Account was not updated in the databse. {}".format(results[1]))
      return -1
    else: 
      return 0



  def readAccount(id):

    activeAccount = Account()

    activeAccount.account_id = id

    results = account_data_controller.read_account(activeAccount)

    if results[0] == True:

      #print("THE ACCOUNT READ WAS {}".format(activeAccount), file=sys.stdout)

      activeAccount.account_type = results[1]
      activeAccount.username = results[2]
      activeAccount.first_name = results[3]
      activeAccount.last_name = results[4]
      activeAccount.email = results[5]

      return activeAccount
    
    else:

      print("readAccount failed")
      return None


  def deleteAccount(): 

      #first update 'active' account object
      AccountController.activeUser.setaccount_type(None)
      AccountController.activeUser.setUsername(None)
      AccountController.activeUser.setPassword(None)
      AccountController.activeUser.setfirst_name(None)
      AccountController.activeUser.setlast_name(None)
      AccountController.activeUser.setEmail(None)

      #then call writeDB to update in DB

      results = account_data_controller.write_account(AccountController.activeUser)

      if results[0] == False:

        print("Account was not deleted in the databse. {}".format(results[1]))
        return -1
      else: 
        return 0

#Cannot test these functions until categories code is completed / debugged
"""
  #Note: can't test until categories code is completed / debugged
  def getAllCat():

    #results = category_data_controller.read_all_category(AccountController.activeUser.account_id)

    results = None
    print("getAllcatResults are: {}".format(results), file=sys.stdout)
    return results


  #Note: can't test until categories code is completed / debugged
  def getSubscriptions():

    results = subscription_data_controller.read_all_subscription(AccountController.activeUser.account_id)
    print("Get All Subscription Results are: {}".format(results), file=sys.stdout)

    return results
"""

