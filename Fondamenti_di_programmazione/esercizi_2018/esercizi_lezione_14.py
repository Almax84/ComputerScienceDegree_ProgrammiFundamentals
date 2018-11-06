# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:20:48 2018

@author: XIBM44
"""
'''
## ESERCIZI

Si vuole disegnare una città sullo schermo, rappresentata da una serie di rettangoli appoggiati in basso, larghi 100 pixel 
   e di altezza, posizione orizzontale e colore variabili. 
Ciascun elemento della lista è una tupla ( coordinata_x, colore, altezza ) che descrive un rettangolo.
Il colore di ciascun rettangolo è una tupla (R, G, B) che indica i valori delle tre componenti (rosso, verde, blu) del colore, ciascuna un intero tra 0 e 255 compresi che ne indica la luminosità (0=min, 255=max).
Esempio: (255, 0, 0) = rosso 
	 (0, 255, 0) = verde
	 (0, 0, 255) = blu
	 (0, 0, 0)   = nero
         (255, 255, 255) = bianco

1. Supponiamo che i rettangoli debbano essere disegnati in ordine dal più alto al più basso in modo che nessun rettangolo resti completamente coperto dagli altri, 
   e che in caso di parità si debba disegnare prima il rettangolo con posizione x minore.
   Si definisca la funzione ordina_palazzi(lista) che torna la lista di rettangoli ordinata come indicato senza modificare la lista originale.
   Esempio:
>>> lista = [(216, (54, 234, 22), 106),
		 (740, (94, 236, 163), 71),
		 (21, (49, 140, 100), 717),
		 (137, (204, 5, 140), 717),
		 (922, (15, 244, 140), 569),
		 (52, (2, 98, 163), 514),
		 (961, (138, 58, 166), 605),
		 (396, (116, 149, 25), 448),
		 (586, (129, 196, 183), 467),
		 (347, (218, 229, 143), 253)]
>>> ordina_palazzi(lista)
[(21, (49, 140, 100), 717),
 (137, (204, 5, 140), 717),
 (961, (138, 58, 166), 605),
 (922, (15, 244, 140), 569),
 (52, (2, 98, 163), 514),
 (586, (129, 196, 183), 467),
 (396, (116, 149, 25), 448),
 (347, (218, 229, 143), 253),
 (216, (54, 234, 22), 106),
 (740, (94, 236, 163), 71)]

########################################################################################################
'''
def ordina_palazzi_no_lambda(lista):
    ordinati = sorted(lista, key = sort_lista)
    return ordinati

def sort_lista(lista):
    
    return -lista[2], lista[1], lista[0]

def ordina_palazzi(lista):
    return sorted(lista, key = lambda ls : (-ls[2], ls[1], ls[0]))
    
lista = [(216, (54, 234, 22), 106),
		 (740, (94, 236, 163), 71),
		 (21, (49, 140, 100), 717),
		 (137, (204, 5, 140), 717),
		 (922, (15, 244, 140), 569),
		 (52, (2, 98, 163), 514),
		 (961, (138, 58, 166), 605),
		 (396, (116, 149, 25), 448),
		 (586, (129, 196, 183), 467),
		 (347, (218, 229, 143), 253)]
my_lista = ordina_palazzi(lista)

correct_lista = [(21, (49, 140, 100), 717),
 (137, (204, 5, 140), 717),
 (961, (138, 58, 166), 605),
 (922, (15, 244, 140), 569),
 (52, (2, 98, 163), 514),
 (586, (129, 196, 183), 467),
 (396, (116, 149, 25), 448),
 (347, (218, 229, 143), 253),
 (216, (54, 234, 22), 106),
 (740, (94, 236, 163), 71)]
#print(my_lista == correct_lista) 
    
'''
2. Si scriva la funzione palazzo_piu_costoso(lista) che torna la tupla che descrive il palazzo più costoso da costruire, 
   tenendo conto che il costo di costruzione:
   - è proporzionale all'altezza del palazzo
   - la costante di proporzionalità è la media dei tre valori che indicano il colore
   - a pari merito vogliamo quello più a destra
   Esempio:
       tupla ( coordinata_x, colore, altezza )
>>> palazzo_piu_costoso(lista)
(137, (204, 5, 140), 717)
'''
def palazzo_piu_costoso(lista):
    palazzo_costoso = max(lista, key= lambda x :  x[2]*(x[1][0] + x[1][1]+x[1][2])/3 )
    return palazzo_costoso

#print(palazzo_piu_costoso(lista))


'''

3. Si scriva la funzione palazzo_coperto(lista) che torna True se, 
    disegnando i palazzi nell'ordine dato nella lista (senza riordinarli),
   esiste almeno un palazzo che è coperto in tutta la sua altezza da un altro, ovvero se:
   - esiste un palazzo P1 tale che esiste un palazzo P2 più alto o uguale a P1, 
	che viene disegnato dopo P1 
	con le due posizioni orizzontali P1.x e P2.x che differiscono meno di 100 (in valore assoluto)
    tupla ( coordinata_x, colore, altezza )
   Esempio:
>>> palazzo_coperto(lista)
True
'''

def palazzo_coperto(lista):

    return_bool = []
    
    
    for p1 in lista:
        ls = list(filter(lambda p2 : p2!=p1 and p2[2] >= p1[2] and abs(p1[0]-p2[0])<100,lista))
        b = any(map(lambda x : len(x)>0, ls))
        return_bool.append(b)
    
    return any(return_bool)

    

print(palazzo_coperto(lista)) 