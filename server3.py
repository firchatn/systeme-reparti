import socket
import select

hote = ''
port = 12800
server_conx = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_conx.bind((hote, port))
server_conx.listen(5)
print("Server open on port {}".format(port))
server_on = True
customer_conx = []

while server_on:


    request_con, wlist, xlist = select.select([server_conx],[], [], 0.05)
    for connexion in request_con:
        customer_link, infos_connexion = connexion.accept()

        customer_conx.append(customer_link)

    customers_data = []
    try:
        customers_data, wlist, xlist = select.select(customer_conx,[], [], 0.05)
    except select.error:
        pass
    else:

        for customer in customers_data:

            msg = customer.recv(1024)

            msg = msg.decode()
            print("Get {}".format(msg))
            customer.send(b"5 / 5")
            if msg == "end":
                server_on = False
print("Close connection")
for customer in customer_conx:
    customer.close()
server_conx.close()
