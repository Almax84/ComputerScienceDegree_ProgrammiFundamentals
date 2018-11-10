'''
I messaggi scambiati all'interno di un forum sono stati sottoposti ad uno studio.
Dai  vari post  sono state estrapolate parole significative e questi dati sono stati poi
raccolti in un  file di testo.
Nel file, l'inizio di ciascun post e' marcato da una linea che contiene  la stringa
"<POST>" e un intero utilizzato come identificativo del post (che nel seguito dovete 
lasciare come stringa).
la stringa e l'identificativo possono essere preceduti e seguiti da un numero arbitrario (anche 0)
 di spazi.
Le parole estrapolate  dal  post sono  nelle linee successive (zero  o piu' parole per 
linea) fino alla linea che marca il prossimo post 
o la fine del file.
Come esempio si veda il file "fp1.txt".
  
Per ognuna delle parole estrapolate si vogliono ora ricavare le seguenti informazioni: 
I1) Il numero totale di occorrenze della parola nei post,
I2) il numero di post in cui la parola compare,
I3) la coppia (occorrenze, post) dove nella seconda coordinata si ha l'identificativo del post 
in cui la parola e' comparsa piu' spesso e nella prima il numero di volte che vi e' comparsa,
(nel caso di  diversi post con pari numero massimo di occorrenze della parola va considerato 
il post con l'identificativo minore in ordine lessicografico).
Bisogna costruire una tabella avente una riga per ognuna delle differenti parole
utilizzate nel forum. La tabella deve avere 4 colonne  
In una colonna  comparira' la parola e nelle altre tre  le informazioni I1), I2) e I3) dette prima.
Le righe della colonna devono essere ordinate rispetto all'informazione I1) decrescente, a parita' 
del valore I1 vanno ordinate rispetto  alla cardinalita' decrescente dell'insieme degli itentificativi 
ed a parita', rispetto all'ordine lessicografico delle parole. 

Scrivere una funzione es2(fposts) che prende in input  il
percorso del file di testo contenente le estrapolazioni dei post del forum
e restituisce la tabella.
La tabella va restituita sotto forma di lista di dizionari dove
ciascun dizionario ha 4 chiavi: 'parola', 'I1','I2' e 'I3' e ad ogni chiave e'
associata la relativa informazione attinente la parola.
Ad esempio per il file di testo fp1.txt la funzione restituira' la lista:
[{'I1': 6, 'I2': 3, 'I3': (3, '30'), 'parola': 'hw1'},
 {'I1': 3, 'I2': 2, 'I3': (2, '30'), 'parola': 'python'},
 {'I1': 2, 'I2': 1, 'I3': (2,  '1'), 'parola': 'hw2'},
 {'I1': 1, 'I2': 1, 'I3': (1, '21'), 'parola': '30'},
 {'I1': 1, 'I2': 1, 'I3': (1, '30'), 'parola': 'monti'},
 {'I1': 1, 'I2': 1, 'I3': (1,  '1'), 'parola': 'spognardi'},
 {'I1': 1, 'I2': 1, 'I3': (1, '21'), 'parola': 'sterbini'}
 ]

NOTA: il timeout previsto per questo esercizio è di XXX secondi per ciascun test.
(il timeout definitivo verrà comunicato non appena avremo completato la generazione di altre istanze di test)

ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder o usate Notepad++)
'''
        

def es2(fposts):
    with open(fposts, 'r', encoding='utf-8') as file:
        splitted_text =' '.join(file.read().splitlines())
        posts = list(map(lambda x: x.strip(' '),list(filter(lambda x: x != '',splitted_text.split("<post>")))))
        #splitted_text = list(filter(lambda x : x != '',list(map(lambda x: x.strip(" "), splitted_text))))
        
        return_list = []
        
        for post in posts:
            words_in_post = post.split(" ")
            print(words_in_post)
            
    
        
        print(posts)

es2("fp1.txt")