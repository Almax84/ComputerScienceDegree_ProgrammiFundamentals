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
    
    

    0   1   2   3   4   5   6   7   8   9
0   C	O	I	H	C	C	E	P	S	B
1   I	N	O	I	Z	I	R	F	I	A
2   E	D	E	N	T	I	A	G	A	C
3   T	E	C	A	S	C	O	R	O	C
4   N	O	H	P	M	D	U	I	N	O
5   E	S	A	E	I	T	L	N	I	N
6   N	P	N	N	N	G	A	O	D	C
7   A	A	I	I	A	O	C	I	N	I
8   M	Z	T	T	I	M	C	Z	A	A
9   R	Z	E	T	I	O	A	O	V	T
10   E	O	R	E	L	L	S	L	A	U
11   P	L	A	P	I	E	G	A	L	R
12   M	A	N	I	C	U	R	E	R	E


ACCONCIATURE
BIGODINI
CASCO
DENTI
FRIZIONI
LACCA
LAVANDINO
LOZIONI
MANICURE
ONDE
PERMANENTE
PETTINE
PHON
PIEGA
RASOI
RETINA
SPAZZOLA
SPECCHIO
TAGLIO
TINTURA


''' 



def es1(ftesto):
    '''Implementare la funzione qui'''
    diagramma = []
    lista_parole = []
    lista_coordinate = []
    with open(ftesto,'r', encoding='utf-8') as file:
        testo = file.read().splitlines()
        
        
        diagramma_n = list(map(lambda el: el.split("\t"),list(filter(lambda line : '\t' in line ,testo))))
        lista_parole = list(filter(lambda line : '\t' not in line and len(line)>0, testo))
        diagramma = list(map(lambda x : ''.join( list(map(lambda word: word ,x)) ), diagramma_n))
        #lista_parole = list(map( lambda x : x.upper(), lista_parole_n  ))
        
                #controllo parole su righe da dx e sx
        for i,riga_diagramma in enumerate(diagramma):
            for parola in lista_parole:
                parola_reversed = parola[::-1]
                if parola in riga_diagramma:
                    indice_riga = riga_diagramma.find(parola)
                    coordinate_parola = [(i,j) for j in range(indice_riga, len(parola)+indice_riga)]
                    lista_coordinate+=coordinate_parola
                elif  parola_reversed in riga_diagramma:
                    indice_riga = riga_diagramma.find(parola_reversed)
                    coordinate_parola = [(i,j) for j in range(indice_riga, len(parola)+indice_riga)]
                    lista_coordinate+=coordinate_parola

        lista_colonne = find_colonne(diagramma)   

            
        # controllo parola su colonna
        for j, colonna_diagramma in enumerate(lista_colonne):
            
            for parola in lista_parole:
                parola_reversed = parola[::-1]
                if parola in colonna_diagramma:
                    indice_colonna = colonna_diagramma.find(parola)
                    coordinate_parola = [(i,j) for i in range(indice_colonna, len(parola)+indice_colonna)]
                    lista_coordinate+=coordinate_parola
                if parola_reversed in colonna_diagramma:
                    indice_colonna = colonna_diagramma.find(parola_reversed)
                    coordinate_parola = [(i,j) for i in range(indice_colonna, len(parola_reversed)+indice_colonna)]
                    lista_coordinate+=coordinate_parola
                    
        lista_coordinate+=find_diagonal_forward_slash(diagramma,lista_parole, True)
        lista_coordinate+=find_diagonal_forward_slash(diagramma,lista_parole, False)

        diagramma_by_char = [list(riga) for riga in diagramma ]
        #print(diagramma_by_char)
        #print(lista_coordinate)
        return_string = ''
        for i,stringa_riga in enumerate(diagramma_by_char):
            for j, char in enumerate(stringa_riga):
                if tuple((i,j)) not in lista_coordinate:
                    #print("coordinate non in lista coordinate ", i," ",j, char)
                    return_string+= char
        return return_string
    
    

#da alto a sinistra in giu
def find_diagonal_forward_slash(diagramma,lista_parole, forward):
    h = len(diagramma)
    w = len(diagramma[0])
    range_list = []
    
    verso = 0
    verso_fatt_molt = 1
    if not forward:
        verso = h - 1 
        verso_fatt_molt = -1
    
    
    for k in range(h+w-1):
        if k == 0:
            i = 0 + verso
            j = 0
        elif k < w:
            diagonal_word = ''
            temp_list = []
            for l in range(k+1):
                i = verso + l * verso_fatt_molt
                j = k-l
                try:
                    temp_list.append(tuple((i,j)))
                    diagonal_word+=diagramma[i][j]
                except:
                    #print(i,j)
                    pass
            #print(diagonal_word)
            word_in_list, indexes = is_word_in_list(diagonal_word, lista_parole, temp_list)
            if word_in_list:
                #print("trovata:", diagonal_word)
                range_list += [xy for xy in indexes]
            
                            
        else:
            diagonal_word = ''
            temp_list = []
            for l in range(k-w+1,k+1):
                i = verso + l * verso_fatt_molt
                j = k-l
                try:
                    if i < 0 or j < 0:
                        break
                    
                    temp_list.append(tuple((i,j)))
                    diagonal_word+=diagramma[i][j]
                except:
                    pass
                
                
            #print(diagonal_word)
            word_in_list, indexes = is_word_in_list(diagonal_word, lista_parole, temp_list)
            if word_in_list:
                #print("trovata:", diagonal_word, " ", indexes)
                range_list += [xy for xy in indexes]
                
            #print(range_list)
    return range_list
        

                
def is_word_in_list(diagonal_string, list_words,index_list):
        #print("is word in list: ",diagonal_string)
        word_index = []
        found = False
        for w in list_words:
            #diagonal_reversed = diagonal_string[::-1]
            word_reversed = w[::-1]
            if w in diagonal_string :
                word_start_index = diagonal_string.index(w)
                word_index += index_list[word_start_index:word_start_index+len(w)]
                #return True, word_index
                found = True
            elif word_reversed in  diagonal_string :
                word_start_index = diagonal_string.index(word_reversed)
                #print("index_list ",index_list)
                word_index += index_list[word_start_index:word_start_index+len(w)]
                #word_index= [x[::-1] for _,x in enumerate(index_list[word_start_index:word_start_index+len(w)]) ]
                #print("indexes for word: ", w, " ", word_index)
                #return True,word_index
                found = True
        return found, word_index       
        #return False, []


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
            

#print(es1("cp1_Tisana.txt"))