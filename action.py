from rule import *
from os import *

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
        try:
            fileList = [f for f in listdir(self.directory_name) if isfile(join(self.directory_name, f))&str(f).endswith(tuple(self.get_rule().get_extensions()))]
        except:
            return False
        for fFile in fileList:
            print(fFile +" -> "+self.ruleToString(fFile))
        return True

    def ruleToString(self, fFile):
        '''
        Prépare une chaine qui sera le nouveau nom du fichier
        '''
        if self.rule.get_primer()=="Lettre":
            if self.increment > 25:
                pass
            else:
                sResult.append(chr(ord() + self.increment))
        sResult.append(self.rule.get_prefix())
        tFilename = self.rule.get_bFilename()
        if tFilename[0]:
            sResult.append(fFile)
        else:
            sResult.append(tFilename[1])
        sResult.append(self.rule.get_suffix())
        sResult.append(os.path.splitext(fFile))

    def __str__(self):
        return "Directory name : '" + self.directory_name + "' \n" + str(self.rule)