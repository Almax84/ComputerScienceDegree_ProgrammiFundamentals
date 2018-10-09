# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 22:13:48 2018

@author: david


Scrivere le funzioni seguenti.
1. wset(fname) ritorna un insieme contenente le parole (distinte) del file fname . Le parole sono ridotte
   alle minuscole e il file è decodificato con UTF-8-SIG. 
   Esempio
>>> wset('alice.txt') ritorna un insieme di cardinalità 3007
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

print(wset("files/alice.txt"))
        


"""

2. wsub(fn1, fn2) ritorna un insieme contenente le parole (distinte) che appaiono nel file fn1 e che non
   appaiono nel file fn2 . Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG. 
   Esempio
>>> wsub('alice.txt', 'holmes.txt') ritorna un insieme di cardinalità 710

3. wdict(fname) ritorna un dizionario che ad ogni parola del file fname associa il numero di occorrenze
   della parola nel file. Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG. 
   Esempio
>>> d = wdict('alice.txt')
>>> d['alice'] --> 403
>>> d['rabbit'] --> 51
>>> d['queen'] --> 75

4. nextw(fname) ritorna un dizionario che ad ogni parola del file fname associa l'insieme delle parole che
   seguono la parola nel file. Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG.
   Esempio
>>> d = nextw('alice.txt')
>>> d['go']
{'and', 'among', 'splashing', 'back', 'down', 'through', 'at', 'in', 'nearer', 'said', 'from', 'for', 
'no', 'there', 'to', 'his', 'after', 'let', 'with', 'by', 'on', 'alice', 'near', 'anywhere', 'round'}
>>> d['write']
{'that', 'this', 'it', 'one', 'with', 'out'}

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

