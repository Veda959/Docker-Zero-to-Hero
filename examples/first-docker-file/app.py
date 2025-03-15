from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, World!")
        else:
            self.send_error(404, "Not Found")

if __name__ == "__main__":
    server_address = ("0.0.0.0", 5000)  # Expose on port 5000
    httpd = HTTPServer(server_address, MyHandler)
    print("Serving on port 5000...")
    httpd.serve_forever()
