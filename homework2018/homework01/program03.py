'''
Definire una funzione es3(lista, testo) che prende:
- una lista di parole (nessuna delle quali e' prefisso dell'altra)
- una stringa di testo. Il testo e' stato ottenuto concatenando alcune
  delle parole presenti nella lista 'lista'
  (una stessa parola puo' comparire piu' volte nella stringa di testo).
- restituisce una coppia (tupla) formata da:
        - la lista delle parole che, concatenate producono il testo
        - la parola che vi occorre piu' spesso
  (se questa parola non e' unica allora viene restituita quella che precede le altre lessicograficamente).
  Nella lista di output ogni parola appare una sola volta e le parole
  risultano ordinate in base alla loro prima apparizione nella concatenazione che produce il testo
  (i.e. quella che compare per prima al primo posto ecc.ecc.)
  Infine al termine della funzione la lista 'lista' deve risultare modificata come segue:
  in essa saranno state cancellate tutte le parole utilizzate in testo, e tornate come risultato.
  Ad esempio: se lista=['gatto','cane','topo']
  - con  testo='topogattotopotopogattogatto' la risposta e' la coppia (['topo','gatto'],'gatto')
    e lista diviene ['cane']
  se lista=['ala','cena','elica','nave','luce','lana','vela']
  - con testo='lucenavelanavelanaveelica' la risposta e' (['luce','nave','lana','vela','elica'],'nave')
  e ls diviene ['ala','cena']

NOTA: il timeout previsto per questo esercizio è di 5 secondi per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 (ad esempio editatelo dentro Spyder)



input:
    -lista di parole (nessuda delle quali è prefisso dell'altra)
    -stringa di testo -> ottenuta concatenando ALCUNE delle parole nella lista
output:
    tupla con 2 elementi contenente:
        1. lista di parole che concatenate producono il testo -> parole ordinate
        2. la parola con maggior frequenza
    la lista di input sarà modificata :
        1. cancellando le parole utilizzate nel testo

'''
def es3(lista, testo):
    txt_copy = testo
    lista_di_parole_contenute = []
    
    for parola in lista:
        parola_da_comporre= ''
        start_index = txt_copy.find(parola)
        if start_index >= 0 :
            for i in range(start_index, len(testo)):
                c = testo[i]
                if c in parola and parola_da_comporre != parola:
                    parola_da_comporre+=c
                elif parola_da_comporre == parola:
                    lista_di_parole_contenute.append(parola)
                    
        return lista_di_parole_contenute


print(es3(["io","sono","ciccio","pasticcio"],"pasticciociccioiosonociccioiopasticciosono"))
                    
            
            
    
   
    

    
    
        
    
    
