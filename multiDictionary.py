import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self, dizionario):
        self.dizionario = d.Dictionary

    def printDic(self, language):
        pass

    def searchWordLinear(self, words, language):
        lista_rw = []
        parole = words.strip().split()
        for parola in parole:
            parola.lower()
            self.replaceChars(parola)
            parola_rw = rw.RichWord(parola)
            self.dizionario.loadDictionary(f"{language}.txt")
            if self.dizionario.contains(parola):
                parola_rw.corretta(True)
            else:
                parola_rw.corretta(False)
            lista_rw.append(parola_rw)
        return lista_rw

    def searchWordDichotomic(self, words, language):
        lista_rw = []
        parole = words.strip().split()
        dizionario = d.Dictionary.loadDictionary(f"{language}.txt")
        indice_iniz = int(len(dizionario) / 2)
        parola_centrale_diz = dizionario[indice_iniz]
        for parola in parole:
            parola.lower()
            self.replaceChars(parola)
            parola_rw = rw.RichWord(parola)
            if parola<parola_centrale_diz:
                for i in range(indice_iniz, 0, -1):
                    if parola == dizionario[i]:
                        parola_rw.corretta(True)
            else:
                for i in range(indice_iniz, len(dizionario)):
                    if parola == dizionario[i]:
                        parola_rw.corretta(False)
        return lista_rw

    def replaceChars(self, parola):
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            parola = parola.replace(c, "")
        return parola
