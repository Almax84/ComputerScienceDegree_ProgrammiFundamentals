r'''

In una immagine in formato PNG è disegnato un albero secondo le seguenti convenzioni:
- lo sfondo dell'immagine è nero (0, 0, 0)
- la radice viene rappresentata da un pixel verde (0, 255, 0)
- tutti gli altri nodi sono rappresentati da un pixel rosso (255, 0, 0)
- due nodi sono in relazione padre-figlio se esiste una sequenza di pixel bianchi
    affiancati in orizzontale e/o verticale che li collega
- se più nodi sono collegati dalla stesso percorso bianco che si dirama,
    vuol dire che uno è il padre e gli altri sono tutti suoi figli
- una volta individuato il nodo radice è possibile individuare quali siano i padri
    e quali siano i figli in tutto l'albero navigandolo a partire dalla radice
- potete assumere che i percorsi non si intersechino (ma possono diramarsi)
    e che siano sempre larghi 1 pixel
- potete assumere che non esistano cicli (altrimenti sarebbe un grafo e non un albero)

Esempio: (R=rosso, w=bianco, V=verde, ' '=nero)
          1111111111222222222233333333334444444444
01234567890123456789012345678901234567890123456789
--------------------------------------------------
   R                                              | 0
   wwwwwww                                        | 1
         w      RwwwwwwwwwwwwwwwR         R       | 2
         w            w                   w       | 3
         w            wwwRwwwwwwww        w       | 4
         w            w          w        w       | 5
         wwwwRwwwwwwwww          Vwwwwwwwww       | 6
         w                       w                | 7
         w               wwwwwwwww                | 8
         w               w                        | 9
         wwwwwwR         R                        |10
--------------------------------------------------

La radice (V) è il pixel alle coordinate        (33, 6)
mentre gli altri nodi (R) sono alle coordinate  ( 3, 0), (13, 6), (15, 10), (16, 2), (25, 4), (25, 10), (32, 2), (42, 2)
L'albero che ne risulta è

                (33, 6)
               /   |   \
             /     |    \
         (25,10) (42,2)  (25,4)
                        /  |   \
                       /   |    \
                   (16,2)(32,2) (13,6)
                                /    \
                            (3,0)  (15,10)

Implementate la funzione es3(filePNGinput, filePNGoutput) che:
    - legge l'immagine PNG contenuta nel file filePNGinput
    - individua e costruisce l'albero corrispondente
    - individua i due nodi più distanti nell'albero e
        - colora di blu (0, 0, 255) tutti i pixel bianchi del percorso che li collega
          passando di nodo in nodo (se necessario ripassando su alcuni pixel 2 volte)
            (lasciando invariato lo sfondo ed i nodi rossi/verdi)
    - salva nel file filePNGoutput l'immagine risultante
    - torna come risultato il numero di pixel che sono stati colorati di blu
        (che potrebbero essere di meno della lunghezza del percorso più lungo
        perchè i tratti su cui si passa due volte vanno contati una sola volta)

NOTA: La distanza tra due nodi è il numero minimo totale dei SOLI pixel BIANCHI che li collegano
passando per i nodi interni (alcuni tratti potrebbero essere percorsi 2 volte).
SUGGERIMENTO: ispiratevi al calcolo del diametro di un albero
NOTA: per calcolare il percorso più lungo i pixel su cui si passa più volte vanno contati più volte
    (ad esempio il numero di pixel per il percorso (16,2)->(25,4)->(32,2) è 10+14=24)
NOTA: potete assumere che il percorso più lungo sia unico

Nel caso dell'esempio i due nodi più distanti sono (42,2) e (3,0) per cui l'immagine da salvare è
(b)=blu
          1111111111222222222233333333334444444444
01234567890123456789012345678901234567890123456789
--------------------------------------------------
   R                                              | 0
   bbbbbbb                                        | 1
         b      RwwwwwwwwwwwwwwwR         R       | 2
         b            w                   b       | 3
         b            bbbRbbbbbbbb        b       | 4
         b            b          b        b       | 5
         bbbbRbbbbbbbbb          Vbbbbbbbbb       | 6
         w                       w                | 7
         w               wwwwwwwww                | 8
         w               w                        | 9
         wwwwwwR         R                        |10
--------------------------------------------------
e la funzione torna 49 che è il numero di pixel bianchi che sono stati colorati di blu (b)

ATTENZIONE: Almeno una delle funzioni/metodi che risolvono l'esercizio DEVE essere ricorsiva.
ATTENZIONE: per fare in modo che il macchinario di test riconosca automaticamente la presenza della ricorsione
    questa funzione ricorsiva DEVE essere una funzione esterna oppure il metodo di una classe.
    Anche questa classe va definita esternamente alle funzioni.

ATTENZIONE: Non potete usare altre librerie a parte immagini.

ATTENZIONE: assicuratevi di salvare il programma con encoding utf8
(ad esempio usando come editor Notepad++ oppure Spyder)

In timeout per ciascuno dei test è di 1 secondo.

'''

import immagini

def es3(filePNGInput, filePNGOutput):
    # inserite qui il vosto codice





# le righe seguenti non vengono eseguite quando si importa il modulo
if __name__ == '__main__':
    # inserite qui i vostri test personali

