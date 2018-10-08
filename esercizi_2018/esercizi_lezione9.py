'''

1. clines(fname, s) ritorna il numero di linee del file 
di testo fname che contengono la stringa s senza
   differenziare tra maiuscole e minuscole. 
   
 Esempi: se il file testo.txt contiene le 4 righe

SUGLI ERRORI
Gli errori sono inevitabili. Errare è umano,
perseverare è diabolico. Non ci sono rimedi
a questo stato di cose (su questa terra).

allora
	clines('testo.txt', 'err')	ritorna 3
	clines('testo.txt', 'Errori')	ritorna 2
'''

def clines(fname,s):
    contatore = 0
    with open(fname) as f:
        
        lines = f.readlines()
        
        for line in lines:
            if s.lower() in line.lower():
                contatore+=1
                
    return contatore
        
        



'''
2. all_char(fname, enc) ritorna una stringa unicode contenente tutti i caratteri, 
    senza ripetizioni e in
   ordine di apparizione, nel file fname decodificato con la codifica enc . Ad esempio se il file è quello
   dell'esercizio precedente, assumendo che sia codificato in UTF-8, si ha:

>>> allc = all_char('testo.txt', 'utf8')
>>> allc
'SUGLI ERO\nlierosnvtab.èum,pdcNq()'
>>> print(allc)
SUGLI ERO
lierosnvtab.èum,pdcNq()

'''


def all_char(fname,enc):
    return_string = ""
    with open(fname, encoding=enc) as f:
        testo = f.read()
        for char in testo:
            if char not in return_string:
                return_string+=char
    return return_string





'''


3. anagrams(fname, w) ritorna una lista contenente tutti gli anagrammi, senza ripetizioni e senza
   differenziare tra maiuscole e minuscole, della parola w nel file fname . Un anagramma di una parola w è
   un'altra parola che usa esattamente le stesse lettere di w ma in ordine diverso, ad esempio mangiare e
   germania, torre e retro. La lista ritornata deve includere anche la parola w stessa, se è presente.
   Possono risultare utili la funzione built-in sorted() e il metodo join() delle stringhe.
   Nel risultato non ci devono essere doppioni.
   Esempi, sia fname il file 'alice.txt' :

>>> anagrams(fname, 'read')	ritorna ['dear', 'read', 'dare']
>>> anagrams(fname, 'elbow')	ritorna ['elbow', 'below']
'''

def anagrams(fname,w):
    anagram_list = []
    with open(fname, encoding="utf8") as f:
        
        for line in f:
            words_in_line = get_words_in_line(line)
            for word in words_in_line:
                if isAnagram(word,w) and word not in anagram_list:
                    anagram_list.append(word)
                   
                    
    return anagram_list
            
def isAnagram(word,w):
    word = list(word)
    w = list(w)
    word.sort()
    w.sort()
    return ''.join(word) == ''.join(w)
            
            
            
def get_words_in_line(line):
    words = []
    word = ""
    for index,char in enumerate(line):
        if char.isalpha():
            word+=char
        elif len(word)>0:
            words.append(word)
            word = ""
    if len(word)>0:
        words.append(word)
    
    return words
            
    
        
#get_words_in_line(" a red-hot")        

'''
4. log_update(filelog, evento) aggiorna il file filelog aggiungendo una nuova linea che inizia con la data e l'orario
   della chiamata e dopo ': ' la stringa in evento . Per ottenere la data e l'orario si possono usare le funzioni
   ctime() e time() del modulo time della libreria standard. Esempio, se il file log contiene:

Mon Oct 7 17:48:22 2013: first event
Mon Oct 7 17:48:32 2013: second event
Mon Oct 7 17:49:15 2013: Event n. 3

e se dopo 84 secondi dall'ultimo aggiornamento viene effettuata la chiamata log_update(log, 'New event!') , il file log diventa:

Mon Oct 7 17:48:22 2013: first event
Mon Oct 7 17:48:32 2013: second event
Mon Oct 7 17:49:15 2013: Event n. 3
Mon Oct 7 17:50:39 2013: New event!


5. findurl(lista_url, s, k) ritorna in una lista gli URL contenuti nella lista lista_urls tali che le pagine da essi puntate contengano almeno k
   occorrenze della stringa s . Si assume che gli URL in urls siano relativi a pagine HTML e quindi documenti di testo. 
   Esempi, sia

>>> urls = ['http://python.org', 'http://google.com', 'http://docs.python.org/2.7/index.html', 'http://pellacini.di.uniroma1.it/teaching/fondamenti13/index.html']
>>> findurl(urls, 'Python', 2) ritorna 
['http://python.org', 'http://docs.python.org/2.7/index.html', 'http://pellacini.di.uniroma1.it/teaching/fondamenti13/index.html'] 
>>> findurl(urls, 'Python', 7) ritorna 
['http://python.org', 'http://docs.python.org/2.7/index.html']

'''