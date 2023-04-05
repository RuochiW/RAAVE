# Written by Austin Shouli

from flask import Flask, render_template, redirect, url_for, request, flash


app = Flask(__name__)
app.secret_key = 'super secret key'


from src import accounts
from src import events
from data.data_controller import account_data_controller
from data.authentication import user_authentication

from data import tables

#tables.create_tables()

import sys

AcController = accounts.AccountController()




@app.route('/event_input', methods=["POST", "GET"])
def event_input():
    if request.method == "POST":
        user = request.form["nm"]
        
        return redirect(url_for("event", usr=user))
    else:
        return render_template('event_input.html')

@app.route("/event_input/<usr>")
def event(usr):
    return f"<h1>Post successful {usr}!</h1>"


@app.route('/')
def index():
    return render_template('index.html')


#remove this
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


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
            return render_template('event_input.html')

        else: 
  
            print("Database Exception: {}", loginAtempt[1], file=sys.stdout) #Debugging: sql error to terminal
            flash('Your Account was not found. Please try again.')
            return redirect(url_for('index')) 

    else:
        print("Test Point 1", sys.stdout)
        user = request.args.get('username')
        return redirect(url_for('success1', name=user))



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

    



    
if __name__ == '__main__':
    app.run(debug=True)

