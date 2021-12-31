from os import name
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
import mysql.connector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SESSION_TYPE'] = 'sqlalchemy'

app = Flask(__name__, static_folder="/static")

db = SQLAlchemy(app)
app.config['SESSION_SQLALCHEMY'] = db

mydb = mysql.connector.connect( host="localhost", port="3306", user="root", password="QWERTY280921", database="prthmdb",auth_plugin="mysql_native_password")
mycursor = mydb.cursor()

class Info(db.Model):
    username = db.Column(db.String(50), primary_key = True)
    password = db.Column(db.String(100), nullable = False)

@app.route('/')
def login():
    return render_template("login.html")

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(200), nullable = False) 
    type = db.Column(db.String(50), nullable = False)
    status = db.Column(db.String(50), nullable = False)
    title = db.Column(db.String(200), nullable = False)
    doi = db.Column(db.String(200), )
    date = db.Column(db.DateTime, nullable = False)
    affiliation = db.Column(db.String(200), nullable = False) 
    indexing = db.Column(db.String(200), nullable = False) 

    def _repr_(self):
        return '<Name %r>' %self.name

@app.route('/home',methods = ["GET","POST"])
def index():
    username = request.form.get("username")
    password = request.form.get("pass")
    mycursor.execute("select username,password from credentials")
    myres=mycursor.fetchall()
    flag = 0
    for row in myres:
        print(row[1])
        if(username == row[0]):
            if(password == row[1]):
                print("hello")
                flag = 1
    if(flag==0):
        return("Username And Password Do Not Match With Our Database!")
    else:
        return render_template("index.html")

@app.route('/submitted', methods=["GET","POST"])
def sub():
    id = request.form.get("id")
    name = request.form.get("name")
    type = request.form.get("type")
    status = request.form.get("status")
    title = request.form.get("title")
    doi = request.form.get("doi")
    date = request.form.get("date")
    affiliation = request.form.get("affiliation")
    indexing = request.form.get("indexing")
    mycursor.execute("select Emp_ID from employee")
    myres=mycursor.fetchall()
    flag = 0
    for row in myres:
        if(id == row[0]):
            flag = 1
    if(flag==0):
        return render_template("error.html")
    else:
        sql = "INSERT INTO publication (Emp_ID, Publisher_Name, Type, Status, Title, DOI, Pdate, Affiliation, Indexing) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (id,name,type,status,title,doi,date,affiliation,indexing)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("select * from publication")
        data=mycursor.fetchall()
        mydb.commit()
        return render_template("display.html", data=data)

if __name__ == '__main__':  
    app.run(debug=True)