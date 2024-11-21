from colorama import init,Fore
from os import system
from socket import gethostbyname,gethostname,AF_INET,SOCK_STREAM,socket
from _thread import start_new_thread
from re import findall
from os.path import join,dirname
import tkinter

init(True)

class main_client_interface:
    def __init__(self) -> None:
        self.list_msg = []
        self.auto_msg = False
        self.check_msg = False
        if int(input("se connecter avec un code session [1]\nse connecter avec une adresse ip [0] : ")):
            ip_host = input("qu'elle est le code session : ")
            ip_co = findall(r"(\d*.\d*.\d*).\d*",gethostbyname(gethostname()))[0]
            self.connexion_server = socket(AF_INET, SOCK_STREAM)
            self.connexion_server.connect((f"{ip_co}.{ip_host}",10999))
        else:
            ip_host = input("qu'elle est l'adresse ip : ")
            self.connexion_server = socket(AF_INET, SOCK_STREAM)
            self.connexion_server.connect((f"{ip_host}",10999))
        system("cls")
        self.pseudo = input("qu'elle est vôtre pseudo : ")
        system("cls")
        start_new_thread(self.reciev,())
        self.fen = tkinter.Tk("messagerie",className="messagerie")
        self.fen.geometry(f"{self.fen.winfo_screenwidth()}x{self.fen.winfo_screenheight()}")
        self.fen.iconphoto(False, tkinter.PhotoImage(file=join(dirname(__file__),"Sans titre.png")))
        self.div = tkinter.Frame(self.fen)
        self.listbox = tkinter.Listbox(self.div)
        scrollbar = tkinter.Scrollbar(self.div)
        self.listbox.config(yscrollcommand=scrollbar.set,height=self.fen.winfo_screenheight(),width=125)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side=tkinter.LEFT)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        for i in range(50):
            self.listbox.insert(tkinter.END, "")
        self.div.pack(side=tkinter.LEFT)

        self.div_input = tkinter.Frame(self.fen)
        self.zone_input = tkinter.Text(self.div_input,width=125,height=30)
        self.bouton = tkinter.Button(self.div_input,command=self.send,border=12,text="envoyer le message")


        self.div_input.pack()
        self.zone_input.pack()
        for i in range(2):
            tkinter.Label(self.div_input,text="").pack()
        self.bouton.pack()
        self.fen.mainloop()

    def reciev(self):
        while True:
            try:
                msg_recu = self.connexion_server.recv(4096).decode(encoding="ascii",errors="xmlcharrefreplace").replace("\n","; ")
                tempo = findall(r"\[([\w|\W]*)\]\(([\w|\W]*)\)",msg_recu)[0]
                msg_recu = f"[{tempo[0]}] : {tempo[1]}"
                test = range(len(msg_recu)%40)
                tempo = ""
                test_2 = 0
                if test:
                    for i in range(len(msg_recu)):
                        tempo += msg_recu[i]
                        test_2 += 1
                        if i == "\n":
                            test_2 = 0
                        if test_2 == 40:
                            tempo += "\n"
                            test_2 = 0
                msg_recu = tempo
            except:
                msg_recu = None
                pass
            if msg_recu:
                if len(self.list_msg)<= 50:
                    self.list_msg.append(msg_recu)
                else:
                    self.list_msg.remove(self.list_msg[0])
                    self.list_msg.append(msg_recu)
                self.affichage()

    def affichage(self):
        self.listbox.delete(first=0,last=49)
        for i in range(len(self.list_msg)):
            self.listbox.insert(tkinter.END,self.list_msg[i])
        for i in range(50-len(self.list_msg)):
            self.listbox.insert(tkinter.END,"")
        self.div.update()
        
    def send(self):
        msg_a_envoyer = self.zone_input.get("1.0","end").replace("\n","; ")
        self.zone_input.delete("1.0","end")
        msg = f"{msg_a_envoyer} : [{self.pseudo}]"

        test = range(len(msg)%40)
        tempo = ""
        test_2 = 0
        if test:
            for i in range(len(msg)):
                tempo += msg[i]
                test_2 += 1
                if i == "\n":
                    test_2 = 0
                if test_2 == 40:
                    tempo += "\n"
                    test_2 = 0
        msg = tempo
        if len(self.list_msg)<= 50:
            self.list_msg.append(msg)
        else:
            self.list_msg.remove(self.list_msg[0])
            self.list_msg.append(msg)
        start_new_thread(self.div_input.update,())
        start_new_thread(self.affichage,())
        test = range(len(msg_a_envoyer)%40)
        tempo = ""
        test_2 = 0
        if test:
            for i in range(len(msg_a_envoyer)):
                tempo += msg_a_envoyer[i]
                test_2 += 1
                if i == "\n":
                    test_2 = 0
                if test_2 == 40:
                    tempo += "\n"
                    test_2 = 0
        msg_a_envoyer = tempo
        self.connexion_server.send(f"[{self.pseudo}]({msg_a_envoyer})".encode(encoding="ascii",errors="xmlcharrefreplace"))

main_client_interface()