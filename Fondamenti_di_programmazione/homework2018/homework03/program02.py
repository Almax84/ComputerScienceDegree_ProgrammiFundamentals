# Possiamo rappresentare lo skyline di una citta' con un numero di rettangoli di 
# diversi colori e dimensioni su di uno sfondo omogeneo. Vedi ad esempio i file es2_risTest*.png .
# Uno skyline e' dunque una sequenza di rettangoli posizionati sull'asse x delle ascisse. 
# La posizione del rettangolo all'interno dello skyline (nel seguito posizione del rettangolo) 
# e' individuata univocamente dalla coordinata x occupata dal suo vertice in basso a sinistra.
# Uno stesso rettangolo puo' essere presente piu' volte all'interno della sequenza in diverse posizioni. 
# 
# Per i nostri skyline valgono i seguenti vincoli:
# 1) nello skyline non compaiono mai due rettangoli con la stessa posizione.
# 2) nello skyline non compare mai un rettangolo che ha lo stesso colore dello sfondo.
# 3) Se due rettangoli si intersecano, quello che ha luminosita' massima appare in primo piano e 
# in caso di pari luminosita'  e' in primo piano il rettangolo posizionato piu' a sinistra 
# (la luminosita' di un rettangolo e' la somma delle tre componenti  del suo colore)
#  
# Definire una classe Colore, una classe Rettangolo e una classe Skyline secondo le seguenti specifiche.
# 
# La classe Colore deve implementare i seguenti metodi:
# - __init__(self,r=0,g=0,b=0)  che inizializza un colore con la terna RGB (r,g,b) valida.
# - utilizzo(self, sk) dove sk e' un oggetto di tipo Skyline. Il metodo ritorna  il numero di occorrenze 
#   di rettangoli con il colore self presenti nello skyline sk 
#   (ricorda che in uno skyline uno stesso rettangolo puo' comparire piu' volte in diverse posizioni)
# - to_tuple(self) che torna la terna (r, g, b)
# 
# La classe Rettangolo deve implementare i seguenti metodi:
# - __init__(base, altezza, colore) Base ed altezza sono due interi positivi e 
#   rappresentano la lunghezza della base e dell'altezza del rettangolo, colore e' un oggetto 
#   della classe Colore. 
# - cancella(self) cancella le occorrenze del rettangolo da tutti gli skyline in cui e' presente. 
# - to_tuple(self) che torna la terna (base, altezza, colore)
# 
# La classe Skyline deve implementare i seguenti metodi:
# - __init__(self, sfondo) dove sfondo e' un oggetto di tipo Colore. 
#   definisce uno skyline vuoto con colore di sfondo uguale a 'sfondo'. 
# - aggiungi(self, ret, x) l' oggetto ret di tipo Rettangolo viene aggiunto  
#   allo skyline a partire dall'ascissa x, l'aggiunta avviene solo se non vengono violate le regole 1), 2) e 3) 
#   dello skyline. 
# - fondi(self, other) con argomento other di tipo Skyline, che inserisce nello skyline self tutte le occorrenze  
#   di rettangoli dello skyline other. I rettangoli vanno inseriti nelle stesse posizioni che occupavano in other 
#   e l'inserimento di ciascun rettangolo avviene solo se non viola le regole degli skyline 
#   (ricorda che in uno skyline non e' possibile inserire rettangoli che hanno lo stesso colore dello sfondo 
#   ne' rettangoli da posizionare ad una ascissa gia' occupata).
# - salva(self, fimg)   salva  l'immagine dello skyline sotto forma di file PNG all'indirizzo fimg. 
# - larghezza(self) restituisce la larghezza dello skyline (vale a dire il valore massimo di x+base, 
#   dove base e' la base del rettangolo inserito alla posizione x).
#   Uno skyline vuoto ha per convenzione larghezza zero.
# - altezza(self) restituisce l'altezza dello skyline (vale a dire l'altezza massima tra quelle dei 
#   rettangoli presenti nello skyline). Uno skyline vuoto ha per convenzione altezza zero.
# - edifici(self) restituisce il numero di rettangoli presenti nello skyline.
# - to_tuple(self) che torna la tupla (sfondo,)
# 
# DEFINIZIONE DELLE CLASSI
# Siete liberi di scegliere sia gli attributi da usare in ciascun oggetto che la loro implementazione.
# Se lo ritenete utile potete aggiungere altri metodi alle vostre classi.
# 
# GESTIONE DEGLI ERRORI
# Tutti i metodi ed i costruttori devono controllare che gli argomenti forniti siano corretti, 
# 
# Per  salvare i file PNG si possono usare la funzione  save della libreria immagini.
# 
# NOTA: il timeout previsto per questo esercizio e' di 1 secondo per ciascun test.
# 
# ATTENZIONE: non potete usare altre librerie.
# 
# ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8   

import immagini 

################################################################################


class Colore:

    def __init__(self, r=0, g=0, b=0):
        if not Colore.isColorValid(r) or not Colore.isColorValid(g) or not Colore.isColorValid(b):
            raise ValueError('Colore non valido')
        self.r = r;
        self.g = g;
        self.b = b;

    def utilizzo(self, sk):
        if not isinstance(sk, Skyline):
            raise ValueError("Skylines non valido")
        counter = 0;
        #if sk.toDraw == True:
            #sk.disegna()

        for position, rect in sk.rectMap.items():
            if self == rect.colore:
                counter = counter + 1
                # per ogni rettangolo che ha lo stesso colore verifichiamo se e' stato disegnato
#                 found = False
#                 # vediamo se il rettangolo e' stato disegnato effettivamente
#                 for row in range(int(position), int(position) + rect.base):
#                         for col in range(rect.altezza):
#                                 if sk.imsAsRectPos[row][col] == int(position):
#                                     found = True
#                                     break
#                         if found == True:
#                             break
#                 if found == True:
#                     counter = counter + 1
                        
#         for position, rect in sk.rectMap.items():
            
#             if self == rect.colore:
#                 leftDownCorner = (int(position), 0)
#                 rightDownCorner = (int(position) + rect.base, 0)
#                 leftUpCorner = (leftDownCorner[0], rect.altezza)
#                 rightUpCorner = (rightDownCorner[0], rect.altezza)
#                 willBePainted = True
#                 # check if current rect will be painted
#                 for position2, rect2 in sk.rectMap.items():
#                     if int(position) != int(position2) and rect.brightness() <= rect2.brightness():
#                         leftDownCorner2 = (int(position2), 0)
#                         rightDownCorner2 = (int(position2) + rect2.base, 0)
#                         leftUpCorner2 = (leftDownCorner2[0], rect2.altezza)
#                         rightUpCorner2 = (rightDownCorner2[0], rect2.altezza)
#                         if(leftDownCorner[0] > leftDownCorner2[0] and rightDownCorner[0] <= rightDownCorner2[0] and leftUpCorner[1] <= leftUpCorner2[1] and rightUpCorner[1] <= rightUpCorner2[1]):
#                             willBePainted = False
#                             break
#                 if willBePainted == True:
#                     counter = counter + 1
        return counter

    def to_tuple(self):
        return (self.r, self.g, self.b)
    
    def __eq__(self, other):
        if not self.to_tuple() == other.to_tuple():
            return False
        else:
            return True

    def brightness(self):
        return self.r + self.g + self.b
    
    @staticmethod
    def static_brightness(tupla):
        return tupla[0] + tupla[1] + tupla[2]
        
    @staticmethod
    def isColorValid(rgbColor):
        try:
            if not isinstance(rgbColor, int):
                return False
        except ValueError:
            return False
           
        if rgbColor < 0 or rgbColor > 255:
            return False;
        else:
            return True
        
################################################################################


class Rettangolo:

    def __init__(self, base, altezza, colore):
        try:
            if not isinstance(base, int):
                raise ValueError("Dimensioni non valide")
            elif not isinstance(altezza, int):
                raise ValueError("Dimensioni non valide")
        except ValueError:
            raise ValueError("Dimensioni non valide")
        
        if base <= 0 or altezza <= 0:
            raise ValueError('Dimensioni non valide')
        
        if not isinstance(colore, Colore):
            raise ValueError("Sfondo Rettangolo non valido")
        self.base = base;
        self.altezza = altezza;
        self.colore = colore;
        self.skylineRef = []

    def cancella(self):
        for ref in self.skylineRef:
            localSkyline = ref[0]
            localPosition = ref[1]
            if localPosition in localSkyline.rectMap:
                del localSkyline.rectMap[localPosition]
                localSkyline.toDraw = True
                maxWidth = 0
                maxHeight = 0
                for position, rect in localSkyline.rectMap.items():
                    if (position + rect.base) > maxWidth:
                        maxWidth = position + rect.base
                    if rect.altezza > maxHeight:
                        maxHeight = rect.altezza
                localSkyline.width = maxWidth
                localSkyline.height = maxHeight
        self.skylineRef = []
        
    def brightness(self):
        return self.colore.brightness();

    def __eq__(self, other):
        if not self.to_tuple() == other.to_tuple():
            return False
        else:
            return True
        
    def aggiungiSkylineRef(self, skyline, position):
        self.skylineRef.append((skyline, position))
        
    def to_tuple(self):
        return (self.base, self.altezza, self.colore);

################################################################################


class Skyline:

    def __init__(self, sfondo):
        if not isinstance(sfondo, Colore):
            raise ValueError("Sfondo Skyline non valido")
        self.sfondo = sfondo
        self.toDraw = True
        self.width = 0
        self.height = 0
        self.imgAsPixelArray = []
        self.rectMap = {}  # dizionario di rettangoli presenti nello skyline, key: posizione (e' univoca) value: rettangolo

    def aggiungi(self, rettangolo, x):
        if not isinstance(rettangolo, Rettangolo):
            raise ValueError("Rettangolo non valido")
        if not isinstance(x, int):
            raise ValueError("Posizione non valida")
        if x < 0:
            raise ValueError("Posizione non valida")
        
        if self.sfondo == rettangolo.colore:
            return
            #raise ValueError('Rettangolo non valido, stesso sfondo dello skyline')
        
        if x in self.rectMap:
            return
            #raise ValueError('Rettangolo gia presente nella stessa posizione')
        
        # aggiungo il rettangolo
        self.rectMap[x] = rettangolo
        
        # ricalcolo massima lunghezza e altezza
        if (x + rettangolo.base) > self.width:
            self.width = x + rettangolo.base
        if rettangolo.altezza > self.height:
            self.height = rettangolo.altezza
        # aggiungo reference
        rettangolo.aggiungiSkylineRef(self, x)
        self.toDraw = True

    def fondi(self, other):
        if not isinstance(other, Skyline):
            raise ValueError("Skyline non valido")
        for position, rect in other.rectMap.items():
            try:
                #newRect = Rettangolo(rect.base, rect.altezza, rect.colore)
                self.aggiungi(rect, position)
            except:
                print('Go head')
        self.toDraw = True

    def salva(self, fimg):
        if not isinstance(fimg, str):
            raise ValueError("FileImg is not a valid file name")
        if not (fimg.endswith('.png')  or fimg.endswith('.PNG')):
            raise ValueError("FileImg is not a valid file name")
        
        if self.toDraw == True:
            self.disegna()
        
        immagini.save(self.imgAsPixelArray, fimg)
        #print("Immagine Salvata!")

    def disegna(self):
        lst = [None] * self.width
        #lstPosition = [-1] * self.width
        for i in range (self.width):
            lst[i] = [self.sfondo.to_tuple()] * self.height
            #lstPosition[i] = [-1] * self.height
            
        self.imgAsPixelArray = lst
        #self.imsAsRectPos = lstPosition
        # scorro i rettangoli da inserire in ordine di posizione, cosi se trovo stessa brightness comunque non lo inserisco
        for position, rect in sorted(self.rectMap.items()):
            for row in range(position, position + rect.base):
                for col in range(rect.altezza):
#                     if row == 80:
#                         print('eccomi')
                    if self.imgAsPixelArray[row][col] == self.sfondo.to_tuple():
                        self.imgAsPixelArray[row][col] = rect.colore.to_tuple()
                        #self.imsAsRectPos[row][col] = position
                    elif rect.colore.brightness() > Colore.static_brightness(self.imgAsPixelArray[row][col]):
                        #print('sovrascrivo ' + row + ' ' + col + ' con ' + rect.colore.to_tuple())
                        self.imgAsPixelArray[row][col] = rect.colore.to_tuple()
                        #self.imsAsRectPos[row][col] = position
                        
        # rotate 3 times
        self.imgAsPixelArray = list(zip(*self.imgAsPixelArray[::-1]))
        self.imgAsPixelArray = list(zip(*self.imgAsPixelArray[::-1]))
        self.imgAsPixelArray = list(zip(*self.imgAsPixelArray[::-1]))
        
        self.toDraw = False
        
    def larghezza(self):
        return self.width

    def altezza(self):
        return self.height

    def edifici(self):
        return len(self.rectMap)

    def to_tuple(self):
        return (self.sfondo,)


# ################################################################################
BLACK = (0, 0, 0);
WHITE = (255, 255, 255);
GREEN = (0, 255, 0);
RED = (255, 0, 0);
 
if __name__ == '__main__':
    green = Colore(0, 255, 0)
    black = Colore(0, 0, 0);
    red = Colore(255, 0, 0)
    white = Colore(255, 255, 255)
    greenRect = Rettangolo(70, 90, green)
    redRect = Rettangolo(50, 50, red)
    whiteRect = Rettangolo(60, 40, white)
    blackRect = Rettangolo(60, 120, black)
    sk = Skyline(black)
#     sk.aggiungi(whiteRect, 10)
#     sk.aggiungi(whiteRect, 60)
#     sk.aggiungi(whiteRect, 140)
#     sk.aggiungi(whiteRect, 180)
    sk.aggiungi(redRect, 30)
    sk.aggiungi(redRect, 70)
    sk.aggiungi(redRect, 110)
    sk.aggiungi(redRect, 150)
    sk.aggiungi(greenRect, 40)
    sk.aggiungi(greenRect, 80)
    sk.aggiungi(greenRect, 120)
    sk.aggiungi(greenRect, 160)
#     sk.aggiungi(blackRect, 20)
#     sk.aggiungi(blackRect, 190)
#     skRed = Skyline(white)
#     skRed.aggiungi(redRect, 1)
#     skRed.aggiungi(redRect, 50)
#     skRed.aggiungi(redRect, 25)
#     sk.fondi(skRed)
    #print(red.utilizzo(sk));
    
    # sk.fondi(sk)
    # greenRect.cancella();
    # print(green.utilizzo(sk))
     
    sk.salva('testSkyline.png')
     
