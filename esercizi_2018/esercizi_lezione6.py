# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 10:39:18 2018

@author: Davide.Scrimieri


## ESERCIZI
Scrivere le funzioni seguenti.

1. firstline(t, s) ritorna la prima linea della stringa t che contiene la stringa s , mentre se s non occorre in t ritorna None . 
	Esempio
>>> t = '''Quant’è bella giovinezza
che si fugge tuttavia!
Chi vuol esser lieto, sia:
del doman non c’è certezza.'''
	firstline(t, 'non')		ritorna		'del doman non c’è certezza.'

2. countw(t, w) ritorna il numero di occorrenze della parola w nella stringa t . 
	Esempio
	t = 'le cose non sono solo cose, ma anche cosette'
	countw(t, 'cose') 		ritorna		2

3. digits(t) ritorna la lista delle sequenze numeriche contenute nella stringa t . 
   Per sequenza numerica intendiamo una sequenza di cifre (caratteri 0 , 1 ,…, 9 ) di lunghezza massimale. 
	Esempio
	t = 'via Po n.23, tel. 06 7867555 - cell. 345 675665676 (cc 34565)'
	digits(t) 			ritorna 	['23', '06', '7867555', '345', '675665676', '34565']

4. column(table, k) ritorna una lista che contiene i valori della colonna k della tabella table . 
   La tabella è rappresentata in modo che ogni linea di table contiene una riga e i valori delle colonne sono separati
   dal carattere ';' . Se table ha n colonne, allora ogni linea di table conterrà esattamente n-1 caratteri ';' .
	Esempio
	table = '''Milano;12;23
Roma;16;25
Napoli;15;27
Firenze;11;20'''
	column(table, 1)		ritorna		['12', '16', '15', '11']
"""

def column(table,k):
    list_lines = table.splitlines()
    lista_colonne = []
    return_list = []
    for line in list_lines:
        lista_colonne.append(line.split(";"))
    
    for line_list in lista_colonne:
        return_list.append(line_list[k])
        
    return return_list
    


def digits(t):
    
    words_list = t.split(" ")
    return_list = []
    for line in words_list:
        numeric_line = ''
        for char in line:
            if char.isdigit():
                numeric_line+=char
        if numeric_line != '':
            return_list.append(numeric_line)
    return return_list            
    
    


def countw(t,w):
    
    #remove all non alpha (the comma ruins the following split)
    new_string = ''
    for char in t:
        if char.isalpha() or char == ' ' :
            new_string += char
            

    
    words_list = new_string.split(" ")
    print(words_list)
    return words_list.count(w)


def firstline(t,s):
    lines = t.splitlines()
    
    for line in lines:
        if s in line:
            return line
    return None


if __name__ == "__main__":
  #  t = '''Quant’è bella giovinezza
#che si fugge tuttavia!
#Chi vuol esser lieto, sia:
#del doman non c’è certezza.'''
  #  firstline(t, 'non')
  #  t = 'le cose non sono solo cose, ma anche cosette'
 #   print(countw(t, 'cose'))
#    t = 'via Po n.23, tel. 06 7867555 - cell. 345 675665676 (cc 34565)'
#    print(digits(t))
    table = '''Milano;12;23
Roma;16;25
Napoli;15;27
Firenze;11;20'''
    print(column(table, 1))


