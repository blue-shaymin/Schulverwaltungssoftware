class Geraet:
    """
    Diese Klasse ist für Geräte, die sich in der Schule befinden

    Attribute
    ---------
    hersteller : str
        Der Name des Herstellers
    modell : str
        Die Modellbezeichnung
    ist_defekt : bool
        gibt an, ob das Gerät defekt ist
    """
    def __init__(self, hersteller, modell):
        self.hersteller = hersteller
        self.modell = modell
        self.ist_defekt = False

    def info(self):
        """ Gibt Informationen über das Gerät aus"""
        if self.ist_defekt:
            print(f"{self.hersteller} - {self.modell} ist defekt")
        else:
            print(f"{self.hersteller} - {self.modell} ist funktionsfähig")