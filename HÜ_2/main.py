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
import re
from tkinter import PIESLICE
from unittest import removeResult 
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
    for i in range(4):
        for j in range(2,15):
            möglich.append(Card(i,j))
        
def ziehen(anzahl):
    for i in range(anzahl+1):
            r = random.randint(0,len(möglich)-1)
            # print(r,len(möglich))
            gezogen.append(möglich[r])
            del möglich[r]
        
def royalFlush(array):
    for i in array:
        if i.farbe != 1:
            return False
        if i.nummer == 14 or i.nummer == 13 or i.nummer == 12 or i.nummer == 11 or i.nummer == 10:
            pass
        else:
            return False
    return True
            

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
            for i in array:
                durchlaufZähler2 = 0
                for j in array:
                    if j.nummer == i.nummer: 
                        durchlaufZähler2+=1
            if durchlaufZähler == 2:
                return True
    return False        
    
    
    pass

def flush(array):
    pass

def straße(array):
    pass

def drilling(array):
    pass

def doppelpaar(array):
    pass

def auswerten(array):
    print("Sie haben gezogen:")
    if(royalFlush(array)):
        return "Royal Flush"
    if(straßeFlush(array)):
        return "Straße Flush"
    if(vierling(array)):
        return "vierling"
    if(fullHouse(array)):
        return "fullhouse"
    if(flush(array)):
        return "flush"
    if(straße(array)):
        return "straße"
    if(drilling(array)):
        return "drilling"
    if(doppelpaar(array)):
        return "doppelpaar"
    else:
        return "Nichts"

def erzeugeRoyalFlush():
    a = [Card(1,14),Card(1,13),Card(1,12),Card(1,11),Card(1,10)]
    return a

def erzeugestraßeFlush():
    a = [Card(2,8),Card(2,6),Card(2,7),Card(2,4),Card(2,5)]
    return a

def erzeugestraßeVierling():
    a = [Card(0,2),Card(1,2),Card(2,2),Card(3,2),Card(2,5)]
    return a

def erzeugestraßeFullHouse():
    a = [Card(0,2),Card(1,2),Card(2,2),Card(0,3),Card(2,3)]
    return a

if __name__ == "__main__":
    init()
    ziehen(5)
    for e in gezogen:
        e.ausgeben()
        
    
    # print(auswerten(erzeugeRoyalFlush()))
    # print(auswerten(erzeugestraßeFlush()))
    # print(auswerten(erzeugestraßeVierling()))
    print(auswerten(erzeugestraßeFullHouse()))
        
# nur höchstwertige zählenq
# prozentueller anteil bei 1000 ziehungen