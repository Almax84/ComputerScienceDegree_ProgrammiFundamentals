'''
In enigmistica il crucipuzzle  e' uno schema di parole crociate dove non sono 
presenti le definizioni. E' composto da un elenco di parole ed un diagramma.
Per risolvere il crucipuzzle bisogna ricercare e poi cancellare dal diagramma TUTTE LE
OCCORRENZE (se multiple) delle parole presenti nell'elenco.
Le lettere del diagramma che rimarranno, prese tutte nel loro ordine per righe e per colonne,
formeranno la soluzione del gioco.
Le parole possono comparire  nel diagramma  in orizzontale (da destra verso sinistra, 
o da sinistra verso destra), in verticale  (dall'alto verso il basso o  dal basso verso 
l'alto)  e in diagonale (dall'alto verso il basso oppure dal basso verso l'alto).

Definire una funzione es1(ftesto), che prende l'indirizzo di un file di testo ftesto, 
contenente  diagramma ed elenco di parole di un crucipuzzle e restituisce la stringa 
soluzione del gioco. 
Il file fname  contiene  il diagramma  e, di seguito a questo  l'elenco delle parole.
Una serie di 1 o piu'  linee vuote precede il diagramma, separa il diagramma dall'elenco
delle parole e segue l'elenco delle parole.
Il diagramma e' registrato per righe (una riga per linea e in linee consecutive) gli 
elementi di ciascuna riga sono separati da un singolo carattere tab ('\t').
La lista delle parole occupa linee consecutive, una parola per ciascuna linea. 
Per un esempio si veda il file di testo esempio1.txt.

NOTA: il timeout previsto per questo esercizio è di XXX secondi per ciascun test
(il timeout definitivo verrà indicato non appena avremo generato le altre istanze di test)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
(ad esempio editatelo dentro Spyder)
''' 

def es1(ftesto):
    '''Implementare la funzione qui'''

