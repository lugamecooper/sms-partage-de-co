from main_back import back_end
import customtkinter as tk
import pyautogui

class login:
    def __init__(self, back : back_end,fen : tk.CTk) -> None:
        self.back = back
        self.fen = fen

        self.login()


    def login(self):
        self.frame_login = tk.CTkFrame(self.fen)
        self.frame_login.anchor("center")
        label = tk.CTkLabel(self.frame_login, text="connectez-vous")
        if self.back.config["auto_log"]:
            self.entry_login = tk.CTkEntry(self.frame_login ,placeholder_text="nom d'utilisateur")
            self.entry_login.insert(0,self.back.config["username"])
            self.entry_password = tk.CTkEntry(self.frame_login, placeholder_text='mot de passe')
            self.entry_password.insert(0,self.back.config["password"])
            self.checkbox_connexion = tk.CTkCheckBox(self.frame_login, text="souhaitez-vous enregistrer vos identifiants")
        else:
            self.entry_login = tk.CTkEntry(self.frame_login ,placeholder_text="nom d'utilisateur")
            self.entry_password = tk.CTkEntry(self.frame_login, placeholder_text='mot de passe')
            self.checkbox_connexion = tk.CTkCheckBox(self.frame_login, text="souhaitez-vous enregistrer vos identifiants")
        self.button_connexion = tk.CTkButton(self.frame_login, text="connexion")
        
        self.frame_login.grid(pady=round(self.fen.winfo_screenheight()/4))
        label.grid(padx = 20, pady = 10)
        self.entry_login.grid()
        self.entry_password.grid()
        self.checkbox_connexion.grid(padx = 10, pady = 10)
        self.button_connexion.grid(padx=10, pady=10)