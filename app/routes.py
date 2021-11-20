from flask import Flask             # From the flask module import the Flask class.

app = Flask(__name__)               # We are instantiating our Flask class into
                                    # our app variable


@app.route("/")                     # A decorator that creates a new HTTP path.
def index():                        # In the context of flask, this is a view function.
    return "<h1>Hello, world!</h1>" # return statement


@app.route("/users/memo")
def about_memo():
    me = {
        "first_name": "Guillermo",
        "last_name": "Monge",
        "hobbies": "Videogames",
        "active": True
    }
    return me


@app.route("/greeting/<name>")
def print_name(name):
    return "<h1>Hello, %s!</h1>" % name


@app.route("/square/<int:num>")
def square_num(num):
    return "<h1>That number, squared, is: %s</h1>" % (num**2)