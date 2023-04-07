# Written by Austin Shouli
import sys
from flask import Flask, render_template, redirect, url_for, request, flash

from data.authentication.user_authentication import user_login
from data.data_controller.account_data_controller import write_account
from data.data_controller.event_data_controller import write_event
from src.account_controller import AccountController, read_user_account
from src.accounts import Account
from src.events import Event

app = Flask(__name__)
# root_path='server', static_folder='server/static',
#             template_folder='server/templates'

app.secret_key = 'super secret key'

# from data import tables

# tables.create_tables()


account_controller = AccountController()


# renders a super simple calendar
@app.route('/calendar')
def show_calendar():
    return render_template('calendar.html')


@app.route('/event_input', methods=["POST", "GET"])
def event_input():
    if request.method == "POST":
        user = request.form["nm"]

        return redirect(url_for("event", usr=user))
    else:
        return render_template('event_input.html')


# clicking on view calendar in navbar will render a calendar
@app.route('/home')
def home_view():
    return render_template('base.html')


@app.route("/event_input/<usr>")
def event(usr):
    return f"<h1>Post successful {usr}!</h1>"


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
            account_controller.active_user = read_user_account(login_attempt[1])

            print("Account logged in is: {}".format(account_controller.active_user), file=sys.stdout)
            print("Account Type is: {}".format(account_controller.active_user.account_type), file=sys.stdout)

            # testing get all subs
            # allSubs = account_controller.getSubscriptions()

            # print("All Subs are: {}".format(*allSubs), file=sys.stdout)

            # end testing

            print("Server Sees Logged In. accountID is: {}".format(login_attempt[1]), file=sys.stdout)
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
        new_account.first_name = request.form['first_name']
        new_account.last_name = request.form['last_name']
        new_account.email = request.form['email']

        result = write_account(new_account)

        # debugging
        # print("Result of write is: " + {result[0]} + result[1])

        if result[0]:
            flash('Account successfully created. Please log in')

        else:

            print("DB Error: {}", result[1], file=sys.stdout)  # Debugging: sql error to terminal
            flash('There was an error creating your account. Please try again.')

        return redirect(url_for('index'))

    return render_template('create_account.html')


# handles log out button
@app.route('/logout', methods=['GET', 'POST'])
def sign_out():
    account_controller.active_user = None

    return redirect(url_for('index'))


# handles navigation to Create Event page
@app.route('/home', methods=['GET', 'POST'])
def returnHome():
    return render_template('base.html')


# handles navigation to the home page
@app.route('/NavCreateEvent', methods=['GET', 'POST'])
def NavCreateEvent():
    return render_template('create_event.html')


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
            flash('Event successfully created')
            print("DB Write Event Successful", file=sys.stdout)  # Debugging: sql error to terminal

        else:

            print("DB Error: {}", result[1], file=sys.stdout)  # Debugging: sql error to terminal
            flash('There was an error creating your event. Please try again.')

        return render_template('base.html')


# sets host port and debug mode
if __name__ == '__main__':
    app.run(host="localhost", port=1234, debug=True)
