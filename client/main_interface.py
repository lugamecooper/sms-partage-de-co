import fenetre.first_use
from main_back import back_end
import customtkinter as tk
import _thread
import socket

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
            fenetre.first_use.first_use(self.fen, self.back).first_use()
        else:
            pass
        self.fen.mainloop()

    
main()