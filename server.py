from http.server import HTTPServer, BaseHTTPRequestHandler
class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        # self.wfile.write(self.path[1:].encode())
        # self.wfile.write("Hello World!".encode())
        f = open('index.html','rb')
        if('.jpg ' in self.path[1:]):
            self.send_response(415)
            a=''
            a+='<html><body>'
            a+='<h1>415 Unsupport media</h1>'
            a+='</body></html>'
            self.wfile.write(a.encode())

        elif('.html' not in self.path[1:]):
            self.send_response(400)
            a=''
            a+='<html><body>'
            a+='<h1>400 Bad Request</h1>'
            a+='</body></html>'
            self.wfile.write(a.encode())
        elif(self.path[1:]!='index.html'):
            self.send_response(403)
            a=''
            a+='<html><body>'
            a+='<h1>403 Forbidden Page</h1>'
            a+='</body></html>'
            self.wfile.write(a.encode())
        elif(self.path[1:]=='index.html'):
            self.wfile.write(f.read())
        # else:
        #     self.send_response(415)
        #     a=''
        #     a+='<html><body>'
        #     a+='<h1>415 Unsupport media type</h1>'
        #     a+='</body></html>'
        #     self.wfile.write(a.encode())
def main():
    PORT=8000
    server=HTTPServer(('',PORT),helloHandler)
    print("Server running on port %s" %PORT)
    server.serve_forever()
if __name__=='__main__':
    main()