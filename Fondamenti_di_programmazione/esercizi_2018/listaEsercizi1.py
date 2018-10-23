def es1(s, x):
    '''ritorna una copia della stringa s dove il carattere di s in posizione x diventa uguale 
    all'ultimo carattere.  Si assume che s sia lunga almeno x+1'''
    #inserite qui il vostro codice
    result = ''
    last_char = s[len(s)-1]
    for i in range(len(s)):
        if i == x:
            result+=last_char
        else:
            result+=s[i]
    return result
'''
>>> es1('ciao', 2)    
'cioo'
>>> es1('cosa', 1)    
'casa'
>>> es1('cane', 3)
'cane'
'''
    

############################################################

def es2(s, x,y):
    '''ritorna una copia della stringa s dove i caratteri nelle posizioni x e y 
    risultano scambiati di posto. Si puo' assumere che i due interi x e y sono 
    inferiori alla lunghezza della stringa s.'''
    #inserite qui il vostro codice

    result = ''
    char_at_x=s[x]
    char_at_y=s[y]
    for i in range(len(s)):
        if i == x:
            result+=char_at_y
        elif i == y:
            result+=char_at_x
        else:
            result+=s[i]
    return result
'''
>>> es2('ciao', 0, 3)    
'oiac'
>>> es2('cosa', 3,1)    
'caso'
>>> es2('cane', 1,1)    
'cane'
'''
##############################################################

def es3(stringa):
    '''data una stringa restituisce il numero di vocali presenti'''
    #inserite qui il vostro codice
    vocali='aeiou'
    contatore=0
    for char in stringa:
        if char in vocali:
            contatore+=1
    return contatore

'''
>>> es3('ciao')
3
>>> es3('cosa')
2
>>> es3('xyz')
0
'''
########################################

def es4(stringa):
    '''data una stringa restituisce il numero di vocali presenti in posizione di indice pari'''
    #inserite qui il vostro codice
    vocali='aeiou'
    contatore=0
    for i in range(len(stringa)):
        char = stringa[i]
        if char in vocali and i%2 == 0 :
            contatore+=1
    return contatore
'''    
>>> es4('ciao')
1
>>> es4('ala')
2
>>> es4('casa')
0
>>> es4('fondamenti di informatica')
7
'''
##############################################################

def es5(stringa):
    '''data una stringa restituisce una nuova stringa in cui le vocali 
    della prima stringa sono state cancellate'''
    #inserite qui il vostro codice
    vocali='aeiou'
    result = ''
    for i in range(len(stringa)):
        char = stringa[i]
        if char not in vocali:
            result+=char
    return result    
'''
>>> es5('ciao')
'c'    
>>> es5('casa')
'cs'
>>> es5('fondamenti di programmazione')
'fndmnt d prgrmmzn' 
'''   
##############################################################

def es6(stringa):
    '''data una stringa restituisce True se le lettere della stringa compaiono in ordine alfabetico'''
    #inserite qui il vostro codice
    sorted_string = ''.join(sorted(stringa))
    print(sorted_string)
    if sorted_string == stringa:
        return True
    else:
        return False

'''    
>>> es6('acccdeq')
True
>>> es6('dhjkoav')
False
>>> es6('Amo')
True
'''
###################################################

def es7(s1,s2):
    '''ritorna True se una delle due stringhe si puo' ottenere dall'altra tramite rotazione.
    Ad esempio le stringhe che si possono ottenere da 'angelo' per rotazione sono:
    angelo
    ngeloa
    geloan
    eloang
    loange
    oangel
    '''
    #inserite qui il vostro codice
    for i in range(len(s1)):
        char_appoggio = s1[0]
        rotated_string = s1[1:]+char_appoggio
        print(rotated_string)
        s1=rotated_string
        if rotated_string == s2:
            return True
    return False
        

'''
>>> es7('angelo','geloan')
True
>>> es7('angelo','laonge')
False
>>> es7('casa','casa')
True
'''
###################################################

def es8(stringa):
    '''data una stringa restituisce la stringa al contrario'''
    #inserite qui il vostro codice
    result_string=''
    counter = len(stringa)-1
    for i in range(len(stringa)):
        result_string+= stringa[counter]
        counter-=1
    return result_string
        

'''    
>>> es8('ciao')
'oaic'
>>> es8('Monti')
'itnoM'
>>> es8('Fondamenti di programmazione')
'enoizammargorp id itnemadnoF'
'''
####################################################

def es9(stringa):
    '''scrivere un programma che presa una stringa numerica restituisce una nuova stringa in cui 
    ogni carattere della stringa originaria risulta sostituito da un numero di caratteri 
    pari alla cifra che rappresenta''' 
    #inserite qui il vostro codice
    result_string = ''
    for char in stringa:
        if char is not '0':
            numero = int(char)
            result_string+=char*numero
    return result_string

''' 
>>> es9('3')
'333'
>>> es9('100')
'1'
>>> es9('23015')
'22333155555'
'''
####################################################

def es10(n):
    '''dato l'intero n 
    restituisce una stringa contenente le cifre dell'intero 
    in verticale, una cifra per riga, con la  cifra  delle unita' 
    alla riga piu' in basso.
    Es: es(2090) torna la stringa    
2
0
9
0
'''
    #inserite qui il vostro codice
    string_value = str(n)
    for num_char in string_value:
        print(num_char)

'''
>>> s=es10(124)
>>> print(s)
1
2
4
>>> s=es10(2090)
>>> print(s)
2
0
9
0
'''
####################################################

def es11(stringa):
    # character: o  found in the next positions [15, 24]
    # fondamenti di programmazione
    '''data una stringa stampa le sottostringhe di almeno due caratteri che iniziano e 
    finiscono con lo stesso carattere'''
    #inserite qui il vostro codice
    for current_index,current_char in enumerate(stringa):
        # find all positions of the current char
       position_list = [position for position, char in enumerate(stringa) if char == current_char and position != current_index]
       #print("character:",current_char," found in the next positions",position_list)
       for current_char_next_position in position_list:
           result_string = stringa[current_index:current_char_next_position+1].strip(" ")
           if len(result_string)>=2:
               print(result_string)
'''
>>>es11('casa')
asa
>>> es11('fondamenti di programmazione')
ondamenti di pro
ondamenti di programmazio
ndamen
ndamenti di programmazion
damenti d
amenti di progra
amenti di programma
menti di program
menti di programm
enti di programmazione
nti di programmazion
i di
i di programmazi
 di 
i programmazi
rogr
ogrammazio
amma
mm
'''
####################################################





