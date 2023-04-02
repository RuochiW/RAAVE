from flask import Flask, render_template, redirect, url_for, request, flash


app = Flask(__name__)
app.secret_key = 'super secret key'


from src import accounts
from data.data_controller import account_data_controller
from data.authentication import user_authentication

from data import tables
import sys

#tables.create_tables()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':

        loginAccount = accounts.Account()

        loginAccount.username = request.form['username']
        loginAccount.password = request.form['password']

        loginAtempt = user_authentication.logging(loginAccount)

        if loginAtempt[0] == True: 

            #create new account controller
            #AcController = accounts.AccountController() 

            print("Server Sees Logged In. accountID is: {}".format(loginAtempt[1]), file=sys.stdout)
            return render_template('logged_in.html')
            #AcController.activeUser.accountID = loginAtempt[2]
            
        else: 
  
            print("DB Error: {}", loginAtempt[1], file=sys.stdout) #Debugging: sql error to terminal
            flash('Your Account was not found. Please try again.')
            return redirect(url_for('index')) ##########

        #  return redirect(url_for('success', name=user))
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

