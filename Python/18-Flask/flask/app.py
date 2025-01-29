from flask import Flask, render_template

# This is the WSGI  application that will
app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    #return 'Welcome to the Flask Course!!!'
    return "<html><head><title>Welcome to the Flask Course</title></head><body><h1>Welcome to the Flask Course</h1></body></html>"
@app.route('/login', methods=['GET', 'POST'])
def welcome_index():
    return render_template('index.html')


# This is a route that will respond to GET requests at the / URL
if __name__ == '__main__':
    app.run(debug=True)