#!/usr/bin/python3
# from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from http.server import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import cgi
import random
import string

PORT_NUMBER = 8081

def good_input(input):
    #Tests if valid input (No Numbers/special characters except ones strictly defined)
    return not set(input).difference(string.ascii_letters + ' ' + '.' + ',' + '?' + '!' + '-' + "'" + '"')

def converter(input):
    if good_input(input) == False:
            return 'INVALID CRYPTOQUOTE SYNTAX... NO NUMBERS'
    #Converts user input to crypto version
    alphabet = string.ascii_lowercase
    cypherbet = ''.join(random.sample(alphabet,len(alphabet)))

    convert_table = str.maketrans(alphabet, cypherbet)
    converted = input.translate(convert_table)
    return(converted)
    
# This class will handle any incoming request from
# a browser 
class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        f = open(curdir + sep + "cryptoquote.html")
        self.wfile.write(f.read().encode())
        f.close()
        return
    
    #Handler for the POST requests
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        original = form['cryptoquote'].value
        self.send_response(200)
        self.end_headers()
        converted = converter(original)
        self.wfile.write(converted.encode())
        return
			

try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print ('Started httpserver on port',PORT_NUMBER)

    # Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print ('^C received, shutting down the web server')