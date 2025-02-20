#!/usr/bin/env python3

import http.server
import json
from http.server import BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(response).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/info":
            self.send_response(200)
            response = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":

    PORT = 8000
    Handler = SimpleHTTPRequestHandler
    with http.server.HTTPServer(("localhost", PORT), Handler) as httpd:
        print(f"Serving on port, {PORT}")
        httpd.serve_forever()
