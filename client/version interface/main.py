from socket import AF_INET,SOCK_STREAM,socket
from _thread import start_new_thread
from re import findall
from os.path import join,split
from os import getlogin
import customtkinter as ct

class main_client_interface:
    def __init__(self) -> None:
        ct.set_default_color_theme("dark-blue")
        ct.set_appearance_mode("dark")
        self.list_msg = []
        self.list_label_msg = []
        self.connexion_server = socket(AF_INET, SOCK_STREAM)
        self.connexion_server.connect((f"127.0.0.1",10999))
        
        self.pseudo = getlogin()
        start_new_thread(self.reciev,())
        self.fen = ct.CTk(className="messagerie")
        self.fen.title = "messagerie"
        self.fen.wm_iconbitmap(join(split(__file__)[0],"Sans-titre.ico"))
        self.fen.focus_force()
        
        self.set_pseudo_frame()

        self.fen.after(0, lambda: self.fen.wm_state('zoomed'))
        self.fen.mainloop()

    def set_interface(self):
        self.main_frame = ct.CTkFrame(self.fen)
        self.msg_frame = ct.CTkFrame(self.main_frame)
        for i in range(50):
            self.list_label_msg.append(ct.CTkLabel(self.msg_frame,text="test"))
        self.input_frame = ct.CTkFrame(self.main_frame)
        self.msg_display()

    def msg_display(self):
        if len(self.list_label_msg) > 100:
            for i in range(len(self.list_label_msg)-100):
                self.list_msg.pop(0)
        for label in self.list_label_msg:
            label : ct.CTkLabel
            label.pack()

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

    def set_pseudo_frame(self):
        self.frame_pseudo = ct.CTkFrame(self.fen)
        
        self.label_pseudo = ct.CTkLabel(self.frame_pseudo, text="entrer vôtre pseudo : ",anchor="w")
        self.label_pseudo.pack()
        self.entry_pseudo = ct.CTkEntry(self.frame_pseudo)
        self.entry_pseudo.pack()
        self.Button_vallid = ct.CTkButton(self.frame_pseudo,text="Vallidez vôtre pseudo",command=self.get_pseudo)
        self.Button_vallid.pack()

        self.frame_pseudo.pack()

    def get_pseudo(self):
        if self.entry_pseudo.get():
            self.pseudo = self.entry_pseudo.get()
            self.frame_pseudo.destroy()
            self.set_interface()
            self.fen.update()

main_client_interface()