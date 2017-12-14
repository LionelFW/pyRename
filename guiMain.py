from tkinter import *
from tkinter.ttk import *
from ruleset import *
from rename import *

class GuiMain():
    def __init__(self, mode=True, rules=Ruleset(), renaming=Rename()):
        '''
        Constructeur
        mode : true pour lister, false pour créer
        '''
        self.master = Tk()
        self.ruleset = rules
        self.mode = mode
        self.InitUI(None)

    def InitUI(self, mode):
        '''
        Initialise l'interface : création et placement des widgets 
        '''
        self.master.title("pyRename")
        self.master.geometry("900x300")        
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu, relief=None)
        self.mainMenu = Menu(self.menu)
        self.mainMenu.add_command(label="Lister",command=lambda: self.refresh(True))
        self.mainMenu.add_command(label="Creer", command=lambda: self.refresh(False))
        self.menu.add_cascade(label="Regles",menu=self.mainMenu)
        self.menu.add_command(label="?",menu=None, command=self.about)

        if(self.mode):
            self.funcLabel = Label(self.master, text="Renommer en lots")
            self.nameLabel = Label(self.master, text="Nom du répertoire")
            self.renameBtn = Button(self.master, text="Renommer",command=None)        
        else:
            self.funcLabel = Label(self.master, text="Créer une règle")
            self.nameLabel = Label(self.master, text="Nom de la règle")
            self.renameBtn = Button(self.master, text="Créer", command=None)

        self.ruleEntry = Entry(self.master)
        self.primerLabel = Label(self.master, text="Amorce")
        self.optSelect = StringVar()
        self.optValues = ("Aucune","Lettre","Chiffre")
        self.optList = Combobox(self.master, textvariable = self.optSelect, values = self.optValues, state = 'readonly')
        self.prefixEntry = Entry(self.master)
        self.prefixLabel = Label(self.master, text="Préfixe")
        self.varCbOriginal=BooleanVar()
        self.varCbCustom=BooleanVar()
        self.cbOriginalName = Checkbutton(self.master, text="Nom original", command=lambda: self.switchComboState("original"), variable=self.varCbOriginal)
        self.filenameLabel = Label(self.master, text="Nom du fichier")
        self.suffixEntry = Entry(self.master)
        self.suffixLabel = Label(self.master, text="Suffixe")
        self.extensionEntry = Entry(self.master)
        self.extensionLabel = Label(self.master, text="Extension concernée")
        self.filenameFrame = Frame(self.master)
        self.cbCustomName = Checkbutton(self.filenameFrame, text="",command=lambda: self.switchComboState("custom"), variable=self.varCbCustom)
        self.entryCustomName = Entry(self.filenameFrame, width=9)
        self.fromlabel = Label(self.master, text="A partir de")
        self.fromEntry = Entry(self.master)

        
        self.funcLabel.grid(row=0,column=1,padx=5,pady=2)
        self.nameLabel.grid(row=1,column=0,padx=5,pady=2)
        self.ruleEntry.grid(row=1,column=1,padx=5,pady=2,sticky=W+E)
        self.primerLabel.grid(row=2,column=0,padx=5,pady=2)
        self.prefixLabel.grid(row=2,column=1,padx=5,pady=2)
        self.filenameLabel.grid(row=2,column=2,padx=5,pady=2)
        self.suffixLabel.grid(row=2,column=3,padx=5,pady=2)
        self.extensionLabel.grid(row=2,column=4,padx=5,pady=2)
        self.optList.grid(row=3,column=0,sticky=W,padx=5,pady=2)
        self.prefixEntry.grid(row=3, column=1,padx=5,pady=2,sticky=W+E)
        self.cbOriginalName.grid(row=3, column=2,padx=5,pady=2)
        self.suffixEntry.grid(row=3, column=3,padx=5,pady=2,sticky=W+E)
        self.extensionEntry.grid(row=3, column=4,padx=5,pady=2,sticky=W+E)
        self.filenameFrame.grid(row=4, column=2,padx=5,pady=2)
        self.cbCustomName.grid(row=0,column=0)
        self.entryCustomName.grid(row=0,column=1)
        self.renameBtn.grid(row=5,column=4,padx=5,pady=2)
        self.fromlabel.grid(row=5,column=0,padx=5,pady=2)
        self.fromEntry.grid(row=6,column=0,padx=5,pady=2)
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
        self.aboutWin = Tk()
        self.aboutWin.geometry("200x50")
        self.aboutWin.title("A propos")
        self.aboutDev = Label(self.aboutWin, text="Lionel FOUCAMBERT")
        self.aboutVer = Label(self.aboutWin, text="pyRename v0.1")
        self.aboutDev.pack()
        self.aboutVer.pack()
        self.aboutWin.lift()
        self.aboutWin.mainloop()
    
    def switchComboState(self, checkbox):
        if checkbox=="original":
            self.varCbCustom.set(0)
        if checkbox=="custom":
            self.varCbOriginal.set(0)
    def renameButton(self):
        pass

    def createButton():
        pass

def main():
    defRuleset = Ruleset()
    defRuleset.load("pyRename.ini")
    GuiMain(True)

if __name__ == '__main__':
    main()
