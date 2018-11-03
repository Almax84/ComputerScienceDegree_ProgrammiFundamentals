# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 08:26:22 2018

@author: david
"""

## ESERCIZI
'''
Scrivere le funzioni seguenti.

################################################################################

1. size(ll) prende in input una lista di liste ll e ritorna il numero di righe, la lunghezza mimima e
   massima delle righe e il numero totale di elementi. 
   Esempio
>>> size([[1,2,3],['a','b'],[1,2,'A',4,5]]) 
(3, 2, 5, 10)
'''

def size(ll):
    numero_righe = len(ll)
    
    lungh_massima_righe = 0
    lungh_minima_righe = len(ll[0])
    sum_elements = 0
    for riga in ll:
        len_riga = len(riga)
        sum_elements+=len_riga
        if len_riga > lungh_massima_righe:
            lungh_massima_righe = len_riga
            
        if len_riga < lungh_minima_righe:
            lungh_minima_righe = len_riga
            
    return numero_righe,lungh_minima_righe, lungh_massima_righe, sum_elements


print(size([[1,2,3],['a','b'],[1,2,'A',4,5]]))
    
        



'''
################################################################################

2. draw_h_line(img, x, y, w, c) che disegna sulla immagine img una linea orizzontale che parte dalla
   coordinata x, y, di lunghezza w e colore c 
   senza sbordare.

   Esempio
>>> import image as im
>>> img = im.create(500,150,(0,255,0))
>>> draw_h_line(img, 100, 50,  300, (255, 0, 0) )
>>> draw_h_line(img,  50, 100, 700, (0, 0, 255) )
>>> im.visd(img)

mostra l'immagine del file es2-1.png
'''

def draw_h_line(img,x,y,w,c):
    
    #if y < len(img):
    riga = img[y]
    
    end_hor_line = x + w
    if x + w > len(riga):
        end_hor_line = len(riga)
    
    
    #if(x < len(riga)):
    for j in range(x, end_hor_line):
         
        riga[j] = c


'''
import image as im
img = im.create(500,150,(0,255,0))
draw_h_line(img,100,50,300,(255,0,0))
draw_h_line(img, 50,100,700, (0,0,255))
im.visd(img)
'''


'''
################################################################################

3. draw_v_line(img, x, y, h, c) che disegna sulla immagine img una linea verticale che parte 
dalla coordinata x, y, di altezza w e colore c
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
    
    end_vert_line = h
    if y + h > len(img):
        end_vert_line = len(img)
        
    print("\n\naltezza img:",len(img), " altezza verticale:", end_vert_line)
        
    for i in range(y, end_vert_line):
        if x < len(img[i]):
            img[i][x] = c
        

'''
import image as im
img = im.create(500,150, (0,0,0))
draw_v_line(img,100,50,300,(255,0,0))
draw_v_line(img,50,100,700,(0,0,255))
im.visd(img)
'''


'''
################################################################################

4. draw_quad_out(img, x1, y1, x2, y2, c) disegna sull'immagine img il contorno di un rettangolo
 di
   colore c che ha lo spigolo in alto a sinistra in (x1, y1)
   e quello in basso a destra in (x2, y2) . 
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
def draw_quad_out(img,x1,y1,x2,y2,c):
   
    if x1 < 0:
        x1 = 0
    elif x2 < 0:
        x2 = 0
    elif y1 < 0:
        y1 = 0
    elif y2 < 0:
        y2 = 0
    
    
    w = x2 - x1
    h = y2 - y1
    
    print("altezza img ",len(img))
    print("altezza calcolata", h)
    
    draw_v_line(img,x1,y1,h,c)
    
    
    draw_h_line(img,x1,y1,w,c)
    
    draw_v_line(img,x2,y1,h,c)
    
    
    print("draw h y2",y2)
    draw_h_line(img,x1,h,w,c)

import image as im
img = im.create(300,150,(0,0,0))
draw_quad_out(img, 50,20,100,140,(255,128,0))
im.visd(img)
draw_quad_out(img,120,-10,180,70,(255,255,255))
im.visd(img)
draw_quad_out(img,140,40,320,120,(80,80,255))
im.visd(img)
'''
################################################################################

5. draw_grid(img, s, c) disegna sull'immagine img una griglia di linee orizzontali e verticali di colore c
   separate da s pixels le une dalle altre. Questo significa che se s è zero, le linee sono adiacenti. 
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