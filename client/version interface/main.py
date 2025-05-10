from socket import AF_INET,SOCK_STREAM,socket
from _thread import start_new_thread
from re import findall
from os.path import join,split
from os import getlogin
import customtkinter as ct

class main_client_interface:
    def __init__(self) -> None:
        self.list_msg = []
        self.connexion_server = socket(AF_INET, SOCK_STREAM)
        self.connexion_server.connect((f"127.0.0.1",10999))
        
        self.pseudo = getlogin()
        start_new_thread(self.reciev,())
        self.fen = ct.CTk(className="messagerie")
        self.fen.title = "messagerie"
        self.fen.geometry(f"{self.fen.winfo_screenwidth()}x{self.fen.winfo_screenheight()}")
        self.fen.wm_iconbitmap(join(split(__file__)[0],"Sans-titre.ico"))
        self.fen.focus_force()
        pass
        self.fen.state('normal')

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
        """self.listbox.delete(first=0,last=49)
        for i in range(len(self.list_msg)):
            self.listbox.insert(ct.END,self.list_msg[i])
        for i in range(50-len(self.list_msg)):
            self.listbox.insert(ct.END,"")"""
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