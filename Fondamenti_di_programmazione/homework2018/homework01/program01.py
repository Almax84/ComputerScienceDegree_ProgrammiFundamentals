''' 
Sono stati appena corretti i compiti di N studenti ed in una lista sono riportati
i voti ottenuti dai vari studenti.
Sia C il voto massimo assegnato (questo significa che i voti sono interi da 0 a C compresi).
Bisona stabilire una soglia tra 0 e C a partire dalla quale gli studenti verranno ammessi all'orale.
(ovvero vengono ammessi tutti quelli con voti maggiori o uguali alla soglia)
Non volendo essere ne' troppo severo ne' troppo generoso nella valutazione, il docente, prima di scegliere la soglia,
decide di generare per ognuna delle possibili C+1 soglie (da 0 a C compreso)
il numero di studenti che verrebbero ammessi all'orale per quella soglia.
Definire una funzione es1(voti) che, data lista non vuota 'voti'  con i voti degli studenti,
restituisce la lista di C+1 interi dove in posizione i si trova  il numero di studenti ammessi
all'orale nel caso la soglia venga fissata al valore i.
ATTENZIONE: la lista ls dei voti al termine della funzione NON DEVE risultare modificata.
Ad esempio per voti=[7,5,8,3,7,2,9] la funzione es2 restituisce la lista
[7, 7, 7, 6, 5, 5, 4, 4, 2, 1]

voti=[7,5,8,3,7,2,9]
voto = 7

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 (ad esempio editatelo dentro Spyder)
'''


def es1(voti):
    # inserite qui il vostro codice
    sorted_voti = sorted(voti)

    return_list = []
    i = 0
    voto_massimo_assegnato = sorted_voti[len(sorted_voti)-1]
    # i ->  voto di riferimento, nonché indice della lista di ritorno
    # voto -> voto singolo studente
    while i < voto_massimo_assegnato+1:
        contatore_studenti_ammessi = 0
        min_value = 0 #valore di riferimento -> butto via la coda sinistra dell'array a partire dal valore minore
        for j, voto in enumerate(sorted_voti):
            if voto >= i:
                contatore_studenti_ammessi = len(sorted_voti[j:])
                break
            else:
                min_value = j
        sorted_voti = sorted_voti[min_value:]
        i += 1
        
        return_list.append(contatore_studenti_ammessi)
            
    return return_list

