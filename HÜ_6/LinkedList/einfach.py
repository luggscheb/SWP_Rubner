# sort
# reverse
# deep copy

import random

import schemdraw
from schemdraw.flow import *

class Element:
    def __init__(self,wert:int):
        self.wert = wert
        self.folgend = None
        
class VerknüpfteListe:
    def __init__(self):
        self.kopf = None
    
    def AusgebenAllerWerte(self) -> str:
        aktuell = self.kopf
        ausgabeString = ""
        while aktuell is not None:
            ausgabeString += str(aktuell.wert) + " "
            aktuell = aktuell.folgend
        return ausgabeString
    
    def AusgebenTupl(self) -> list:
        aktuell = self.kopf
        ausgabeString = []
        while aktuell is not None:
            ausgabeString.append(aktuell.wert)
            aktuell = aktuell.folgend
        return tuple(ausgabeString)
    
    def AusgebenVisuell(self):
        with schemdraw.Drawing() as d:
            aktuell = self.kopf
            d+= Start().label("Start")
            
            while aktuell is not None:
                d+= Arrow(w = 7).right(d.unit/2)
                d+= Box(w = 2).label(str(aktuell.wert))
                aktuell = aktuell.folgend
                
            d+= Arrow(w = 5).right(d.unit/2)    
            d+= (end := Ellipse().label("Ende"))
                

    def AnfangEinfügen(self,wert:int):
        if self.kopf is None:
            neuesElement = Element(wert)
            self.kopf = neuesElement
        else:
            neuesElement = Element(wert)
            neuesElement.folgend = self.kopf
            self.kopf = neuesElement
    
    def AnfangEinfügenArgs(self, *args:int):
        for a in args:
            self.AnfangEinfügen(a)
    
    def EndeEinfügen(self, wert:int):
        if self.kopf is None:
            neuesElement = Element(wert)
            self.kopf = neuesElement
        else:
            aktuellesElement = self.kopf
            while aktuellesElement.folgend is not None:
                aktuellesElement = aktuellesElement.folgend
            neuesElement = Element(wert)
            aktuellesElement.folgend = neuesElement
        
    def EndeEinfügenArgs(self, *args:int):
        for a in args:
            self.EndeEinfügen(a)
    
    def ElementeZählen(self) -> int:
        anzahl = 0
        aktuellesElement = self.kopf
        while aktuellesElement is not None:
            anzahl += 1
            aktuellesElement = aktuellesElement.folgend
        return anzahl

    def ElementFinden(self,zufinden) -> int:
        anzahl = 0
        aktuellesElement = self.kopf
        try:
            while aktuellesElement.wert is not zufinden:
                anzahl += 1
                aktuellesElement = aktuellesElement.folgend
        except:
                return None
        return anzahl
    
    def AddireAlleElemente(self) -> int:
        summe = 0
        aktuellesElement = self.kopf
        while aktuellesElement is not None:
            summe += aktuellesElement.wert
            aktuellesElement = aktuellesElement.folgend
        return summe
    
    def EntferneErstesElement(self):
        if self.kopf is None:
            raise Exception("Liste ist Leer, kann nicht gelöscht werden.")
        else:
            aktuellesElement = self.kopf
            self.kopf = self.kopf.folgend
            del aktuellesElement
    
    def EntferneLetztesElement(self):
        if self.kopf is None:
            raise Exception("Liste ist Leer, kann nicht gelöscht werden.")
        else:
            aktuellesElement = self.kopf
            vorherigesElement = None
            while aktuellesElement.folgend is not None:
                vorherigesElement = aktuellesElement
                aktuellesElement = aktuellesElement.folgend
            vorherigesElement.folgend = None
            del aktuellesElement
            
    def EntferneAnPosition(self, position:int):
        if self.kopf is None:
            raise Exception("Liste ist Leer, kann nicht gelöscht werden.")
        else:
            aktuellesElement = self.kopf
            vorherigesElement = None
            zähler = 0
            while aktuellesElement.folgend is not None and zähler < position:
                vorherigesElement = aktuellesElement
                aktuellesElement = aktuellesElement.folgend
                zähler += 1
            if aktuellesElement == self.kopf:
                self.kopf = aktuellesElement.folgend
                del aktuellesElement
            else:
                vorherigesElement.folgend = aktuellesElement.folgend
                del aktuellesElement
    
    def ListeLöschen(self):
        self.kopf = None
        
    def ZufälligBefüllen(self,anzahl:int, min:int, max:int):
        for i in range(anzahl+1):
           self.EndeEinfügen(random.randint(min,max))
    
    def Umdrehen(self):
        vorher = None
        aktuell = self.kopf
        while(aktuell is not None):
            nächstes = aktuell.folgend
            aktuell.folgend = vorher
            vorher = aktuell
            aktuell = nächstes
        self.kopf = vorher
        
    def Kopieren(self,zukopieren):
        neueListe = VerknüpfteListe()
        neueListe.EndeEinfügenArgs(*zukopieren.AusgebenTupl())
        return neueListe
    
    def insertionSortieren(self,kopfvonUnsort):
        
        sortiert = None
        aktuell = kopfvonUnsort
        while (aktuell != None):
            nächstes = aktuell.folgend
            sortiert = self.sortiertEinfügen(sortiert,aktuell)
            aktuell = nächstes
        
        kopfvonUnsort = sortiert
        return kopfvonUnsort
    
    def sortiertEinfügen(self,kopfvonUnsort, nächstes):
        aktuell = None
        if (kopfvonUnsort == None or kopfvonUnsort.wert >= nächstes.wert):   
            nächstes.folgend = kopfvonUnsort
            kopfvonUnsort = nächstes
        else:
            aktuell = kopfvonUnsort
            
            while (aktuell.folgend != None and aktuell.folgend.wert < nächstes.wert):       
                aktuell = aktuell.folgend
            nächstes.folgend = aktuell.folgend
            aktuell.folgend = nächstes
        return kopfvonUnsort
        
   
        
def main():
    Liste = VerknüpfteListe()
    # Liste.EndeEinfügenArgs(5,55677,3,244,635,746,8)
    Liste.ZufälligBefüllen(20,0,200)
    
    # Liste.AnfangEinfügen(88)
    # print(Liste.AusgebenVisuell())
    # print(Liste.ElementeZählen())
    # print(Liste.AddireAlleElemente())
    # Liste.EntferneAnPosition(3)
    # Liste.AusgebenVisuell()
    
    print(Liste.ElementFinden(3))
    
    # Liste.Umdrehen()
    Liste.AusgebenVisuell()
    
    # Liste2 = Liste.Kopieren(Liste)
    # Liste2.AusgebenVisuell()
    
    Liste.insertionSortieren(Liste.kopf)
    Liste.AusgebenVisuell()
    
    
        
if __name__ == '__main__':
    main()
    