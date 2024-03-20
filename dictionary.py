class Dictionary:
    def __init__(self):
        self.dizionario = []

    def loadDictionary(self,nome_file):
        with open(nome_file, "r") as file_dizionario:
            righe = file_dizionario.readlines()
            for riga in righe:
                self.dizionario.append(riga)

    # A COSA SERVE QUESTA FUNZIONE??
    def printAll(self):
        pass

    # A COSA SERVE QUESTA FUNZIONE??
    @property
    def dict(self):
        return self._dict