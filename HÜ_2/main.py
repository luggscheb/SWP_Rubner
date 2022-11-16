"""
Paar = 2 gleiche Zahlen
doppelPaar = 2 gleiche Zahlen *2
drilling = 3 gleiche Zahlen
Straße = zb: 10,9,8,7,6
Flush = 5 gleiche Farben
FullHouse = drilling und zwilling
vierling = 4 gleiche zahlen 
straßen flush = straße und flush
royal flush = A,K,Q,J,10 und stern    
"""
import random
import os
import platform
from tabulate import tabulate

möglich=[]
gezogen=[]

class Card:
    nummer = 0
    farbe = 0
    
    def __init__(self,farbe, nummer):
        self.farbe = farbe
        self.nummer = nummer
        
        
    
    def ausgeben(self):
        ausgabe = "["
        if self.farbe == 0:
            ausgabe += "'Herz'".center(9, ' ')
        if self.farbe == 1:
            ausgabe += "'Karo'".center(9, ' ')
        if self.farbe == 2:
            ausgabe += "'Pik'".center(9, ' ')
        if self.farbe == 3:
            ausgabe += "'Kreuz'".center(9, ' ')
        ausgabe += "|" 
        if self.nummer == 14:
               ausgabe += "'A'".center(5, ' ') 
        elif self.nummer == 11:
               ausgabe += "'J'".center(5, ' ') 
        elif self.nummer == 12:
               ausgabe += "'Q'".center(5, ' ') 
        elif self.nummer == 13:
           ausgabe += "'K'".center(5, ' ') 
        else:
           ausgabe += str(self.nummer).center(5, ' ')
        ausgabe += "]\n" 
        print(ausgabe)
            
    
    
def init():
    del gezogen[::]
    del möglich[::]
    for i in range(4):
        for j in range(2,15):
            möglich.append(Card(i,j))
        
def ziehen(anzahl):
    for i in range(anzahl):
            r = random.randint(0,len(möglich)-1)
            # print(r,len(möglich))
            gezogen.append(möglich[r])
            del möglich[r]
        
def royalFlush(array):
    for i in array:
        if i.farbe != 1:
            return False
        if i.nummer == 14 or i.nummer == 13 or i.nummer == 12 or i.nummer == 11 or i.nummer == 10:
            return True
        else:
            return False
            

def straßeFlush(array):
    farbe = array[0].farbe
    for i in array:
        if i.farbe != farbe:
            return False
        
    start = -1
    for i in array:
        if i.nummer > start:
            start = i.nummer 
    b = 0
    for i in array:
        vorhanden = False
        for j in array:
            if j.nummer == (start - b):
                vorhanden = True
        if not vorhanden:
            return False     
        b+=1
    return True    

def vierling(array):
    for i in array:
        durchlaufZähler = 0
        nummer1 = i.nummer
        for j in array:
            if j.nummer == i.nummer: 
                durchlaufZähler+=1
        if durchlaufZähler == 4:
            return True
    return False

def fullHouse(array):
    for i in array:
        durchlaufZähler = 0
        for j in array:
            if j.nummer == i.nummer: 
                durchlaufZähler+=1
                
        if durchlaufZähler == 3:
            for a in array:
                durchlaufZähler2 = 0
                for b in array:
                    if b.nummer == a.nummer: 
                        durchlaufZähler2+=1
            if durchlaufZähler2 == 2:
                return True
            
    return False        
    
    
    

def flush(array):
    start = array[0].farbe
    zähler = 0
    for i in array:
        if i.farbe == start: 
            zähler+=1
    if zähler >= 5:
        return True

def straße(array):
    start = -1
    for i in array:
        if i.nummer > start:
            start = i.nummer 
    b = 0
    for i in range(0,5):
        vorhanden = False
        for j in array:
            if j.nummer == (start - b):
                vorhanden = True
        if not vorhanden:
            return False     
        b+=1
    return True  
    

def drilling(array):
    for i in array:
        durchlaufZähler = 0
        for j in array:
            if j.nummer == i.nummer: 
                durchlaufZähler+=1
                
        if durchlaufZähler == 3:
            return True
    return False

def doppelpaar(array):
    nummerbereits = 0
    fabrebereits = 0
    for i in array:
        durchlaufZähler = 0
        for j in array:
            if j.nummer == i.nummer: 
                nummerbereits = j.nummer
                fabrebereits = j.farbe
                durchlaufZähler+=1
                
        if durchlaufZähler == 2:
            for a in array:
                durchlaufZähler2 = 0
                for b in array:
                    if b.nummer == a.nummer: 
                        if b.nummer != nummerbereits and b.farbe != fabrebereits:
                            durchlaufZähler2+=1 
            if durchlaufZähler2 == 2:
                return True
    return False
    
def paar(array):
    for i in array:
        durchlaufZähler = 0
        for j in array:
            if j.nummer == i.nummer: 
                durchlaufZähler+=1
                
        if durchlaufZähler == 2:
            return True
    return False

def auswerten(array):
    if(royalFlush(array)):
        return "Royal Flush"
    if(straßeFlush(array)):
        return "Straße Flush"
    if(vierling(array)):
        return "Vierling"
    if(fullHouse(array)):
        return "Fullhouse"
    if(flush(array)):
        return "Flush"
    if(straße(array)):
        return "Straße"
    if(drilling(array)):
        return "Drilling"
    if(doppelpaar(array)):
        return "Doppel Paar"
    if(paar(array)):
        return "Paar"
    else:
        return "High Card"

RoyalFlush = 0
StraßeFlush = 0
Vierling = 0
Fullhouse = 0
Flush = 0
Straße = 0
Drilling = 0
DoppelPaar = 0
Paar = 0
HighCard = 0
def Statistik(auswertung='none',wiederholung=0, isReturn=False):
    global RoyalFlush, StraßeFlush, Vierling, Fullhouse, Flush, Straße, Drilling, DoppelPaar, Paar, HighCard
    
    if (auswertung == "Royal Flush"):
        RoyalFlush+=1
    if (auswertung =="Straße Flush"):
        StraßeFlush+=1
    if (auswertung =="Vierling"):
        Vierling+=1
    if (auswertung =="Fullhouse"):
        Fullhouse+=1
    if (auswertung =="Flush"):
        Flush+=1
    if (auswertung =="Straße"):
        Straße+=1
    if (auswertung =="Drilling"):
        Drilling+=1
    if (auswertung == "Doppel Paar"):
        DoppelPaar+=1
    if ( auswertung == "Paar"):
        Paar+=1
    if (auswertung == "High Card"):
        HighCard+=1
    if isReturn:
        return [[RoyalFlush,(RoyalFlush/wiederholung)*100],[StraßeFlush,(StraßeFlush/wiederholung)*100],[Vierling,(Vierling/wiederholung)*100],[Fullhouse,(Fullhouse/wiederholung)*100],[Flush,(Flush/wiederholung)*100],[Straße,(Straße/wiederholung)*100],[Drilling,(Drilling/wiederholung)*100],[DoppelPaar,(DoppelPaar/wiederholung)*100],[Paar,(Paar/wiederholung)*100],[HighCard,(HighCard/wiederholung)*100]]
    
    

def erzeugeRoyalFlush():
    a = [Card(1,14),Card(1,13),Card(1,12),Card(1,11),Card(1,10)]
    return a

def erzeugestraßeFlush():
    a = [Card(2,8),Card(2,6),Card(2,7),Card(2,4),Card(2,5)]
    return a

def erzeugeVierling():
    a = [Card(0,2),Card(1,2),Card(2,2),Card(3,2),Card(2,5)]
    return a

def erzeugeFullHouse():
    a = [Card(0,2),Card(1,2),Card(2,2),Card(0,3),Card(2,3)]
    return a

def erzeugeFlush():
    a = [Card(2,0),Card(2,1),Card(2,2),Card(2,4),Card(2,5)]
    return a

def erzeugeStraße():
    a = [Card(0,0),Card(1,1),Card(2,2),Card(3,3),Card(3,4)]
    return a

def erzeugeDrilling():
    a = [Card(0,0),Card(1,0),Card(2,0),Card(3,3),Card(3,4)]
    return a

def erzeugeDoppelPaar():
    a = [Card(0,0),Card(1,5),Card(2,2),Card(3,3),Card(3,4)]
    return a

def Logik(wiederholung,ziehungsZahl):
    for i in range(1,wiederholung+1):
        init()
        ziehen(ziehungsZahl)
        Statistik(auswerten(gezogen),wiederholung)
# Da das 'clearen' der Console paar ms braucht, ist das Programm stark verlangsamt (Zu faul Multithreading einzubauen). Schaut aber Cool aus finde ich.
        if i % 1000 == 0: 
            if platform.system() == "Windows":
                os.system('cls')    
            if platform.system() == "Linux":
                os.system('clear')    
            print(i)   
            
    # ausgabeStatistik(Statistik(wiederholung=wiederholung,isReturn=True))
    ausgabeStatistikSchön(Statistik(wiederholung=wiederholung,isReturn=True))
    
def ausgabeStatistik(array):
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("Statistik:")
    print("-------------")
    print("Royale Flush\tStraße Flush\tVierling\tFull House\tFlush\t\tStraße\t\tDrilling\tDoppel Paar\tPaar\tHigh Card")
    print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(array[0][0],array[1][0],array[2][0],array[3][0],array[4][0],array[5][0],array[6][0],array[7][0],array[8][0],array[9][0]))
    print("%.2f\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f" %(array[0][1],array[1][1],array[2][1],array[3][1],array[4][1],array[5][1],array[6][1],array[7][1],array[8][1],array[9][1]))
    print("------------------------------------------------------------------------------------------------------------------------------")
    pass

def ausgabeStatistikSchön(array):
    zwischenSpeicher1 = [array[0][0],array[1][0],array[2][0],array[3][0],array[4][0],array[5][0],array[6][0],array[7][0],array[8][0],array[9][0]]
    zwischenSpeicher2 = [array[0][1],array[1][1],array[2][1],array[3][1],array[4][1],array[5][1],array[6][1],array[7][1],array[8][1],array[9][1]]
    zwischenSpeicher = [zwischenSpeicher1,zwischenSpeicher2]
    # for i in array:
    #     zwischenSpeicher.append(format(i[1],'f'))
    # print(zwischenSpeicher)
    print(tabulate(zwischenSpeicher,headers=["Royale Flush","Straße Flush","Vierling","Full House","Flush","Straße","Drilling","Doppel Paar","Paar","High Card"],tablefmt="github",numalign="right"))

if __name__ == "__main__":
    Logik(1000000,7)
   
    # for e in gezogen:
    #     e.ausgeben()
    
    # print(auswerten(gezogen))
    
    # print(auswerten(erzeugeRoyalFlush()))
    # print(auswerten(erzeugestraßeFlush()))
    # print(auswerten(erzeugeVierling()))
    # print(auswerten(erzeugeFullHouse()))
    # print(auswerten(erzeugeFlush()))
    # print(auswerten(erzeugeStraße()))
    # print(auswerten(erzeugeDrilling()))
    # print(auswerten(erzeugeDoppelPaar()))
        
# nur höchstwertige zählenq
# prozentueller anteil bei 1000 ziehungen