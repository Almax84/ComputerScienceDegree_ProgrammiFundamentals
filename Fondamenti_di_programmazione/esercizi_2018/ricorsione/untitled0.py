# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:36:15 2019

@author: david
"""


###################################################################################
'''
Es 1: Definite la funzione ricorsiva rovescia(lista) che rovescia una lista costruendo mano a mano il risultato all'uscita dalla ricorsione.
Per estrarre elementi dalla lista usate solo il metodo lista.pop(0) che torna il primo elemento della lista togliendolo dalla lista.
Nota: la lista originale viene modificata.
'''
###################################################################################

def rovescia(lista):
    
    if len(lista)==1:
        return lista
    
    el = lista.pop(0)
    rovescia(lista)
    lista.append(el)
    
lista = [1,2,3,4,5]
rovescia(lista)
#print(lista)        


'''


###################################################################################

Es 2: Definite la funzione rovescia2(lista) che torna una copia rovesciata di una lista sfruttando una funzione
ricorsiva ausiliaria a cui passa una lista di appoggio iniziale vuota alla quale aggiungere gli elementi.
La funzione ausiliaria ricorsiva sfrutta il passaggio di argomenti in avanti e modifica mano a mano la lista di 
appoggio in cui aggiunge mano a mano i valori, uno per chiamata.
Per estrarre elementi dalla lista usate solo il metodo lista.pop(0)
 che torna il primo elemento della lista togliendolo dalla lista.
Nota: la lista originale viene modificata.

###################################################################################


'''
def rovescia2(lista):
    lista_appoggio = list()
    
    for el in lista:
        _rovescia2(lista_appoggio, el)
    
    return lista_appoggio
    
    
    

def _rovescia2(lista_appoggio, arg):
    
    if len(lista_appoggio) == 0:
        lista_appoggio.append(arg)
        return lista_appoggio
    
    if len(lista_appoggio) == 1:
        el = lista_appoggio.pop(0)
        lista_appoggio.append(arg)
        lista_appoggio.append(el)
        return lista_appoggio
    
    
    el = lista_appoggio.pop(0)
    _rovescia2(lista_appoggio, el)
    lista_appoggio.insert(0,arg)
    
    return lista_appoggio

#print(rovescia2([1,2,3,4,5,7,8,9,10,11,12]))


'''
###################################################################################

Es 3: A partire dalla definizione iterativa di massimo comun divisore (GCD) di due numeri positivi x ed y, ovvero:

# per calcolare il GCD di x ed y interi positivi
    # ripeti se x != y
        # x = x-y		se x>y
        # y = y-x		se x<y
    # torna x

a) definite sua implementazione iterativa.
b) definite la implementazione ricorsiva che simula il ciclo passando i valori x ed y in avanti

'''
def gcd(x,y):
    
    while x != y:
        if x > y:
            
            x = x-y
        if x < y:
            y = y-x
    return x


    
def gcd_iter(x,y):
    if x == y:
        return x
    
    if x > y:
       x =  gcd_iter(x-y,y)
    if x < y:
       x =  gcd_iter(x, y-x)
        
    return x

print("gcd: ",gcd_iter(100,20))  

'''
Es 4: Ripetete l'esercizio al contrario, partendo da questa diversa definizione ricorsiva di massimo comun divisore 
(GCD) di due numeri positivi x ed y, ovvero
	GCD2(x, y) = x			se x==y
	GCD2(x, y) = GCD2(x%y,y)	se x>y
	GCD2(x, y) = GCD2(x,y%x)	se x<y

a) definite la funzione ricorsiva corrispondente
b) definite la funzione iterativa corrispondente partendo da quella ricorsiva

'''


def gcd2(x,y):
    
    if x == y:
        return x
    
    if x == 0:
        return y
    
    if y == 0:
        return x
    
    if x > y:
       x = gcd2(x%y,y)
    if x < y:
       x =  gcd2(x,y%x)
     
    return x


def gcd2_iter(x,y):
    
    while x != y:
        if x > y:
            x = x%y
        if x == 0:
            return y
        if y == 0:
            return x
        if x < y:
            y = y%x
        if x == 0:
            return y
        if y == 0:
            return x


print("gcd2:", gcd2_iter(10,12))
    
    