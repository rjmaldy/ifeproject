# this is my ife project (legit)
import os
from app import app
from flask import render_template, request, redirect
# events = [
#         {"event":"First Day of Classes", "date":"2019-08-21"},
#         {"event":"Winter Break", "date":"2019-12-20"},
#         {"event":"Finals Begin", "date":"2019-12-01"},
#         {"event":"Marieke's Birthday", "date":"2020-02-27"}
#     ]
from flask_pymongo import PyMongo
# name of database
app.config['MONGO_DBNAME'] = 'ife' 
# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://bigbody:bruh@cluster0-qxa0w.mongodb.net/ife?retryWrites=true&w=majority' 
mongo = PyMongo(app)
# INDEX
@app.route('/')
@app.route('/index')
def index():
    # connect to the database
    collection = mongo.db.events
    # pull data from database
    events = collection.find({}).sort("date", -1)
    # use data
    return render_template('index.html', events = events)
# CONNECT TO DB, ADD DATA
@app.route('/add')
def add():
    # connect to the database
    events = mongo.db.events
    # insert new data
    events.insert({"event":"Marieke's Birthday", "date":"2019-02-27"})
    # return a message to the user
    return "Event added"
@app.route('/events/new', methods=["GET","POST"])
def events_new():
    userdata = dict(request.form)
    print(userdata)
    events = mongo.db.events
    events.insert(userdata)
    return redirect('/')
@app.route('/name/<name>')
def name(name):
    # connect to the database
    collection = mongo.db.events
    # pull data from database
    events = collection.find({"user_name":name}).sort("date", -1)
    # use data
    return render_template('index.html')
    
@app.route('/signup', methods=["GET","POST"])
def signup():
    if request.method == "POST":
        users = mongo.db.users
        existing_users = users.find_one({"username":request.form['username']})
        if existing_users is None:
            users.insert({"username":request.form['username'],"password":request.form})
            return "Login successful"
        else:
            return "Username unavailable, fool. Log in or pick a new name."
    else:
        return render_template('signup.html')
    





    
