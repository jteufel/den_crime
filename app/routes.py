from flask import render_template
from app import app
from db_query import *

@app.route('/')
@app.route('/index')

def index(): #from flask tutorial

    conn = DB_Connect() #connect to database
    json_data = Build_JSON(conn,"crime") #function to query database and store statisical data in dict
    Write_JSON(json_data ,"data/crime.json") #write json to be read by .js file
    DB_Close(conn)

    return render_template('crime.html')
