import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):


    def handleSentence(self, txtIn, language):
        tempo_in_l = time.time()
        lista_parole_rw = md.MultiDictionary.searchWordLinear(txtIn, language)
        tempo_fin_l = time.time()
        tempo_l_impiegato = tempo_fin_l - tempo_in_l
        for parola in lista_parole_rw:
            if parola.corretta:
                print(parola)
        print(tempo_l_impiegato)
        tempo_in_d = time.time()
        lista_parole_rw = md.MultiDictionary.searchWordDichotomic(txtIn, language)
        tempo_fin_d = time.time()
        tempo_d_impiegato = tempo_fin_d - tempo_in_d
        for parola in lista_parole_rw:
            if parola.corretta:
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
