from socket import socket,gethostbyname,gethostname,AF_INET,SOCK_STREAM
from _thread import start_new_thread
from re import findall

class main:
    def __init__(self) -> None:
        #initialise le serveur et lance en parralèlle la méthode start_co
        self.client_connecter = []
        self.ip_pc = gethostbyname(gethostname())
        code_session = findall(r"\d*.\d*.\d*.(\d*)",self.ip_pc)
        print(f"l'ip est {self.ip_pc}")
        print(f"le code session est {code_session}")
        del code_session
        start_new_thread(self.start_co,())
        #la boucle infinie est là pour que le coeur géréant le server ne se ferme pas
        while True:
            pass

    def on_new_client(self,socket):
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

    def start_co(self):
        #initialise la connexion est lance une nouvelle méthode on_new_client à chaque client qui se connecte
        while True:
            self.connexion_principale = socket(AF_INET, SOCK_STREAM)
            try:
                self.connexion_principale.bind((self.ip_pc,10999))
            except Exception as er:
                print(er)
                input()
                exit()
            self.connexion_principale.listen(5)
            self.client,info_connexion = self.connexion_principale.accept()
            del info_connexion
            start_new_thread(self.on_new_client,(self.client,))

    def send(self,msg,exeption):
        #envoi un message à tout connecter à l'instant T sauf au client qui as émis le message
        for client in self.client_connecter:
            if client != exeption:
                client.send(msg.encode('UTF-8'))

main()