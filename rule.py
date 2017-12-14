class Rule:
    def __init__(self, primer="Aucun", sFrom="a", prefix=None, bFilename=(False,""), suffix=None, extensions=[".txt"]):
        self.primer = primer
        self.sFrom = sFrom
        self.prefix = prefix
        self.bFilename = bFilename
        self.suffix = suffix
        self.extensions = extensions
    
    def get_primer(self):
        return self.primer
    
    def set_primer(self, pprimer):
        self.primer = pprimer

    def get_sFrom(self):
        return self.sFrom

    def set_sFrom(self, psFrom):
        self.sFrom = psFrom

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, pprefix):
        self.prefix = pprefix

    def get_bFilename(self):
        return self.bFilename

    def set_bFilename(self, pbFilename):
        self.bFilename = pbFilename

    def get_suffix(self):
        return self.suffix

    def set_suffix(self, psuffix):
        self.suffix = psuffix

    def get_extensions(self):
        return get_extensions

    def set_extensions(self, pextensions):
        self.extensions = pextensions

    def __str__(self):
        return "primer : " + self.primer + ", sFrom : " + self.sFrom + ", prefix : " + self.prefix + ", bFilename : " + str(bFilename) + ", suffix : " + self.suffix + ", extensions :" + str(self.extensions)
    