from http.server import ThreadingHTTPServer
from .handler import RequestHandler


class HttpServer(ThreadingHTTPServer):
    def __init__(self, server_address, server_port, handler_class=RequestHandler):
        self.server_address = server_address
        self.server_port = server_port
        self.handler_class = handler_class
        super().__init__((self.server_address, self.server_port), self.handler_class)
