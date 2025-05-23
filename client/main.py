from os import system
from socket import AF_INET, SOCK_STREAM, socket
from _thread import start_new_thread
from re import findall
from subprocess import Popen
from os.path import join,dirname
try:
    from colorama import init,Fore
except:
    system("pip install colorama")
    from colorama import init,Fore
init(True)

class main_client_interface:
    def __init__(self) -> None:
        #initialise la connexion avec le serveur puis lance en parralèlle les méthodes reciev et commande_reciev
        #ouvre le terminal destiné à la saisie des message dans une nouvelle fenêtre
        self.auto_msg = False
        self.check_msg = False
        ip_host = input("quelle est l'adresse ip : ")
        self.connexion_server = socket(AF_INET, SOCK_STREAM)
        self.connexion_server.connect((f"{ip_host}",10999))
        system("cls")
        start_new_thread(self.commande_recieve,())
        Popen(f'start cmd /C "{join(dirname(__file__),"main_aux.py")}"',shell=True)
        while True:
            try:
                msg_recu = self.connexion_server.recv(4096).decode(encoding="utf-8")
            except:
                pass
            if msg_recu:
                self.auteur,self.message = findall(r"\[([\w|\W]*)\]\(([\w|\W]*)\)",msg_recu)[0]
                self.auto_msg = False
                self.print_msg()

    def print_msg(self):
        #affiche le message
        if self.auto_msg:
            color = Fore.GREEN
            message_color = Fore.LIGHTGREEN_EX
        else:
            color = Fore.CYAN
            message_color = Fore.LIGHTCYAN_EX
        print(f"{color}[{self.auteur}]--: {message_color}{self.message}{Fore.RESET}\n")

    def commande_recieve(self):
        #intialise la connexion vers le terminal de saisie des message
        #receptionne le mesage à envoyé puis apelle la méthode print_msg et l'envoi au serveur
        self.connexion_commande = socket(AF_INET, SOCK_STREAM)
        try:
            self.connexion_commande.bind(("127.1.1.1",11000))
        except Exception as er:
            print(er)
            input()
            exit()
        self.connexion_commande.listen(5)
        self.commande,info_connexion = self.connexion_commande.accept()
        del info_connexion
        while True:
            msg_recu = self.commande.recv(4096).decode(encoding="utf-8")
            if msg_recu:
                self.auteur,self.message = findall(r"\[([\w|\W]*)\]\(([\w|\W]*)\)",msg_recu)[0]
                self.auto_msg = True
                self.print_msg()
                self.connexion_server.send(msg_recu.encode(encoding="utf-8"))

main_client_interface()
