# pylint: disable=all
"""
Geschlecht:
true -> Mann
false -> Frau
"""

class Firma:
    Name = ""
    Abteilungen = []
    
    def __init__(self, name,abteilungen):
        self.Name = name
        self.Abteilungen = abteilungen
        
    def zaehleMitarbeiter(self):
        zahlMitarbeiter = 0
        zahlGruppenleiter = 0
        for i in self.Abteilungen:
            for j in i.Mitarbeiter:
                if isinstance(j,Gruppenleiter):
                    zahlGruppenleiter+=1
                elif isinstance(j,Mitarbeiter):
                    zahlMitarbeiter+=1
        return zahlMitarbeiter, zahlGruppenleiter
    
    def anzahlAbteilungen(self):
        return len(self.Abteilungen)
    
    def staerksteAbteilung(self):
        starkeAbteilung = ""
        zwischenSpeicher = 0
        for i in self.Abteilungen:
            zahlMitarbeiter = 0
            for j in i.Mitarbeiter:
                if isinstance(j,Mitarbeiter) or isinstance(j,Gruppenleiter):
                    zahlMitarbeiter+=1
            if zahlMitarbeiter > zwischenSpeicher:
                starkeAbteilung = i.Name
        return starkeAbteilung
    
    def prozentteilFrauMann(self):
        frauen = 0
        maenner = 0
        for i in self.Abteilungen:
            for j in i.Mitarbeiter:
                if isinstance(j,Mitarbeiter) or isinstance(j,Gruppenleiter):
                    if(j.Geschlecht):
                        maenner+=1
                    else:
                        frauen+=1
        return (frauen/(frauen+maenner))*100, (maenner/(frauen+maenner))*100
               
        
        
class Person:
    Name = ""
    Geschlecht = True
    
    def __init__(self,name,geschlecht):
        self.Name = name
        self.Geschlecht = geschlecht
        
    def __str__(self):
        if self.Geschlecht:
            return ("Herr " + self.Name)
        
        return ("Frau " + self.Name)

class Mitarbeiter(Person):
    
    
    def __init__(self, person):
        super().__init__(person.Name, person.Geschlecht)
    
    def __str__(self):
        return super().__str__() + " Abteilung:" + self.Abteilung
    

class Gruppenleiter(Mitarbeiter):
    
    def __init__(self, mitarbeiter):
        super().__init__(mitarbeiter)
    
    def __str__(self):
        return super().__str__() + " Gruppenleiter"
    
class Abteilung:
    Name = ""
    Mitarbeiter = []
    
    def __init__(self,name,mitarbeiter):
        self.Name = name
        self.Mitarbeiter = mitarbeiter

    def __str__(self):
        return self.Name + " " + self.Mitarbeiter.__str__()
    
    

def main():
    Mannfred = Person("Mannfred",True)
    Mueller = Person("Mueller",True)
    Thorsten = Person("Thorsten",True)
    Horst = Person("Horst",True)
    Anna = Person("Anna",False)
    Maria = Person("Maria",False)
    Laura = Person("Laura",False)
    
    
    mitMannfred = Mitarbeiter(Mannfred)
    mitMueller = Mitarbeiter(Mueller)
    mitThorsten = Mitarbeiter(Thorsten)
    mitHorst = Mitarbeiter(Horst)
    mitAnna = Mitarbeiter(Anna)
    mitMaria = Mitarbeiter(Maria)
    
    grupAnna = Gruppenleiter(mitAnna)
    
    abtLager = Abteilung("Lager", [mitHorst,mitMannfred])
    abtPost = Abteilung("Post", [mitMaria])
    abtChef = Abteilung("Chef", [grupAnna])
    abtGast = Abteilung("Gast", [Laura])
    abtProduktion = Abteilung("Produktion", [mitMueller,mitThorsten])
    
    FirmaABC = Firma("ABC-Teile",[abtChef,abtGast,abtLager,abtPost,abtProduktion])
    
    print("ANZ ABT: " + str(FirmaABC.anzahlAbteilungen()))
    print("ANZ MIT: " + str(FirmaABC.zaehleMitarbeiter()) + " Mit / Grup")
    print("Stär ABT: " + FirmaABC.staerksteAbteilung())
    print("Proz M/F: " + str(FirmaABC.prozentteilFrauMann()) + " F / M")
    
    




if __name__ == '__main__':
    main()

