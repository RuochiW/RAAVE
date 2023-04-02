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

  def __init__(self, activeUser): 

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

    #then call writeDB to update in DB
    if data.writeAccount(AccountController.activeUser):

      print("Account was not updated in the databse")
      return -1

    else: 

      #need to get back account ID from DB here
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
    if data.writeAccount(AccountController.activeUser):

      print("Account was not updated in the databse")
      return -1
    else: 
      return 0



  def readAccount(id):

    results = data.readAccount(id)

    read_account = Account()

    read_account.account_id = results[2]
    read_account.account_type = results[3]
    read_account.username = results[5]
    read_account.password = results[6]
    read_account.first_name = results[7]
    read_account.last_name = results[8]
    read_account.email = results[9]

    return read_account


def deleteAccount(): 

     #first update 'active' account object
    AccountController.activeUser.setaccount_type(None)
    AccountController.activeUser.setUsername(None)
    AccountController.activeUser.setPassword(None)
    AccountController.activeUser.setfirst_name(None)
    AccountController.activeUser.setlast_name(None)
    AccountController.activeUser.setEmail(None)

    #then call writeDB to update in DB
    if data.writeAccount(AccountController.activeUser):

      print("Account was not deleted in the databse")
      return -1
    else: 
      return 0


def getAllCat():

  results = data.readAllCategory(AccountController.activeUser.account_id)
  return results


#get and return a list of all courses the user is subscribed to
def getSubscriptions():

  #note: data.readAllSubscriptions does not exist yet...
  results = data.readAllSubscriptions(AccountController.activeUser.account_id)
  return results



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





#Testing Account Class 
"""
# testAccount = Account(1234, 0, "username1", "password1", "fname", "lname", "email")

# print("Print Account: ", testAccount)
  
# print("Account ID is: ", testAccount.getaccount_id())

# print("Account Type is: ", testAccount.getaccount_type())

# testAccount.setEmail("email@emails.com")

# print("My new email is: ", testAccount.getEmail())
	
"""