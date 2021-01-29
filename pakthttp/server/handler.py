from http.server import BaseHTTPRequestHandler
import os

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
