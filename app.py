from flask import Flask, redirect, render_template, request
import sqlite3 
from helpers import hash 
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
@app.route("/login", methods=["GET", "POST"])
def login():
    
    return render_template("login.html") 


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")  
        password = hash(request.form.get("password"))
        con = sqlite3.connect("quote.db")
        cur = con.cursor()
        action = cur.execute("insert into users(username, password) values(?,?)",(username,password,))
    
        con.commit() 
        con.close()
        return redirect("/") 


    return render_template("register.html");
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = hash(request.form.get("password")) 
        con = sqlite3.connect("quote.db")
        cur = con.cursor
        query = cur.execute("SELECT * FROM users WHERE username=?",(username,))
        if(len(query) > 0 and query[0]["password"] == password):
            print("why u gay")
            return True; 
    return render_template("gay")

@app.route("/")
def index():
     
    return render_template("home.html")
