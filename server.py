import http.server
import socketserver

PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"Requested path: {self.path}")  # Debugging statement
        if self.path in ['/', '/index.html']:
            self.path = 'index.html'
        elif self.path == '/404.html':
            self.path = '404.html'
        else:
            print("404 Error: File Not Found")  # Debugging statement
            self.path = '404.html'
            self.send_error(404, "File Not Found")
            return
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
