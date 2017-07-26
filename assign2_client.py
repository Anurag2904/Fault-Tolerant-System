#!/bin/python

import sys

# http related facilities
import httplib

# import timer stuff to record the time
import time

# json stuff
import json



# print the response (for debugging purposes)
def print_response (resp):
    print "printing response headers"
    try:
        for hdr in resp.getheaders ():
            print hdr
    except:
        print "Exception thrown: ", sys.exc_info()[0]
        raise

    print "printing received data"
    try:
        data = resp.read ()
        print "Length of data = ", len(data)
        print data
    except:
        print "Exception thrown: ", sys.exc_info()[0]
        raise

# send a http request to the server.
def send_req (conn, arg):

    # send GET request to the server using the args
    try:
        conn.request ("GET", arg)
    except:
        print "Exception thrown: ", sys.exc_info()[0]
        raise

    # retrieve the response
    try:
        resp = conn.getresponse ()
    except:
        print "Exception thrown: ", sys.exc_info()[0]
        raise

    return resp


	
def main ():

    print "Instantiating a connection obj"
    try:
        conn = httplib.HTTPConnection ("129.59.107.83", "8904")
    except:
        print "Exception thrown: ", sys.exc_info()[0]
        raise


    print "Sending request for top level page"
    send_req (conn, "/")

    print "Sending request for the dummy op 10 times"
    print "Server Time  ||  Client Time"

    req = "/dummy_op"
    for i in range (1, 10):

        # send dummy request
        json_obj, response = executeRequest(conn, req)
        print json_obj['time'], response
        
		
    conn.close ()


def executeRequest(conn, query):
    start_time = time.time()
    resp = send_req(conn, query)
    end_time = time.time()

    response = end_time - start_time
    json_obj = json.loads(resp.read())

    return json_obj, response

    
# invoke main
if __name__ == "__main__":
    sys.exit (main ())
    
