'''
Possiamo rappresentare lo skyline di una citta' con un numero di rettangoli di 
diversi colori e dimensioni su di uno sfondo omogeneo. Vedi ad esempio i file es2_risTest*.png .
Uno skyline e' dunque una sequenza di rettangoli posizionati sull'asse x delle ascisse. 
La posizione del rettangolo all'interno dello skyline (nel seguito posizione del rettangolo) 
e' individuata univocamente dalla coordinata x occupata dal suo vertice in basso a sinistra.
Uno stesso rettangolo puo' essere presente piu' volte all'interno della sequenza in diverse posizioni. 

Per i nostri skyline valgono i seguenti vincoli:
1) nello skyline non compaiono mai due rettangoli con la stessa posizione.
2) nello skyline non compare mai un rettangolo che ha lo stesso colore dello sfondo.
3) Se due rettangoli si intersecano, quello che ha luminosita' massima appare in primo piano e 
in caso di pari luminosita'  e' in primo piano il rettangolo posizionato piu' a sinistra 
(la luminosita' di un rettangolo e' la somma delle tre componenti  del suo colore)
 
Definire una classe Colore, una classe Rettangolo e una classe Skyline secondo le seguenti specifiche.

La classe Colore deve implementare i seguenti metodi:
- __init__(self,r=0,g=0,b=0)  che inizializza un colore con la terna RGB (r,g,b) valida.
- utilizzo(self, sk) dove sk e' un oggetto di tipo Skyline. Il metodo ritorna  il numero di occorrenze 
  di rettangoli con il colore self presenti nello skyline sk 
  (ricorda che in uno skyline uno stesso rettangolo puo' comparire piu' volte in diverse posizioni)
- to_tuple(self) che torna la terna (r, g, b)

La classe Rettangolo deve implementare i seguenti metodi:
- __init__(base, altezza, colore) Base ed altezza sono due interi positivi e 
  rappresentano la lunghezza della base e dell'altezza del rettangolo, colore e' un oggetto 
  della classe Colore. 
- cancella(self) cancella le occorrenze del rettangolo da tutti gli skyline in cui e' presente. 
- to_tuple(self) che torna la terna (base, altezza, colore)

La classe Skyline deve implementare i seguenti metodi:
- __init__(self, sfondo) dove sfondo e' un oggetto di tipo Colore. 
  definisce uno skyline vuoto con colore di sfondo uguale a 'sfondo'. 
- aggiungi(self, ret, x) l' oggetto ret di tipo Rettangolo viene aggiunto  
  allo skyline a partire dall'ascissa x, l'aggiunta avviene solo se non vengono violate le regole 1), 2) e 3) 
  dello skyline. 
- fondi(self, other) con argomento other di tipo Skyline, che inserisce nello skyline self tutte le occorrenze  
  di rettangoli dello skyline other. I rettangoli vanno inseriti nelle stesse posizioni che occupavano in other 
  e l'inserimento di ciascun rettangolo avviene solo se non viola le regole degli skyline 
  (ricorda che in uno skyline non e' possibile inserire rettangoli che hanno lo stesso colore dello sfondo 
  ne' rettangoli da posizionare ad una ascissa gia' occupata).
- salva(self, fimg)   salva  l'immagine dello skyline sotto forma di file PNG all'indirizzo fimg. 
- larghezza(self) restituisce la larghezza dello skyline (vale a dire il valore massimo di x+base, 
  dove base e' la base del rettangolo inserito alla posizione x).
  Uno skyline vuoto ha per convenzione larghezza zero.
- altezza(self) restituisce l'altezza dello skyline (vale a dire l'altezza massima tra quelle dei 
  rettangoli presenti nello skyline). Uno skyline vuoto ha per convenzione altezza zero.
- edifici(self) restituisce il numero di rettangoli presenti nello skyline.
- to_tuple(self) che torna la tupla (sfondo,)

DEFINIZIONE DELLE CLASSI
Siete liberi di scegliere sia gli attributi da usare in ciascun oggetto che la loro implementazione.
Se lo ritenete utile potete aggiungere altri metodi alle vostre classi.

GESTIONE DEGLI ERRORI
Tutti i metodi ed i costruttori devono controllare che gli argomenti forniti siano corretti, 
e altrimenti lanciare l'eccezione ValueError (già presente in Python).

Per  salvare i file PNG si possono usare la funzione  save della libreria immagini.

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test.

ATTENZIONE: non potete usare altre librerie.

ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder o usate Notepad++)

'''



################################################################################

import immagini


class Colore:


    '''

    - __init__(self,r=0,g=0,b=0)  che inizializza un colore con la terna RGB (r,g,b) valida.
    - utilizzo(self, sk) dove sk e' un oggetto di tipo Skyline. Il metodo ritorna  il numero di occorrenze
      di rettangoli con il colore self presenti nello skyline sk
      (ricorda che in uno skyline uno stesso rettangolo puo' comparire piu' volte in diverse posizioni)
    - to_tuple(self) che torna la terna (r, g, b)
    '''

    def __init__(self,r=0,g=0,b=0):
       self.r, self.g, self.b = r, g, b

    def utilizzo(self, sk):

        self_color = self.color
        sfondo = sk.sfondo


    def to_tuple(self):
        return self.r, self.g, self.b
    
        
################################################################################

class Rettangolo:
    '''
    La classe Rettangolo deve implementare i seguenti metodi:
- __init__(base, altezza, colore) Base ed altezza sono due interi positivi e
  rappresentano la lunghezza della base e dell'altezza del rettangolo, colore e' un oggetto
  della classe Colore.
- cancella(self) cancella le occorrenze del rettangolo da tutti gli skyline in cui e' presente.
- to_tuple(self) che torna la terna (base, altezza, colore)

    '''

    def __init__(self, base, altezza, colore):
        self.colore_rettangolo = colore.r, colore.g, colore.b
        self.altezza = altezza
        self.base = base

    def cancella(self):
        return


    def to_tuple(self):
        return self.colore_rettangolo[0], self.colore_rettangolo[1], self.colore_rettangolo[2]

################################################################################

class Skyline:

    '''
La classe Skyline deve implementare i seguenti metodi:
- __init__(self, sfondo) dove sfondo e' un oggetto di tipo Colore.
  definisce uno skyline vuoto con colore di sfondo uguale a 'sfondo'.
- aggiungi(self, ret, x) l' oggetto ret di tipo Rettangolo viene aggiunto
  allo skyline a partire dall'ascissa x, l'aggiunta avviene solo se non vengono violate le regole 1), 2) e 3)
  dello skyline.
- fondi(self, other) con argomento other di tipo Skyline, che inserisce nello skyline self tutte le occorrenze
  di rettangoli dello skyline other. I rettangoli vanno inseriti nelle stesse posizioni che occupavano in other
  e l'inserimento di ciascun rettangolo avviene solo se non viola le regole degli skyline
  (ricorda che in uno skyline non e' possibile inserire rettangoli che hanno lo stesso colore dello sfondo
  ne' rettangoli da posizionare ad una ascissa gia' occupata).
- salva(self, fimg)   salva  l'immagine dello skyline sotto forma di file PNG all'indirizzo fimg.
- larghezza(self) restituisce la larghezza dello skyline (vale a dire il valore massimo di x+base,
  dove base e' la base del rettangolo inserito alla posizione x).
  Uno skyline vuoto ha per convenzione larghezza zero.
- altezza(self) restituisce l'altezza dello skyline (vale a dire l'altezza massima tra quelle dei
  rettangoli presenti nello skyline). Uno skyline vuoto ha per convenzione altezza zero.
- edifici(self) restituisce il numero di rettangoli presenti nello skyline.
- to_tuple(self) che torna la tupla (sfondo,)
    '''


    def __init__(self, sfondo):
        self.colore_sfondo = sfondo
        self.skyline_image = []

    def aggiungi(self, rettangolo, x):
        altezza_rettangolo = rettangolo.altezza
        base_rettangolo = rettangolo.base
        colore_rettangolo = rettangolo.colore_rettangolo

        #rule n.1, if x is contained in the already existing skylin
        # and the old skyline has height > 0
        altezza_skyline_original = self.altezza()
        larghezza_skyling_original = self.larghezza()
        if x < larghezza_skyling_original and altezza_skyline_original > 0:
            #if the preceding pixel and the x's pixel have different color
            #this is the start of a pre-existing building. todo questo check, ed il fatto che una nuova rica deve avere il colore di sfondo
            #first part of if: case when there is a rectangle of base 1, second part of if: case of rectangle of base > 1
            if (self.skyline_image[self.altezza()-1][x] != self.skyline_image[self.altezza()-1][x - 1] and \
                    self.skyline_image[self.altezza() - 1][x] != self.skyline_image[self.altezza()-1][x+1]) or \
                    (self.skyline_image[self.altezza()-1][x] != self.skyline_image[self.altezza()-1][x - 1] and
                     self.skyline_image[self.altezza() - 1][x] == self.skyline_image[self.altezza()-1][x+1]):
                return
        if x == 0 and larghezza_skyling_original > 0:
            return # if larghezza_skyline_original>0 it means that a rectangle was already created starting from 0, and that that
            #would be it's lower left corner


        #rule n.2
        if colore_rettangolo == self.colore_sfondo:
            return

        #if length of skyline_image is 0, create a skyline image as big as the passed rectangle
        if altezza_skyline_original == 0:
            self.skyline_image = [[colore_rettangolo for _ in range(base_rettangolo)] for _ in range(altezza_rettangolo)]
        else:
            for i in range(altezza_rettangolo):
                self.draw_horizontally( base_rettangolo,altezza_rettangolo, colore_rettangolo, i, x)

    def draw_horizontally(self, base_rettangolo,altezza_rettangolo, colore_rettangolo, i, x):

        self.increase_height_if_needed(base_rettangolo, colore_rettangolo, i,
                                       self.larghezza(), x)

        for j in range(x, base_rettangolo + x):

            if j > self.larghezza() - 1:
                #if it needs to add an extra column, then add it to every line by colouring it with the preceding pixel
                larghezza_old = self.larghezza()
                for i in range(len(self.skyline_image)):
                    if i < altezza_rettangolo:
                        self.skyline_image[self.altezza()-1-i].append(colore_rettangolo)
                    else:
                        self.skyline_image[self.altezza()-1-i].append(self.colore_sfondo.to_tuple())


            else:
                current_pixel_color = self.skyline_image[self.altezza()-1-i][j]
                if current_pixel_color != colore_sfondo.to_tuple() and\
                        sum(current_pixel_color) >= sum(colore_rettangolo):  # preexisting color is more luminous
                    continue

                self.skyline_image[self.altezza()-1-i][j] = colore_rettangolo

    def increase_height_if_needed(self, base_rettangolo, colore_rettangolo, i,
                                  larghezza_skyling_original, x):
        if i > self.altezza() - 1 and x + base_rettangolo <= self.larghezza():
            self.skyline_image.insert(0, [self.colore_sfondo.to_tuple() for _ in range(larghezza_skyling_original)])
        # because in the previous line we added one more line, we need to draw the "top" of the building on top of the background color
            for j in range(x, base_rettangolo + x):
                self.skyline_image[0][j] = colore_rettangolo

    def fondi(self, other):
        return
        '''
            - fondi(self, other) con argomento other di tipo Skyline, che inserisce nello skyline self tutte le occorrenze
              di rettangoli dello skyline other. I rettangoli vanno inseriti nelle stesse posizioni che occupavano in other
              e l'inserimento di ciascun rettangolo avviene solo se non viola le regole degli skyline
              (ricorda che in uno skyline non e' possibile inserire rettangoli che hanno lo stesso colore dello sfondo
              ne' rettangoli da posizionare ad una ascissa gia' occupata).
        '''

    def salva(self, fimg):
        immagini.save(self.skyline_image,fimg)

    def larghezza(self):
        if self.altezza() > 0:
            return len(self.skyline_image[0])
        return 0


    def altezza(self):
        return len(self.skyline_image)

    def edifici(self):
        #logic: count the colors in the image except for the background color?
        color_set = set()
        for i in range(self.altezza()):
            row_set = set(self.skyline_image[i])
            for pixel in row_set:
                if pixel != self.colore_sfondo.to_tuple():
                    color_set.add(pixel)
        return len(color_set)


    def to_tuple(self):
        return self.colore_sfondo,


################################################################################
if __name__ == "__main__":

    colore_sfondo = Colore(255, 255, 255)
    colore_rettangolo = Colore(21, 32, 98)
    skyline = Skyline(colore_sfondo)
    rettangolo = Rettangolo(10, 10, colore_rettangolo)

    skyline.aggiungi(rettangolo,0)

    #rettangolo più alto
    colore_rettangolo = Colore(100, 100, 100)
    rettangolo = Rettangolo(5,12, colore_rettangolo)

    skyline.aggiungi(rettangolo, 2)

    #rettangolo più largo e basso
    colore_rettangolo = Colore(150, 150, 100)
    rettangolo = Rettangolo(20, 2, colore_rettangolo)

    skyline.aggiungi(rettangolo, 1) #verde chiaro

    #rettangolo standard meno luminoso
    colore_rettangolo = Colore(9, 9, 9)
    rettangolo = Rettangolo(6,13 , colore_rettangolo)

    skyline.aggiungi(rettangolo, 7)


    #rettangolo più largo e alto
    colore_rettangolo = Colore(45, 55, 65)
    rettangolo = Rettangolo(7,9 , colore_rettangolo)

    skyline.aggiungi(rettangolo, 3)

    #pari luminosità in primo piano quello a sinistra
    colore_rettangolo = Colore(55, 65, 45)
    rettangolo = Rettangolo(25,13 , colore_rettangolo)

    skyline.aggiungi(rettangolo, 4) #quello precedente è a sx

#todo test pià lunga, più larga, e più lunga e più larga
    print(skyline.skyline_image)
    immagini.save(skyline.skyline_image,"test_davide.png")

    print(skyline.edifici())