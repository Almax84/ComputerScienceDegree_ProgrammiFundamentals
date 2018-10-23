''' Scrivere una funzione pad_r(x,n) che, dati due interi x ed n, 
ritorna una stringa lunga  n e ed  in cui l'intero x e' giustificato a destra
e le posizioni a sinistra sono riempite con il carattere punto '.'.
Se x ha un numero di cifre superiore ad n va restituita la stringa contenente il solo numero x.

Ad esempio pad_r(5, 7) restituisce la stringa '......5'
mentre pad_r(556,2) restituisce la stringa '556'


Suggerimento: potete usare solo stringhe, con
le operazioni di concatenamento (+), ripetizione (*) e la funzione len().
Il ciclo for non e' necessario.
'''
import sys

def pad_r(x, n):
  
    result = ""
    if len(str(x)) > n:
        return x
    
    result = '.'*(n-1)+str(x)

    return result

    
if __name__ == "__main__":
    x = sys.argv[1]
    
    n = sys.argv[2]
    print('you have enetered: '+x+','+n)
    print('result: '+str(pad_r(int(x),int(n))))
