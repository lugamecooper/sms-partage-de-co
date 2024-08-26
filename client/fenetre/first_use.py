import customtkinter as tk
import main_back
from fenetre.login import login

class first_use :
    def __init__(self,fen : tk.CTk, back : main_back.back_end) -> None:
        self.back = back
        self.fen = fen

    def first_use(self):
        self.frame_first_use = tk.CTkFrame(self.fen, width=200, height=200)
        self.frame_first_use.anchor("center")

        self.entry_ip_first_use = tk.CTkEntry(self.frame_first_use, placeholder_text="entrer l'adresse ip")
        self.button_first_use = tk.CTkButton(self.frame_first_use,text="vallidez l'addresse ip à utiliser", command=self.get_first_use)

        self.label_error_first_use = tk.CTkLabel(self.frame_first_use,text="")

        self.frame_first_use.grid(row=0, column=0, padx=20, pady=round(self.fen.winfo_screenheight()/4), sticky="nsew")
        self.entry_ip_first_use.grid()
        self.button_first_use.grid()
        self.label_error_first_use.grid()

    def get_first_use(self):
        if self.entry_ip_first_use.get():
            result_back = self.back.check_ip(self.entry_ip_first_use.get())
            if type(result_back) == type([]):
                if result_back[0] == "#00#":
                    self.label_error_first_use.configure(text=result_back[1])
            elif result_back:
                self.frame_first_use.destroy()
                self.lunch_connection()

    def lunch_connection(self):
        self.back.lunch_connection()
        while not self.back.connection_error and not self.back.connection_started:
            pass
        if self.back.connection_started:
            login(self.back,self.fen)
        else:
            self.frame_error_connection = tk.CTkFrame(self.fen)
            label = tk.CTkLabel(self.frame_error_connection, text="une erreur est survenue lors de la connection")
            boutton_1 = tk.CTkButton(self.frame_error_connection, text="retenter de se connecter", command=self.relaunch_connection)
            boutton_2 = tk.CTkButton(self.frame_error_connection, text="saisir une nouvelle adresse ip", command=self.enter_new_ip)

            self.frame_error_connection.grid()
            label.grid()
            boutton_1.grid()
            boutton_2.grid()

    def relaunch_connection(self):
        self.frame_error_connection.destroy()
        self.lunch_connection()
    
    def enter_new_ip(self):
        self.frame_error_connection.destroy()
        first_use(self.fen, self.back).first_use()