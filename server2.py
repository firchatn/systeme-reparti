import socket

connexion_principale = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
connexion_principale.bind(('', 8000))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))
connexion_avec_client, infos_connexion = connexion_principale.accept()
msg_recu = b""
while msg_recu != b"end":
    msg_recu = connexion_avec_client.recv(1024)
    print(msg_recu.decode())
    connexion_avec_client.send(b"5 / 5")
print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
