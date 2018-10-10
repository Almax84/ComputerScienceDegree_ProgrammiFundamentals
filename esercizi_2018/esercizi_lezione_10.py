# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 22:13:48 2018

@author: david


Scrivere le funzioni seguenti.
1. wset(fname) ritorna un insieme contenente le parole (distinte) del file fname . Le parole sono ridotte
   alle minuscole e il file è decodificato con UTF-8-SIG. 
   Esempio
wset('alice.txt') ritorna un insieme di cardinalità 3007
"""


def words(string):
    #substitute noalpha with space char
    for char in string:
        if not char.isalpha() and char != ' ':
          string =  string.replace(char, ' ')

    return string.split()

def wset(fname):
    
    with open(fname, encoding = 'UTF-8-SIG') as f:
        file_text = set(words(f.read().lower()))
        
    return len(file_text)

#print(wset("files/alice.txt"))
        


"""

2. wsub(fn1, fn2) ritorna un insieme contenente le parole (distinte) che appaiono nel file fn1 e che non
   appaiono nel file fn2 . Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG. 
   Esempio
>>> wsub('alice.txt', 'holmes.txt') ritorna un insieme di cardinalità 710
"""

def wsub(fn1,fn2):

    with open(fn1, 'r', encoding="UTF-8-SIG") as f:
        fn1_text = set(words(f.read().lower()))
    with open(fn2, 'r', encoding="UTF-8-SIG") as f:
        fn2_text = set(words(f.read().lower()))

    result = fn1_text - fn2_text
    print(len(result))


#wsub("files/alice.txt","files/holmes.txt")




""""
3. wdict(fname) ritorna un dizionario che ad ogni parola del file fname associa il numero di occorrenze
   della parola nel file. Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG. 
   Esempio
>>> d = wdict('alice.txt')
>>> d['alice'] --> 403
>>> d['rabbit'] --> 51
>>> d['queen'] --> 75
"""

def wdict(fname):
    result_map = {}
    with open(fname, 'r', encoding="UTF-8-SIG") as f:
        words_in_file = words(f.read().lower())
    for word in words_in_file:
        if word not in result_map:
            result_map[word] = words_in_file.count(word)
    return result_map

#d=wdict("files/alice.txt")
#print('ALICE:',d['alice'])
#print('RABBIT:',d['rabbit'])
#print('queen:',d['queen'])
"""
4. nextw(fname) ritorna un dizionario che ad ogni parola del file fname associa l'insieme delle parole che
   seguono la parola nel file. Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG.
   Esempio
>>> d = nextw('alice.txt')
>>> d['go']
{'and', 'among', 'splashing', 'back', 'down', 'through', 'at', 'in', 'nearer', 'said', 'from', 'for', 
'no', 'there', 'to', 'his', 'after', 'let', 'with', 'by', 'on', 'alice', 'near', 'anywhere', 'round'}
>>> d['write']
{'that', 'this', 'it', 'one', 'with', 'out'}
"""
def nextw(fname):
    with open(fname,'r',encoding='UTF-8-SIG') as f:
      parole = words(f.read())
    parole = [ p.lower() for p in parole ]
    risultato = {}
    for i in range(len(parole)-1):
        p1, p2 = parole[i:i+2]
        if p1 in risultato:
            risultato[p1].add(p2)
        else:
            risultato[p1] = { p2 }
    return risultato

#d = nextw("files/alice.txt")
#print(d["go"])
"""
5. mostf(fname, l) ritorna un insieme contenente le parole di lunghezza l di massima frequenza nel file
   fname . Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG. 
   Esempi
>>> mostf('holmes.txt', 7)
{'nothing', 'however'}
mostf('holmes.txt', 8)
{'sherlock'}
mostf('frankenstein.txt', 16) 
{'unenforceability', 'impracticability', 'perpendicularity', 'indiscriminately', 'inextinguishable'}

"""
def mostf(fname,l):
    with open(fname,'r',encoding='UTF-8-SIG') as f:
        list_of_words = words(f.read().lower())
    
    
    set_of_words_of_length_l={word for word in list_of_words if len(word) == l}
   
    
    highest_frequency = 0
    words_frequency = dict()
    
    for word in set_of_words_of_length_l:
        count = 0
        max_occurrence = 0
        for index,w in enumerate(list_of_words):
            if w == word:
                count+=1
                if max_occurrence < count:
                    max_occurrence = count
                    if max_occurrence > highest_frequency:
                        highest_frequency = max_occurrence
        words_frequency[word] = max_occurrence 
   
    return_list = list()
    
    for k,v in words_frequency.items():
        if v == highest_frequency:
            return_list.append(k)
        
        
    return return_list,highest_frequency
        
        
        
            

print(mostf("files/frankenstein.txt",16))