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
   hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
   #insert the new user into the database
   db = MySQLdb.connect("localhost","cs3630","password","cs3630")
   cursor = db.cursor()
   cursor.execute('''INSERT INTO users VALUES (%s, %s, %s)''', (username, hash, "active"))
   db.commit()
   cursor.close()
   db.close()
   return redirect("http://web:5000/", code=302)

