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

diagonale superiore (contiene la diagonale principale)

diagonale inferiore




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
    lista_coordinate = []
    with open(ftesto,'r', encoding='utf-8') as file:
        testo = file.read().splitlines()
        
        
        diagramma_n = list(map(lambda el: el.split("\t"),list(filter(lambda line : '\t' in line ,testo))))
        lista_parole_n = list(filter(lambda line : '\t' not in line and len(line)>0, testo))
        diagramma = list(map(lambda x : ''.join( list(map(lambda word: word.upper() ,x)) ), diagramma_n))
        lista_parole = list(map( lambda x : x.upper(), lista_parole_n  ))
        
        #print(diagramma)
        #print(lista_parole)
        
                #controllo parole su righe da dx e sx
        for i,riga_diagramma in enumerate(diagramma):
            for parola in lista_parole:
                parola_reversed = parola[::-1]
                if parola in riga_diagramma:
                    indice_riga = riga_diagramma.find(parola)
                    #print(parola, " in ", riga_diagramma, " index: ", indice_riga)
                    coordinate_parola = [(i,j) for j in range(indice_riga, len(parola)+indice_riga)]
                    lista_coordinate+=coordinate_parola
                    #print(coordinate_parola)
                elif  parola_reversed in riga_diagramma:
                    indice_riga = riga_diagramma.find(parola_reversed)
                    #print(parola_reversed, " in ", riga_diagramma, " index: ", riga_diagramma.find(parola_reversed))
                    coordinate_parola = [(i,j) for j in range(indice_riga, len(parola)+indice_riga)]
                    lista_coordinate+=coordinate_parola

        lista_colonne = find_colonne(diagramma)   

            
        #controllo parole su colonne alto verso basso e viceversa
        #print(lista_colonne)
        
        for j, colonna_diagramma in enumerate(lista_colonne):
            
            for parola in lista_parole:
                parola_reversed = parola[::-1]
                if parola in colonna_diagramma:
                    indice_colonna = colonna_diagramma.find(parola)
                    #print(parola, " in ", colonna_diagramma, " index: ", indice_colonna)
                    coordinate_parola = [(i,j) for i in range(indice_colonna, len(parola)+indice_colonna)]
                    lista_coordinate+=coordinate_parola
                    #print(coordinate_parola)
                if parola_reversed in colonna_diagramma:
                    indice_colonna = colonna_diagramma.find(parola_reversed)
                    #print(parola_reversed, " in ", colonna_diagramma, " index: ", indice_colonna)
                    coordinate_parola = [(i,j) for i in range(indice_colonna, len(parola_reversed)+indice_colonna)]
                    lista_coordinate+=coordinate_parola
                    #print(coordinate_parola)
                    
        find_diagonal_back_slash(diagramma,lista_parole)        
    
        





def es1_bkp(ftesto):
    '''Implementare la funzione qui'''
    diagramma = []
    lista_parole = []
    lista_coordinate = []
    with open(ftesto,'r', encoding='utf-8') as file:
        testo = file.read().splitlines()
        
        
        diagramma = list(map(lambda el: el.split("\t"),list(filter(lambda line : '\t' in line ,testo))))
        lista_parole = list(filter(lambda line : '\t' not in line and len(line)>0, testo))
        diagramma_upper = list(map(lambda x : ''.join( list(map(lambda word: word.upper() ,x)) ), diagramma))
        lista_parole_upper = list(map( lambda x : x.upper(), lista_parole  ))
        
        #print(diagramma_upper)
      
        #controllo parole su righe da dx e sx
        for i,riga_diagramma in enumerate(diagramma_upper):
            for parola in lista_parole_upper:
                parola_reversed = parola[::-1]
                if parola in riga_diagramma:
                    indice_riga = riga_diagramma.find(parola)
                    #print(parola, " in ", riga_diagramma, " index: ", indice_riga)
                    coordinate_parola = [(i,j) for j in range(indice_riga, len(parola)+indice_riga)]
                    lista_coordinate+=coordinate_parola
                    #print(coordinate_parola)
                elif  parola_reversed in riga_diagramma:
                    indice_riga = riga_diagramma.find(parola_reversed)
                    #print(parola_reversed, " in ", riga_diagramma, " index: ", riga_diagramma.find(parola_reversed))
                    coordinate_parola = [(i,j) for j in range(indice_riga, len(parola)+indice_riga)]
                    lista_coordinate+=coordinate_parola

        lista_colonne = find_colonne(diagramma_upper)   

            
        #controllo parole su colonne alto verso basso e viceversa
        #print(lista_colonne)
        
        for j, colonna_diagramma in enumerate(lista_colonne):
            
            for parola in lista_parole_upper:
                parola_reversed = parola[::-1]
                if parola in colonna_diagramma:
                    indice_colonna = colonna_diagramma.find(parola)
                    #print(parola, " in ", colonna_diagramma, " index: ", indice_colonna)
                    coordinate_parola = [(i,j) for i in range(indice_colonna, len(parola)+indice_colonna)]
                    lista_coordinate+=coordinate_parola
                    #print(coordinate_parola)
                if parola_reversed in colonna_diagramma:
                    indice_colonna = colonna_diagramma.find(parola_reversed)
                    #print(parola_reversed, " in ", colonna_diagramma, " index: ", indice_colonna)
                    coordinate_parola = [(i,j) for i in range(indice_colonna, len(parola_reversed)+indice_colonna)]
                    lista_coordinate+=coordinate_parola
                    #print(coordinate_parola)

                    

#da alto a sinistra in giu
def find_diagonal_back_slash(diagramma,lista_parole):
    h = len(diagramma)
    w = len(diagramma[0])
    range_list = []
    
    
    for k in range(h+w-1):
        print("==============================")
        if k == 0:
            #print("k=",k)
            i = 0
            j = 0
            print(i," ", j)
        elif k < w:
            #print("k=",k)
            diagonal_word = ''
            temp_list = []
            for l in range(k+1):
                i = l
                j = k-l
                print(i," ", j)
                temp_list.append(tuple((i,j)))
                diagonal_word+=diagramma[i][j]
            #print( diagonal_word)
            word_in_list, indexes = is_word_in_list(diagonal_word, lista_parole, temp_list)
            if word_in_list:
                #print("found: ", diagonal_word)
                #print("diagonal index range: ", temp_list)
                #print("word index range: ", temp_list)
                range_list.append(indexes)
            
                
        else:
            #print("k=",k, " w=",w)
            diagonal_word = ''
            temp_list = []
            for l in range(k-w+1,k+1):
                i = l
                j = k-l
                if i>w or j>h:
                    break
                temp_list.append(tuple((i,j)))
                diagonal_word+=diagramma[i][j]
                print(i, " ", j)
            #print( diagonal_word)
            word_in_list, indexes = is_word_in_list(diagonal_word, lista_parole, temp_list)
            if word_in_list:
                #print("found: ", diagonal_word)
                #print("diagonal index range: ", temp_list)
                #print("word index range: ", temp_list)
                range_list.append(indexes)

                
def is_word_in_list(diagonal_string, list_words,index_list):
        for w in list_words:
            diagonal_reversed = diagonal_string[::-1]
            if w in diagonal_string :
                word_start_index = diagonal_string.index(w)
                word_index = index_list[word_start_index:word_start_index+len(w)]
                return True, word_index
            elif w in  diagonal_reversed :
                word_start_index = diagonal_string.index(diagonal_reversed)
                word_index = index_list[word_start_index:word_start_index+len(w)]
                return True,word_index
                
        return False, []




#find_diagonal_back_slash([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])            


def find_colonne(diagramma_upper):
        lista_colonne = []
        for j in range(len(diagramma_upper[0])):
            colonna = []
            colonna_string = ''
            for i in range(len(diagramma_upper)):
                colonna.append(diagramma_upper[i][j])
                colonna_string = ''.join(colonna)
            lista_colonne.append(colonna_string)
        return lista_colonne
            

es1("C:/universita/ComputerScienceDegree_ProgrammiFundamentals/Fondamenti_di_programmazione/homework2018\homework02/cp3_Sport.txt")