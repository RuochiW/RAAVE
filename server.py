from flask import Flask, render_template, redirect, url_for, request, flash


app = Flask(__name__)
app.secret_key = 'super secret key'


from src import accounts
from data.data_controller import account_data_controller


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        passw = request.form['password']

        loginAtempt = accounts.ViewAccountController.login(username, passw)

        if loginAtempt == True: 

            #create new account controller
            #AcController = accounts.AccountController() 
            print("Server Sees Logged In")
            return render_template('logged_in.html')
            #AcController.activeUser.accountID = loginAtempt[2]
            
        else: 
            flash('Your Account was not found. Please try again.')
            return redirect(url_for('LoginFailed', name=user))

        #  return redirect(url_for('success', name=user))
    else:
        user = request.args.get('username')
        return redirect(url_for('success1', name=user))



@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':


        
        #try to create account in DB. 
        newAccount = accounts.Account()
        newAccount.username = request.form['username']
        newAccount.password = request.form['password']
        newAccount.AccountType = request.form['type']
        newAccount.firstName = request.form['fname']
        newAccount.lastName = request.form['lname']
        newAccount.email = request.form['email']

        if account_data_controller.write_account(newAccount):
            flash('Account Succesfully created. Please log in')

        else: 
            flash('There was an error creating your account. Please try again.')
        
        return redirect(url_for('index'))

    return render_template('create_account.html')

    



    
if __name__ == '__main__':
    app.run(debug=True)

