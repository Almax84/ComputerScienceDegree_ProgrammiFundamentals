'''
Una regione e' stata suddivisa concettualmente in quadrati adiacenti.
Ogni  quadrato della griglia risultante e' univocamente identificato da una 
coppia di interi positivi (x,y) ad indicare che il quadrato appartiene alla x-ma colonna 
e y-ma riga della griglia, CON IL QUADRATO (1,1) SITUATO IN BASSO A SINISTRA (ATTENZIONE!).

Disponiamo di robottini in grado di muoversi tra i quadrati della griglia ma solo in 
orizzontale (da sinistra verso destra) e verticale (dal basso verso l'alto). 
Uno spostamento del robottino viene indicato da un intero A (positivo o negativo). 
Se il robottino si trova nel quadratino di coordinate (x,y):
-  l'intero +A positivo indica uno spostamento in verticale fino al quadrato (x,y+|A|)
-  l'intero -A negativo indica uno spostamento in orizzontale della griglia fino al quadrato (x+|A|,y)
Una sequenza di interi (positivi o negativi) indica dunque un percorso del robottino.
Ad esempio se il robottino e' nel quadrato (1,1), la sequenza 5,-2,-2,2,-4 lo porta nel quadrato (9,8). 

Ci vengono forniti un insieme I di quadrati della griglia indicati dalle loro coordinate (x,y)
e due percorsi di due robottini, che partono entrambi dal quadrato (1,1) e terminano in uno stesso quadrato.
Il primo percorso comincia con un numero positivo, il secondo con un numero negativo 
e il quadrato iniziale e quello finale sono gli unici quadrati che i due percorsi hanno in comune.
Vogliamo sapere quanti dei quadrati dell'insieme I ricadono nella zona circoscritta dai due percorsi. 
Nota che un quadrato (x,y) e' nella zona circoscritta se i due robottini  
attraversano la colonna x della griglia e i quadrati di quella colonna attraversati
dai due robottini  sono rispettivamente (x,y1) ed (x,y2) con y1>y>y2).
(quindi i quadrati di I che si trovano sui percorsi NON vanno contati)

Ad esempio per per l'insieme 
    I={ (11, 2), (8,5), (4,6), (7,1), (2,9), (3,4), (7,6), (6,6), (5,2)}
e i due percorsi: 
    p1 =  5 -2 -2 2 -4
    p2 = -3  2 -5 5
Ovvero (indicando con '+' i movimenti con A positivo, con '-' quelli con A negativo, 
        con '*' i quadrati di I, con 'o' l'origine e con 'X' la destinazione)
    y
    ^
  11|
  10|
   9| *
   8|    +---X
   7|    +   +
   6|+--*-** +
   5|+      *+
   4|+ *     +
   3|+  +-----
   2|+  +*     *
   1|o---  *
    |_______________________>x
              11111111112
     12345678901234567890

la risposta e' 4 perche' gli unici quadrati che ricadono nella zona circoscritta sono
{(3, 4), (6, 6), (7, 6), (8, 5)}

Scrivere una funzione es3(fmappa) che prende in input  il percorso del file di testo contenente 
i percorsi dei due robottini e l'insieme dei quadrati I e restituisce il numero di quadrati 
dell'insieme I che risultano circoscritti dai due percorsi.

I dati sono organizzati  nel file come segue:
- una serie di righe vuote
- il percorso del primo robottino ( ciascuno spostamento del percorso
  separato dal successivo da spazi e il tutto in una o piu' righe consecutive) 
- una serie di righe vuote 
- il percorso del secondo  robottino ( ciascuno spostamento del percorso
  separato dal successivo da spazi e il tutto in una o piu' righe consecutive) 
- una serie di righe vuote 
- una sequenza di coppie (x,y) che indicano i quadrati dell'insieme (le coppie separate 
 da virgole e spazi ed in una o piu' righe consecutive)
- una serie di righe vuote

Si veda ad esempio il file mp1.txt

NOTA: il timeout previsto per questo esercizio è di XXX secondi per ciascun test.
(il timeout definitivo verrà comunicato non appena avremo generato le altre istanze di test)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
(ad esempio editatelo dentro Spyder)'''


def es3(fmappa):
    with open(fmappa, 'r', encoding='utf-8') as file:
        file_lines = file.read().strip().splitlines()
        print(file_lines)

        p1 = []
        p2 = []
        insieme_I = []

        p1 = get_percorso_robottino(file_lines, p1)
        p2 = get_percorso_robottino(file_lines, p2)

        tuples_string = ''.join(file_lines).strip()

        get_tuple_list(insieme_I, tuples_string)

        print("insieme I", insieme_I)
        print("primo robottino p1", p1)
        print("secondo robottino p2", p2)

        # 'intero +A positivo indica uno spostamento in verticale fino al quadrato (x,y+|A|)

        # 'intero -A negativo indica uno spostamento in orizzontale della griglia fino al quadrato (x+|A|,y)

        spostamento_p1 = [(1,1)]+get_spostamento_robottino(p1)
        print("spostamento p1", spostamento_p1)
        spostamento_p2 = [(1,1)]+get_spostamento_robottino(p2)
        print("spostamento p2", spostamento_p2)

        print(spostamento_p2[-1], spostamento_p1[-1])

        contatore_circoscritti = 0

        for tuple_i in insieme_I:
            x, y = tuple_i  # es 3,4 dovrebbe essere preso
            # crea funzione, colonna_attraversata(x, p1, p2)
            for p_p1 in spostamento_p1:
                x1, y1 = p_p1
                if x1 == x and y1 > y:
                    for p_p2 in spostamento_p2:
                        x2, y2 = p_p2
                        if x2 == x and y2 < y:
                            contatore_circoscritti += 1
                            # print("found!: p1:", p1, " p2:", p2, "tupleI", tuple_i)

        return contatore_circoscritti

        # restituisce booleano e la tupla contenente la colonna
        # se si, crea funzione compreso(y, p1, p2) che ritorna il contatore

        '''
        Nota che un quadrato (x,y) e' nella zona circoscritta se i due robottini  
        attraversano la colonna x della griglia e i quadrati di quella colonna attraversati
        dai due robottini  sono rispettivamente (x,y1) ed (x,y2) con y1>y>y2).
        la risposta e' 4 perche' gli unici quadrati che ricadono nella zona circoscritta sono
        {(3, 4), (6, 6), (7, 6), (8, 5)}
        '''


def get_spostamento_robottino(percorso_primo_robottino):
    x = 1
    y = 1
    lista_spostamenti_robottino = []
    for spostamento in percorso_primo_robottino:
        if spostamento > 0:
            for i in range(1, spostamento + 1):
                y += 1
                lista_spostamenti_robottino.append(tuple((x, y)))
        elif spostamento < 0:
            spostamento = spostamento * -1
            for i in range(1, spostamento + 1):
                x += 1
                lista_spostamenti_robottino.append(tuple((x, y)))
    return lista_spostamenti_robottino


def get_tuple_list(insieme_I, tuples_string):
    while len(tuples_string) > 0:
        first_par_index = tuples_string.find("(")
        second_par_index = tuples_string.find(")")
        tuple = tuples_string[first_par_index:second_par_index + 1]
        try:
            insieme_I.append(eval(tuple))  # se voglio una lista di tuple
            # insieme_I.append(tuple)
            tuples_string = tuples_string[second_par_index + 2:]
        except:
            print("could not eval: ", tuple)
            break


def get_percorso_robottino(file_lines, percorso_rotottino):
    i = 0
    while i < len(file_lines):
        line = file_lines[i]
        if line != '' or len(percorso_rotottino) == 0:
            percorso_rotottino += list(map(lambda x: int(x), line.split()))
            file_lines.pop(i)
            i -= 1
        else:
            break
        i += 1
    return percorso_rotottino


print(es3("mp5.txt"))
