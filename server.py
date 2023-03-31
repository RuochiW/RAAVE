from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


from src import accounts


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
            return redirect(url_for('LoginFailed', name=user))

        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('username')
        return redirect(url_for('success1', name=user))



if __name__ == '__main__':
    app.run(debug=True)




    