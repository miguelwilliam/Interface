from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack(side=RIGHT)
        self.msg = Label(self.widget1, text=
        'O hulk \n'
        'do finado caldeirão do hulk \n'
        'é muito feio \n'
        'na moral irmão')
        self.msg["font"] = ("Helvetica", "10", "italic", "bold")
        self.msg.pack()
        
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack(side=RIGHT)


root = Tk()
Application(root)

root.mainloop()