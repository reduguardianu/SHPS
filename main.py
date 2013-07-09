from http.server import HTTPServer
import sys
import handlers.simple_http_request_handler
from handlers.simple_http_request_handler import SimpleHTTPRequestHandler

class SimpleHTTPServer:
    def __init__(self, port_number, listen_address):
        self.server = HTTPServer((listen_address, int(port_number)), SimpleHTTPRequestHandler)
    def run(self):
        self.server.serve_forever()

server = SimpleHTTPServer(sys.argv[2], sys.argv[1])
server.run()
