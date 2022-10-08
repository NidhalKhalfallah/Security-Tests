from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)


def get_db_connection():
        try:
        conn = MySQLdb.connect(host=os.environ['DB_HOST'],
                               user=os.environ['DB_USER'],
                               passwd=os.environ['DB_PASSWORD'],
                               db=os.environ['DB_NAME'])
        return conn


