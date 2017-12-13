from tkinter import *
from tkinter.ttk import *

class GuiMain():
    def __init__(self, mode):
        '''
        Constructeur
        mode : true pour lister, false pour créer
        '''
        self.master = Tk()
        self.mode = mode
        self.InitUI(None)

    def InitUI(self, mode):
        '''
        Initialise l'interface : création et placement des widgets 
        '''
        self.master.title("pyRename")
        self.master.geometry("900x300")        
        menu = Menu(self.master)
        self.master.config(menu=menu, relief=None)
        mainMenu = Menu(menu)
        mainMenu.add_command(label="Lister",command=lambda: self.refresh(True))
        mainMenu.add_command(label="Creer", command=lambda: self.refresh(False))
        menu.add_cascade(label="Regles",menu=mainMenu)
        menu.add_command(label="?",menu=None, command=self.about)

        if(self.mode):
            funcLabel = Label(self.master, text="Renommer en lots")
            nameLabel = Label(self.master, text="Nom du répertoire")
            renameButton = Button(self.master, text="Renommer",command=None)        
        else:
            funcLabel = Label(self.master, text="Créer une règle")
            nameLabel = Label(self.master, text="Nom de la règle")
            renameButton = Button(self.master, text="Créer", command=None)

        ruleEntry = Entry(self.master)
        primerLabel = Label(self.master, text="Amorce")
        optSelect = StringVar()
        optValues = ("Aucune","Lettre","Chiffre")
        optList = Combobox(self.master, textvariable = optSelect, values = optValues, state = 'readonly')
        prefixEntry = Entry(self.master)
        prefixLabel = Label(self.master, text="Préfixe")
        cbOriginalName = Checkbutton(self.master, text="Nom original")
        filenameLabel = Label(self.master, text="Nom du fichier")
        suffixEntry = Entry(self.master)
        suffixLabel = Label(self.master, text="Suffixe")
        extensionEntry = Entry(self.master)
        extensionLabel = Label(self.master, text="Extension concernée")
        filenameFrame = Frame(self.master)
        cbCustomName = Checkbutton(filenameFrame, text="")
        entryCustomName = Entry(filenameFrame, width=9)
        fromLabel = Label(self.master, text="A partir de")
        fromEntry = Entry(self.master)

        
        funcLabel.grid(row=0,column=1,padx=5,pady=2)
        nameLabel.grid(row=1,column=0,padx=5,pady=2)
        ruleEntry.grid(row=1,column=1,padx=5,pady=2,sticky=W+E)
        primerLabel.grid(row=2,column=0,padx=5,pady=2)
        prefixLabel.grid(row=2,column=1,padx=5,pady=2)
        filenameLabel.grid(row=2,column=2,padx=5,pady=2)
        suffixLabel.grid(row=2,column=3,padx=5,pady=2)
        extensionLabel.grid(row=2,column=4,padx=5,pady=2)
        optList.grid(row=3,column=0,sticky=W,padx=5,pady=2)
        prefixEntry.grid(row=3, column=1,padx=5,pady=2,sticky=W+E)
        cbOriginalName.grid(row=3, column=2,padx=5,pady=2)
        suffixEntry.grid(row=3, column=3,padx=5,pady=2,sticky=W+E)
        extensionEntry.grid(row=3, column=4,padx=5,pady=2,sticky=W+E)
        filenameFrame.grid(row=4, column=2,padx=5,pady=2)
        cbCustomName.grid(row=0,column=0)
        entryCustomName.grid(row=0,column=1)
        renameButton.grid(row=5,column=4,padx=5,pady=2)
        fromLabel.grid(row=5,column=0,padx=5,pady=2)
        fromEntry.grid(row=6,column=0,padx=5,pady=2)
        self.master.mainloop()

    def refresh(self, argmode):
        '''
        "rafraichis" l'interface selon le mode. True pour Lister, False pour Créer
        '''
        self.master.destroy()
        GuiMain(mode=argmode)
    
    def about(self):
        '''
        Affiche les infos de l'application
        '''
        aboutWin = Tk()
        aboutWin.geometry("200x50")
        aboutWin.title("A propos")
        aboutDev = Label(aboutWin, text="Lionel FOUCAMBERT")
        aboutVer = Label(aboutWin, text="pyRename v0.1")
        aboutDev.pack()
        aboutVer.pack()
        aboutWin.lift()
        aboutWin.mainloop()

def main():
    GuiMain(True)

if __name__ == '__main__':
    main()
