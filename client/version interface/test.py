import tkinter

class main:
    def __init__(self) -> None:
        
        self.fen = tkinter.Tk()
        
        self.listbok = tkinter.Text(self.fen)
        self.listbok.pack()
        
        tkinter.Button(self.fen,command=self.test).pack()
        
        self.fen.mainloop()

    def test(self):
            self.listbok.delete("1.0","end")
            self.fen.update()
main()