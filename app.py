from flask import Flask, redirect, render_template, request, jsonify 
 
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
    return render_template("register.html"); 

@app.route("/")
def index():
    return render_template("home.html")
 
