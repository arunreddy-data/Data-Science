from flask import Flask

"""
It Creates an instance of the Flask Class,
which will be your WSGI (Web Server Gateway Interface) application.
"""
### WSGI Application
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to best Flask Course"


@app.route("/index")
def index():
    return "Welcome to the index page"


print(app.url_map)


if __name__ == "__main__":  # From here execution will start (starting point)
    app.run(debug=True)
