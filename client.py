import socket

server_conx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_conx.connect(('10.30.252.225', 8008))

msg = server_conx.recv(1024)
msg = msg.decode()
print(msg)
server_conx.close()
