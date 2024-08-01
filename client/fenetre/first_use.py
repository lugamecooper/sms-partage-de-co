import customtkinter as tk
import main_back

class first_use :
    def __init__(self,fen : tk.CTk, back : main_back.back_end) -> None:
        self.back = back
        self.fen = fen
        pass

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