#!/usr/bin/python3

#python version 3.7

from http import server

from http.server import SimpleHTTPRequestHandler  

import socket  

import ssl  

import sys

 

 

if sys.argv[1:]:

        port = int(sys.argv[1])

else :

        port = 8000

 

server_address = ("127.0.0.1", port)

 

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

#context.load_cert_chain("xxx.pem","xxx.key")

 

httpd = server.HTTPServer(server_address,SimpleHTTPRequestHandler)

httpd.socket = context.wrap_socket(httpd.socket, server_side = True)

httpd.serve_forever()
