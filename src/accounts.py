# Written by Austin Shouli
# Contains Account and Account Controller Classes


import pydoc
import sys

from data.data_controller.account_data_controller import write_account, read_account


#from data.data_controller import category_data_controller
#from data.data_controller import subscription_data_controller


#Accounts Class
class Account:
  """
  A class to represent an user's account
  
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
      returns the account_id

  !Continue adding methods..
  
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
  A class to controller account objects
  
  ...
  Attributes
  ----------
  activeUser : Account
      The currently logged in user

  Methods
  -------
  createAccount():
      creates a new account object and calls function to update the database

  

  !Continue adding methods..
  
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

    results = write_account(AccountController.activeUser)

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
    results = write_account(AccountController.activeUser)

    if results[0] == False:

      print("Account was not updated in the databse. {}".format(results[1]))
      return -1
    else: 
      return 0



  def readAccount(id):

    account_r = Account()

    account_r.account_id = id

    results = read_account(account_r)

    if results[0] == True:

      #print("THE ACCOUNT READ WAS {}".format(read_account), file=sys.stdout)

      account_r.account_type = results[1]
      account_r.username = results[2]
      account_r.first_name = results[3]
      account_r.last_name = results[4]
      account_r.email = results[5]

      return account_r
    
    else:

      print("readAccount FAILED!!")
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

      results = write_account(AccountController.activeUser)

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


#NO LONGER NEEDED. WILL PROBABLY REMOVE
# class ViewAccountController:

  # def login(uname, passw): 

  #   tempAcc = Account

  #   tempAcc.username = uname
  #   tempAcc.password = passw

  #   print("Accessed Login Function...")

  #   #Uncomment when linked to DB functions
  #   if data.readAccount(tempAcc):

  #     #login successful 
  #     return True
  #   else: 
  #     return None

  #   return True

