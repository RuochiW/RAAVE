# Written by Austin Shouli
# Contains Account and Account Controller Classes


# import pydoc
# import sys

# Accounts Class
class Account:
    """
    A class to represent a user's account
    
    ...
    Attributes
    ----------
    account_id : int
        unique id for the account
    account_type : int
        account type - student, professor
    username : str
        unique account username
    password : str
        unique account password
    first_name : str
        user's first name
    last_name : str
        user's last name
    email : str
        user's email address
  
    Methods
    -------
    get_account_id():
        returns the account_id field
  
    get_account_type(self):
      returns the account_type field
  
    set_account_type(self, account_type):
      sets the account_type field
  
    get_username(self):
      returns the username field
    
    set_username(self, username):
     sets the username field
  
    get_password(self):
      returns the password field
  
    set_password(self, password):
      sets the password field
  
    get_first_name(self):
     returns the first_name field
  
    set_first_name(self, first_name):
      sets the first_name field
  
    get_last_name(self):
      returns the last_name field
  
    set_last_name(self, last_name):
      sets the last_name field
  
    get_email(self):
      returns the email field
  
    set_email(self, email):
      sets the email field

    """

    account_id = int()
    account_type = int()
    username = str()
    password = str()
    first_name = str()
    last_name = str()
    email = str()

    def __init__(self, account_id=None, account_type=None, username="", password="", first_name="", last_name="",
                 email=""):
        self.account_id = account_id
        self.account_type = account_type
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return f"{self.last_name}, {self.first_name} [{self.account_id}]"

    def get_account_id(self):
        return self.account_id

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
