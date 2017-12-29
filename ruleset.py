from rule import *
import ast

class Ruleset:
    def __init__(self, rules=[Rule()]):
        self.rules = rules

    def get_rules(self):
        return self.rules

    def set_rules(self, prules):
        self.prules = prules

    def load(self, filename="pyRename.ini"):
        '''
        Charge les règles depuis le fichier filename
        Retourne True sur un succès, False sur un échec
        '''
        try:
            with open(filename,'r') as ruleFile:
                ruleList=ruleFile.readlines()
        except:
            return False
        self.rules = []
        for sRule in ruleList:
            lRule = sRule.split(",")
            self.rules.append(Rule(lRule[0],lRule[1],lRule[2],lRule[3],lRule[4],lRule[5]))
        return True

    def save(self, filename="pyRename.ini"):
        '''
        Sauvegarde les règles dans le fichier filename (overwrite le fichier filename)
        Retourne True sur un succès, False sur un échec
        '''
        try:
            ruleFile = open(filename,'w')
        except:
            return False
        for rule in self.rules:
            str(rule.get_primer())+","+str(rule.get_sFrom())+","+str(rule.get_prefix())+","+str(rule.get_bFilename())+","+str(rule.get_suffix())+","+str(rule.get_extensions())
        return True

    def __str__(self):
        sResult = ''
        for rule in self.rules:
            sResult += "\n"+str(rule)
        return sResult