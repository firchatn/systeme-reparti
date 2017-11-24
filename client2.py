import socket
hote = "localhost"
port = 12800
server_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_connection.connect((hote, port))
print("Connection with Server on  port{}".format(port))
msg = b""
while msg != b"end":
    msg = input("> ")
    msg = msg.encode()
    server_connection.send(msg)
    data = server_connection.recv(1024)
    print(data.decode()) 
print("Close Connection")
server_connection.close()
