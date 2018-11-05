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
def ordina_palazzi(lista):
    pass
    
    
    
    
    