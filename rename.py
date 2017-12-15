from action import *
from os import listdir, rename, sep
from os.path import isfile, join

class Rename(Action):
    def __init__(self, directory_name=".", rule=Rule()):
        super().__init__(directory_name, rule)
        self.increment=0
    
    def renameFiles(self):
        '''
        Renomme les fichiers selon la règle rule membre
        '''
        increment = 0
        try:
            extensions = tuple(self.get_rule().get_extensions())
            fileList = [f for f in listdir(self.get_directory_name()) if f.endswith(extensions)]
        except:
            return False
        for fFile in fileList:
            rename(self.directory_name+sep+fFile, self.directory_name+sep+self.ruleToString(fFile, increment))
            increment += 1
        increment = 0
        return True