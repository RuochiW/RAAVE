# Written by Austin Shouli, Ethan Ondzik
import sys
from flask import Flask, render_template, redirect, url_for, request, flash

from data.authentication.user_authentication import user_login
from data.data_controller.account_data_controller import write_account
from data.data_controller.event_data_controller import write_event
from data.data_controller.category_data_controller import write_category 
from src.account_controller import AccountController, read_user_account
from src.accounts import Account
from src.events import Event
from src.categories import Category
from data.data_controller import category_data_controller
from data.data_controller.event_data_controller import read_all_event
from data.data_controller import calendar_data_controller


app = Flask(__name__)
app.secret_key = 'super secret key'


ac_controller = AccountController()




@app.route('/login/calendar/view_events/')
def view_events():
    """Gets passed a list of the user events from the user_events() function.
    It takes this list of events and passes it to table.html to be rendered. The current event output from
    the database is very unconditioned."""

    #if event list is empty redirect back to calendar view
    if request.args.getlist('event_list') is None:
        return redirect('/calendar')
    else:
        headers = ("Event ID", "Event Type", "Visibility", "Name", "Category", "Start Date", "End Date")
        ls = request.args.getlist('event_list')
        ls.pop(0) #remove the [True] from the start of the list
        
        #tuple of tuples that displays nicely for the demo video
        demo_data = (
            ("1", "2", "0", "A1", "1", "2023-04-15 10:30:00", "2023-04-15 12:00:00"),
            ("1", "1", "0", "Wash Car", "1", "2023-04-15 14:30:00", "2023-04-15 15:15:00"),
            ("1", "1", "0", "Work Out", "1", "2023-04-15 20:00:00", "2023-04-15 20:45:00")
        )
        
        return render_template('table.html', headings=headers, data=demo_data)



@app.route('/login/calendar/', methods=['POST', 'GET'])
def user_events():
    """Gets the account_id of the currently logged in user and queries the database to return
    all accessable events for that user. Redirects to the ./view_events route and passes the 
    list of events from the database."""

    id = ac_controller.active_user.account_id #acc_id of the currently logged in user
    c = Category(id)
    events = read_all_event(c) #get all user events from the db

    if request.method == 'GET':
        return redirect(url_for('view_events', event_list=events))
    else:
        return redirect('calendar')


@app.route('/calendar')
def show_calendar():
    """Renders the calendar.html template. This template inherits a 
    navigation bar from the base.html template."""

    return render_template('calendar.html')


@app.route('/home')
def home_view():
    """Renders the home view for the application which consists of a navigation bar."""
    return render_template('base.html')



@app.route('/')
def index():
    """Handles the initial launch of the application, and loads the login page"""
    return render_template('index.html')



@app.route('/login', methods=('GET', 'POST'))
def login():
    """Handles the submission of the login form. Gets username and password from 
    the login page and calls functions to check if credentials are found in database.
    If found, the active_user object is populated with the account's data, and the 
    application loads the home page. If not found, a message is displayed to indicate
    the account was not found"""
    if request.method == 'POST':

        login_account = Account()

        login_account.username = request.form['username']
        login_account.password = request.form['password']

        login_attempt = user_login(login_account)

        if login_attempt[0]:

            # set activeUser's attributes to the database values
            ac_controller.active_user = read_user_account(login_attempt[1][0])

            print("Account logged in is: {}".format(ac_controller.active_user), file=sys.stdout)
            print("Account Type is: {}".format(ac_controller.active_user.account_type), file=sys.stdout)


            print("Server Sees Logged In. accountID is: {}".format(login_attempt[1]), file=sys.stdout)
            #Added By: Ethan Ondzik
            #ac_controller.active_user.account_id = int(login_attempt[1])
            return render_template('base.html')

        else:

            print("Database Exception: {}", login_attempt[1], file=sys.stdout)  # Debugging: sql error to terminal
            flash('Your Account was not found. Please try again.')
            return redirect(url_for('index'))

    else:
        print("Test Point 1", sys.stdout)
        user = request.args.get('username')
        return redirect(url_for('success1', name=user))



@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    """Handles the submission of the create account form. Gets the fields from 
    the form and passes to database function. If account is successfully created, 
    redirects to login page and displays success message. Otherwise, redirects to 
    to login page and flashes failure message."""
    if request.method == 'POST':

        # try to create account in DB.
        new_account = Account()
        new_account.username = request.form['username']
        new_account.password = request.form['password']
        new_account.account_type = request.form['type']
        new_account.first_name = request.form['fname']
        new_account.last_name = request.form['lname']
        new_account.email = request.form['email']

        result = write_account(new_account)

        # debugging
        # print("Result of write is: " + {result[0]} + result[1])

        if result[0]:
            flash('Account Succesfully created. Please log in')

        else:

            print("DB Error: {}", result[1], file=sys.stdout)  # Debugging: sql error to terminal
            flash('There was an error creating your account. Please try again.')

        return redirect(url_for('index'))

    return render_template('create_account.html')


@app.route('/logout', methods=['GET', 'POST'])
def sign_out():
    """Handles sign out button in nav bar. active_user is set to None
    and application redirects to login page."""
    ac_controller.active_user = None

    return redirect(url_for('index'))


@app.route('/home', methods=['GET', 'POST'])
def returnHome():
    """Handles the home (and 'Raven') button in the nav bar, and redirects
    to the home page."""
    return render_template('base.html')


@app.route('/NavCreateCat', methods=['GET', 'POST'])
def NavCreateCat():
    """Handles the Create Category button in the navbar. Redirects to 
    Create Category Page"""
    return render_template('create_category.html')


@app.route('/NavCreateEvent', methods=['GET', 'POST'])
def NavCreateEvent():
    """Handles the Create Event button in the navbar. Redirects to 
    Create Event Page"""
    return render_template('create_event.html')


@app.route('/createCategory', methods=['GET', 'POST'])
def createCategory():
    """Handles submission of Create Category form. Gets all form data from 
    webpage and calls function to add category to the database. Redirects to
    home page and flashes success/failure messasge."""
    if request.method == 'POST':

        # handle submit for create category
        new_cat = Category()

        new_cat.name = request.form['cat_name']
        new_cat.description = request.form['desc']
        new_cat.category_type = request.form['type']
        new_cat.owner = ac_controller.active_user.account_id
        new_cat.visibility = request.form['visibility']

        result = write_category(new_cat)

        print("DB return is: ".format(result[0]), file=sys.stdout)  # Debugging: sql error to terminal

        if result[0]:
            flash('Category Succesfully created')
            print("DB Write Category Successful", file=sys.stdout)  # Debugging: sql error to terminal

        else:

            print("DB Error: {}", result[1], file=sys.stdout)  # Debugging: sql error to terminal
            flash('There was an error creating your Category. Please try again.')

        return render_template('base.html')



@app.route('/createEvent', methods=['GET', 'POST'])
def createEvent():
    """Handles submission of Create Event form. Gets all form data from 
    webpage and calls function to add Event to the database. Redirects to
    home page and flashes success/failure messasge."""
    if request.method == 'POST':

        # handle submit for create event
        new_event = Event()

        new_event.name = request.form['event_name']
        new_event.category = request.form['category']
        new_event.start_date = request.form['start_date']
        new_event.end_date = request.form['end_date']
        new_event.visibility = request.form['visibility']

        result = write_event(new_event)

        if result[0]:
            flash('Event Succesfully created')
            print("DB Write Event Successful", file=sys.stdout)  # Debugging: sql error to terminal

        else:

            print("DB Error: {}", result[1], file=sys.stdout)  # Debugging: sql error to terminal
            flash('There was an error creating your event. Please try again.')

        return render_template('base.html')


# sets host port and debug mode
if __name__ == '__main__':
    app.run(host="localhost", port=1234, debug=True)
