class Ruleset:
    def __init__(self, rules=[Rule()])
        self.rules = rules

    def get_rules(self):
        return self.rules

    def set_rules(self, prules):
        self.prules = prules

    def load(filename="pyRename.ini"):
        pass

    def save(filename="pyRename.ini"):
        pass

    def __str__(self):
        for rule in self.rules:
            sResult += "\n"+str(rule)
        return sResult