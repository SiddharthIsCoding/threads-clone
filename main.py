import flask
from flask import *

myapp = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html")


