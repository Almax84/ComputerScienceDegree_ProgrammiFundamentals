# -*- coding: utf-8 -*-
"""
NOTA: La descrizione è lunga ma il compito non è difficile, è solo lungo da spiegare con precisione.


Bisogna definire tre Classi (Attore, Film e Regista) con i relativi attributi e
metodi per realizzare una videoteca di film, i cui dati sono memorizzati in file
di tipo json che hanno la struttura come nei file di esempio "actors.json" e
"films.json". Le specifiche delle tre classi sono illustrate più avanti.
Bisogna implementare inoltre due funzioni che leggono i file json ed istanziano gli Attori, Film e Registi.

FUNZIONI DA IMPLEMENTARE

Per costruire l'elenco delle istanza di Attore, Film e Regista a partire dai due file
"actors.json" e "films.json" dovete realizzare le seguente due funzioni.
Le classi da realizzare sono descritte dopo.

- leggi_archivio_attori(file_json)
    che legge l'archivio json fornito in input che descrive tutti gli attori
    (con lo stesso formato del file di esempio actors.json)
    e torna un dizionario catalogo_attori { nome -> oggetto di tipo Attore } in cui:
    - le chiavi sono i nomi degli attori
        (prese dal campo "NAME" del dizionario presente per ogni attore nel file json)
    - i valori sono le corrispondenti istanze di tipo Attore create col costruttore passando
        come argomento il dizionario (letto dal file json) che contiene le informazioni dell'attore.

- leggi_archivio_film(file_json, catalogo_attori)
    - che legge dal file json fornito in input che descrive tutti i film
    (con lo stesso formato del file di esempio films.json)
    - ed inoltre riceve il dizionario catalogo_attori { nome->Attore } prodotto con la funzione precedente
    e torna come risultato una coppia di dizionari ( catalogo_film, catalogo_registi )
    Il catalogo_film deve essere un dizionario { titolo -> oggetto di tipo Film } in cui:
        - le chiavi sono i titoli dei film
            (preso dal campo "TITLE" del dizionario presente per ogni film nel file json)
        - i valori sono le corrispondenti istanze di tipo Film create col costruttore passando
            come argomento il dizionario (letto dal file json) che contiene le informazioni del Film.
    Il catalogo_registi deve essere un dizionario { nome -> oggetto di tipo Regista } in cui:
        - le chiavi sono i nomi dei registi
            ( presi dal campo "DIRECTORS" dei dizionari json che descrivono i film presi dal file json)
        - i valori sono istanze del tipo Regista (di cui vedete la definizione più sotto)

    La funzione leggi_archivio_film deve fare in modo che:
    - all'interno di ciascun oggetto Film siano inseriti gli oggetti Attore in modo che:
        - ogni Film contenga gli Attori che ci hanno lavorato
        - ogni Attore contenga i Film in cui è comparso
    - all'interno di ciascun oggetto Film siano contenuti gli oggetti di tipo Regista in modo che:
        - ogni Film contenga i Registi che l'hanno diretto
        - ogni Regista contenga i Film che ha diretto

    NOTA: le istanze che rappresentano ciascun Attore, Film e Regista devono essere uniche.
        (a tal proposito sfruttate i dizionari catalogo_attori, catalogo_film e catalogo_registi
        che avete costruito / state costruendo)

CLASSI DA IMPLEMENTARE

La classe Attore rappresenta la scheda di un attore.
Al suo interno devono essere definiti tutti gli attributi di istanza che ritenete necessari
per realizzare i metodi seguenti a partire dalle informazioni json ottenute dal file actors.json
allegato (o da file json simile).

    Implementate i metodi di istanza:

    - Il costruttore della classe riceve un dizionario ottenuto dal file json actors.json (o file simile).
        Il dizionario passato come argomento contiene le informazioni relative ad un solo attore.
        Il costruttore assegna agli attributi tutti i valori necessari a partire dal dizionario json passato.
    - nome(self)        che ne torna il nome
    - vero_nome(self)   che ne torna il vero nome
    - films(self)       che torna l'insieme di oggetti Film in cui l'attore ha partecipato
    - registi(self)     che torna un set contenente le istanze di oggetti di tipo
      Regista, con cui l'attore ha girato almeno un film.
    - regista_preferito(self), che restituisce un'istanza di un oggetto Regista,
      che rappresenta il regista con cui l'attore self ha girato più film.
      In caso di pareggio, viene preso il regista il cui nome viene prima in ordine alfabetico.
    - coprotagonisti(self), che restituisce un set contenente le istanze di oggetti
      di tipo Attore, che rappresentano tutti gli attori con cui l'attore self ha girato
      almeno un film.
    - in_coppia(self, partner=None), che restituisce:
      Se il parametro partner (stringa) NON viene specificato:
        - un set di tuple: ogni tupla è del tipo (a_f, a_m, n_f),
        dove a_f e a_m sono due istanze di oggetto di tipo Attore
        (di cui una rappresenta l'attore self), di genere diverso (campo "GENDER" dei dati json)
        (a_f è femmina e a_m è maschio) ed n_f è il numero di film in cui self e il suo partner
        hanno fatto coppia (ovvero hanno girato PIU' DI UN film assieme).
      Se il parametro partner VIENE specificato (di tipo stringa), viene restituito invece
        - il set di tutti i Film (che può essere vuoto) in cui l'attore self e l'attore partner che ha quel nome
        hanno fatto coppia (ovvero hanno girato ALMENO quel film assieme).
    - luogo_preferito(self), che restituisce la stringa con il paese in cui l'attore
      self ha girato più film.
      In caso di pareggio, viene restituito il luogo che viene prima in ordine alfabetico.
      Se non esiste si torna None
    - film_durata(self, inf=0, sup=None), che restituiscela lista delle istanze
      degli oggetti di tipo Film, dei film in cui l'attore self ha recitato e che
      durano almeno inf minuti e, se sup è specificato, massimo sup minuti. La
      lista deve essere ordinata per durata dei film in ordine crescente.
      In caso di parità per titolo crescente in ordine alfabetico.
      Se nel file json sono specificate più durate per lo stesso film, usate la durata minore.
      Se nei dati json la durata non è indicata ignorate quel film.
      NOTA: per estrarre la durata dalla proprieta' "RUNTIME" dei dati json che descrivono un film
            avete il permesso di usare la libreria re per le espressioni regolari.
    - eta(self), che restituisce un intero che indica l'età dell'attore:
        - se l'anno di nascita NON è presente tornate None (e ignorate questo attore nel metodo Regista.attore_preferito)
        - se l'anno di morte NON è presente usate il 2018 come anno di riferimento
        - altrimenti tornate il numero di anni vissuti
            Es. nato: 1950 oggi: 2018 -> 69
      NOTA: per estrarre l'anno dalle proprieta' "BIRTH" e "DIED" dei dati json che descrivono un attore
            avete il permesso di usare la libreria re per le espressioni regolari.

    - tutti gli altri metodi che ritenete utili

La classe Film rappresenta la scheda di un film, costruita a partire dalle informazioni json.
Al suo interno devono essere definiti tutti gli attributi di istanza che ritenete necessari
all'implementazione dei metodi descritti.

    Implementate i metodi di istanza:
    - Il costruttore riceve come argomento un dizionario ricavato dal file films.json (o file json simile)
        che rappresenta un solo film
        ed assegna tutti i valori possibili agli attributi di istanza a partire dal dizionario json passato.
    - titolo(self)  torna il titolo del film
    - attori(self)  torna l'insieme di istanze di tipo Attore che hanno lavorato al film
    - registi(self) torna l'insieme di istanze di tipo Regista che hanno diretto il film
    - luoghi(self)  torna l'insieme di luoghi in cui è stato fatto il film (campo "COUNTRY" dei dati json)
    - durata(self)  torna la durata minima in minuti (intero) del film (campo "RUNTIME" dei dati json)
    - anno(self)    torna l'anno di produzione del film (dal campo "TITLE" dei dati json)

    - tutti gli altri metodi che ritenete utili

La classe Regista rappresenta la scheda di un regista.
Gli attributi di istanza della classe Regista sono quelli necessari ad implementare i seguenti metodi.

    Implementate i metodi di istanza:
    - Il costruttore della classe assegna il nome.
    - nome(self)    che torna il nome del regista
    - films(self)   che torna l'insieme delle istanze dei Film in cui il regista ha lavorato
    - attore_preferito(self)    che torna l'istanza di tipo Attore che ha lavorato più volte col regista
        In caso di parità si torni l'attore più giovane (vedi metodo Attore.eta())
        In caso di parità si torni l'attore di genere femminile
        In caso di parità quello col vero nome (campo "REALNAME") che viene prima in ordine alfabetico.
        Se il campo REALNAME nel dizionario json non è presente o non contiene un valore usate il campo NAME.
    - anni_di_lavoro(self)    che torna per quanti anni ha lavorato il regista
        a partire dal primo film prodotto all'ultimo compresi (vedi Film.anno())

    - tutti gli altri metodi che ritenete utili

GESTIONE DEGLI ERRORI
I test NON proporranno dati errati per cui ci aspettiamo che NON vengano mai generate eccezioni
e quindi non è necessario che controlliate la validità delle informazioni fornite ai metodi.

"""

##################################################################################################
import json, re

def leggi_archivio_attori(archivio_attori_json):
    '''legge l'archivio json fornito in input che descrive tutti gli attori
    (con lo stesso formato del file di esempio actors.json)
    e torna un dizionario catalogo_attori { nome -> oggetto di tipo Attore } in cui:
    - le chiavi sono i nomi degli attori
        (prese dal campo "NAME" del dizionario presente per ogni attore nel file json)
    - i valori sono le corrispondenti istanze di tipo Attore create col costruttore passando
        come argomento il dizionario (letto dal file json) che contiene le informazioni dell'attore.
    '''
    # inserite qui il vosto codice
    with open(archivio_attori_json,"r", encoding="utf-8") as f:
       
        #[^\x00-\x7F]
        actors_json = json.load(f)

        #regex = r'[^A-Za-z0-9\s]'
        
        catalogo_attori = dict()
        
        #find_result = regex.findall("[^\x00-\x7F]",my_json)
        #print(find_result)
        #print(my_json)
        #for key, value in my_json.items():
            #escaped_chars = re.findall(regex, key)
            #for escaped_char in escaped_chars:
                #print(escaped_char, " diventa", escaped_char.encode("unicode-escape").decode())
               #print(escaped_char)
               
        for nome, dati in actors_json.items():
            attore = Attore(dati)
            name_attore = ''.join(dati["NAME"])
            catalogo_attori[name_attore] = attore
            
        
        return catalogo_attori
            
            
        
        
        #print(my_json)
        
        



def leggi_archivio_film(archivio_film_json, catalogo_attori):
    '''- leggi_archivio_film(file_json, catalogo_attori)
    - che legge dal file json fornito in input che descrive tutti i film
    (con lo stesso formato del file di esempio films.json)
    - ed inoltre riceve il dizionario catalogo_attori { nome->Attore } prodotto con la funzione precedente
    e torna come risultato una coppia di dizionari ( catalogo_film, catalogo_registi )
    Il catalogo_film deve essere un dizionario { titolo -> oggetto di tipo Film } in cui:
        - le chiavi sono i titoli dei film
            (preso dal campo "TITLE" del dizionario presente per ogni film nel file json)
        - i valori sono le corrispondenti istanze di tipo Film create col costruttore passando
            come argomento il dizionario (letto dal file json) che contiene le informazioni del Film.
    Il catalogo_registi deve essere un dizionario { nome -> oggetto di tipo Regista } in cui:
        - le chiavi sono i nomi dei registi
            ( presi dal campo "DIRECTORS" dei dizionari json che descrivono i film presi dal file json)
        - i valori sono istanze del tipo Regista (di cui vedete la definizione più sotto)

    La funzione leggi_archivio_film deve fare in modo che:
    - all'interno di ciascun oggetto Film siano inseriti gli oggetti Attore in modo che:
        - ogni Attore contenga i Film in cui è comparso
        - ogni Film contenga gli Attori che ci hanno lavorato
    - all'interno di ciascun oggetto Film siano contenuti gli oggetti di tipo Regista in modo che:
        - ogni Film contenga i Registi che l'hanno diretto
        - ogni Regista contenga i Film che ha diretto
    '''
    # inserite qui il vosto codice
    catalogo_film = dict()
    catalogo_registi = dict()
    with  open(archivio_film_json, "r", encoding = "utf-8") as f:
        film_json = json.load(f)
        
        
        for nome_film, dati in film_json.items():
            
            directors = dati["DIRECTORS"]
            for director in directors:
                regista = Regista(director)
                regista.catalogo_attori = catalogo_attori
                regista.catalogo_film = catalogo_film
                catalogo_registi[director] = regista
                
                
            film = Film(dati)
            film.catalogo_attori(catalogo_attori)
            film.catalogo_registi = catalogo_registi
            nome_film = dati["TITLE"]
            catalogo_film[nome_film[0]] = film
    
    #setto i cataloghi per ogni istanza degli attori
    for attore_nome, istanza_attore in catalogo_attori.items():
        istanza_attore.catalogo_attori(catalogo_attori)
        istanza_attore.catalogo_registi(catalogo_registi)
        istanza_attore.catalogo_film(catalogo_film)
        
        
            

        
        
    return catalogo_film, catalogo_registi
        
        
        
        
        
##################################################################################################
# Esempio di voce json che descrive un film estratta dal file films.json
##################################################################################################
# Esempio di blocco dati json
# "'Baby' Paul Cullen": {
#     "NAME": [
#         "'Baby' Paul Cullen"
#     ],
#     "LASTFIRST": [
#         "Cullen, 'Baby' Paul"
#     ],
#     "REALNAME": [
#         "Paul Michael Cullen"
#     ],
#     "NICKNAMES": [],
#     "GENDER": [
#         "M"
#     ],
#     "BIRTH": [
#         "1962, Ireland"
#     ],
#     "DIED": [
#         "21 July 2009, Los Angeles, California, USA"
#     ]
# },

class Attore():
    
    '''
    La classe Attore rappresenta la scheda di un attore.
    Al suo interno devono essere definiti tutti gli attributi di istanza che ritenete necessari
    per realizzare i metodi seguenti a partire dalle informazioni json ottenute dal file actors.json
    allegato (o da file json simile).
    '''

    def __init__(self, data):
        '''riceve un dizionario ottenuto dal file json actors.json (o file simile).
        Il dizionario passato come argomento contiene le informazioni relative ad un solo attore.
        Il costruttore assegna agli attributi tutti i valori possibili a partire dal dizionario json passato.
        '''
        regex_anno = "[1-9][0-9][0-9][0-9]"
        for key,value in data.items():
            if key == "NAME":
                if len(value) > 0:
                    self.name = value[0]
                else:
                    self.name = ""
                    
            elif key == "LASTFIRST":
                self.last_first = value
            elif key == "REALNAME":
                if len(value) > 0:
                    self.real_name = value[0]
                else:
                    self.real_name = ""
            elif key == "NICKNAMES":
                self.nick_names = value
            elif key == "GENDER":
                if len(value) > 0:
                    self.gender = value[0]
                else:
                    self.gender = ""
            elif key == "BIRTH":
                if len(value) > 0:
                    self.birth = ''.join(value)
                else:
                    self.birth = ""
            elif key == "DIED":
                if len(value) > 0:
                    self.died = ''.join(value)
                else:
                    self.died = ""

            self.registi_occurrences = None

    def nome(self):
        '''restituisce il nome'''
        return self.name

    def genere(self):
        '''restituisce il genere'''
        return self.gender

    def vero_nome(self):
        '''restituisce il vero nome'''
        return self.real_name

    def eta(self):
        '''restituisce un intero che indica l'età dell'attore in anni:
        - se l'anno di nascita NON è presente tornate None (e ignorate questo attore nel metodo Regista.attore_preferito)
        - se l'anno di morte NON è presente usate il 2018 come anno di riferimento
        - altrimenti tornate il numero di anni vissuti
            Es. nato: 1950 oggi: 2018 -> 69
        NOTA: per estrarre l'anno dalle proprieta' "BIRTH" e "DIED" dei dati json che descrivono un attore
              avete il permesso di usare la libreria re per le espressioni regolari.
        '''
        # inserite qui il vosto codice
        regex_anno = "[1-9][0-9][0-9][0-9]"
        if self.birth == None or self.birth == '':
            return None
        if self.died == None or self.died == '':
            try:
                anno_nascita = int(re.findall(regex_anno, self.birth)[0])
            except:
                print(self.birth)
            return 2018 - anno_nascita
        else:
            
            anno_morte = int(re.findall(regex_anno, self.died)[0])
            anno_nascita = int(re.findall(regex_anno, self.birth)[0])
            return anno_morte - anno_nascita+1

    def films(self):
        '''restituisce il set di film in cui ha lavorato'''
        film_s = set()
        for film_name, film in self.catalogo_film.items():
            attori_film = film.attori()
            

                
            for  attore in attori_film:
                if attore.nome() == self.nome():
                    film_s.add(film) # -> prova con la list comprehension!
                    
                    
        return film_s
            

    def registi(self):
        '''restituisce un set contenente le istanze di oggetti di tipo Regista,
        con cui l'attore ha girato almeno un film.'''
        registi_con_cui_ha_lavorato = set()
        registi_occurrences = dict()
        for regista_nome, regista_value in self.catalogo_registi.items():
            for film_nome, film in self.catalogo_film.items():
                #se l'attore non compare nel film skippare
                if regista_nome not in film.directors:
                    continue
                
                registi_con_cui_ha_lavorato.add(regista_nome)

                if regista_nome in registi_occurrences:
                    registi_occurrences[regista_nome] = registi_occurrences[regista_nome] +1
                else:
                    registi_occurrences[regista_nome] = 1


        self.registi_occurrences = registi_occurrences


        return registi_con_cui_ha_lavorato                
            

    def regista_preferito(self):
        '''restituisce un'istanza di un oggetto Regista, che rappresenta il regista con cui l'attore
        ha girato più film.
        In caso di pareggio, viene preso il regista il cui nome viene prima in ordine alfabetico.
        '''
        if self.registi_occurrences == None:
            # this sets the attori_dict if it's none
            self.registi()

        max_value = self.registi_occurrences[max(self.registi_occurrences, key=self.registi_occurrences.get)]

        max_registi = [k for k, v in self.registi_occurrences.items() if v == max_value]

        if len(max_registi) > 1:
            max(max_registi, key=lambda x: x.nome())
        elif len(max_registi) == 1:
            return max_registi[0]
        else:
            return None

        return max(self.attori_dict, key=self.attori_dict.get)

    def coprotagonisti(self):
        '''
        restituisce un set contenente le istanze di oggetti di tipo Attore,
        che rappresentano tutti gli attori con cui l'attore self ha girato almeno un film.
        '''
        attori_coprotagonisti = set()
        for film_nome, film in self.catalogo_film.items():
            attori = film.attori()
            for attore in attori:
                if attore.nome() == self.name:
                    attori_coprotagonisti = attori_coprotagonisti | attori

        attori_coprotagonisti.remove(self)

        return attori_coprotagonisti




    def in_coppia(self, partner=None):
        '''restituisce:
          Se il parametro partner (stringa) NON viene specificato:
            - un set di tuple: ogni tupla è del tipo (a_f, a_m, n_f),
            dove a_f e a_m sono due istanze di oggetto di tipo Attore
            (di cui una rappresenta l'attore self), di genere diverso (campo "GENDER" dei dati json)
            (a_f è femmina e a_m è maschio) ed n_f è il numero di film in cui self e il suo partner
            hanno fatto coppia (ovvero hanno girato PIU' DI UN film assieme).
          Se il parametro partner VIENE specificato (di tipo stringa), viene restituito invece
            - il set di tutti i Film (che può essere vuoto) in cui l'attore self e l'attore partner che ha quel nome
            hanno fatto coppia (ovvero hanno girato ALMENO quel film assieme).
        '''
        # inserite qui il vosto codice

    def luogo_preferito(self):
        '''restituisce la stringa con il paese in cui l'attore self ha girato più film.
        In caso di pareggio, viene restituito il luogo che viene prima in ordine alfabetico.
        Se non esiste si torna None
        '''
        # inserite qui il vosto codice

    def film_durata(self, inf=0, sup=None):
        '''restituisce la lista delle istanze degli oggetti di tipo Film,
        dei film in cui l'attore self ha recitato e che durano almeno inf minuti e,
        se sup è specificato, massimo sup minuti.
        La lista deve essere ordinata per durata dei film in ordine crescente.
        In caso di parità per titolo crescente in ordine alfabetico.
        Se nel file json sono specificate più durate per lo stesso film, usate la durata minore.
        Se nei dati json la durata non è indicata ignorate quel film.
          NOTA: per estrarre la durata dalla proprieta' "RUNTIME" dei dati json che descrivono un film
                avete il permesso di usare la libreria re per le espressioni regolari.
        '''
        # inserite qui il vosto codice
    def catalogo_attori(self, catalogo_attori):
        self.catalogo_attori = catalogo_attori
    def catalogo_registi(self, catalogo_registi):
        self.catalogo_registi = catalogo_registi
    def catalogo_film(self, catalogo_film):
        self.catalogo_film = catalogo_film



class Film():
    '''
    La classe Film rappresenta la scheda di un film, costruita a partire dalle informazioni json.
    Al suo interno devono essere definiti tutti gli attributi di istanza che ritenete necessari
    all'implementazione dei metodi descritti.
    '''
    def __init__(self, data):
        '''riceve come argomento un dizionario ricavato dal file films.json (o file json simile)
            che rappresenta un solo film
            ed assegna tutti i valori possibili agli attributi di istanza a partire dal dizionario json passato.
        '''
        self.actors = data["ACTORS"] #TYPE LIST - VIVA JAVA!
        self.directors = data["DIRECTORS"] #TYPE LIST - VIVA JAVA!
        self.countries = data["COUNTRY"]
        self.runtime = ' '.join(data["RUNTIME"])
        
        title_data = data["TITLE"]
        
        if len(title_data) > 0:
            self.title = data["TITLE"][0]
        else: 
            self.title = ""
        if len(title_data) >= 1:
            self.year = data["TITLE"][1]
        else:
            self.year = ""
        

    def attori(self):
        '''torna l'insieme di istanze di tipo Attore che hanno lavorato al film'''
        attori_set = {self.catalogo_attori[attore_nome] for attore_nome in self.actors \
                      if attore_nome in self.catalogo_attori}
        return attori_set
        

    def registi(self):
        '''torna l'insieme di istanze di tipo Regista che hanno diretto il film'''
        registi_set = {self.catalogo_registi[regista_nome] for regista_nome in self.directors \
                       if regista_nome in self.catalogo_registi}
        return registi_set

    def luoghi(self):
        '''torna l'insieme di luoghi in cui è stato fatto il film (campo "COUNTRY" dei dati json)'''
        return set(self.countries)

    def durata(self):
        '''torna la durata minima in minuti (intero) del film (campo "RUNTIME" dei dati json)'''
        regex = "[0-9]+"
        runtime_string = self.runtime
        runtimes = re.findall(regex, runtime_string)
        runtime_total = 0
        for runtime in runtimes:
            runtime_total += int(runtime)
        
        return runtime
        

    def titolo(self):
        return self.title
        

    def anno(self):
        '''torna l'anno di produzione del film (dal campo "TITLE" dei dati json)'''
        return int(self.year)
    def catalogo_attori(self, catalogo_attori):
        self.catalogo_attori = catalogo_attori
    def catalogo_registi(self, catalogo_registi):
        self.catalogo_registi = catalogo_registi

##################################################################################################

class Regista:
    '''
    La classe Regista rappresenta la scheda di un regista.
    Gli attributi di istanza della classe Regista sono quelli necessari ad implementare i seguenti metodi.
    '''
    def __init__(self, nome):
        '''Il costruttore assegna il nome.'''
        self.name = nome
        self.attori_dict = None
        self.catalogo_film = None

    def films(self):
        '''torna l'insieme delle istanze dei Film in cui il regista ha lavorato'''
        films_set = set()

        if self.catalogo_film == None:
            return set()


        for film_name, film in self.catalogo_film.items():
            registi_film = film.registi()
            for regista in registi_film:
                if regista.nome() == self.name:
                    films_set.add(film)
        return films_set
                    

    def nome(self):
        '''torna il nome del regista'''
        return self.name

    def attori(self):
        '''torna l'insieme di attori che hanno lavorato col regista'''
        attori_set = set()
        attori_dict = dict()
        for film_name, film_value in self.catalogo_film.items():
            registi_film = film_value.registi()
            for regista in registi_film:
                if regista.nome() == self.name:
                    film_attori = film_value.attori()
                    for attore in film_attori:
                        attori_set.add(attore)
                        if attore in attori_dict:
                            attori_dict[attore] = attori_dict[attore] + 1
                        else:
                            attori_dict[attore] = 1
        #mappa necessaria per attore preferito                            
        self.attori_dict = attori_dict
        return attori_set


    def attore_preferito(self):

        
        if self.attori_dict == None:
            # this sets the attori_dict if it's none
            self.attori()


        max_value = self.attori_dict[max(self.attori_dict, key=self.attori_dict.get)]

        max_actors = [k for k,v in self.attori_dict.items() if v == max_value]

        if len(max_actors) > 1:
            max(max_actors, key=self.max_attore_preferito)
        elif len(max_actors) == 1:
            return max_actors[0]
        else:
            return None

        return max(self.attori_dict, key=self.attori_dict.get)
        
    def max_attore_preferito(self,attore):
        '''torna l'istanza di tipo Attore che ha lavorato più volte col regista
            In caso di parità si torni l'attore più giovane (vedi metodo Attore.eta())
            In caso di parità si torni l'attore di genere femminile
            In caso di parità quello col vero nome (campo "REALNAME") che viene prima in ordine alfabetico.
            Se il campo REALNAME nel dizionario json non è presente o non contiene un valore usate il campo NAME.
        '''


        eta_attore = attore.eta()
        gender_attore = attore.genere()
        vero_nome_attore = attore.vero_nome()

        if eta_attore != None and gender_attore != None and vero_nome_attore != None:
            return -eta_attore, -ord(gender_attore), vero_nome_attore
        if eta_attore != None and gender_attore != None:
            return -eta_attore, -ord(gender_attore)
        if eta_attore != None and vero_nome_attore != None:
            return -eta_attore, vero_nome_attore
        if gender_attore != None and vero_nome_attore != None:
            return gender_attore, vero_nome_attore

        if eta_attore != None:
            return -eta_attore
        if gender_attore != None:
            return ord(gender_attore)
        if vero_nome_attore != None:
            return vero_nome_attore





        return eta_attore, -ord(gender_attore), vero_nome_attore




    def anni_di_lavoro(self):
        set_anni = set()
        for film_name, film in self.catalogo_film.items():
            lista_registi = film.registi()
            for regista in lista_registi:
                if regista.nome() == self.name:
                    set_anni.add(film.anno())
        return max(set_anni)-min(set_anni)+1


    def catalogo_attori(self, catalogo_attori):
        self.catalogo_attori = catalogo_attori
    def catalogo_film(self, catalogo_film):
        self.catalogo_film = catalogo_film


##################################################################################################


if __name__ == '__main__':
    # inserite qui il vosto codice personale di test
    catalogo_attori = leggi_archivio_attori("actors.json")
    catalogo_film, catalogo_registi = leggi_archivio_film("films.json",catalogo_attori)
    
    kidman = catalogo_attori["Nicole Kidman"]
    
    print(kidman.coprotagonisti())
    
    
    ##attore preferito
    
    
        