import socket

ClientSocket = socket.socket()
host = '192.168.56.103'
port = 8888

print('Waiting for connection')
try:
	ClientSocket.connect((host,port))
except socket.error as e:
	print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
	Input = input('Say Something: ')
	ClientSocket.send(str.encode(Input))
	Response = ClientSocket.recv(1024)
	print(Response.decode('utf-8'))

ClientSocket.close()
