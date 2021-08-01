server_address = ('', 8443)


import sys, os 
import http.server, ssl

utdir = os.path.dirname(__file__)

httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
	server_side=True,
	certfile= f'{utdir}/localdev.pem',
	ssl_version=ssl.PROTOCOL_TLSv1_2,
)
print('You can go to https://localhost:8443 now.')
httpd.serve_forever()
