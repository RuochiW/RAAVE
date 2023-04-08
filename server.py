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



#ls has major formatting issues
@app.route('/login/calendar/view_events/')
def view_events():

    if request.args.get('event_list') is None:
        return redirect('calendar')
    else:
        headers = ("Event ID", "Event Type", "Visibility", "Name", "Category", "Start Date", "End Date")
        ls = request.args.getlist('event_list')
        ls.pop(0)
        

        demo_data = (
            ("1", "2", "0", "A1", "1", "2023-09-15 10:30:00", "2023-09-15 12:00:00"),
            ("1", "1", "0", "Wash Car", "1", "2023-09-15 14:30:00", "2023-09-15 15:15:00"),
            ("1", "1", "0", "Work Out", "1", "2023-09-15 20:00:00", "2023-09-15 20:45:00")            
        )
        
        return render_template('table.html', headings=headers, data=demo_data)
        #return f"{ls[0]},\n{ls[1]},\n{ls[2]}, \t {len(ls)}"
        #can access ls row by row but it is filled with whitespaces



@app.route('/login/calendar/', methods=['POST', 'GET'])
def user_events():

    id = ac_controller.active_user.account_id #acc_id of the currently logged in user
    c = Category(id)
    events = read_all_event(c)

    if request.method == 'GET':
        return redirect(url_for('view_events', event_list=events))
    else:
        return redirect('calendar')

# renders a super simple calendar
@app.route('/calendar')
def show_calendar():
    return render_template('calendar.html')


# clicking on view calendar in navbar will render a calendar
@app.route('/home')
def home_view():
    return render_template('base.html')




# loads login page on application launch
@app.route('/')
def index():
    return render_template('index.html')


# handles submission of login form
@app.route('/login', methods=('GET', 'POST'))
def login():
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

            # testing get all subs
            # allSubs = AcController.getSubscriptions()

            # print("All Subs are: {}".format(*allSubs), file=sys.stdout)

            # end testing

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



# handles create account form submission
@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
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


# handles log out button
@app.route('/logout', methods=['GET', 'POST'])
def sign_out():
    ac_controller.active_user = None

    return redirect(url_for('index'))


# handles navigation to the home page
@app.route('/home', methods=['GET', 'POST'])
def returnHome():
    return render_template('base.html')


# handles navigation to the create category page
@app.route('/NavCreateCat', methods=['GET', 'POST'])
def NavCreateCat():
    return render_template('create_category.html')

# handles navigation to the create event page
@app.route('/NavCreateEvent', methods=['GET', 'POST'])
def NavCreateEvent():
    return render_template('create_event.html')

# handles submission of create category form
@app.route('/createCategory', methods=['GET', 'POST'])
def createCategory():
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


# handles submission of create event form
@app.route('/createEvent', methods=['GET', 'POST'])
def createEvent():
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
