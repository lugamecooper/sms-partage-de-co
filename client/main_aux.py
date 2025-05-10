from colorama import init,Fore
from os import system
from socket import socket,AF_INET,SOCK_STREAM
init(True)

class main_commandes:
    def __init__(self) -> None:
        #se connecte au terminal gérant l'affichage et l'envoi des messages
        #attend la saisie d'un message puis appelle la méthode sender
        self.connexion_interface = socket(AF_INET, SOCK_STREAM)
        self.connexion_interface.connect(("127.1.1.1",11000))
        self.pseudo = input("qu'elle est votre pseudo :")
        system("cls")
        while True:
            self.msg = input(f"{Fore.CYAN}message : {Fore.GREEN}")
            system("cls")
            self.sender()
            
    def sender(self):
        #envoi le message
        message = f"[{self.pseudo}]({self.msg})"
        self.connexion_interface.send(message.encode(encoding="utf-8"))

main_commandes()