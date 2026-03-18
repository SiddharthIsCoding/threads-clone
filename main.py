import flask , mysql.connector
from flask import *



myapp = Flask(__name__)


@myapp.route("/home")
def home():
    return render_template("home.html")

@myapp.route("/login")
def login():
    return render_template("login.html")

@myapp.route("/signup")
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    myapp.run(debug=True)