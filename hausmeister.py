from mitarbeiter import Mitarbeiter
class Hausmeister(Mitarbeiter):
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
       super().__init__(vorname, nachname, geburtsdatum)


    def repariere_geraet(self, geraet):
        """ Setze den Zustand des Geräts auf: nicht defekt"""
        geraet.ist_defekt = False

    def pausenverkauf(self):
        # TODO: Kunden fragen, inwiefern diese Funktion im ASM benötigt wird
        pass