class Schueler:
    """
    Diese Klasse repräsentiert einen Schüler

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

    def verlasse_schule(self):
        pass