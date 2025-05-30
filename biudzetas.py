from models import PajamuIrasas, IslaiduIrasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def parodyti_irasus(self):
        print(self.zurnalas)

    def ivesti_pajamas(self):
        suma = float(input("Suma: "))
        siuntejas = input("Siuntėjas: ")
        info = input("Info: ")
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)

    def ivesti_islaidas(self):
        suma = float(input("Suma: "))
        pirkinys = input("Pirkinys: ")
        info = input("Info: ")
        irasas = IslaiduIrasas(suma, pirkinys, info)
        self.zurnalas.append(irasas)

    def parodyti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                suma += irasas.suma
            if type(irasas) is IslaiduIrasas:
                suma -= irasas.suma
        print("Balansas", suma)