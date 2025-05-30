from models import PajamuIrasas, IslaiduIrasas
import pickle

class Biudzetas:
    def __init__(self):
        self.zurnalas = self.gauti_zurnala()

    def gauti_zurnala(self):
        try:
            with open("zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except:
            zurnalas = []
        return zurnalas

    def issaugoti_zurnala(self):
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def parodyti_irasus(self):
        print(self.zurnalas)

    def ivesti_pajamas(self):
        suma = float(input("Suma: "))
        siuntejas = input("Siuntėjas: ")
        info = input("Info: ")
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self.issaugoti_zurnala()

    def ivesti_islaidas(self):
        suma = float(input("Suma: "))
        pirkinys = input("Pirkinys: ")
        info = input("Info: ")
        irasas = IslaiduIrasas(suma, pirkinys, info)
        self.zurnalas.append(irasas)
        self.issaugoti_zurnala()

    def parodyti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                suma += irasas.suma
            if type(irasas) is IslaiduIrasas:
                suma -= irasas.suma
        print("Balansas", suma)