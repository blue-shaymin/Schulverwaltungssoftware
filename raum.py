class Raum:
    def __init__(self, nummer, laenge, breite):
        self._breite = 0
        self.raumnummer = nummer
        self.laenge = laenge
        self.breite = breite
        self.geraete = []

    def set_raumnummer(self,nummer):
        self._raumnummer = nummer

    def get_raumnummer(self):
        return self._raumnummer

    raumnummer = property(get_raumnummer, set_raumnummer)

    def set_laenge(self,l):
        if l < 0:
            raise ValueError
        self._laenge = l
        self._flaeche = self._breite * self._laenge

    def get_laenge(self):
        return self._laenge

    laenge = property(get_laenge, set_laenge)

    def set_breite(self, b):
        if b < 0:
            raise ValueError
        self._breite = b
        self._flaeche = self._breite * self._laenge

    def get_breite(self):
        return self._breite

    breite = property(get_breite,set_breite)


    def get_flaeche(self):
        return self.flaeche

    flaeche = property(get_flaeche)

n = Raum(1,2,3)


