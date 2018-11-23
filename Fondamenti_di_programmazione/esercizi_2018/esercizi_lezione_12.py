# -*- coding: utf-8 -*-
'''
1. rotL90(img) ritorna una nuova immagine che è l'immagine img ruotata a sinistra di 90 gradi. 
   Esempio: nel file es1.png vedete come l'immagine img_in_01.png viene ruotata

'''

import image as im

def transponse(img):
    h = len(img)
    w = len(img[0])
    
    #to do rotation, create matrix of width h and height w
    return_image = [ [0 for j in range(h)] for i in range(w) ]
    
    new_w, new_h = h, w
    print("w:",new_w,"h:", new_h)
    
    for i in  range(new_w): #h original
        for j in range(new_h): #w original    
            #return_image[j][i] = img[i][w-j-1]
            return_image[j][i] = img[i][new_h-j-1]
            
           
    return return_image
'''

In questo caso da una immagine w X h si deve ottenere una immagine h X w con i pixel che mappano le coordinate x0,y0 in 
	y1 = x0
	x1 = h-y0-1
    
'''     
def rotL90(img):
    orig_h, orig_w = len(img), len(img[0])
    w, h = orig_h, orig_w			# dimensioni scambiate
    ris = im.create(w, h, im.black)
    for x in range(w):
        for y in range(h):
            ris[y][x] = img[x][orig_w-y-1]
    im.visd(ris)
    return ris


    
    
    
    
    


if __name__ == '__main__':

    image = im.load('files_ese12/files/es1_1.png')
    print("immagine originale")
    im.visd(image)
    
    print("trasposta")
    im.visd(transponse(image))
    
    #transponse(transponse(image))
    print("giusta")
    rotL90(image)




