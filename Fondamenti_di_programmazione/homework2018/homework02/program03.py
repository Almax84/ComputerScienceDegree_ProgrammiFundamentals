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
        file_lines = file.read().splitlines()
        print(file_lines)




        percorso_primo_robottino = []
        percorso_secondo_robottino = []
        insieme_I = []



        get_percorsi(file_lines, 0, percorso_primo_robottino)

        get_percorsi(file_lines, 0, percorso_secondo_robottino)

        get_percorsi(file_lines, 0, insieme_I)

        print(percorso_primo_robottino)
        print(percorso_secondo_robottino)
        print(insieme_I)


def get_percorsi(file_lines, i, target_list):
    while i < len(file_lines):
        line = file_lines[i]
        if line != '':
            target_list.append(line)
            file_lines.pop(i)
        elif len(target_list) > 0:
            break
        i += 1


es3("mp1.txt")