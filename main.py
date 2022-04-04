from lehrer import Lehrer
from hausmeister import Hausmeister
from geraet import  Geraet
import datetime

if __name__ == "__main__":
    srg = Lehrer(vorname="Markus", nachname="Scherg", geburtsdatum=datetime.date(1987,2,18), dienstbezeichnung="StRef")
    mst = Hausmeister(vorname="Horst", nachname="Fiebig", geburtsdatum=None)

    drucker = Geraet(hersteller="HP", modell="DeskJet 3762")

    drucker.info()

    srg.melde_defekt(drucker)

    drucker.info()

    mst.repariere_geraet(drucker)

    drucker.info()

    mst.melde_defekt(drucker)

    drucker.info()