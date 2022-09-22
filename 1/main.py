import random


#für besseres debugging ausgeschrieben
mögliche_ziehungen = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
bereich_zum_ziehen = 45
index_wo_hin_verschoben_werden_muss = 45
wie_oft_noch_ziehen = 6
gezogene_zufalls_zahl = 0
a = 0
speicher = {}

def Gezogene_zahl_verschieben(zahl):
    global bereich_zum_ziehen, index_wo_hin_verschoben_werden_muss,a 
    a = zahl
    if a <= bereich_zum_ziehen:
        mögliche_ziehungen[a], mögliche_ziehungen[index_wo_hin_verschoben_werden_muss] = mögliche_ziehungen[index_wo_hin_verschoben_werden_muss], mögliche_ziehungen[zahl]
        index_wo_hin_verschoben_werden_muss -= 1
        bereich_zum_ziehen -= 1
        return 1
    else:
        return 0
        
def Zufallszahl_ziehen():
    global wie_oft_noch_ziehen, gezogene_zufalls_zahl
    if wie_oft_noch_ziehen == 0:
        return "finished"
    gezogene_zufalls_zahl = random.randint(0,bereich_zum_ziehen)
    if Gezogene_zahl_verschieben(gezogene_zufalls_zahl):
        wie_oft_noch_ziehen -= 1
        return Zufallszahl_ziehen()
    else:
        return "Ein unerwarteter Fehler ist aufgetreten!"
    
def Print_alle_gezogenen_zahlen():
    s = ""
    for i in range(40,46):
        s += str(mögliche_ziehungen[i])
        s += " "
    return s
       
def zuruecksetzen():
    global mögliche_ziehungen, mögliche_ziehungen_original, bereich_zum_ziehen, index_wo_hin_verschoben_werden_muss, wie_oft_noch_ziehen
    mögliche_ziehungen = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
    bereich_zum_ziehen = 45
    index_wo_hin_verschoben_werden_muss = 45
    wie_oft_noch_ziehen = 6
    
def Schon_in_speicher_vorhanden(zahl):
    global speicher
    if zahl in speicher:
        return 1
    return 0
def Abspeichern_der_ziehungen():
    
    for i in range(40,46):
        if Schon_in_speicher_vorhanden(mögliche_ziehungen[i]):
            speicher[mögliche_ziehungen[i]] += 1
        else:
            speicher[mögliche_ziehungen[i]] = 1
    
if __name__ == '__main__':
    for i in range(1000):
        
        print(Zufallszahl_ziehen())
        print(Print_alle_gezogenen_zahlen())
        Abspeichern_der_ziehungen()
        zuruecksetzen()
    print(speicher)