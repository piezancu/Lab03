class Dictionary:
    def __init__(self):
        self.dizionario = []

    def loadDictionary(self, nome_file):
        with open(nome_file, "r") as file_dizionario:
            righe = file_dizionario.readlines()
            for riga in righe:
                self.dizionario.append(riga.strip())

    def __iter__(self):
        return iter(self.dizionario)

    def __len__(self):
        return len(self.dizionario)

    def __getitem__(self, item):
        return self.dizionario[item]

    # A COSA SERVE QUESTA FUNZIONE??
    def printAll(self):
        pass

