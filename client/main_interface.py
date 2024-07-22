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
            self.first_use()

        self.fen.mainloop()

    def custom_ip(self):
        dico_state = {True:["normal","readonly"],False:["disabled","disabled"]}
        self.first_use_test_bool_1 = not self.first_use_test_bool_1
        self.dropdown_menu_first_use.configure(state=dico_state[self.first_use_test_bool_1][1])
        self.entry_netmask_first_use.configure(state=dico_state[not self.first_use_test_bool_1][0], placeholder_text="entrer le masque réseaux",)
        self.entry_ip_first_use.configure(state=dico_state[not self.first_use_test_bool_1][0], placeholder_text="entrer l'adresse ip")

    def first_use(self):
        self.data, self.netmask_and_data = self.back.get_all_ip()
        self.frame_first_use = tk.CTkFrame(self.fen, width=200, height=200)
        self.frame_first_use.anchor("center")

        self.checkbutton_1_first_use = tk.CTkCheckBox(self.frame_first_use,text="rentrer sa propre adresse ip et masque de sous réseaux",command=self.custom_ip)
        self.dropdown_menu_first_use = tk.CTkComboBox(self.frame_first_use, values=self.data, state="readonly")
        self.dropdown_menu_first_use.set(self.data[0])
        self.entry_ip_first_use = tk.CTkEntry(self.frame_first_use, placeholder_text="entrer l'adresse ip", state="disable")
        self.entry_netmask_first_use = tk.CTkEntry(self.frame_first_use, placeholder_text="entrer le masque réseaux", state="disable")
        self.button_first_use = tk.CTkButton(self.frame_first_use,text="vallidez l'addresse ip à utiliser", command=self.get_first_use)
        self.label_error_first_use = tk.CTkLabel(self.frame_first_use,text="")

        self.frame_first_use.grid(row=0, column=0, padx=20, pady=round(self.fen.winfo_screenheight()/4), sticky="nsew")
        self.checkbutton_1_first_use.grid()
        self.dropdown_menu_first_use.grid()
        self.entry_ip_first_use.grid()
        self.entry_netmask_first_use.grid()
        self.button_first_use.grid()
        self.label_error_first_use.grid()

    def get_first_use(self):
        if self.first_use_test_bool_1:
            self.back.check_ip_and_mask(self.dropdown_menu_first_use.get(),self.netmask_and_data[self.dropdown_menu_first_use.get()])
            while True:
                if self.back.validate_deafault_ip:
                    if type(self.back.validate_deafault_ip) == type([]):
                        if self.back.validate_deafault_ip[0] == "#00#":
                            self.label_error_first_use.configure(text=self.back.validate_deafault_ip[1])
                            break
                        
main()