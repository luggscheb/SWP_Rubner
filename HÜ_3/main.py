import random

from flask import Flask
from sqlalchemy import Column, Integer, Text
from sqlalchemy import create_engine,  or_
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func

from simple_term_menu import TerminalMenu

Base = declarative_base()  # Basisklasse aller in SQLAlchemy verwendeten Klassen
metadata = Base.metadata

engine = create_engine('sqlite:///C:/Schual/Rubner/HÜ_3/db.sqlite3')
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
Base.query = db_session.query_property() #Dadurch hat jedes Base - Objekt (also auch ein Millionaire) ein Attribut query für Abfragen
app = Flask(__name__)
"""
0 - rock
1 - Spock
2 - paper
3 - lizard
4 - scissors
"""

class Data(Base):
    __tablename__ = 'data'  # Abbildung auf diese Tabelle

    id = Column(Integer, primary_key=True)
    player = Column(Integer)
    computer = Column(Integer)
    won = Column(Text)

    def serialize(self):
        return {'id' : self.id,
                'player':  self.player,
                'computer' : self.computer,
                'won' : self.won}

def numbertoname(number):
 
    if number==0: return "Stein"
    elif number==1: return "Spock"
    elif number==2: return "Papier"
    elif number==3: return "Echse"
    elif number==4: return "Schere"
    
 
def nametonumber(name):
 
    if name=="Stein": return 0
    elif name=="Spock": return 1
    elif name=="Papier": return 2
    elif name=="Echse": return 3
    elif name=="Schere": return 4
    
 
def spiel(decision):
     
    
 
    compNummer=random.randrange(0, 5)
    hatGewonnen = ""

    Unterschied=(decision-compNummer) % 5
    if Unterschied == 0:
        Gewinner = "Unentschieden!"
        hatGewonnen = "U"
    elif Unterschied == 1:
        Gewinner = "Spieler gewinnt!"
        hatGewonnen = "S"
    elif Unterschied == 2:
        Gewinner = "Spieler gewinnt!"
        hatGewonnen = "S"
    elif Unterschied == 3:
        Gewinner = "Computer gewinnt!"
        hatGewonnen = "C"
    elif Unterschied == 4:
        Gewinner = "Computer gewinnt!"
        hatGewonnen = "C"
 
    CompName=numbertoname(compNummer)
 
    print ("Spieler wählt: ", numbertoname(decision))
    print ("Computer wählt: ", CompName)
    print (Gewinner, "\n")
    
    toSave = '{ "Spieler":' + str(decision) + ', "Computer":' + str(compNummer) + ', "gewonnen":"' + hatGewonnen  + '"},'
    #File safe
    with open("data.json", "a") as file:
       file.writelines(toSave)
    #DB safe
    info = Data(player = decision, computer = compNummer, won = hatGewonnen)
    db_session.add(info)
    db_session.flush()

    
"""
{
   'Spieler': (gezogen),
   'Computer': (gezogen),
   'gewonnen': (S/C/U),
   
}   
"""
 

print ("0 - Stein")
print ("1 - Spock")
print ("2 - Papier")
print ("3 - Lizard")
print ("4 - Schere\n")
  
def main(number):
    Base.metadata.create_all(bind=engine)
    
    
    options = ["entry 1", "entry 2", "entry 3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    
    
    
    for item in range(number):  
        
      decision = int(input("Bitte geben Sie die Nummer ein: "))
      
      if (decision > 4 ) or (decision < 0):
         print ("Error: It has to be a number between 0 and 4")
         exit()
      
      name = numbertoname(decision)
      spiel(decision)
    
if __name__ == '__main__':
    main(5)
    