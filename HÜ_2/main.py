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
        ausgabe += str(self.nummer).center(3, ' ')
        ausgabe += "]\n" 
        print(ausgabe)
            
    
    
def init():
    del gezogen[::]
    for i in range(4):
        for j in range(1,14):
            möglich.append(Card(i,j))
        
def Ziehen(anzahl):
    for i in range(anzahl+1):
            r = random.randint(0,len(möglich)-1)
            # print(r,len(möglich))
            gezogen.append(möglich[r])
            del möglich[r]
        

if __name__ == "__main__":
    init()
    Ziehen(5)
    for e in gezogen:
        e.ausgeben()
        
        
