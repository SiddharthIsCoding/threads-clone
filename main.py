import flask , mysql.connector , random , time

from flask import *

myconn = mysql.connector.connect(host='localhost',user='root',passwd='root',db="threadsbase")

mycur = myconn.cursor()

print("db connection : " ,myconn)

myapp = Flask(__name__)

myapp.secret_key = "billiejean##notmylover&&&"

@myapp.route("/login")
def login():
    return render_template("login.html")

@myapp.route("/signup")
def signup():
    return render_template("signup.html")

@myapp.route("/submit", methods=['POST'])
def submit():
    

    uid = random.randint(0,1000)
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    name = request.form.get("full_name")


    try:
        query = "INSERT INTO users VALUES (%s, %s, %s, %s, %s)"
        values = (uid, username, password, email, name)

        mycur.execute(query, values)
        myconn.commit()

        session['user'] = username

        print("inserted data", uid, username, email, password, name)
        return redirect("/") 
    
    

    except Exception as e:
        print(e)
        return redirect("/signup")




@myapp.route("/")
def home():
    if 'user' in session:
        return render_template("home.html",logged_in = True , user = session['user'])
    else:
        return render_template("home.html" , logged_in = False)

@myapp.route("/logout")
def logout():
    session.pop('user',None)
    return redirect('/')

@myapp.route("/loginsubmit", methods=['POST'])
def loginsubmit():
    username = request.form.get("username")
    password = request.form.get("password")

    print(username , password)

    mycur.execute("SELECT * FROM users WHERE username = %s AND password = %s",(username,password))

    user = mycur.fetchone()

    if user:
        print("found")
        session['user'] = username
        return redirect("/")
    else:
        return redirect("/login")
    
@myapp.route("/profile")
def profile():
    return render_template('profile.html',logged_in=True, user = session['user'])
    
    

if __name__ == "__main__":
    myapp.run(debug=True)