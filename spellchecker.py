import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multi_dizionario = md.MultiDictionary()


    def handleSentence(self, txtIn, language):
        tempo_in_l = time.time()
        lista_parole_rw1 = self.multi_dizionario.searchWordLinear(txtIn, language)
        tempo_fin_l = time.time()
        tempo_l_impiegato = tempo_fin_l - tempo_in_l
        for parola in lista_parole_rw1:
            if not parola.corretta:
                print(parola)
        print(tempo_l_impiegato)
        tempo_in_d = time.time()
        lista_parole_rw2 = self.multi_dizionario.searchWordDichotomic(txtIn, language)
        tempo_fin_d = time.time()
        tempo_d_impiegato = tempo_fin_d - tempo_in_d
        for parola in lista_parole_rw2:
            if not parola.corretta:
                print(parola)
        print(tempo_d_impiegato)


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")
