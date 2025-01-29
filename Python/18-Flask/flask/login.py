from flask import Flask, render_template, request, redirect

# This is the WSGI  application that will
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # This is where you would handle the POST request
        username = request.form['username']
        password = request.form['password']
        # Here you would check the username and password against a database or
        # some other secure authentication method
        if username == 'admin' and password == 'secret':
            return 'Login successful!'
        else:
            return 'Invalid credentials!'
    return render_template('login.html')

@app.route('/success/<result>')
def success(result):
    if result == 'TRUE':
        res = f'Congratulations you have passed!'
    else:
        res = 'Sorry, you have failed!'
    exp = {'code':result, 'message':res}
    return render_template('success.html', res=exp)

# Redirect example

@app.route('/')
def home():
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)