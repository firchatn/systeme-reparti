import socket

connex = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connex.bind(('', 12800))
connex.listen(5)
connex_client, info_connex = connex.accept()
print(info_connex)
print(connex_client.send(b"Je viens d'accepter la connexion"))
connex_client.close()

