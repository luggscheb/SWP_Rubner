# Aufwandsklassen:

Speicherkompläxität:

- wie viel speicher braucht es

Zeikomplexität:

- wie lange braucht es




# Sortieralgorythmen:

[Happycoders](https://www.happycoders.eu)
erkenne an Code was für ein algorythmus / Aufwandsklasse ist

- O(n²) [weil 2 Schleifen]
  - bubblesort sort
  - insertiant sort (einzelne links-rechts-verschiebung ob kleiner oder größer )
  - selection sort ( alles anschauen, kleinstes ganz vor, dann alles anschauen -1)


- O(n*log(n)) [tendenziell zu bevorzugen]
log(n) weil immer halbiert wird bis man bei einem Element ist -> Dauert log(n) schritte
  - quick sort (Biwo (Standart letzte, aber kann irgend eins sein). Zwei Zeiger rechts[kleiner] und links[größer])
  - merge sort (Sortierung passiert beim zusammenfügen)
  - heap sort (Größe zahl steht an der Qurzel, weiter unten kleinere Zahlen -> Baumstruktur.  Rebalangieren -> log(n). Sortiert mithilfe einer Baumstrukur, ein rebalangier durchgang dauert log(n) Schritte)

O(1) = Konstant


## beurteilung:
- Aufwandsklasse
- Inplace / Outofplace



# Inplace:
Inplace wenn der Zusatzspeicher nicht von `n` abhängig ist und konstant ist.

# stabilität:
gleichwärtige Daten bleiben in deren Reihenfolge wie sie in der Original Datenstruktur erscheinen:

[7_1 , 5 , 4 , 7_2 , 6 , 0 , 7_3]
sort
[0 , 4 , 5 , 6 , 7_1 , 7_2 , 7_3] stabil



### Java hat unter 43 Länge bei Datenstruktur insertiont sort ... darüber quick sort





