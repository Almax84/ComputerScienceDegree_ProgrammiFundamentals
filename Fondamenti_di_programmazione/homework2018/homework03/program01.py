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

    fimgAsArray = immagini.load(fimg)
    lunghezza = len(fimgAsArray)
    altezza = len(fimgAsArray[0])
    finalSolution = []
    
    
    for r in range(lunghezza):
        for c in range(altezza):
            currentPixel = fimgAsArray[r][c]

            if(isWhite(currentPixel)):
                canStartARectFromHere(r, c, fimgAsArray, lunghezza, altezza, finalSolution)
            
    for rect in finalSolution:
        writeGreen(rect, fimgAsArray)
        writeRed(rect, fimgAsArray)

    immagini.save(fimgAsArray, fimg1)
    return len(finalSolution)


def writeGreen(rect, fimgAsArray):
    GREEN = (0, 255, 0)

    leftUpCorner = rect[0]
    rightUpCorner = rect[1]
    leftDownCorner = rect[2]
    rightDownCorner = rect[3]
    
    # lato sopra
    for c in range(leftUpCorner[1], rightUpCorner[1] + 1):
        fimgAsArray[leftUpCorner[0]][c] = GREEN
    
    # lato sotto
    for c in range(leftDownCorner[1], rightDownCorner[1] + 1):
        fimgAsArray[leftDownCorner[0]][c] = GREEN
    
    # LATO SINISTRO
    for r in range(leftUpCorner[0], leftDownCorner[0] + 1):
        fimgAsArray[r][leftUpCorner[1]] = GREEN
    
    # LATO DESTRO
    for r in range(rightUpCorner[0], rightDownCorner[0] + 1):
        fimgAsArray[r][rightUpCorner[1]] = GREEN

    
def writeRed(rect, fimgAsArray):

     RED = (255, 0, 0)
     leftUpCorner = rect[0]
     rightUpCorner = rect[1]
     leftDownCorner = rect[2]

     for c in range(leftUpCorner[1]+1, rightUpCorner[1]):
         for r in range(leftUpCorner[0]+1, leftDownCorner[0]):
             #SCRIVO COLONNE
             fimgAsArray[r][c] = RED
     
    
def canStartARectFromHere(r, c, fimgAsArray, lunghezza, altezza, finalSolution):
    MIN_LENGTH = 3
    # andiamo a destra fino a che troviamo un nero o finisce l'immagine
    # contemporaneamente cerchiamo se nella riga di sotto ci sono pixel bianchi, se si ci fermiamo
    leftUpCorner = (r, c)
    rightUpCorner = -1
    leftDownCorner = -1
    rightDownCorner = -1
    # scorro verso destra, quindi il range e' da leftUpCorner.LEFT+1 fino alla fine della riga

    for y in range(leftUpCorner[1] + 1, lunghezza):
        currentPixel = fimgAsArray[leftUpCorner[0]][y]
        # bottomSideCurrentPixel = fimgAsArray[leftUpCorner[0] + 1][r]
        # se nero o alla fine dell'immagine allora OK
        # Se e l'ultima riga verifico se e' bianco o nero
        if y == (lunghezza - 1):
            if isBlack(currentPixel):
                # era la colonna precedente il corner
                rightUpCorner = (leftUpCorner[0], y - 1)
                break
            elif isWhite(currentPixel):
                # questa colonna e' l'ultima
                rightUpCorner = (leftUpCorner[0], y)
                break
            
        if isBlack(currentPixel):
            rightUpCorner = (leftUpCorner[0], y - 1)
            break
        # se il pixel nell'ultima colonna e' bianco quindi la riga continua verifichiamo se sotto e' bianco in tal caso e' un angolo in alto a destra e ci fermiamo
        elif isWhite(currentPixel) and (leftUpCorner[0] + 1) < altezza and isWhite(fimgAsArray[leftUpCorner[0] + 1][y]):
            rightUpCorner = (leftUpCorner[0], y)
            break
        
    if rightUpCorner == -1:
        return False
    
    # confrontiamo le colonne per capire la lunghezza
    if rightUpCorner[1] - leftUpCorner[1] + 1 < MIN_LENGTH :
        # print("Rettangolo troppo poco lungo")
        # TOO SMALL
        return False
    
    # LETS GO DOWN NOW
    
    # scoperta la base di sopra scendiamo a destra e a sinistra verticalmente fino a che non troviamo 
    # un nero o la fine dell'immagine, se anche dall'altra parte e' nero allora abbiamo trovato i lati
    for y in range(leftUpCorner[0] + 1, altezza):
        leftPixel = fimgAsArray[y][leftUpCorner[1]]
        rightPixel = fimgAsArray[y][rightUpCorner[1]]

        if y == (altezza - 1):
            # se proprio l ultima riga e' bianca almeno negli inner allora puo essere un rettangolo
            if isWhite(leftPixel) and isWhite(rightPixel):
                leftPixelInner = fimgAsArray[r][leftUpCorner[1] + 1]
                rightPixelInner = fimgAsArray[r][leftUpCorner[1] - 1]
                if isWhite(leftPixelInner) and isWhite(rightPixelInner):
                    # e' una possibile riga bianca quindi e' la base del rett
                    leftDownCorner = (y, leftUpCorner[1])
                    rightDownCorner = (y, rightUpCorner[1])
                    break
                break
            else:
                # se non sono entrambi bianchi e siamo arrivati alla fine allora non e' un rettangolo, manca la base
                return False
          
        if isWhite(leftPixel) and isWhite(rightPixel):
            # se sono entrambi bianchi allora va bene, controlliamo solo che non sia una potenziale riga bianca
            leftPixelInner = fimgAsArray[y][leftUpCorner[1] + 1]
            rightPixelInner = fimgAsArray[y][rightUpCorner[1] - 1]
            if isWhite(leftPixelInner) and isWhite(rightPixelInner):
                # e' una possibile riga bianca quindi e' la base del rett
                leftDownCorner = (y, leftUpCorner[1])
                rightDownCorner = (y, rightUpCorner[1])
                break
            elif isBlack(leftPixelInner) and isBlack(rightPixelInner):
                # se gli inner sono entrambi neri allora dobbiamo proseguire
                continue
            else:
                # se sono uno bianco e uno nero allora non va bene
                return False
        else:
            # se sono entrambi neri o uno bianco e uno nero allora non puo' essere un rettangolo
            return False
        
    if leftUpCorner == -1 or rightUpCorner == -1 or leftDownCorner == -1 or rightDownCorner == -1:
        print("Qualcosa non va!!!")
        return False
    
    if leftDownCorner[0] - leftUpCorner[0] + 1 < MIN_LENGTH:
        # print("Rettangolo troppo poco alto")
        return False
    
    # controlliamo la base sia interamente bianca
    for i in range(leftDownCorner[1], rightDownCorner[1] + 1):
        currentPixel = fimgAsArray[leftDownCorner[0]][i]
        if isBlack(currentPixel):
            return False
    
    # OK e' un rettangolo, manca solo da controllare che sia tutto nero all'interno
    for r in range(leftUpCorner[0] + 1, leftDownCorner[0]):
        for c in range(leftUpCorner[1] + 1, rightUpCorner[1]):
            currentPixel = fimgAsArray[r][c]
            if isWhite(currentPixel):
                return False
    
    finalSolution.append([leftUpCorner, rightUpCorner, leftDownCorner, rightDownCorner])
    return True
    
    
def isBlack(tupla):
    BLACK = (0, 0, 0)
    return tupla == BLACK


def isWhite(tupla):
    WHITE = (255, 255, 255)
    return tupla == WHITE


if __name__ == '__main__':
    es1('e1_f7.png', 'test7.png')

