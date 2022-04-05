class Mitarbeiter:
    def __init__(self, vorname, nachname, geburtsdatum):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
    def melde_defekt(self, geraet):
        geraet.ist_defekt = True