import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import socket
import select
import time

hote = ''
port = 12800

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

        
    def on_server(self, on):

        connexion_principale = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connexion_principale.bind((hote, port))
        connexion_principale.listen(5)
        print("Le serveur écoute à présent sur le port {}".format(port))
        time.sleep(5)
        connect.set_text("Le serveur écoute à présent sur le port {}".format(port))
        time.sleep(5)
        connexion_avec_client, infos_connexion = connexion_principale.accept()
        msg_recu = b""
        while msg_recu != b"fin":
            msg_recu = connexion_avec_client.recv(1024)
            print(msg_recu.decode())
            msg.set_text(msg.get_text() + " " + msg_recu.decode())
            connexion_avec_client.send(b"5 / 5")
        print("Fermeture de la connexion")
        connexion_avec_client.close()
        connexion_principale.close()


builder = Gtk.Builder()
builder.add_from_file("server.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.connect("delete-event", Gtk.main_quit)
window.set_default_size(600, 250)
connect = builder.get_object("label1")
msg = builder.get_object("label2")

window.show_all()


Gtk.main()



