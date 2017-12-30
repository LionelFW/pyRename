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
        self.okBtn = Button(self.master,state=DISABLED, text="OK", command=lambda: self.guiMain.fillUIfromRule(self.lineToRule()))
        self.cancelBtn = Button(self.master, text="Annuler", command=self.master.destroy)
        self.saveBtn = Button(self.master, text="Sauvegarder les règles", command=self.guiMain.get_ruleset().save())
        self.okBtn.grid(row=1,column=1,padx=5,pady=2)
        self.pardonLbl = Label(self.master, text="Ne fonctionne pas...")
        self.pardonLbl.grid(row=2, column=1,padx=5,pady=2)
        self.cancelBtn.grid(row=1,column=2,padx=5,pady=2)
        self.saveBtn.grid(row=1,column=3,padx=5,pady=2)
        self.master.mainloop()
    
    def lineToRule(self):
        '''
        transforme la ligne sélectionnée en règle
        '''
        paramList = str(self.optList.get()).split(":")[::2]
        x = [y.strip() for y in paramList]
        print(x)
        returnRule = Rule(x[0],x[1],x[2],x[3],x[4],x[5])
        return returnRule
        


    def ruleset_to_rulenameset(self):
        lResult = []
        for element in self.guiMain.get_ruleset().get_rules():
            lResult.append(str(element))
        return lResult