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
   hash = bcrypt.hashpw(str.encode(password),bcrypt.gensalt())
   #save username and hashed password to database
   cursor.execute("INSERT into users (username, password, admin) VALUES (%s, %s, 0)", (username, hash))
   db.commit()
   return redirect('/')

