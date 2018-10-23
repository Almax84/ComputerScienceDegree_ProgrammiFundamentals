# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:35:14 2018

@author: Davide.Scrimieri


## ESERCIZI

Scrivere le funzioni seguenti.
"""
"""
1. occ(lst, v) ritorna una lista contenente gli indici delle occorrenze di v nella lista lst . 
   Esempi, sia	lst = ['red','blue','red','gray','yellow','red']
	occ(lst, 'red')		ritorna [0,2,5]
	occ(lst, 'green')	ritorna []
"""
def occ(lst,v):
    return_list = []
    for index,value in enumerate(lst):
        if v == value:
            return_list.append(index)
    return return_list
      
"""
2. rep(lst, k) ritorna una lista, senza ripetizioni, che contiene i valori che nella lista lst occorrono
   almeno k volte. 
   Esempi, sia lst = [1,2,1,5,3,4,2,1,3,5,6]

	rep(lst, 2)	ritorna [1,2,5,3]
	rep(lst, 3)	ritorna [1]
	rep(lst, 4)	ritorna []
"""  
def rep(lst, k):

    return_list = []
    for index,value in enumerate(lst):
        
        value_counter = 0
        for val in lst:
            if val == value:
                value_counter+=1
        if value_counter>= k and value not in return_list:
            return_list.append(value)
    return return_list

"""
3. lastfirst(lst) presa in input una lista lst di parole, ritorna la prima parola che inizia con un
   carattere diverso dall'ultimo carattere della parola precedente, se non c'è ritorna None . 
   Esempi
	lastfirst(['sole','elmo','orco','alba','asta'])		ritorna 'alba'
	lastfirst(['sky','you','use','ear','right'])		ritorna None
"""        
def lastfirst(lst):
    for index,value in enumerate(lst):
        first_char = value[0]
        last_char = ''
        if index + 1 < len(lst)-1:
            next_word = lst[index+1]
            last_char = next_word[len(next_word)-1]
'''
4. groupd(lst) presa in input una lista lst di interi tale che i primi tre rappresentano una data, 
   i secondi tre un'altra data, i successivi tre un'altra data e così via, 
   modifica la lista lst raggruppando ogni tripla in una stringa separando i numeri con il carattere '/' . 
   Si assume che la lista lst abbia una lunghezza multipla di 3. 
   Esempio
>>> lst = [1, 2, 2013, 23, 9, 2011, 10, 11, 2000]
>>> groupd(lst)
>>> lst=[1,2,2013,23,9,2011] ritorna ['1/2/2013','23/9/2011']
'''     

def groupd(lst):
    if len(lst)%3!=0:
        return None
    return_list=[]
    i = 0
    while i < len(lst):
        sub_list=lst[i:i+3]
        date_string = ''
        for index,s in enumerate(sub_list):
            if index != len(sub_list)-1:
                date_string+=str(s)+"/"
            else:
                date_string+=str(s)
        return_list.append(date_string)
        i+=3
    return return_list
    
    

if __name__ == "__main__":
    ''' 
    lst = [1,2,1,5,3,4,2,1,3,5,6]
    print(rep(lst, 2)) #ritorna [1,2,5,3]
    print(rep(lst, 3)) #ritorna [1]
    print(rep(lst, 4)) #ritorna []

    lst = ['red','blue','red','gray','yellow','red']
    print(occ(lst, 'red')) #ritorna [0,2,5]
    print(occ(lst, 'green')) #ritorna []
    lst = [1,2,1,5,3,4,2,1,3,5,6]

    print(lastfirst(['sole','elmo','orco','alba','asta']))   #ritorna 'alba'
    print(lastfirst(['sky','you','use','ear','right']))      #ritorna None
    '''
    lst=[1,2,2013,23,9,2011,4,3,1984] #ritorna ['1/2/2013','23/9/2011']
    print(groupd(lst))