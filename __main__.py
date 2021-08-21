
iface, port = '0.0.0.0', 8443

import sys, os 
import http.server, ssl

try:
	port = int(sys.argv[1])
	iface = str(sys.argv[2])
except:
	pass

utdir = os.path.dirname(__file__)

httpd = http.server.HTTPServer((iface, port), http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
	server_side=True,
	keyfile= f'{utdir}/cyue.key', certfile= f'{utdir}/cyue.crt',
	ssl_version=ssl.PROTOCOL_TLSv1_2,
)
print(f'You can go to https://{iface}:{port} now.')
httpd.serve_forever()
