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

"""
2. l2d(lst) che, presa in input una lista lst i cui elementi sono numeri da 0 a 9 espressi in lettere
   ( 'zero' , 'uno' , …, 'nove' ), ritorna una nuova lista i cui elementi sono la traduzione in numeri degli
   elementi di lst . Esempio
   l2d(['nove','due','due','tre'])	ritorna	[9,2,2,3]
"""
def l2d(lst):

    return_list = []
    
    for text in lst:
        if text == "zero":
            return_list.append(0)
        elif text == "uno":
            return_list.append(1)
        elif text == "due":
            return_list.append(2)
        elif text == "tre":
            return_list.append(3)
        elif text == "quattro":
            return_list.append(4)
        elif text == "cinque":
            return_list.append(5)
        elif text == "sei":
            return_list.append(6)
        elif text == "sette":
            return_list.append(7)
        elif text == "otto":
            return_list.append(8)
        elif text == "nove":
            return_list.append(9)
        else:
            return_list.append(-1)

    return return_list

"""
3. distinct(lst) ritorna una nuova lista che contiene gli stessi elementi di lst ma senza le eventuali
   ripetizioni.
   Esempi
   distinct([3,1,3,2,6,6])		ritorna	[3, 1, 2, 6]
   distinct(['a','ab','a','ab'])	ritorna	['a', 'ab']
"""
def distinct(lst):
    return_list = []
    for index,value in enumerate(lst):
        if value not in return_list:
            return_list.append(value)
    return return_list


def distinct2(lst):
    return set(lst)

"""
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
def search(lst,andc,orc,notc):
    
    return_lst = []
    for index, s in  enumerate(lst):
        viable_and_string = True
        viable_or_string = False
        viable_not_string = True
        for andc_s in andc:
            if andc_s not in s:
                viable_and_string = False
                break
        if len(orc) == 0:
            viable_or_string = True
        for orc_s in orc:
            if orc_s in s:
                viable_or_string = True
        for notc_s in notc:
            if notc_s in s:
                viable_not_string = False
                
        if viable_and_string and viable_not_string and viable_or_string:
            return_lst.append(s)
            
    return return_lst
            
                
            
    



if __name__ == "__main__":
    """
    print(prec(13, 11, 2012,  2,  3, 2013))
    print(prec(13, 11, 2012, 27, 12, 2011))
    print(prec( 1, 10, 2013,  1, 11, 2013))
    print(prec( 1, 11, 2013,  1, 11, 2013))
    print(l2d(['nove','due','due','tre']))
    print("distinct",distinct([3,1,3,2,6,6]))
    print("distinct",distinct(['a','ab','a','ab']))
    print("set",distinct2([3,1,3,2,6,6]))
    print("set",distinct2(['a','ab','a','ab']))
"""
    lst = ['mela','pera','melo']
    print(search(lst,['el','a'],['ra','pe','m'],['tt','lo'])) #ritorna ['mela']
    print(search(lst,[],['ra','pe','m'],['tt','lo'])) #ritorna ['mela','pera']
    print(search(lst,['el','a'],[],['tt''lo'])) #ritorna ['mela']
    print(search(lst,[],['ra','pe','m'],[])) #ritorna ['mela','pera','melo']
    
