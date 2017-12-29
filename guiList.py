from tkinter import *
from tkinter.ttk import *

class GuiList():
    def __init__(self, p_guiMain):
        self.master = Tk()
        self.guiMain = p_guiMain
        self.InitUI()

    def InitUI(self):
        self.master.title("Règles")
        self.master.geometry("400x75")
        self.optSelect = StringVar()
        self.optValues = self.ruleset_to_rulenameset()
        self.optList = Combobox(self.master, textvariable = self.optSelect, values = self.optValues, state = 'readonly')
        self.optList.grid(row=0,column=1,padx=5,pady=2,sticky=W+E)
        self.okBtn = Button(self.master, text="OK", command=lambda: self.guiMain.fillUIfromRule())
        self.cancelBtn = Button(self.master, text="Annuler", command=self.master.destroy)
        self.saveBtn = Button(self.master, text="Sauvegarder les règles", command=self.guiMain.get_ruleset().save())
        self.okBtn.grid(row=1,column=1,padx=5,pady=2)
        self.cancelBtn.grid(row=1,column=2,padx=5,pady=2)
        self.saveBtn.grid(row=1,column=3,padx=5,pady=2)
        self.master.mainloop

    def ruleset_to_rulenameset(self):
        lResult = []
        for element in self.guiMain.get_ruleset().get_rules():
            lResult.append(str(element))
        return lResult