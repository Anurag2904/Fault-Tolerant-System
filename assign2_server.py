#!/bin/python

import sys

# import timer stuff to record the time
import time

from socket import *

# number crunching
import numpy as np
from numpy import linalg

# import the Flask class
from flask import Flask
from flask import request
from flask import json

# the following instance of the Flask class will act as the
# WSGI (web server gateway interface) application
app = Flask(__name__)

# the @app.route is a decorator telling flask how to route the incoming
# http web request

# Note that each route method below by default is handling a GET request
# If we were to handle other methods, then we will need the methods = 
# The following is a top level request. It just returns a welcome message
@app.route("/")
def welcome ():
    return "Welcome to Assignment2 Server!"


@app.route("/dummy_op")
def dummy_op ():

    print "dummy_op"
    start_time = time.time()
    arr = np.random.random((1200,1200))
    arr_inv = linalg.inv(arr)
    end_time = time.time()

    
    # My goal is to encode the response as a json-ified structure
    resp_dict = {}
    resp_dict["op"] = "dummy_op"
    resp_dict["server"] = "Assign1_Server"
    resp_dict["time"] = end_time - start_time

    # dumps converts the json obj to a string. When we return it, Flask will
    # convert it to a response object before actually sending it out.
    return json.dumps (resp_dict)



# main function
if __name__ == "__main__":

    print ("Starting the Assignment2 Server")
    app.run (host="0.0.0.0", port= 8904)
