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

i -> riga
j -> colonna

tutte le colonne i fisso j variabile
tutte le righe i variabile j fisso
diagonali:
    diagonale principale i = j i iniz 1
    anti diagonale da dx a sx 
    
    
    d. p secondaria
    
    
11 12 13 14
21 22 23 24
31 32 33 34
41 42 43 44

anti diagonale principale
41 32 23 14 
i = len(righe)-1
j =  1+0  incrementato fino a len(righe) (len colonne?)


seconda - a-d secondaa
42 33 24
43 34
44

i = len(righe) -1
j = 1+ 1 fino a che j = len(colonne)




O	M	S	I	N	I	P	L	A	P
M	C	A	P	E	L	O	T	A	A
S	O	I	C	N	A	L	M	L	L
I	C	B	A	S	E	B	A	L	L
L	I	C	S	T	P	N	R	I	A
I	O	I	I	O	U	A	C	P	C
B	T	C	L	O	L	O	I	P	A
O	A	O	T	L	A	S	A	I	N
M	L	O	Y	A	S	R	O	C	E
O	I	S	C	H	E	R	M	A	S
T	G	T	E	K	C	I	R	C	T
U	U	O	M	S	I	D	O	P	R
A	P	A	L	L	A	V	O	L	O



ALPINISMO
ATLETICA
AUTOMOBILISMO
BASEBALL
CORSA
CRICKET
IPPICA
LANCIO
MARCIA
NUOTO
PALLACANESTRO
PALLAVOLO
PELOTA
PODISMO
POLO
PUGILATO
RALLY
SALTO
SCHERMA
SCI


''' 








def es1(ftesto):
    '''Implementare la funzione qui'''
    diagramma = []
    lista_parole = []
    with open(ftesto,'r', encoding='utf-8') as file:
        testo = file.read().splitlines()
        
        
        diagramma = list(map(lambda el: el.split("\t"),list(filter(lambda line : '\t' in line ,testo))))
        lista_parole = list(filter(lambda line : '\t' not in line and len(line)>0, testo))

            
    print(diagramma)
    print(lista_parole)

es1("C:/universita/ComputerScienceDegree_ProgrammiFundamentals/Fondamenti_di_programmazione/homework2018\homework02/cp3_Sport.txt")