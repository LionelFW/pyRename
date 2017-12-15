from os import *
from rule import *
import string
import modal

class Action:
    def __init__(self, directory_name=".", rule=Rule()):
        self.directory_name = directory_name
        self.rule = rule
        

    def get_directory_name(self):
        return self.directory_name

    def set_directory_name(self, pdirectory_name):
        self.directory_name = pdirectory_name

    def get_rule(self):
        return self.rule

    def set_rule(self, prule):
        self.rule = prule

    def simulate(self):
        '''
        Affiche une simulation du renommage dans la console
        '''
        if self.get_rule().get_primer()=="Lettre":
            sList = self.get_rule().get_primer().split("")
            #Pas eu le temps de faire l'algo...
            #En gros, il faudrait repasser les valeurs de la base 26 à la base 10
            #Le problème c'est que je me base sur une liste, dont la taille n'est pas garantie
            #cela peutêtre 1, 2 ou 3 éléments...
            #mais en gros
            # increment = list[2]* (26²) + list[1]*(26¹) + list[0]*(26⁰)
            increment = 0
        else:
            try:
                increment = int(self.get_rule().get_sFrom())
            except:
                Modal("value")
                return
        try:
            extensions = tuple(self.get_rule().get_extensions())
            fileList = [f for f in listdir(self.get_directory_name()) if f.endswith(extensions)]
        except:
            return False    
        for fFile in fileList:
            print(fFile +" -> "+self.ruleToString(fFile, increment))
            increment += 1
        increment = 0  
        return True

    def ruleToString(self, fFile, incrementArg):
        '''
        Prépare une chaine qui sera le nouveau nom du fichier
        '''
        sResult = ""
        if self.rule.get_primer()=="Lettre":
            sBuffer = []
            if incrementArg==0:
                sBuffer+=string.ascii_uppercase[0]
            while incrementArg:
                sBuffer+=string.ascii_uppercase[incrementArg % 26]
                incrementArg = incrementArg // 26
            sBuffer.reverse()
            sResult += ''.join(sBuffer)
        elif (self.rule.get_primer()=="Chiffre") | (self.rule.get_primer()=="Aucun"):
            #Aucune amorce ne fait pas de sens... Sinon, rien ne change dans la chaine
            #Et on ne peut pas avoir n fichiers avec le même 
            sResult += "{0:03}".format(incrementArg)
        sResult+=self.rule.get_prefix()
        tFilename = self.rule.get_bFilename()
        if tFilename[0]:
            sResult+=fFile.split(".")[0]
        else:
            sResult+=tFilename[1]
        sResult+=self.rule.get_suffix()
        sResult+="."
        sResult+=fFile.split(".")[-1]
        return sResult

    def __str__(self):
        return "Directory name : '" + self.directory_name + "' \n" + str(self.rule)