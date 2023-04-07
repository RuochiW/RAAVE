# Written by Austin Shouli
# Contains Account and Account Controller Classes


# import pydoc
# import sys

from data.data_controller.account_data_controller import write_account, read_account
from data.data_controller.category_data_controller import read_all_category
from data.data_controller.subscription_data_controller import read_all_subscription
from src.accounts import Account


# Account Controller


def create_account(username, password, first_name, last_name, email):
    # first update 'active' account object
    update_account(None, username, password, first_name, last_name, email)


def update_account(account_type, username, password, first_name, last_name, email):
    # first update 'active' account object
    AccountController.active_user.set_account_type(account_type)
    AccountController.active_user.set_username(username)
    AccountController.active_user.set_password(password)
    AccountController.active_user.set_first_name(first_name)
    AccountController.active_user.set_last_name(last_name)
    AccountController.active_user.set_email(email)

    # then call writeDB to update in DB
    result = write_account(AccountController.active_user)

    if not result[0]:

        print("Account was not updated in the database. {}".format(result[1]))
        return -1
    else:
        return 0


def read_user_account(account_id):
    active_account = Account()

    active_account.account_id = account_id

    result = read_account(active_account)

    if result[0]:

        # print("THE ACCOUNT READ WAS {}".format(active_account), file=sys.stdout)

        active_account.account_type = result[1]
        active_account.username = result[2]
        active_account.first_name = result[3]
        active_account.last_name = result[4]
        active_account.email = result[5]

        return active_account

    else:

        print("read_account failed")
        return None


def delete_account():
    # first update 'active' account object
    AccountController.active_user.set_account_type(None)
    AccountController.active_user.set_username(None)
    AccountController.active_user.set_password(None)
    AccountController.active_user.set_first_name(None)
    AccountController.active_user.set_last_name(None)
    AccountController.active_user.set_email(None)

    # then call writeDB to update in DB

    result = write_account(AccountController.active_user)

    if not result[0]:

        print("Account was not deleted in the database. {}".format(result[1]))
        return -1
    else:
        return 0


def get_all_category():
    result = read_all_category(AccountController.active_user.account_id)

    if not result[0]:

        print("Unable to get all categories. {}".format(result[1]))
        return -1
    else:

        # print("get_all_category result are: {}".format(result), file=sys.stdout)
        return result[:1]


def get_subscriptions():
    result = read_all_subscription(AccountController.active_user.account_id)

    if not result[0]:

        print("Unable to get subscriptions. {}".format(result[1]))
        return -1
    else:

        # print("get_subscriptions result are: {}".format(result), file=sys.stdout)
        return result[:1]


class AccountController:
    """
    A controller class for account objects, in particular the active_user object
    which represents the currently logged-in user in a session

    ...
    Attributes
    ----------
    active_user : Account
        The currently logged in user

    Methods
    -------
    create_account(username, password, first_name, last_name, email):
        creates a new account object and calls function to update the database

    update_account(account_type, username, password, first_name, last_name, email):
        updates the active_user information and writes the new values to the database

    read_active_account(account_id):
        calls the account_data_controller to read the database, and sets
        the active_account to the returned values

    delete_account():
        sets the active_user to null (except for id) and then updates the
        database with the null values

    get_all_category():
        calls the database to get a list of all categories belonging to the active_user
        *note, requires categories.py functions that are not functioning

    getSubscriptions():
        calls the database to get a list of all categories the active_user is subscribed to
        *note, requires categories.py functions that are not functioning

    """
    active_user = Account()

    def __init__(self, active_user=None):
        self.active_user = active_user

    # not needed. Use updateAccount instead
