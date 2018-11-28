'''
Abbiamo una immagine  .PNG . 
L'immagine presenta, su uno sfondo nero ( vale a dire di colore (0,0,0)), 
segmenti di colore bianco (vale a dire (255,255,255)) orizzontali e verticali di diversa lunghezza. 
Si veda ad esempio il file f1.png.
I segmenti, in alcuni casi, nell'incrociarsi creano rettangoli. 
Siamo interessati a trovare quei rettangoli di altezza e larghezza almeno 3 
(compreso il bordo, quindi con la parte nera alta e larga almeno 1 pixel)
e che, tranne il bordo completamente bianco, presentano tutti i pixel al loro interno di colore nero. 
A questo scopo vogliamo creare una nuova immagine identica alla prima se non per il 
fatto che questi rettangoli vengono evidenziati. 
Il bordo di questi rettangoli deve essere di colore verde (vale a dire (0,255,0)) e 
i pixel interni devono essere di colore rosso (vale a dire (255,0,0)).
Ad esempio l'immagine che vogliamo ricavare da quella nel file  f1.png e' 
nel file Risf1.png.

Scrivere una funzione es1(fimg,fimg1) che, presi in input gli indirizzi  di due file .PNG, 
legge dal primo l'immagine del tipo descritto sopra e salva nel secondo l'immagine 
con i rettangoli evidenziati. 
La funzione deve infine restituire  il numero di rettangoli che risultano evidenziati.

Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test.

ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder o usate Notepad++)

ATTENZIONE: non sono permesse altre librerie.
'''

import immagini

def es1(fimg, fimg1):
    '''scova in fimg i rettangoli da evidenziale, crea una copia dell'immagine 
    in cui questi rettangoli risultano evidenziati (vale a dire hanno bordo  verde e
    interno  rosso) salva l'immagine in fimg1 e restituisce il numero di rettangoli
    evidenziati. '''
    # inserite qui il vostro codice

