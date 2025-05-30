from models import Irasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def parodyti_irasus(self):
        print(self.zurnalas)

    def ivesti_pajamas(self):
        suma = float(input("Suma: "))
        irasas = Irasas(suma, "pajamos")
        self.zurnalas.append(irasas)

    def ivesti_islaidas(self):
        suma = float(input("Suma: "))
        irasas = Irasas(suma, "išlaidos")
        self.zurnalas.append(irasas)

    def parodyti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if irasas.tipas == "pajamos":
                suma += irasas.suma
            if irasas.tipas == "išlaidos":
                suma -= irasas.suma
        print("Balansas", suma)