from tkinter import *
from tkinter.ttk import *
from ruleset import *
from rename import *
from modal import *
from guiList import * 
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class GuiMain():
    def __init__(self, mode=True, rules=Ruleset(), renaming=Rename()):
        '''
        Constructeur
        mode : true pour lister, false pour créer
        '''
        self.master = Tk()
        self.ruleset = rules
        self.mode = mode
        self.checkBoxesState = None
        self.InitUI(None)

    def InitUI(self, mode):
        '''
        Initialise l'interface : création et placement des widgets
        param :
        mode - booléen : si True, mode renommage unique, sinon, mode création de règle
        '''
        self.master.title("pyRename")
        self.master.geometry("700x300")        
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu, relief=None)
        self.mainMenu = Menu(self.menu)
        self.mainMenu.add_command(label="Lister",command=self.openListUI)
        self.mainMenu.add_command(label="Renommer",command=lambda: self.refresh(True))
        self.mainMenu.add_command(label="Creer", command=lambda: self.refresh(False))
        self.menu.add_cascade(label="Regles",menu=self.mainMenu)
        self.menu.add_command(label="?",menu=None, command=self.about)
        if(self.mode):
            self.funcLabel = Label(self.master, text="Renommer en lots")
            self.nameLabel = Label(self.master, text="Nom du répertoire")
            self.renameBtn = Button(self.master, text="Renommer",command=self.renameButton)        
        else:
            self.funcLabel = Label(self.master, text="Créer une règle")
            self.nameLabel = Label(self.master, text="Nom de la règle")
            self.renameBtn = Button(self.master, text="Créer", command=self.createButton)
        self.logo = PhotoImage(file=resource_path("logo.png"))
        self.logoObject = Label(self.master, image = self.logo)
        self.ruleEntry = Entry(self.master)
        self.primerLabel = Label(self.master, text="Amorce")
        self.optSelect = StringVar()
        self.optValues = ("Aucune","Lettre","Chiffre")
        self.optList = Combobox(self.master, textvariable = self.optSelect, values = self.optValues, state = 'readonly')
        self.prefixEntry = Entry(self.master)
        self.prefixLabel = Label(self.master, text="Préfixe")
        self.varCbOriginal=BooleanVar()
        self.varCbOriginal.set(1)
        self.varCbCustom=BooleanVar()
        self.varCbCustom.set(0)
        self.checkBoxesState = True
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
        self.logoObject.grid(row=0,column=4)
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
        '''
        Permet de garantir que l'utilisateur ne peut cocher qu'une checkbox à la fois
        '''
        if checkbox=="original":
            self.varCbCustom.set(0)
            self.checkBoxesState = True
        if checkbox=="custom":
            self.varCbOriginal.set(0)
            self.checkBoxesState = False
            
    def renameButton(self):
        '''
        Lance le renommage des fichiers selon les widgets remplis
        '''
        if(self.optSelect.get()=="") | (self.varCbCustom.get()==self.varCbOriginal.get()) | (self.extensionEntry.get()==""):
            Modal()
            return  
        bufferRule = Rule(primer=self.optSelect.get(),\
                          sFrom=self.fromEntry.get(), \
                          prefix=self.prefixEntry.get(), \
                          bFilename=(self.checkBoxesState,self.entryCustomName.get()), \
                          suffix=self.suffixEntry.get(), \
                          extensions=self.inputToList(self.extensionEntry.get()))
        Rename(directory_name=self.ruleEntry.get(),rule=bufferRule).renameFiles()

    def inputToList(self, input):  
        return input.split(",")

    def createButton(self):
        '''
        Crée une règle et l'ajoute dans le ruleset.
        '''
        if(self.optSelect.get()=="") | (self.varCbCustom.get()==self.varCbOriginal.get()) | (self.extensionEntry.get()==""):
            Modal()
            return  
        bufferRule = Rule(primer=self.optSelect.get(),\
                          sFrom=self.fromEntry.get(), \
                          prefix=self.prefixEntry.get(), \
                          bFilename=(self.checkBoxesState,self.entryCustomName.get()), \
                          suffix=self.suffixEntry.get(), \
                          extensions=self.inputToList(self.extensionEntry.get()))
        self.ruleset.get_rules().append(bufferRule)
        self.ruleset.save()

    def openListUI(self):
        '''
        Ouvre l'UI qui liste les règles
        '''
        GuiList(self)
        return 


    def fillUIfromRule(self, prule):
        '''
        remplit l'UI avec une règle
        '''
        self.optSelect.delete()
        self.optSelect.insert(prule.get_primer())
        self.prefixEntry.delete()
        self.prefixEntry.insert(prule.get_prefix())
        if(prule.get_bFilename[0] is True):
            switchComboState("original")
        else:
            switchComboState("custom")
            self.entryCustomName.delete()
            self.entryCustomName.insert(prule.get_bFilename[1])
        self.suffixEntry.delete()
        self.suffixEntry.insert(prule.get_suffix())

    def get_ruleset(self):
        return self.ruleset

    
def main():
    defRuleset = Ruleset()
    defRuleset.load("pyRename.ini")
    GuiMain(True, defRuleset)

if __name__ == '__main__':
    main()
