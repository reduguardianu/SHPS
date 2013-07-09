import http.server

class SimpleHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET():
        print("GET")

