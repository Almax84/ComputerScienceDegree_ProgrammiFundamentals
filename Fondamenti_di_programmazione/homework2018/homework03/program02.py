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

    def __init__(self,r=0,g=0,b=0):

       if r == None or g == None or b == None: raise ValueError

       if not type(r) == int: raise ValueError
       if not type(g) == int: raise ValueError
       if not type(b) == int: raise ValueError

       if  (r < 0 or g < 0 or b < 0): raise  ValueError
       if (r > 255 or g > 255 or b > 255): raise ValueError

       self.r, self.g, self.b = r, g, b

    def utilizzo(self, sk):
        #TODO CONTROLLA SE: DEVE ESSERE LA STESSA ISTANZA, OPPURE GLI STESSI VALORI!
        if not type(sk) == Skyline: raise ValueError
        return sk.colors_used.count(self.to_tuple())


    def to_tuple(self):
        return self.r, self.g, self.b
    
        
################################################################################

class Rettangolo:

    def __init__(self, base, altezza, colore):
        if not type(colore) == Colore: raise ValueError
        if not type(base) == int: raise ValueError
        if not type(altezza) == int: raise ValueError

        if not base > 0: raise ValueError
        if not altezza > 0: raise ValueError

        self.colore_rettangolo = colore
        self.altezza = altezza
        self.base = base
        self.skylines_list = []
        self.x_position = None

    def cancella(self):
        # because it feels too hard to do otherwise, I won't delete the rectangle. I will redraw the whole image
        for skyline in self.skylines_list:
            rettangoli_in_istanza = skyline.rettangoli_in_istanza.copy()
            skyline.skyline_image = []
            skyline.rettangoli_in_istanza = []
            skyline.colors_used = []
            for rettangolo in rettangoli_in_istanza:

                if rettangolo != self:
                    skyline.aggiungi(rettangolo, rettangolo.x_position)

    def to_tuple(self):
        return self.base, self.altezza, self.colore_rettangolo

################################################################################

class Skyline:


    def __init__(self, sfondo):
        if not type(sfondo) == Colore: raise ValueError

        self.colore_sfondo = sfondo
        self.skyline_image = []
        self.rettangoli_in_istanza = []
        self.colors_used = []

    def aggiungi(self, rettangolo, x):

        if rettangolo == None : raise ValueError
        if x == None : raise ValueError
        if not (type(rettangolo) == Rettangolo): raise ValueError
        if not (type(x) == int) : raise ValueError
        if x < 0 : raise ValueError



        altezza_rettangolo = rettangolo.altezza
        base_rettangolo = rettangolo.base
        colore_rettangolo = rettangolo.colore_rettangolo

        self.colors_used.append(colore_rettangolo)

        #rule n.1, if x is contained in the already existing skylin
        # and the old skyline has height > 0
        altezza_skyline_original = self.altezza()
        larghezza_skyling_original = self.larghezza()
        if x < larghezza_skyling_original and altezza_skyline_original > 0:
            #if the preceding pixel and the x's pixel have different color
            #this is the start of a pre-existing building.
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
            self.skyline_image = [[colore_rettangolo.to_tuple() for _ in range(base_rettangolo)] for _ in range(altezza_rettangolo)]
        else:
            for i in range(altezza_rettangolo):
                self.draw_horizontally( base_rettangolo,altezza_rettangolo, colore_rettangolo, i, x)

        #add the produced skyline image to the rectangle property
        rettangolo.skylines_list.append(self)

        #if added, add this rectangle to the ones in this self instance
        rettangolo.x_position = x
        self.rettangoli_in_istanza.append(rettangolo)


    def draw_horizontally(self, base_rettangolo,altezza_rettangolo, colore_rettangolo, i, x):

        self.increase_height_if_needed(base_rettangolo, colore_rettangolo, i,
                                       self.larghezza(), x)

        for j in range(x, base_rettangolo + x):

            if j > self.larghezza() - 1:
                #if it needs to add an extra column, then add it to every line by colouring it with the preceding pixel
                self.increase_width_if_needed(altezza_rettangolo, colore_rettangolo, i,x)


            else:
                current_pixel_color = self.skyline_image[self.altezza()-1-i][j]
                if current_pixel_color != self.colore_sfondo.to_tuple() and \
                        sum(current_pixel_color) >= sum(colore_rettangolo.to_tuple()):  # preexisting color is more luminous
                    continue

                self.skyline_image[self.altezza()-1-i][j] = colore_rettangolo.to_tuple()

    def increase_width_if_needed(self, altezza_rettangolo, colore_rettangolo, i,x):
        for i in range(len(self.skyline_image)):
            if i < altezza_rettangolo and len(self.skyline_image[0]) >= x:
                self.skyline_image[self.altezza() - 1 - i].append(colore_rettangolo.to_tuple()) # caso se il rettangolo inizia prima
            else:
                self.skyline_image[self.altezza() - 1 - i].append(self.colore_sfondo.to_tuple())


    def increase_height_if_needed(self, base_rettangolo, colore_rettangolo, i,
                                  larghezza_skyling_original, x):
        if i > self.altezza() - 1 and x + base_rettangolo <= self.larghezza():
            self.skyline_image.insert(0, [self.colore_sfondo.to_tuple() for _ in range(larghezza_skyling_original)])
            # because in the previous line we added one more line, we need to draw the "top" of the building on top of the background color
            for j in range(x, base_rettangolo + x):
                self.skyline_image[0][j] = colore_rettangolo.to_tuple()

    def fondi(self, other):
        if not type(other) == Skyline: raise ValueError

        mappa_rettangoli_da_fondere = dict()
        lista_rettangoli_da_fondere = []


        #find rectangle in other
        for i in range(other.altezza()):
            j = 0
            while j < other.larghezza()-1:
                image = other.skyline_image
                colore = image[i][j]
                if colore != other.colore_sfondo.to_tuple():
                    left_up_corner = i,j,
                    #browse the line until the color changes

                    for c in range(j+1, other.larghezza()):
                        if colore != image[i][c] or c == other.larghezza()-1:
                            if c < other.larghezza()-1:
                                right_up_corner = i,c-1,
                            else:
                                right_up_corner = i,c
                            base = right_up_corner[1] - left_up_corner[1] + 1
                            altezza = other.altezza() - i
                            size = base, altezza  #larghezza, altezza
                            if tuple((colore, left_up_corner[1])) not in mappa_rettangoli_da_fondere:
                                mappa_rettangoli_da_fondere[tuple((colore,left_up_corner[1]))]=size  # key (color, column_left_up_corner) : (width, height)
                                rettangolo = Rettangolo(base,altezza,Colore(colore[0],colore[1],colore[2]))
                                rettangolo.x_position = left_up_corner[1]
                                lista_rettangoli_da_fondere.append(rettangolo)

                            j = c
                            break


                    j += 1
                else:
                    j+=1

        for rettangolo in lista_rettangoli_da_fondere:
            self.aggiungi(rettangolo, rettangolo.x_position)




    def salva(self, fimg):
        if not type(self) == Skyline: raise ValueError
        if fimg == None: raise ValueError
        if not type(fimg) == str: raise ValueError
        if not fimg[-3:] == 'png': raise ValueError
        immagini.save(self.skyline_image,fimg)

    def larghezza(self):
        if self.altezza() > 0:
            return len(self.skyline_image[0])
        return 0


    def altezza(self):
        return len(self.skyline_image)

    def edifici(self):
        #given that it's possible that a whole rectangle might be deleted by a brighter one
        #i have to check that a single rectangle is present in the position given with at least a pixel
        edifici_counter = 0

        for rettangolo in self.rettangoli_in_istanza:
            edifici_counter += self.increment_edifici_counter(rettangolo)

        return edifici_counter

    def increment_edifici_counter(self, rettangolo):
        #TODO: da ottimizzare: è inutile scandirsi tutta l'immagine, basterebbe vedere nell'intorno in cui ci si aspetta
        #che sia il rettangolo?
        for i in range(len(self.skyline_image)):
            for j in range(len(self.skyline_image[0])):
                if self.skyline_image[i][j] == rettangolo.colore_rettangolo and self.colore_sfondo.to_tuple != self.skyline_image[i][j]:
                    return 1
        return 0


    def to_tuple(self):
        return self.colore_sfondo,


################################################################################
if __name__ == "__main__":

    colore_sfondo = Colore(255, 255, 255)
    colore_rettangolo = Colore(21, 32, 98)
    primo_skyline = Skyline(colore_sfondo)
    rettangolo = Rettangolo(10, 10, colore_rettangolo)

    rettangolo.to_tuple()

    primo_skyline.aggiungi(rettangolo, 0)

    #rettangolo più alto
    colore_rettangolo = Colore(100, 100, 100)
    rettangoloc = Rettangolo(5,12, colore_rettangolo)

    primo_skyline.aggiungi(rettangoloc, 2)

    #rettangolo più largo e basso
    colore_rettangolo = Colore(150, 150, 100)
    rettangolo = Rettangolo(20, 2, colore_rettangolo)

    primo_skyline.aggiungi(rettangolo, 1) #verde chiaro

    #rettangolo standard meno luminoso
    colore_rettangolo = Colore(9, 9, 9)
    rettangolo = Rettangolo(6,13 , colore_rettangolo)

    primo_skyline.aggiungi(rettangolo, 7)


    #rettangolo più largo e alto
    colore_rettangolo = Colore(45, 55, 65)
    rettangolo = Rettangolo(7,9 , colore_rettangolo)

    primo_skyline.aggiungi(rettangolo, 3)

    #pari luminosità in primo piano quello a sinistra
    colore_rettangolo = Colore(0, 65, 45)
    rettangolo = Rettangolo(25,13 , colore_rettangolo)

    primo_skyline.aggiungi(rettangolo, 4) #quello precedente è a sx


    #edificio con stesso colore in posizione diversa
    colore_rettangolo = Colore(220, 200, 145)
    rettangolo = Rettangolo(10,9 , colore_rettangolo)

    primo_skyline.aggiungi(rettangolo, 26) #quello precedente è a sx

    # rettangolo.cancella()
    # rettangoloc.cancella()

    #print("utilizzo colore(55,65,45)", colore_rettangolo.utilizzo(primo_skyline))

#todo test pià lunga, più larga, e più lunga e più larga
    #print(primo_skyline.skyline_image)
    immagini.save(primo_skyline.skyline_image, "test_davide.png")

    #print(primo_skyline.edifici())

if __name__ == "__main__":

    colore_sfondo = Colore(255, 255, 255)
    colore_rettangolo = Colore(21, 32, 98)
    primo_skyline = Skyline(colore_sfondo)
    rettangolo = Rettangolo(10, 10, colore_rettangolo)

    primo_skyline.aggiungi(rettangolo, 0)

    #rettangolo più alto
    colore_rettangolo = Colore(100, 100, 100)
    rettangolo = Rettangolo(5,12, colore_rettangolo)

    primo_skyline.aggiungi(rettangolo, 2)

    #rettangolo più largo e basso
    colore_rettangolo = Colore(150, 150, 100)
    rettangolo = Rettangolo(20, 2, colore_rettangolo)

    primo_skyline.aggiungi(rettangolo, 1) #verde chiaro

    #rettangolo standard meno luminoso
    colore_rettangolo = Colore(9, 9, 9)
    rettangolo = Rettangolo(6,13 , colore_rettangolo)

    primo_skyline.aggiungi(rettangolo, 7)

    primo_skyline.salva("primo_skyline.png")

    primo_skyline.fondi(primo_skyline)


    colore_sfondo = Colore(255, 0, 0)
    secondo_skyline = Skyline(colore_sfondo)
    #rettangolo più largo e alto
    colore_rettangolo = Colore(45, 55, 65)
    rettangolo = Rettangolo(7,9 , colore_rettangolo) # BASE ALTEZZA COLORE

    secondo_skyline.aggiungi(rettangolo, 3)

    #pari luminosità in primo piano quello a sinistra
    #pari luminosità in primo piano quello a sinistra
    colore_rettangolo = Colore(0, 65, 45)
    rettangolo = Rettangolo(3,6 , colore_rettangolo)

    secondo_skyline.aggiungi(rettangolo, 4) #quello precedente è a sx


    #edificio con stesso colore in posizione diversa
    colore_rettangolo = Colore(220, 200, 145)
    rettangolo = Rettangolo(4,8 , colore_rettangolo)

    secondo_skyline.aggiungi(rettangolo, 10) #quello precedente è a sx
    secondo_skyline.salva("secondo_skyline.png")

    primo_skyline.fondi(secondo_skyline)

    primo_skyline.salva("risultato_fondi.png")


