from mitarbeiter import Mitarbeiter
class Lehrer(Mitarbeiter):
    """
    Diese Klasse repräsentiert eine Lehrkraft

    Attribute
    ---------
    vorname : str
        Der Vorname der Lehrkraft
    nachname : str
        Der Nachname der Lehrkraft
    geburtsdatum : Date
        Das Geburtsdatum der Lehrkraft
    dienstbezeichnung : str
        Die Dienst/Amtsbezeichnung der Lehrkraft

    """

    def __init__(self, vorname, nachname, geburtsdatum, dienstbezeichnung):
        super().__init__(vorname, nachname, geburtsdatum)
        self.dienstbezeichnung = dienstbezeichnung

    def unterrichten(self, klasse):
        pass