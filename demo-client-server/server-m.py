import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0', 8008))
server.listen(5)

clients = []

while True:
    reqs, _, _ = select.select([server] + clients, [], [])
    for req in reqs:
        if req is server:
            print("New client")
            client, _ = server.accept()
            clients.append(client)
        else:
            msg = req.recv(1024)
            if not msg:
                print("Client out")
                clients.remove(req)
            else:
                print("New message:", msg.decode())
                i = clients.index(req)
                msg = '(client:{}) {}'.format(i, msg.decode()).encode()
                for client in clients:
                    client.send(msg)
