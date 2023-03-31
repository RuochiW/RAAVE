# Written by Austin Shouli
# Contains Account and Account Controller Classes


import pydoc



import data


#Accounts Class
class Account:
  """
  A class to represent an user's account
  
  ...
  Attributes
  ----------
  accountID : int
      unique id for the account
  AccountType : int
      account type - student, proffesor
  username : str
      unique account username
  password : str
      unique account password
  firstName : str
      user's first name
  lastName : str
      user's last name
  email : str
      user's email adddress

  Methods
  -------
  getAccountID():
      returns the accountID

  !Continue adding methods..
  
  """
  accountID = int()
  AccountType = int()
  username = str()
  password = str()
  firstName = str()
  lastName = str()
  email = str()

  def __init__(self, accountID = -1, AccountType = -1, 
              username = "", password = "", 
              firstName = "",  lastName = "", email = ""):

      self.accountID = accountID
      self.AccountType = AccountType
      self.username = username
      self.password = password
      self.firstName = firstName
      self.lastName = lastName
      self.email = email


  def __str__(self): 
    return f"{self.lastName}, {self.firstName} [{self.accountID}]"


  def getAccountID(self):
    return self.accountID


  def getAccountType(self):
    return self.AccountType

  def setAccountType(self, AccountType):
    self.AccountType = AccountType


  def getUsername(self):
    return self.username
  
  def setUsername(self, uname):
    self.username = uname


  def getPassword(self):
    return self.password

  def setPassword(self, password):
    self.password = password


  def getFirstName(self):
    return self.firstName

  def setFirstName(self, fname):
    self.firstName = fname


  def getLastName(self):
    return self.lastName

  def setLastName(self, lname): 
    self.lastName = lname


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

  def __init__(self, activeUser): 

    self.acvtiveUser = activeUser

    
  #not needed. Use updateAccount instead
  def createAccount(aType, uname, passw, fname, lname, email):

    #first update 'active' account object
    AccountController.activeUser.setAccountType(None)
    AccountController.activeUser.setUsername(uname)
    AccountController.activeUser.setPassword(passw)
    AccountController.activeUser.setFirstName(fname)
    AccountController.activeUser.setLastName(lname)
    AccountController.activeUser.setEmail(email)

    #then call writeDB to update in DB
    if data.writeAccount(AccountController.activeUser):

      print("Account was not updated in the databse")
      return -1

    else: 

      #need to get back account ID from DB here
      return 0



  def updateAccount(id, aType, uname, passw, fname, lname, email):

    #first update 'active' account object
    AccountController.activeUser.setAccountType(aType)
    AccountController.activeUser.setUsername(uname)
    AccountController.activeUser.setPassword(passw)
    AccountController.activeUser.setFirstName(fname)
    AccountController.activeUser.setLastName(lname)
    AccountController.activeUser.setEmail(email)

    #then call writeDB to update in DB
    if data.writeAccount(AccountController.activeUser):

      print("Account was not updated in the databse")
      return -1
    else: 
      return 0



  def readAccount(id):

    results = data.readAccount(id)

    read_account = Account()

    read_account.accountID = results[2]
    read_account.AccountType = results[3]
    read_account.username = results[5]
    read_account.password = results[6]
    read_account.firstName = results[7]
    read_account.lastName = results[8]
    read_account.email = results[9]

    return read_account


def deleteAccount(): 

     #first update 'active' account object
    AccountController.activeUser.setAccountType(None)
    AccountController.activeUser.setUsername(None)
    AccountController.activeUser.setPassword(None)
    AccountController.activeUser.setFirstName(None)
    AccountController.activeUser.setLastName(None)
    AccountController.activeUser.setEmail(None)

    #then call writeDB to update in DB
    if data.writeAccount(AccountController.activeUser):

      print("Account was not deleted in the databse")
      return -1
    else: 
      return 0


def getAllCat():

  results = data.readAllCategory(AccountController.activeUser.accountID)
  return results


#get and return a list of all courses the user is subscribed to
def getSubscriptions():

  #note: data.readAllSubscriptions does not exist yet...
  results = data.readAllSubscriptions(AccountController.activeUser.accountID)
  return results



class ViewAccountController:

  def login(uname, passw): 

    tempAcc = Account

    tempAcc.username = uname
    tempAcc.password = passw

    print("Accessed Login Function...")

    #Uncomment when linked to DB functions
    # if data.readAccount(tempAcc):

    #   #login successful 
    #   return True
    # else: 
    #   return None

    return True





#Testing Account Class 
"""
# testAccount = Account(1234, 0, "username1", "password1", "fname", "lname", "email")

# print("Print Account: ", testAccount)
  
# print("Account ID is: ", testAccount.getAccountID())

# print("Account Type is: ", testAccount.getAccountType())

# testAccount.setEmail("email@emails.com")

# print("My new email is: ", testAccount.getEmail())
	
"""