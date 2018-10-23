''' Scrivere una funzione prod_list(n) che, preso l'intero n, restituisce una stringa che 
contiene nell'ordine i prodotti di n per 2, 3, 5 e 7, i prodotti compaiono nella stringa separati da una virgola ed uno spazio.
Ad esempio prod_list(1) restituisce la stringa '2, 3, 5, 7'


'''
import sys

def prod_list(n):
    prodotti=(2,3,5,7)
    result = ""
    for array_item in prodotti[:-1]:
        result+=str(array_item*n)+", "
    #last element in array treated differently
    result+=str(prodotti[-1]*n)

    return result;
    

if __name__ == "__main__":
    print(prod_list(int(sys.argv[1])))
