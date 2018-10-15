6# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:03:00 2018

@author: Davide.Scrimieri
"""
"""
draw chessboard
"""
bianco = (255,255,255)
nero = (0,0,0)
rosso = (255,0,0)
verde = (0,255,0)
blu = (0,0,255)
import image
#image.visd(img)


def draw_rectangle(h,w,c):
    colors_array = []
    for i in  range(h):
        riga = []
        for j in  range(w):
            riga.append(c)
        colors_array.append(riga)
    return colors_array


def draw_box_inside_image(colors_array,color,h,w,x,y):
    for i in range(y,y+h):
        for j in range(x,x+w):
            colors_array[i][j] = color
            

 
    

#
#immagine = draw_rectangle(200,200,rosso)
#draw_box_inside_image(immagine,nero,20,20,100,100)

#image.visd(immagine)


'''

## ESERCIZI

Scrivere le funzioni seguenti.

################################################################################

1. size(ll) prende in input una lista di liste ll e ritorna il numero di righe, la lunghezza mimima e
   massima delle righe e il numero totale di elementi. 
   Esempio
>>> size([[1,2,3],['a','b'],[1,2,'A',4,5]]) 
(3, 2, 5, 10)


################################################################################
'''


def size(ll):
    #(numero righe, lunghezza minima righe, lunghezza massima righe, numero totale elementi)
    numero_righe = len(ll)
    lunghezze_righe = [len(riga) for riga in ll ]
    minimo_riga = min(lunghezze_righe)
    massimo_riga = max(lunghezze_righe)
    numero_totale_elementi = sum(lunghezze_righe)

    return  (numero_righe,minimo_riga,massimo_riga,numero_totale_elementi)


#print(size([[1,2,3],['a','b'],[1,2,'A',4,5]]))    
    

'''
2. draw_h_line(img, x, y, w, c) che disegna sulla immagine img una linea orizzontale che parte dalla coordinata x, y, di lunghezza w e colore c
   senza sbordare.

   Esempio
>>> import image as im
>>> img = im.create(500,150,(0,255,0))
>>> draw_h_line(img, 100, 50,  300, (255, 0, 0) )
>>> draw_h_line(img,  50, 100, 700, (0, 0, 255) )
>>> im.visd(img)

mostra l'immagine del file es2-1.png

'''
import image as im
img = im.create(500,150,(0,255,0))

def draw_h_line(img,x,y,w,c):
    
    riga = img[y]
    end = x+w
    if x + w > len(riga):
        end = len(riga)
        
    
    for index in range(x, end):
        if im.inside(img,x,y):
            riga[index] = c

        
#draw_h_line(img, 100, 50, 300, (255, 0, 0))  
#draw_h_line(img,  50, 100, 700, (0, 0, 255) )    
#im.visd(img)



'''

################################################################################

3. draw_v_line(img, x, y, h, c) che disegna sulla immagine img una linea verticale
 che parte dalla coordinata x, y, di altezza w e colore c
   senza sbordare.

   Esempio
>>> import image as im
>>> img = im.create(500,150,(0,0,0))
>>> draw_v_line(img, 100, 50,  300, (255, 0, 0) )
>>> draw_v_line(img,  50, 100, 700, (0, 0, 255) )
>>> im.visd(img)

mostra una immagine uguale al file es3-1.png

'''

def draw_v_line(img,x,y,h,c):
    # cicla tutte le righe a partire da x fino a x + h
      # per ogni riga vai alla colonna y e setta il suo valore a c
    for yy in range(y, y+h):
        if im.inside(img,x, yy):
            img[yy][x] = c
        


#img = im.create(500,150,(0,0,0))
#draw_v_line(img, 100, 50,  300, (255, 0, 0) )
#draw_v_line(img,  50, 100, 700, (0, 0, 255) )
#im.visd(img)
#print(img)
      




'''
################################################################################

4. draw_quad_out(img, x1, y1, x2, y2, c) disegna sull'immagine img il contorno di un rettangolo di
   colore c che ha lo spigolo in alto a sinistra in (x1, y1) e quello in basso a destra in (x2, y2) . 
   Esempi
>>> import image as im
>>> img = im.create(300,150,(0,0,0))
>>> draw_quad_out(img,  50,  20, 100,140,(255,128,0))
>>> im.visd(img)
>>> draw_quad_out(img, 120, -10, 180, 70, (255,255,255))
>>> im.visd(img)
>>> draw_quad_out(img, 140,  40, 320, 120, (80,80,255))
>>> im.visd(img)

mostra immagini uguali a quelle allegate es4-1.png, es4-2.png, es4-3.png
'''
def draw_quad_out(img, x1,y1, x2,y2,c):
    h = y2 - y1
    w = x2 - x1
    
    
    draw_v_line(img, x2, y1, h, c)
    draw_v_line(img, x1, y1, h, c)
    
    draw_h_line(img,x1,y1,w,c)
    draw_h_line(img,x1,y2,w,c)
    return img
     
img = im.create(300,150,(0,0,0))
draw_quad_out(img,  50,  20, 100,140,(255,128,0))
im.visd(img)
draw_quad_out(img, 120, -10, 180, 70, (255,255,255))
im.visd(img)
draw_quad_out(img, 140,  40, 320, 120, (80,80,255))
im.visd(img)
    
    
    

'''
################################################################################

5. draw_grid(img, s, c) disegna sull'immagine img una griglia di linee orizzontali e verticali
 di colore c
   separate da s pixels le une dalle altre.
   Questo significa che se s è zero, le linee sono adiacenti. 
   Esempi
>>> img = im.create(200, 100, (200,200,200))
>>> draw_grid(img, 2, (0,0,0))
>>> im.visd(img)

mostra una immagine uguale al file es5-1.png

>>> img = im.create(400, 200, (240,240,240))
>>> for k in range(6):
...     s = int(8*(1.5**k))
...     c = 200 - 40*k
...     draw_grid(img, s, (c, c, c))
>>> im.visd(img)

mostra una immagine uguale al file es5-2.png


################################################################################

'''

def draw_grid(img, s, c):
    
    h = len(img)
    w = len(img[0])
    
    
    for i in range(0,len(img),s+1):
        riga = img[i]
        draw_h_line(img, 0, i, w,c)
    for x in range(0, w, s+1):
        draw_v_line(img, x, 0, h, c)
        
img = im.create(400, 200, (240,240,240))
for k in range(6):
     s = int(8*(1.5**k))
     c = 200 - 40*k
     draw_grid(img, s, (c, c, c))
im.visd(img)
            
            
            




