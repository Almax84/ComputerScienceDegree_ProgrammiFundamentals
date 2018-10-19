'''
Abbiamo n pulsanti numerati da 1 a N ed N lampadine anch'esse numerate da 1 a N.
Il generico pulsante x cambia lo stato (da accesa a spenta o viceversa) della lampadina x 
e di tutte le lampadine il cui numero identificativo e' un divisore di x.
Ad esempio il pulsante 18 cambia lo stato delle lampadine 1,2,3,6,9,18.
Ogni pulsante puo' essere premuto al massimo una volta e i pulsanti vanno premuti 
in ordine crescente (una volta premuto il pulsante x  non e' piu' possibile premere 
i pulsanti da 1 a x-1).
Sapendo N e l'insieme 'accese' delle lampadine al momento accese
bisogna individuare la sequenza crescente di bottoni da premere perche'
tutte le lampadine risultino accese.
Definire una funzione es2(N, accese) che dati:
- il numero N di lampadine
- l'insieme 'accese' contenente gli identificativi delle lampadine al momento accese
determina e restituisce la lista contenente nell'ordine i pulsanti da premere perche' 
le N lampadine risultino tutte accese.
Ad esempio per N=6 e accese={2,4} es2(N, accese) restituisce la lista [2,5,6] infatti:
-all'inizio sono accese le lampadine {2,4}
-dopo aver premuto il pulsante 2 saranno accese le lampadine {1,4}
-dopo aver premuto il pulsante 5 saranno accese le lampadine {4,5}
-dopo aver premuto il pulsante 6 saranno accese le lampadine {1,2,3,4,5,6}

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 (ad esempio editatelo dentro Spyder)

dati:
    #lista di pulsanti da 1 ad N
    #lista di lampadine da 1 ad N
    #il pulsante x cambia lo stato (on off) di tutte le lampadine divisore di x
    #un pulsante può essere premuto una sola volta
    #i pulsanti vanno premuti in ordine crescente
    #N = lista pulsanti
    #accese = insieme delle lampadine al momento accese
    #bisogna restituire la lista contenente ordinati, i pulsanti da premere affinché
    tutte le N lampadine risultino accese

'''
def es2(N, ins):
    # 0 False
    # != 0 True

    mappa_lampadine = {}
    return_set = set()    
    for i in range(1,N+1) :
        
        bool_value = i in ins
        
        mappa_lampadine[i] = bool_value
        
    
    
    for i in range(N,0,-1):
        for key,value in mappa_lampadine.items():
            
            if  mappa_lampadine[i] != True and i % key == 0:
                
                mappa_lampadine[key] = not value
                return_set.add(i)
                print(i,key,value, mappa_lampadine)
        
        mappa_lampadine.pop(i)
                
                
    return sorted(list(return_set))
               
  
    
    
 
    
    
    # risposta [2,5,6] -> saltati i bottoni 1,3,4
    # [1,2,3,4,5,6]
    
'''
stato iniziale
      {1: False, 2: True, 3: False, 4: True, 5: False, 6: False}
6 - > {1: True, 2: False, 3: True, 4: True, 5: False, 6: True}

5 - > {1: False, 2: False, 3: True, 4: True, 5: True, 6: True}

4 -> salto perchè già acceso?
3 -> salto perchè già acceso?

2 - > {1: True, 2: True, 3: True, 4: True, 5: True, 6: True}


    
'''
    
    
print(es2(6,[2,4]))