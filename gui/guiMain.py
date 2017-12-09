from tkinter import *
from tkinter.ttk import *

class GuiMain(Frame):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.master.title = "pyRename"
        menu = Menu(self.master)
        self.master.config(menu=menu, relief=None)
        mainMenu = Menu(menu)
        mainMenu.add_command(label="Lister")
        mainMenu.add_command(label="Creer")
        menu.add_cascade(label="Regles",menu=mainMenu)
        headerFrame = Frame(self.master, borderwidth=1)
        funcLabel = Label(headerFrame, text="Renommer en lots")
        nameLabel = Label(headerFrame, text="Nom du répertoire")
        ruleEntry = Entry(headerFrame, width=100)
        bodyFrame = Frame(self.master, borderwidth=1)
        primerLabel = Label(bodyFrame, text="Amorce")
        optSelect = StringVar()
        optValues = ("Aucune","Lettre","Chiffre")
        optList = Combobox(bodyFrame, textvariable = optSelect, values = optValues, state = 'readonly')
        optList.pack(side=LEFT)
        headerFrame.pack()
        funcLabel.pack()
        nameLabel.pack(side=LEFT)
        ruleEntry.pack()

def main():
    mainWin = Tk()
    mainWin.geometry("900x300")
    app = GuiMain()
    mainWin.mainloop()

if __name__ == '__main__':
    main()
