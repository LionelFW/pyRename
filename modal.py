from tkinter import *

class Modal():
    def __init__(self, context="remplissage"):
        self.InitUI()
        self.context = context

    def InitUI(self):
        self.errorModal = Tk()
        self.errorModal.geometry("400x50")
        self.errorModal.title("Erreur")
        if(self.context == "remplissage"):
            self.errorMessage = Label(self.errorModal, text="Les inputs Amorce, Nom du fichier,\n et Extension doivent être remplis")
        if(self.context=="value"):
            self.errorMessage = Label(self.errorModal, text="Erreur de valeur dans A partir de")
        self.errorMessage.pack()
        self.okBtn = Button(self.errorModal, text="OK", command=self.errorModal.destroy)
        self.okBtn.pack()
        self.errorModal.lift()
        self.errorModal.mainloop()
