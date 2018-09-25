# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:10:46 2018

@author: david

## ESERCIZI

Scrivere le funzioni seguenti.
1. prec(g1, m1, a1, g2, m2, a2) ritorna True se la data g1, m1, a1 (giorno, mese, anno) è precedente
   o uguale alla data g2, m2, a2 .
   Esempi
   prec(13, 11, 2012,  2,  3, 2013)	ritorna	True
   prec(13, 11, 2012, 27, 12, 2011)	ritorna	False
   prec( 1, 10, 2013,  1, 11, 2013)	ritorna	True

2. l2d(lst) che, presa in input una lista lst i cui elementi sono numeri da 0 a 9 espressi in lettere
   ( 'zero' , 'uno' , …, 'nove' ), ritorna una nuova lista i cui elementi sono la traduzione in numeri degli
   elementi di lst . Esempio
   l2d(['nove','due','due','tre'])	ritorna	[9,2,2,3]

3. distinct(lst) ritorna una nuova lista che contiene gli stessi elementi di lst ma senza le eventuali
   ripetizioni.
   Esempi
   distinct([3,1,3,2,6,6])		ritorna	[3, 1, 2, 6]
   distinct(['a','ab','a','ab'])	ritorna	['a', 'ab']

4. search(lst, andc, orc, notc) ritorna una nuova lista di stringhe che contiene le stringhe s della lista
   lst tali che tutte le stringhe della lista andc sono sottostringhe di s, almeno una delle stringhe della
   lista orc (se orc non è vuota) è una sottostringa di s e nessuna delle stringhe della lista notc è una
   sottostringa di s. 
   Esempi, sia lst = ['mela','pera','melo']
   search(lst,['el','a'],['ra','pe','m'],['tt','lo'])	ritorna ['mela']
   search(lst,[],['ra','pe','m'],['tt','lo'])		ritorna ['mela','pera']
   search(lst,['el','a'],[],['tt''lo'])			ritorna ['mela']
   search(lst,[],['ra','pe','m'],[])			ritorna ['mela','pera','melo']


"""

def prec(g1,m1,a1,g2,m2,a2):
    giorno1 = int(g1)
    giorno2 = int(g2)
    mese1 = int(m1)
    mese2 = int(m2)
    anno1 = int(a1)
    anno2 = int(a2)
    
    
    if int(a2)==int(a1) and int(m2)==int(m1) and int(g2)==int(g1):
        return True
    
    if anno2 > anno1:
        return True
    elif anno2 == anno1 and mese2>mese1:
        return True
    elif anno2 == anno1 and mese2 == mese1 and giorno1>giorno2:
        return True
    else:
        return False
    
    


if __name__ == "__main__":
    print(prec(13, 11, 2012,  2,  3, 2013))
    print(prec(13, 11, 2012, 27, 12, 2011))
    print(prec( 1, 10, 2013,  1, 11, 2013))
    print(prec( 1, 11, 2013,  1, 11, 2013))