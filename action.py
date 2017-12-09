import Rule from rule

class Action:
    def __init__(self, directory_name="default", rule=Rule()):
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

    def __str__(self):
        return "Directory name : '" + self.directory_name + "' \n" + str(self.rule)