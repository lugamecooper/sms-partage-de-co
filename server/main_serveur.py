from socket import socket, AF_INET, SOCK_STREAM
from _thread import start_new_thread

class main:
    def __init__(self) -> None:
        #initialise le serveur et lance en parralèlle la méthode start_co
        self.client_connecter = []
        while True:
            self.connexion_principale = socket(AF_INET, SOCK_STREAM)
            try:
                self.connexion_principale.bind(("127.0.0.1",10999))
            except Exception as er:
                print(er)
                input()
                exit()
            self.connexion_principale.listen(140)
            self.client,info_connexion = self.connexion_principale.accept()
            del info_connexion
            start_new_thread(self.on_new_client,(self.client,))

    def on_new_client(self, socket : socket):
        #gére la réception des message de chaque client de manière individuel
        #si un message est reçus apelle la méthode send
        self.client_connecter.append(socket)
        while True:
            try:
                msg_recu = socket.recv(4096).decode('UTF-8')
            except:
                break
            if msg_recu:
                self.send(msg_recu,socket)
        self.client_connecter.pop(self.client_connecter.index(socket))

    def send(self, msg : str, exeption):
        #envoi un message à tout connecter à l'instant T sauf au client qui as émis le message
        for client in self.client_connecter:
            if client != exeption:
                client.send(msg.encode('UTF-8'))

main()