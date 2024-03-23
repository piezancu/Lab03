import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dizionario = d.Dictionary()

    def printDic(self, language):
        pass

    def searchWordLinear(self, words, language):
        lista_rw = []
        parole = words.strip().split()
        self.dizionario.loadDictionary(f"C:/Users/39348/PycharmProjects/Lab03/resources/{language}.txt")
        for parola in parole:
            parola.lower()
            self.replaceChars(parola)
            parola_rw = rw.RichWord(parola)
            if parola in self.dizionario:
                parola_rw.corretta = True
            else:
                parola_rw.corretta = False
            lista_rw.append(parola_rw)
        return lista_rw

    def searchWordDichotomic(self, words, language):
        lista_rw = []
        parole = words.strip().split()
        indice_iniz = int(len(self.dizionario) / 2)
        parola_centrale_diz = self.dizionario[indice_iniz]
        for parola in parole:
            parola.lower()
            self.replaceChars(parola)
            parola_rw = rw.RichWord(parola)
            parola_rw.corretta = False
            if parola<parola_centrale_diz:
                for i in range(indice_iniz, 0, -1):
                    if parola == self.dizionario[i]:
                        parola_rw.corretta = True
            else:
                for i in range(indice_iniz, len(self.dizionario)):
                    if parola == self.dizionario[i]:
                        parola_rw.corretta = True
            lista_rw.append(parola_rw)
        return lista_rw

    def replaceChars(self, parola):
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            parola = parola.replace(c, "")
        return parola
