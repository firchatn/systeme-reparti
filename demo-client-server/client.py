import socket

server_conx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_conx.connect(('0.0.0.0', 8008))

msg = server_conx.recv(1024)
print(msg)
server_conx.close()
