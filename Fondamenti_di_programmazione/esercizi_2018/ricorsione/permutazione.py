'''
################################################################################

1. countf(path) che preso in input il percorso path di un file o directory ritorna
    il numero di totale di
   file contenuti a qualsiasi livello nella directory (se è una directory). Esempi
>>> countf('Informatica')					ritorna 27
>>> countf('Informatica/Software')				ritorna 19
>>> countf('Informatica/Hardware/Architetture/cache.txt')	ritorna  1
'''
################################################################################
import os
import rtrace
def countf(path):
    listdir = os.listdir(path)
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








if __name__ == "__main__":
    countf = rtrace.trace(countf)
    countf.trace("Informatica")

'''



2. maxlev(path) che preso in input il percorso path di un file o directory ritorna il massimo livello
   dell'albero dei file e directory contenute nella directory (se è una directory). 
   Esempi

>>> maxlev('Informatica')					ritorna 7
>>> maxlev('Informatica/Teoria')				ritorna 0	(non esiste)
>>> maxlev('Informatica/Hardware')				ritorna 6
>>> maxlev('Informatica/Software/SistemiOperativi/Linux.txt')	ritorna 1

################################################################################

3. permute_d(seq) ritorna una lista di tutte le permutazioni della sequenza seq , senza duplicati. 
   Esempio
>>> permutazioni('ala')		ritorna ['ala', 'aal', 'laa', 'laa', 'aal', 'ala']
>>> permute_d('ala')		ritorna ['ala', 'aal', 'laa']

################################################################################

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