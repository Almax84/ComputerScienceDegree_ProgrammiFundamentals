'''
################################################################################

1. countf(path) che preso in input il percorso path di un file o directory ritorna
    il numero di totale di
   file contenuti a qualsiasi livello nella directory (se è una directory). Esempi

# >>> countf('Informatica')					ritorna 27
# >>> countf('Informatica/Software')				ritorna 19
# >>> countf('Informatica/Hardware/Architetture/cache.txt')	ritorna  1
'''
################################################################################
import os
import rtrace
import unittest
def countf(path):
    if os.path.isdir(path):
        listdir = os.listdir(path)
    else:
        return 1
    count = 0
    for name in listdir:
        pathname = os.path.join(path, name)
        if name.startswith("."):
            continue
        if os.path.isdir(pathname):
            count += countf(pathname)
        else:
            count+=1
    return count

import permutazione
class TestPrimooEsercizio(unittest.TestCase):
    def test_informatica(self):
        countf = rtrace.trace(permutazione.countf)
        self.assertEqual(countf("Informatica"),27)
    def test_informatica_software(self):
        countf = rtrace.trace(permutazione.countf)
        self.assertEqual(countf("Informatica/Software"),19)

    def test_informatica_software_cache(self):
        countf = rtrace.trace(permutazione.countf)
        self.assertEqual(countf('Informatica/Hardware/Architetture/cache.txt'),1)


if __name__ == "__main__":
    unittest.main()




'''



2. maxlev(path) che preso in input il percorso path di un file o directory ritorna
 il massimo livello
 dell'albero dei file e directory contenute nella directory (se è una directory). 
 Esempi

>>> maxlev('Informatica')					ritorna 7
>>> maxlev('Informatica/Teoria')				ritorna 0	(non esiste)
>>> maxlev('Informatica/Hardware')				ritorna 6
>>> maxlev('Informatica/Software/SistemiOperativi/Linux.txt')	ritorna 1

'''
def maxlev(path):
    count = 1
    pathname = os.path.join(path)
    if not os.path.exists(pathname):
        return 0
    if not os.path.isdir(path):
        return 1

    listdir = os.listdir(pathname)
    profondita = []
    for name in listdir:
        path_ = os.path.join(path,name)
        profondita.append( maxlev(path_))

    if profondita:
        return 1 + max( profondita )
    else:
        return 1
            
    return count

def maxlev_mio(path):
    basename = os.path.basename(path)
    if basename and basename[0] == '.' :	return 0	# se il path va ignorato
    if not os.path.exists(path):		return 0	# se il path non esiste
    if not os.path.isdir(path):			return 1	# se è un file
    profondita = []
    for filename in os.listdir(path):
        profondita.append(maxlev(os.path.join(path,filename)))
    #profondita = [ maxlev(os.path.join(path, filename)) for filename in os.listdir(path) ]
    if profondita:
        return 1 + max( profondita )
    else:
        return 1




class TestSecondoEsercizio(unittest.TestCase):
    def test_ritorno_0(self):
        self.assertEqual(maxlev("Informatica/Teoria"),0)
        
    def test_ritorno_7(self):
        self.assertEqual(maxlev("Informatica"),7)
    def test_ritorno_6(self):
        self.assertEqual(maxlev("Informatica/Hardware"),6)
    def test_ritorno_1(self):
        self.assertEqual(maxlev("Informatica/Software/SistemiOperativi/Linux.txt"),1)

    
if __name__ == "__main__":
    unittest.main()

'''
################################################################################

3. permute_d(seq) ritorna una lista di tutte le permutazioni della sequenza seq , senza duplicati. 
   Esempio
>>> permutazioni('ala')		ritorna ['ala', 'aal', 'laa', 'laa', 'aal', 'ala']
>>> permute_d('ala')		ritorna ['ala', 'aal', 'laa']

################################################################################

'''

def permute_d(seq):
    
    if len(seq) == 1:
        return [seq]
    
    
    return_list = []
    for i in range(len(seq)):
        X = seq[i:i+1]
        seq_remainder = seq[:i] + seq[i+1:]

        sotto_permutazioni = permute_d(seq_remainder)

        for arr in sotto_permutazioni:
            # if type(arr) != list:
            #     arr = [arr]

            x_arr = X + arr
            if x_arr not in return_list:
                return_list.append(x_arr)

    return return_list


'''
4. change(r, coins) ritorna il numero di combinazioni diverse di dare il resto r con i valori delle
   monete nella lista coins . Si assume che coins contenga sempre il valore 1 e che sia ordinata in senso
   crescente. 
   Esempi
>>> change(8, [1, 5])			ritorna 2 infatti abbiamo 1+1+1+1+1+1+1+1 e 1+1+1+5
>>> change(15, [1, 5, 10])		ritorna 6
>>> change(100, [1, 5, 10, 20, 50])	ritorna 343

Suggerimento: conviene contare le combinazioni "generandole" con i valori ordinati in senso crescente 
(per evitare di contare due volte la stessa combinazione); generare tutte quelle che iniziano con il primo
valore, poi quelle che iniziano con il secondo valore e così via.

'''
def change(r, coins):

    if len(coins) == 1:
        return coins[0]
    coins.sort()

    return_list = []
    for i in range(len(coins)):
        count = 0
        X = coins[i]
        while count < r:
            count += X + change(r, [X])
        if count == r:
            return_list.append(1)
        else:
            pass



    for i in range(len(coins)):
        count = 0
        X = coins[i]
        seq_remainder = coins[:i] + coins[i + 1:]
        while count < r:
            count += X + change(r, seq_remainder)
        if count == r:
            return_list.append(1)
        else:
            return 0




    return len(return_list)



print("change ", change(8, [1,5]))



'''
################################################################################

5. node_fstree(root, path) ritorna il nodo dell'albero di radice tree (di tipo FSNode ) che ha il path
   uguale a quello di input. Se non c'è, ritorna None . 
   Esempi
>>> tree = gen_fstree('Informatica')
>>> node_fstree(tree, 'Informatica')
FSNode("Informatica", False)
>>> node_fstree(tree, 'Informatica/Hardware/Architetture')
FSNode("Informatica/Hardware/Architetture", False)
>>> print(repr(node_fstree(tree, 'Informatica/Software/Android')))
None

################################################################################

6. file_fstree(root) ritorna una lista contenente i percorsi di tutti i file (no directory) contenuti
   nell'albero di radice root (di tipo FSNode ). 
   Esempio
>>> tree = gen_fstree('Informatica')
>>> subtree = node_fstree(tree, 'Informatica/Hardware')
>>> file_fstree(subtree)
['Informatica/Hardware/Architetture/cache.txt',
'Informatica/Hardware/Architetture/memorie.txt',
'Informatica/Hardware/Architetture/Processori/CISC/x86/AMD_Phenom.txt',
'Informatica/Hardware/Architetture/Processori/CISC/x86/Intel_Haswell.txt',
'Informatica/Hardware/Architetture/Processori/CISC/x86/Pentium4.txt',
'Informatica/Hardware/Architetture/Processori/RISC/ARM.txt',
'Informatica/Hardware/Architetture/Processori/RISC/MIPS.txt',
'Informatica/Hardware/Architetture/storia.txt']

################################################################################

7. size_fstree(root) ritorna un dizionario che associa ad ogni percorso di directory nell'albero di radice
   root (di tipo FSNode ) il numero di nodi del suo sottoalbero (cioè il numero di directory e file contenuti
   a qualsiasi livello nella directory). Se il nodo root rappresenta un file, ritorna un dizionario vuoto.
   Esempio
>>> tree = gen_fstree('Informatica')
>>> size_fstree(tree)
{'Informatica': 40,
 'Informatica/Hardware': 13,
 'Informatica/Hardware/Architetture': 12,
 'Informatica/Hardware/Architetture/Processori': 8,
 'Informatica/Hardware/Architetture/Processori/CISC': 4,
 'Informatica/Hardware/Architetture/Processori/CISC/x86': 3,
 'Informatica/Hardware/Architetture/Processori/RISC': 2,
 'Informatica/Software': 25,
 'Informatica/Software/Linguaggi': 17,
 'Informatica/Software/Linguaggi/Imperativi': 4,
 'Informatica/Software/Linguaggi/OO': 5,
 'Informatica/Software/Linguaggi/Funzionali': 4,
 'Informatica/Software/SistemiOperativi': 5,
 'Informatica/Software/BasiDati': 0}

################################################################################

'''