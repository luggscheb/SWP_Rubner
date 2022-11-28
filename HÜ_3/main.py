import random
"""
0 - rock
1 - Spock
2 - paper
3 - lizard
4 - scissors
"""
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
     
    
 
    CompNummer=random.randrange(0, 5)
    hatGewonnen = ""

    Unterschied=(decision-CompNummer) % 5
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
 
    CompName=numbertoname(CompNummer)
 
    print ("Spieler wählt: ", numbertoname(decision))
    print ("Computer wählt: ", CompName)
    print (Gewinner, "\n")
    
    toSave = '{ "Spieler":' + str(decision) + ', "Computer":' + str(CompNummer) + ', "gewonnen":"' + hatGewonnen  + '"},'
    with open("data.json", "a") as file:
       file.writelines(toSave)
    
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
   for item in range(number):
       
      decision = int(input("Bitte geben Sie die Nummer ein: "))
      
      if (decision > 4 ) or (decision < 0):
         print ("Error: It has to be a number between 0 and 4")
         exit()
      
      name = numbertoname(decision)
      spiel(decision)
    
if __name__ == '__main__':
    main(5)
    