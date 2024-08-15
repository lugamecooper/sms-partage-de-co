from fenetre.first_use import first_use
from fenetre.login import login
from main_back import back_end
import customtkinter as tk

class main:
    def __init__(self) -> None:
        self.back = back_end()
        self.fen = tk.CTk()
        self.fen.anchor("n")

        # variable use to be check boolean
        self.first_use_test_bool_1 = True


        self.fen.title("messagerie canardessque")
        self.fen._state_before_windows_set_titlebar_color = 'zoomed'
        if self.back.config["first use"]:
            first_use(self.fen, self.back).first_use()
        else:
            self.lunch_connection()

        self.fen.mainloop()

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

    def relaunch_connection(self):
        self.frame_error_connection.destroy()
        self.lunch_connection()
    
    def enter_new_ip(self):
        self.frame_error_connection.destroy()
        first_use(self.fen, self.back).first_use()
        


main()