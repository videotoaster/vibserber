from http.server import BaseHTTPRequestHandler

class PakTTP(BaseHTTPRequestHandler):

    routes = {}

    def __init__(self, request, client_address, server):
        print(f"[-] Request from {client_address[0]} on port {client_address[1]}.")

    def route(self, path, methods):
        def inner(func):
            def wrapper_route(*args, **kwargs):
                self.routes[path] = {
                    "path": path,
                    "methods": methods,
                    "function": func
                }
            return wrapper_route()
        return inner