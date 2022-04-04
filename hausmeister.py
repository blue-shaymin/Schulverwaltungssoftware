class Hausmeister:
    """
    Diese Klasse repräsentiert den Hausmeister einer Schule

    Attribute
    ---------
    vorname : str
        der Vorname
    nachname : str
        der Nachname
    geburtsdatum : Date
        das Geburtsdatum
    """

    def __init__(self, vorname, nachname, geburtsdatum):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum

    def melde_defekt(self, geraet):
        # TODO : Funktionalität umsetzen
        pass

    def repariere_geraet(self, geraet):
        """ Setze den Zustand des Geräts auf: nicht defekt"""
        geraet.ist_defekt = False

    def pausenverkauf(self):
        # TODO: Kunden fragen, inwiefern diese Funktion im ASM benötigt wird
        pass