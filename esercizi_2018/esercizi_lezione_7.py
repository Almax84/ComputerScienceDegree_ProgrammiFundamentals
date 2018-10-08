## ESERCIZI
'''
Usando la list comprehension definite le seguenti funzioni:

1. Definite la funzione triangolo(N) che torna una matrice triangolare di N*N/2 elementi, 
   contenente solo la parte in basso a sinistra della matrice dei prodotti (tabelline).
   Il risultato quindi dev'essere una lista di N liste di lunghezza crescente da 1 a N.
   Esempio:
>>> triangolo(4)
[[1],
 [2, 4],
 [3, 6, 9],
 [4, 8, 12, 16]] 

2. Definite la funzione potenze_crescenti(lista) che produce come risultato una lista
   in cui ciascun elemento è ottenuto come la potenza i-esima del corrispondente elemento
   in posizione i della lista passata come argomento.
   Esempio:
>>> potenze_crescenti([2, 3, 4, 5, 6])
[1, 3, 16, 125, 1296]

3. Definite la funzione non_divisibili(N, divisori) che trova tutti i numeri tra 1 e N (compresi)
   che non sono divisibili per nessuno dei valori presenti nella lista di divisori (interi).
   Esempio:
>>> non_divisibili(10, [2, 3])
[1, 5, 7]


4.  Definite la funzione doppio_dado() che stampa una successione di estrazioni casuali di due dadi a 6 facce 
    e che conta e torna come risultato quante ne sono state necessarie prima di ottenere un doppio 6.
    Esempio:
>>> doppio_dado()
3 5
2 2
1 6
6 4
3 1
5 4
6 6
7

################################################################################
'''
def doppio_dado():
    '''
    4.  Definite la funzione doppio_dado() che stampa una successione di estrazioni casuali di due dadi a 6 facce 
    e che conta e torna come risultato quante ne sono state necessarie prima di ottenere un doppio 6.
    Esempio:
>>> doppio_dado()
3 5
2 2
1 6
6 4
3 1
5 4
6 6
7

    '''
    import random
    random.seed(10000000)
    isTrue = True
    contatore = 0
    while isTrue:
        contatore+=1
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        print(num1, " ", num2)
        if num1 == 6 & num2 == 6:
            isTrue = False
    return contatore
        
    
    
    
print(doppio_dado())



def non_divisibili(N,divisori):
    '''
     Definite la funzione non_divisibili(N, divisori) che trova tutti i numeri tra 1 e N (compresi)
   che non sono divisibili per nessuno dei valori presenti nella lista di divisori (interi).
       
   Si richiede che, dato un N, di trovare tutti i numeri da 1 ad N compresi che diano n % divisore != 0
   per qualunque divisore in divisori
   
   
    '''
    
    
    #Costruisco la lista da 1 ad N

    
    #Creo una lista contenente tutti i valori di n tali che se divisi per divisore diano resto 0
    divisori_list =  [n for n in range(1,N+1) for divisore in divisori if n%divisore==0]

    #creo una terza lista con tutti i valori da 1 ad N che non siano presenti in divisori_list
    return [ n for n in range(1,N+1) if n not in divisori_list   ]
 
    

    
 #print(non_divisibili(10, [2, 3]))
        



# 2)

def potenze_crescenti(lst):
    
    return_list = [lst[index]**index for index in range(len(lst))]
    #print(return_list)
    return return_list
    
potenze_crescenti([2,3,4,5,6])  
    

# 1)
def triangolo(intero):
    return_list = [[0]*x for x in range(1,intero+1)]
    
    return_list=[[i*j for j,column in enumerate(row,1)] for i,row in enumerate(return_list,1)]
    
    #print(return_list)
    return return_list        
