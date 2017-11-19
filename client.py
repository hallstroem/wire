import socket

def Main():

	hostname='node-1'
	hostip=socket.gethostbyname(hostname)
	port = 12345
	print("Connect to "+hostname+' with IP '+str(hostip)+' on port '+str(port)) 
	mySocket = socket.socket()
	mySocket.connect((hostip,port))
	message = input(" ? ")
	while message != 'q':
		mySocket.send(message.encode())
		data = mySocket.recv(1024).decode()
		print ('Received from server: ' + data)
		message = input(" ? ")
	mySocket.close()

if __name__ == '__main__':
	Main()
