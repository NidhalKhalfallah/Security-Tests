from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)



def ping():
    url = request.args.get('url')
    output = subprocess.Popen(["/usr/bin/ping", "-c 1", url], stdout=subprocess.PIPE).communicate()[0]
    return output



