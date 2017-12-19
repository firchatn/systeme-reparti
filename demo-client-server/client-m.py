import socket
from threading import Thread

host = input("Server IP: ")
port = int(input("Server Port: "))

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((host, port))


class InputThread(Thread):
    def run(self):
        while True:
            msg = input()
            soc.send(msg.encode())


class MessageThread(Thread):
    def run(self):
        while True:
            msg = soc.recv(1024)
            if not msg:
                print("Disconnected...")
                exit(0)
                break
            print(msg.decode())


input_thread = InputThread()
message_thread = MessageThread()

input_thread.start()
message_thread.start()
