# pylint: disable=all
import random

import requests
from simple_term_menu import TerminalMenu

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
    
 
def spiel(decision,saveToDB,isHardMode):
     
    compNummer=0
    if(isHardMode == 0):
        compNummer=random.randrange(0, 5)
    elif(isHardMode == 1):
        #get meisten gezogen
        response = requests.get('http://127.0.0.1:5000/dbmode')
        rj = response.json()
        
        #ziehen was dagegen gewinnt
        for i in range(5):
            if (rj['index']-i) % 5 == 3 or (rj['index']-i) % 5 == 4:
                compNummer = i
                break
    elif(isHardMode ==2):
        for i in range(5):
            if (decision-i) % 5 == 3 or (decision-i) % 5 == 4:
                compNummer = i
                break
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
    
    # toSave = '{ "Spieler":' + str(decision) + ', "Computer":' + str(compNummer) + ', "gewonnen":"' + hatGewonnen  + '"},'
    #File safe
    # with open("data.json", "a") as file:
    #    file.writelines(toSave)
    if saveToDB:
        upData(decision,compNummer,hatGewonnen)

    
"""
{
   'Spieler': (gezogen),
   'Computer': (gezogen),
   'gewonnen': (S/C/U),
   
}   
"""
 


  
def main(number):
    
    
    
    
    options = ["Spielen", "Statistik", "Daten Uploaden"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"{options[menu_entry_index]}!")
    saveToDB = False
    
    if(menu_entry_index == 0):
        options = ["Leicht", "Schwer","Unmöglich"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print("Wie oft spielen?")
        play(int(input()),saveToDB,menu_entry_index)
    elif(menu_entry_index == 1):
        statistik()
    elif(menu_entry_index == 2):
        saveToDB = True
        print("Spiele werden nun hochgeladen!")
        main(number)
    
def statistik():
    response = requests.get('http://127.0.0.1:5000/db')
    json_res = response.json()
    print("Insgesamt Gespielt: "+str(json_res['insg']))
    print("Mensch Gewonnen: "+str(json_res['mensch']))
    print("Computer Gewonnen: "+str(json_res['comp']))
    print("Mensch %: "+str(json_res['proz']))
#get data from server
# print with tabulate


def upData(Spieler:int,Computer:int,Gewonnen:str):
    j = {'player': Spieler, 'computer': Computer, 'won': Gewonnen}
    response = requests.put('http://127.0.0.1:5000/db' , json=j)
    
    res_json = response.json()
    
    
def play(number,saveToDB, isHardMode) :
    options = ["Stein", "Spock", "Papier","Lizard","Schere"]
    
    for item in range(number):  
        
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"{options[menu_entry_index]}!")
        decision = menu_entry_index

        name = numbertoname(decision)
        spiel(decision,saveToDB,isHardMode) 

if __name__ == '__main__':
    main(5)
    