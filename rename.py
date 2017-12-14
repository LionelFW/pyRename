from action import *
from os import listdir, rename
from os.path import isfile, join

class Rename(Action):
    def __init__(self, directory_name=".", rule=Rule()):
        super().__init__(directory_name, rule)
        self.increment=0
    
    def renameFiles(self):
        '''
        Renomme les fichiers selon la règle rule membre
        '''
        try:
            fileList = [f for f in listdir(self.directory_name) if isfile(join(self.directory_name, f))&str(f).endswith(tuple(self.get_rule().get_extensions()))]
        except:
            return False
        for fFile in fileList:
            os.rename(fFile, self.ruleToString(fFile))
        return True