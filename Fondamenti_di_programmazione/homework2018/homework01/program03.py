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

    lista_parole_in_testo, list_of_max_words = find_parole_in_testo(lista,testo)
    word_highest_freq = ''

    if len(list_of_max_words)>0:
        word_highest_freq = list_of_max_words[0]
        
    return lista_parole_in_testo, word_highest_freq    
    


def find_parole_in_testo(lista,testo):
    lista_di_parole_contenute = []
    list_of_max_words = []
    max_val = 0;
    
    while len(testo)>0:
               
        parola = find_word_at_index_zero(lista,testo)
        
         
        if parola is None:
            break
        
        
        parola_count = testo.count(parola)
        if parola_count > max_val:
            list_of_max_words.clear()
            list_of_max_words.append(parola)
            max_val = parola_count
        elif parola_count == max_val:
            list_of_max_words.append(parola)

        
        if parola not in lista_di_parole_contenute :
            lista_di_parole_contenute.append(parola)
            testo = testo.replace(parola,'')
            
        elif parola in lista_di_parole_contenute:
             testo = testo.replace(parola,'')
             
        if parola in lista:
            lista.remove(parola)

        
    list_of_max_words.sort()
    return lista_di_parole_contenute,list_of_max_words

def find_word_at_index_zero(lista,testo):
    for parola in lista:
        if testo.find(parola)==0:
            return parola


            
    
   
    

    
    
        
    
    
