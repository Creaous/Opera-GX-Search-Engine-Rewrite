from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

normal = "redir.opera.com"
port = 443
newengine = "https://search.brave.com/search?q="

class WebServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		print(self.path)
		url = self.path
		new = url.split("/amazon/?q=")
		self.send_response(301)
		self.send_header('Location',newengine + new[1])
		self.end_headers()
		return

def main():
	try:
		server = HTTPServer((normal, port), WebServerHandler)
		server.socket = ssl.wrap_socket(server.socket,
                               server_side=True,
                               certfile='cacert.pem',
                               keyfile='privkey.pem',
                               ssl_version=ssl.PROTOCOL_TLS)
		print ("Web Server running on port %s" % port)
		server.serve_forever()
	except KeyboardInterrupt:
		print (" ^C entered, stopping web server....")
		server.socket.close()

if __name__ == '__main__':
	main()