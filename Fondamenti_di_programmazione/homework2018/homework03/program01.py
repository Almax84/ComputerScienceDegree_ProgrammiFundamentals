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
from _operator import length_hint

MIN_LENGTH = 3;
BLACK = (0, 0, 0);
WHITE = (255, 255, 255);
GREEN = (0, 255, 0);
RED = (255, 0, 0);


def es1(fimg, fimg1):
    '''scova in fimg i rettangoli da evidenziale, crea una copia dell'immagine 
    in cui questi rettangoli risultano evidenziati (vale a dire hanno bordo  verde e
    interno  rosso) salva l'immagine in fimg1 e restituisce il numero di rettangoli
    evidenziati. '''
    # inserite qui il vostro codice
    fimgAsArray = immagini.load(fimg);
    lunghezza = len(fimgAsArray);
    altezza = len(fimgAsArray[0]);
    finalSolution = []
    
    print("immagine " + str(lunghezza) + "x" + str(altezza));
    for r in range(lunghezza):
        #for c in range(altezza):
        c = 0
        while c < altezza:
            currentPixel = fimgAsArray[r][c]
            # print("position [" + str(r) + "," + str(c)+"]" )
            if(isWhite(currentPixel)):
                partialSolution = []
                canStartARectFromHere(r, c, fimgAsArray, lunghezza, altezza, finalSolution, partialSolution)
                if not len(partialSolution) == 0:
                    c = partialSolution[0][1]
                    #we continue because we start from the rightupcorner
                    continue
            
            c = c + 1
                
                # allWhitePosition.append((r,c))
    for rect in finalSolution:
        writeGreen(rect, fimgAsArray)
        writeRed(rect, fimgAsArray)

    immagini.save(fimgAsArray, fimg1)
    print("Immagine Salvata!")
    return len(finalSolution)


def writeGreen(rect, fimgAsArray):
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
    leftUpCorner = rect[0]
    rightUpCorner = rect[1]
    leftDownCorner = rect[2]
    rightDownCorner = rect[3]
     
    for c in range(leftUpCorner[1] + 1, rightUpCorner[1]):
        for r in range(leftUpCorner[0] + 1, leftDownCorner[0]):
            # SCRIVO COLONNE
            fimgAsArray[r][c] = RED
     
    
def canStartARectFromHere(r, c, fimgAsArray, lunghezza, altezza, finalSolution, partialSolution):
    # andiamo a destra fino a che troviamo un nero o finisce l'immagine
    # contemporaneamente cerchiamo se nella riga di sotto ci sono pixel bianchi, se si ci fermiamo
    
    leftUpCorner = (r, c)
    rightUpCorner = -1
    leftDownCorner = -1
    rightDownCorner = -1
    
    # scorro verso destra, quindi il range e' da leftUpCorner.LEFT+1 fino alla fine della riga
    for r in range(leftUpCorner[1] + 1, lunghezza):
        currentPixel = fimgAsArray[leftUpCorner[0]][r]
        # bottomSideCurrentPixel = fimgAsArray[leftUpCorner[0] + 1][r]
        # se nero o alla fine dell'immagine allora OK
        # Se e l'ultima colonna verifico se e' bianco o nero
        if r == (lunghezza - 1):
            if isBlack(currentPixel):
                # se all'ultima colonna troviamo nero e ancora non abbiamo individuato un angolo allora non e' un rettangolo
                break;
            elif isWhite(currentPixel):
                # questa colonna e' l'ultima
                rightUpCorner = (leftUpCorner[0], r);
                partialSolution.append(rightUpCorner)
                break;
        #se e' nero e al passo precedente non abbiamo trovato un angolo allora non puo' essere un angolo
        if isBlack(currentPixel):
            return False;
        # se il pixel nell'ultima colonna e' bianco quindi la riga continua verifichiamo se sotto e' bianco in tal caso e' un angolo in alto a destra e ci fermiamo
        #(leftUpCorner[0] + 1) < altezza controlla che sotto sia presente una riga
        elif isWhite(currentPixel) and (leftUpCorner[0] + 1) < altezza and isWhite(fimgAsArray[leftUpCorner[0] + 1][r]):
            rightUpCorner = (leftUpCorner[0], r);
            partialSolution.append(rightUpCorner)
            break;
        
    if rightUpCorner == -1:
        return False;
    
    rectLength = rightUpCorner[1] - leftUpCorner[1] + 1
    # confrontiamo le colonne per capire la lunghezza
    if rectLength < MIN_LENGTH :
        # print("Rettangolo troppo poco lungo");
        # TOO SMALL
        return False;
    
    # LETS GOING DOWN NOW
    
    # scoperta la base di sopra scendiamo a destra e a sinistra verticalmente fino a che non troviamo 
    # un nero o la fine dell'immagine, se anche dall'altra parte e' nero allora abbiamo trovato i lati
    for r in range(leftUpCorner[0] + 1, altezza):
        leftPixel = fimgAsArray[r][leftUpCorner[1]]
        rightPixel = fimgAsArray[r][rightUpCorner[1]]
        
        if r == (altezza - 1):
            # se proprio l ultima riga e' bianca almeno negli inner allora puo essere un rettangolo
            if isWhite(leftPixel) and isWhite(rightPixel):
                leftPixelInner = fimgAsArray[r][leftUpCorner[1] + 1]
                rightPixelInner = fimgAsArray[r][leftUpCorner[1] - 1]
                if isWhite(leftPixelInner) and isWhite(rightPixelInner):
                    # e' una possibile riga bianca quindi e' la base del rett
                    leftDownCorner = (r, leftUpCorner[1])
                    rightDownCorner = (r, rightUpCorner[1])
                    break;
                else:
                    return False;
            else:
                # se non sono entrambi bianchi e siamo arrivati alla fine allora non e' un rettangolo, manca la base
                return False
        elif isWhite(leftPixel) and isWhite(rightPixel):
            # se sono entrambi bianchi allora va bene, controlliamo solo che non sia una potenziale riga bianca
            leftPixelInner = fimgAsArray[r][leftUpCorner[1] + 1]
            rightPixelInner = fimgAsArray[r][rightUpCorner[1] - 1]
            if isWhite(leftPixelInner) and isWhite(rightPixelInner):
                # e' una possibile riga bianca quindi e' la base del rett
                leftDownCorner = (r, leftUpCorner[1])
                rightDownCorner = (r, rightUpCorner[1])
                break;
            elif isBlack(leftPixelInner) and isBlack(rightPixelInner):
                # se gli inner sono entrambi neri allora dobbiamo proseguire, prima pero' controlliamo che la riga sia nera
                if not rectLength == MIN_LENGTH:
                    for ir in range(leftUpCorner[1] + 2, rightUpCorner[1] - 1):
                        if isWhite(fimgAsArray[r][ir]):
                            return False;
                        else:
                            continue;
            else:
                # se sono uno bianco e uno nero allora non va bene
                return False;
        else:
            # se sono entrambi neri o uno bianco e uno nero allora non puo' essere un rettangolo
            return False;
        
    if leftUpCorner == -1 or rightUpCorner == -1 or leftDownCorner == -1 or rightDownCorner == -1:
        print("Qualcosa non va!!!");
        return False;
    
    if leftDownCorner[0] - leftUpCorner[0] + 1 < MIN_LENGTH:
        # print("Rettangolo troppo poco alto");
        return False;
    
    # controlliamo la base sia interamente bianca
    for i in range(leftDownCorner[1], rightDownCorner[1] + 1):
        currentPixel = fimgAsArray[leftDownCorner[0]][i];
        if isBlack(currentPixel):
            return False;
    
    # OK e' un rettangolo, manca solo da controllare che sia tutto nero all'interno
    #TODO POTREMMO FARLO MENTRE SCENDO!!!
#     for r in range(leftUpCorner[0] + 1, leftDownCorner[0]):
#         for c in range(leftUpCorner[1] + 1, rightUpCorner[1]):
#             currentPixel = fimgAsArray[r][c]
#             if isWhite(currentPixel):
#                 return False;
    
    # INCREDINILE E' UN RETTANGOLO
    # print("RETTANGOLO!!!")
    print("Ecco i Lati" + str(leftUpCorner) + " - " + str (rightUpCorner) + " - " + str(leftDownCorner) + " - " + str(rightDownCorner))
    finalSolution.append([leftUpCorner, rightUpCorner, leftDownCorner, rightDownCorner])
    return True;
    
    
def isBlack(tupla):
    return tupla == BLACK;


def isWhite(tupla):
    return tupla == WHITE;


if __name__ == '__main__':
    es1('e1_f5.png', 'test5.png');

