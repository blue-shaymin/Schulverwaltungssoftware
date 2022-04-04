class Raum:
    def __init__(self, nummer, laenge, breite):
        self.raumnummer = nummer
        self.laenge = laenge
        self.breite = breite
        self.flaeche = laenge * breite
        self.geraete = []

    def qm(self):
        return self.flaeche