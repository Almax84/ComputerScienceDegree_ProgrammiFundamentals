
'''
    Considera alberi i cui nodi hanno come valore stringhe sempre composte da due caratteri. 
    Vogliamo costruire stringhe di testo che raffigurano questi alberi. Ad esempio:

                                                        60                                    
                                        ________________|________________                     
                                       |                                 |                    
                                       66                                25                   
                  _____________________|_____________________        ____|_____               
                 |                            |              |      |          |              
                 56                           58             19     96         77             
     ____________|____________           _____|_____       __|__         ______|______        
    |             |           |         |       |   |     |     |       |   |         |       
    36            33          55        67      66  05    54    50      52  42        72      
 ___|___     _____|_____     _|_     ___|___    |        _|_    |       |   |    _____|_____  
|   |   |   |   |   |   |   |   |   |   |   |   57      |   |   84      03  89  |   |   |   | 
70  99  05  28  52  80  84  79  66  48  80  16          28  86                  94  87  85  26

    Le stringhe di testo che rappresentano l'albero sono composte da un certo numero di righe tutte 
    con lo stesso numero di caratteri. Ne diamo di seguito la definizione ricorsiva 
        -Se l'albero T e' una foglia la stringa di testo e' composta da un'unica riga 
        in cui compaiono i due caratteri che corrispondono al valore  del nodo.  
        -Se l'albero T ha t figli:
         vengono prima ricorsivamente costruite le t stringhe di testo corrispondenti ai t sottoalberi.
          Le t stringhe vengono poi concatenate a formare la stringa corrispondente all'albero T. 
          L'operazione di fusione delle t stringhe avviene attraverso  i seguenti passi:  
         a) per ciascun sottoalbero la prima riga di ciascuna stringa di testo contiene il valore
            della radice del sottoalbero. Sia c la posizione nella riga della prima cifra di questo valore.
            In testa a ciascuna stringa viene inserita una nuova riga. La riga contiene 
            il simbolo '|' in posizione c e spazi in tutte altre posizioni.
         b) sia h il numero massimo di righe per le t stringhe di testo dei t sottoalberi. 
            Ad ognuna delle t stringhe vanno  aggiunte righe di soli spazi in modo che 
            tutte le stringhe risultino avere h righe. 
         c) dalle t  stringhe si ottiene poi un'unica stringa di testo T1 di h righe, 
            la stringa si ottiene concatenando le righe delle t stringhe e lasciando 
            tra ciascuna riga e la seguente  due  spazi. Piu' precisamente 
            la riga i-esima della nuova stringa e' ottenuta dalla concatenazione  delle righe 
            i-esime delle t  stringhe di testo (nel  concatenare due stringhe tra l'una e 
            l'altra vengono inseriti sempre DUE spazi).
         d) Considera la prima riga di T1. Sia a la posizione  in cui in questa riga  
            compare per la prima volta il carattere '|' 
            e sia b la posizione in cui il carattere '|' compare per l'ultima volta.
            Si costruisce una nuova riga, che conterra' un unico carattere '|' , 
            degli spazi ed eventualmente dei caratteri '_'.
            - Se a=b (questo significa che  la radice dell'albero  ha un unico figlio) 
            la nuova riga conterra' lo spazio in tutte le posizioni  tranne che 
            in posizione a dove compare il  carattere '|'.
            - Se a<b (questo significa  che la radice dell'albero ha piu' figli) 
            allora la nuova riga conterra' spazi fino alla posizione a e dalla posizione b in poi, 
            conterra' il simbolo '|' in posizione (a+b)//2 e le rimanenti posizioni 
            saranno occupate dal simbolo '_'.
            Questa nuova riga viene inserita in testa alla stringa T1. 
         e) Nella attuale prima riga di T1 sia c la posizione in cui compare il carattere '|' .
            Si crea una nuova riga che  contiene   spazi in tutte le posizioni
            tranne che nelle posizioni c e c+1 dove viene inserito il valore  della radice di T. 
            Questa nuova riga viene inserita in testa alla stringa T1.
         f) La stringa di testo T1 cosi' ottenuta dopo aver effettuato i passi a)-e) e' la stringa 
            di testo che rappresenta l'albero.
    
    Si definisca la funzione es(r) ricorsiva (o che fa uso di funzioni o metodi ricorsive/i) che:
    riceve come argomento un nodo r radice  di un  albero  (i nodi dell'albero sono di tipo  
    Albero definito nella libreria albero.py allegata ed hanno tutti come valore stringhe 
    di due caratteri) e restituisce una stringa di testo che rappresenta l'albero.

NOTA: il timeout previsto per questo esercizio è di 0.5 secondi per ciascun test.

ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder o usate Notepad++)
   
ATTENZIONE: non sono permesse altre librerie oltre a quelle già importate.
    
'''

import albero

def es2(albero1):
    sotto_alberi_della_radice = list()
    tree(albero1, sotto_alberi_della_radice)
    return sotto_alberi_della_radice



def tree(albero1, sotto_alberi_della_radice):
    NEWLINE = '\n'
    PIPE = '|'
    DUE_SPAZI = '  '
    UNO_SPAZIO = ' '
    SPAZI_TRA_PIPE = 4
    foglie_sottoalbero_t = []

    #print("radice: " + albero1.id)
    #print("lista f.s.: " + str(foglie_sottoalbero_t))
    #print("figli: \n" + str(albero1.f))

    if len(albero1.f) == 0:
        return albero1.id
    else:
        indici_foglie_sottoableri = dict()
        for i , foglia in enumerate(albero1.f):
           foglia_sottoalbero = tree(foglia, sotto_alberi_della_radice) #RICORSIONE QUI!

            # se il dict non è vuoto allora la foglia ha un suo sottoalbero

           if foglia_sottoalbero is not None:
               foglie_sottoalbero_t.append(foglia_sottoalbero)

           if len(foglia.f) > 0: # data la mappa sotto, prova a sostituire all'inindice la stringa del sottoalbero!, dopo che hai costruito la stringa a partire dalla riga 116
               # in questo modo puoi prendere la stringa sotto_alberi_della_radice[-1] e prima di sostituirla aggiungerci tutti gli spazi necessari affinche siano uguali in larghezza
               print("qui c'è un sotto albero!")
               indici_foglie_sottoableri[len(foglie_sottoalbero_t)-1] = sotto_alberi_della_radice[-1]





        radice = albero1.id

        numero_di_foglie = len(foglie_sottoalbero_t)
        stringa_foglie = ''
        for i,  foglia_t in enumerate(foglie_sottoalbero_t):

            if i < len(foglie_sottoalbero_t) - 1:
              stringa_foglie += foglia_t + DUE_SPAZI
            else:
                stringa_foglie += foglia_t
        lunghezza_massima_stringa = len(stringa_foglie)


        prima_riga_stringa_foglie = costruisci_prima_riga_foglie(PIPE, SPAZI_TRA_PIPE, UNO_SPAZIO,
                                                                 lunghezza_massima_stringa, numero_di_foglie)

        sottoalbero_t = costruisci_sottoalbero_t(NEWLINE, PIPE, UNO_SPAZIO, albero1, lunghezza_massima_stringa, numero_di_foglie,
                                 prima_riga_stringa_foglie, radice, stringa_foglie)

        #in questo caso la lista contiene la stringa del sottoalbero
        sotto_alberi_della_radice.append(sottoalbero_t)
        #in questo caso la lista contiene una sotto lista di foglie
        sotto_alberi_della_radice.append(foglie_sottoalbero_t)
        
        
        print(sottoalbero_t)



        return albero1.id



def costruisci_prima_riga_foglie(PIPE, SPAZI_TRA_PIPE, UNO_SPAZIO, lunghezza_massima_stringa, numero_di_foglie):
    prima_riga_stringa_foglie = ''.join([UNO_SPAZIO for _ in range(lunghezza_massima_stringa)])
    prima_riga_stringa_foglie = put_pipes_in_leaves(PIPE, SPAZI_TRA_PIPE, numero_di_foglie,
                                                    prima_riga_stringa_foglie)
    return prima_riga_stringa_foglie


def costruisci_sottoalbero_t(NEWLINE, PIPE, UNO_SPAZIO, albero1, lunghezza_massima_stringa, numero_di_foglie,
                             prima_riga_stringa_foglie, radice, stringa_foglie):
    stringa_foglie = prima_riga_stringa_foglie + NEWLINE + stringa_foglie
    if numero_di_foglie > 1:
        prima_riga_sottoalbero_t = ''.join([UNO_SPAZIO for _ in range(lunghezza_massima_stringa)])
        prima_riga_sottoalbero_t = prima_riga_sottoalbero_t[:len(prima_riga_sottoalbero_t) // 2 - 1] \
                                   + albero1.id \
                                   + prima_riga_sottoalbero_t[len(prima_riga_sottoalbero_t) // 2:]

        terza_riga_sottoalbero_t = ''.join(['_' for _ in range(lunghezza_massima_stringa)])
        terza_riga_sottoalbero_t = terza_riga_sottoalbero_t[:len(terza_riga_sottoalbero_t) // 2 - 1] \
                                   + PIPE \
                                   + terza_riga_sottoalbero_t[len(terza_riga_sottoalbero_t) // 2:]

        terza_riga_sottoalbero_t = ' ' + terza_riga_sottoalbero_t[1:len(terza_riga_sottoalbero_t) - 2] + ' '

        sottoalbero_t = prima_riga_sottoalbero_t + NEWLINE + terza_riga_sottoalbero_t + NEWLINE + stringa_foglie
        return sottoalbero_t

    elif numero_di_foglie == 1:
        sottoalbero_t = radice + NEWLINE + stringa_foglie
        return sottoalbero_t



def put_pipes_in_leaves(PIPE, SPAZI_TRA_PIPE, numero_di_foglie, prima_riga_stringa_foglie):
    for i in range(0, numero_di_foglie):
        prima_riga_stringa_foglie = prima_riga_stringa_foglie[:i * SPAZI_TRA_PIPE] + PIPE + prima_riga_stringa_foglie[
                                                                                            i * SPAZI_TRA_PIPE + 1:]
    return prima_riga_stringa_foglie


#'''              05
 #_____________|_____________
#|             |             |
#02            04            06
#|    _________|_________
#01  |     |     |   |   |
#    01    02    09  08  02    
#         _|_
#        |   |                 
#        03  06                '''









if __name__ == '__main__':
    lista1= ['05', [['02', [['01', []]]], ['04', [['01', []], ['02', [['03', []], ['06', []]]], ['09', []], ['08', []],['02', []]]],['06', []]]]
    print(es2(albero.fromLista1(lista1)))
    stringa1='''              05              
 _____________|_____________  
|             |             | 
02            04            06
|    _________|_________      
01  |     |     |   |   |     
    01    02    09  08  02    
         _|_                  
        |   |                 
        03  06                '''

