import socket
import select

hote = ''
port = 12800
connexion_principale = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))
serveur_lance = True
clients_connectes = []

while serveur_lance:


    connexions_demandees, wlist, xlist = select.select([connexion_principale],[], [], 0.05)
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()

        clients_connectes.append(connexion_avec_client)

    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes,[], [], 0.05)
    except select.error:
        pass
    else:

        for client in clients_a_lire:

            msg_recu = client.recv(1024)

            msg_recu = msg_recu.decode()
            print("Reçu {}".format(msg_recu))
            client.send(b"5 / 5")
            if msg_recu == "fin":
                serveur_lance = False
print("Fermeture des connexions")
for client in clients_connectes:
    client.close()
connexion_principale.close()