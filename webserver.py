import socket
import re

host = ""
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)


while 1:
	cs, cadd = s.accept()
	req = cs.recv(2000)
	print req
	is_match = re.match('GET /(\w+)\sHTTP/1', req)
	if is_match:
		msg = is_match.group(1)
		http_response = """"HTTP/1.0 200 OK
		Content-Type: text/html

		<html>
		<head>
		<title>Success</title>
		</head>
		<body>
		"""+msg+"""
		</body>
		</html>
		"""
		cs.sendall(http_response)

	else:	
		http_response = """"HTTP/1.0 200 OK
		Content-Type: text/html

		<html>
		<head>
		<title>Success</title>
		</head>
		<body>
			Error 404
		</body>
		</html>
		"""
		cs.sendall(http_response)
	cs.close()
