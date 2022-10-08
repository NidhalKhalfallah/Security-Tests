from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os
import bcrypt

app = Flask(__name__)


def register():
   username = request.form['username']
   password = request.form['password']
   #hash the password
   pw_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(14))
   #connect to database
   conn = MySQLdb.connect(host="localhost",
       user="lz1599",
       passwd="password",
       db="cwe522_flask")
   cursor = conn.cursor()

   cursor.execute('INSERT into person VALUES (DEFAULT, %s, %s)', (username, pw_hash))
   username = request.form['username']
   password = request.form['password']
   query = ("SELECT username FROM person")
   cursor.execute(query)
   isUser = cursor.fetchall()
   reUsername = [row[0] for row in isUser]
   if username in reUsername or password != pw_hash:
       return "Please re-enter your information"
   else:
       return redirect("/")

