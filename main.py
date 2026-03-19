import flask , mysql.connector , random

from flask import *

myconn = mysql.connector.connect(host='localhost',user='root',passwd='root',db="threadsbase")

mycur = myconn.cursor()

print("db connection : " ,myconn)

myapp = Flask(__name__)


@myapp.route("/")
def home():
    return render_template("home.html")

@myapp.route("/login")
def login():
    return render_template("login.html")

@myapp.route("/signup")
def signup():
    return render_template("signup.html")

@myapp.route("/submit", methods=['POST'])
def submit():
    print("bitch look at me")
    uid = random.randint(0,1000)
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    name = request.form.get("name")

    try:
        query = "INSERT INTO users VALUES (%s, %s, %s, %s, %s)"
        values = (uid, username, password, email, name)

        mycur.execute(query, values)
        myconn.commit()

        print("inserted data", uid, username, email, password, name)
        return "Signup successful"

    except Exception as e:
        print("Error:", e)
        return "Signup failed"
    


if __name__ == "__main__":
    myapp.run(debug=True)