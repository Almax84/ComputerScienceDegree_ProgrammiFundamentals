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
    lista_parole_in_testo = find_parole_in_testo(lista,txt_copy)
    
    
    word_highest_freq = find_freq_max(lista_parole_in_testo,txt_copy)[0]
    
        
    return lista_parole_in_testo, word_highest_freq    
    


def find_parole_in_testo(lista,txt_copy):
    lista_di_parole_contenute = []
    while len(txt_copy)>0:
               
        parola = find_word_at_index_zero(lista,txt_copy)
        
            
        if parola is not None and parola not in lista_di_parole_contenute :
            lista_di_parole_contenute.append(parola)
            txt_copy = txt_copy.replace(parola,'')
            
        elif parola in lista_di_parole_contenute:
             txt_copy = txt_copy.replace(parola,'')
             
        if parola in lista:
            lista.remove(parola)
        
        
    return lista_di_parole_contenute

def find_word_at_index_zero(lista,txt_copy):
    for parola in lista:
        if txt_copy.find(parola)==0:
            return parola




def find_freq_max(lista_parole_in_testo, txt_copy):
    list_of_max_words = []
    max_val = 0;
    for  parola in lista_parole_in_testo:
        parola_count = txt_copy.count(parola)
        if parola_count > max_val:
            list_of_max_words.clear()
            list_of_max_words.append(parola)
            max_val = parola_count
        elif parola_count == max_val:
            list_of_max_words.append(parola)
            
    return sorted(list_of_max_words)

           

                    
            
            
    
   
    

    
    
        
    
    
