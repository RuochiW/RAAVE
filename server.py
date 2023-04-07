# Written by Austin Shouli

from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = 'super secret key'


from src import accounts
from src import events
from data.data_controller import account_data_controller
from data.data_controller import event_data_controller
from data.authentication import user_authentication

from data import tables

#tables.create_tables()

import sys

AcController = accounts.AccountController()

#renders a super simple calendar
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

#clicking on view calendar in navbar will render a calendar
@app.route('/home')
def home_view():
    return render_template('base.html')

@app.route("/event_input/<usr>")
def event(usr):
    return f"<h1>Post successful {usr}!</h1>"

#loads login page on application launch
@app.route('/')
def index():
    return render_template('index.html')


#handles submission of login form
@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':

        loginAccount = accounts.Account()

        loginAccount.username = request.form['username']
        loginAccount.password = request.form['password']

        loginAtempt = user_authentication.login(loginAccount)

        if loginAtempt[0] == True: 


            #set activeUser's attributes to the database values
            AcController.activeUser = accounts.AccountController.readAccount(loginAtempt[1])

            print("Account logged in is: {}".format(AcController.activeUser), file=sys.stdout) 
            print("Account Type is: {}".format(AcController.activeUser.account_type), file=sys.stdout) 

            #testing get all subs
            # allSubs = AcController.getSubscriptions()

            # print("All Subs are: {}".format(*allSubs), file=sys.stdout)

            #end testing

            print("Server Sees Logged In. accountID is: {}".format(loginAtempt[1]), file=sys.stdout)
            return render_template('base.html')

        else: 
  
            print("Database Exception: {}", loginAtempt[1], file=sys.stdout) #Debugging: sql error to terminal
            flash('Your Account was not found. Please try again.')
            return redirect(url_for('index')) 

    else:
        print("Test Point 1", sys.stdout)
        user = request.args.get('username')
        return redirect(url_for('success1', name=user))


#handles create account form submission
@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':

        #try to create account in DB. 
        newAccount = accounts.Account()
        newAccount.username = request.form['username']
        newAccount.password = request.form['password']
        newAccount.account_type = request.form['type']
        newAccount.first_name = request.form['fname']
        newAccount.last_name = request.form['lname']
        newAccount.email = request.form['email']

        result = account_data_controller.write_account(newAccount)

        #debugging
        #print("Result of write is: " + {result[0]} + result[1])
        
        if result[0] == True:
            flash('Account Succesfully created. Please log in')

        else: 

            print("DB Error: {}", result[1], file=sys.stdout) #Debugging: sql error to terminal
            flash('There was an error creating your account. Please try again.')
        
        return redirect(url_for('index'))

    return render_template('create_account.html')


#handles log out button
@app.route('/logout', methods=['GET', 'POST'])
def sign_out():
     
     AcController.activeUser = None

     return redirect(url_for('index'))


#handles navigation to Create Event page
@app.route('/NavCreateEvent', methods=['GET', 'POST'])
def NavCreateEvent():

    return render_template('create_event.html')
    

#handles submission of create event form 
@app.route('/createEvent', methods=['GET', 'POST'])
def createEvent():
    if request.method == 'POST':

        #handle submit for create event
        newEvent = events.Event()

        newEvent.name = request.form['event_name']
        newEvent.category = request.form['category']
        newEvent.start_date = request.form['start_date']
        newEvent.end_date = request.form['end_date']
        newEvent.visibility = request.form['visibility']

        result = event_data_controller.write_event(newEvent)        

        if result[0] == True:
            flash('Event Succesfully created.')
            print("DB Write Event Successful", file=sys.stdout) #Debugging: sql error to terminal
        
        else: 

            print("DB Error: {}", result[1], file=sys.stdout) #Debugging: sql error to terminal
            flash('There was an error creating your event. Please try again.')
        

        return render_template('base.html')


#sets host port and debug mode
if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)

