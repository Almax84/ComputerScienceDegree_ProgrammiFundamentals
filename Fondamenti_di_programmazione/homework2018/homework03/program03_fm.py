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
    - film_durata(self, inf=0, sup=None), che restituisce la lista delle istanze
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

patternDigit = re.compile(r'\d+')


def getFirstElement(lst):
    if not lst:
        return ''
    else:
        return lst[0]


def takeSecond(elem):
        return elem[1][1]


def takeFirst(elem):
        return elem[0]

    
def leggi_archivio_attori(archivio_attori_json):
    '''legge l'archivio json fornito in input che descrive tutti gli attori
    (con lo stesso formato del file di esempio actors.json)
    e torna un dizionario catalogo_attori { nome -> oggetto di tipo Attore } in cui:
    - le chiavi sono i nomi degli attori
        (prese dal campo "NAME" del dizionario presente per ogni attore nel file json)
    - i valori sono le corrispondenti istanze di tipo Attore create col costruttore passando
        come argomento il dizionario (letto dal file json) che contiene le informazioni dell'attore.
    '''
    dizionarioAttori = {}
    # inserite qui il vosto codice
    with open(archivio_attori_json) as f:
        data = json.load(f)
    for key, value in data.items():
        nome = value['NAME'][0]
        dizionarioAttori[nome] = Attore(value)
    
    return dizionarioAttori
    

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
    catalogo_film = {}
    catalogo_registi = {}
    with open(archivio_film_json) as f:
        data = json.load(f)
    for key, value in data.items():
        
        titolo = value['TITLE'][0]
        currentFilm = Film(value)
        catalogo_film[titolo] = currentFilm
        
        # Attori
        listaAttori = value['ACTORS']
        creaBiiezioneAttoreFilm(currentFilm, listaAttori, catalogo_attori)
        
        # Directors
        registiList = value['DIRECTORS']
        for nomeRegista in registiList:
            if nomeRegista in catalogo_registi:
                registaObj = catalogo_registi[nomeRegista]
            else:
                registaObj = Regista(nomeRegista)
            catalogo_registi[nomeRegista] = registaObj
            creaBiiezioneRegistaFilm(currentFilm, nomeRegista, registaObj)

    return (catalogo_film, catalogo_registi)


def creaBiiezioneAttoreFilm(film, listaAttori, catalogoAttori):
    for nomeAttore in listaAttori:
        # cerco attore dal catalogo
        attoreObj = catalogoAttori[nomeAttore]
        # assegno l'attore al film
        film.dizionarioAttori[attoreObj.name] = attoreObj
        
    # faccio 2 cicli per i coprotagonisti
    for nomeAttore, attore in film.dizionarioAttori.items():
        # assegno il film all'attore
        attore.aggiungiFilm(film)
        
    return


def creaBiiezioneRegistaFilm(film, nomeRegista, registaObj):
    # associo regista al film
    film.dizionarioRegistri[nomeRegista] = registaObj
    # assegno film al regista
    registaObj.aggiungiFilm(film)
    
    # assegno ad ogni attore del film il regista
    for nome, attoreObj in film.dizionarioAttori.items():
        attoreObj.aggiungiRegista(registaObj)
    return


def calcolaAge(birth, died):
    birthYear = extractYear(birth)
    diedYear = extractYear(died)
     
    if not birthYear:
        return None
    if not diedYear:
        diedYear = 2018
    
    return diedYear - birthYear + 1

            
def extractYear(date):
    if date:
        # pattern = re.compile(r'\d+')
        patternMatch = patternDigit.findall(date)
        if len(patternMatch) == 1:
            return int(patternMatch[0])
        elif len(patternMatch) == 2:
            return int(patternMatch[1])
        
    return None
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
        # inserite qui il vosto codice
        self.name = getFirstElement(data['NAME'])
        self.surname = getFirstElement(data['LASTFIRST'])
        self.realName = getFirstElement(data['REALNAME'])
        # self.nickname = getFirstElement(data['NICKNAMES'])
        self.gender = getFirstElement(data['GENDER'])
        self.birth = getFirstElement(data['BIRTH'])
        self.died = getFirstElement(data['DIED'])
        self.dizionarioFilm = {}
        self.dizionarioRegisti = {}
        self.dizionarioRegistiContatore = {}
        self.dizionarioCoprotagonisti = {}
        self.age = calcolaAge(self.birth, self.died)
        
    def nome(self):
        '''restituisce il nome'''
        # inserite qui il vosto codice
        return self.name

    def genere(self):
        '''restituisce il genere'''
        # inserite qui il vosto codice
        return self.gender

    def vero_nome(self):
        '''restituisce il vero nome'''
        # inserite qui il vosto codice
        return self.realName

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
        return self.age

    def films(self):
        '''restituisce il set di film in cui ha lavorato'''
        # inserite qui il vosto codice
        return set(self.dizionarioFilm.values())

    def aggiungiFilm(self, film):
        # aggiungi film 
        self.dizionarioFilm[film.title] = film
        # aggiungo attori Coprotagonisti
        for nome, attore in film.dizionarioAttori.items():
            if(nome != self.name):
                if nome not in self.dizionarioCoprotagonisti:
                    self.dizionarioCoprotagonisti[nome] = (attore, 1)
                else:
                    partecipazioni = self.dizionarioCoprotagonisti[nome][1]
                    self.dizionarioCoprotagonisti[nome] = (attore, partecipazioni + 1)
        
    def aggiungiRegista(self, regista):
        self.dizionarioRegisti[regista.name] = regista
        if regista.name in self.dizionarioRegistiContatore:
            self.dizionarioRegistiContatore[regista.name] = (regista, self.dizionarioRegistiContatore[regista.name][1] + 1)
        else :
            self.dizionarioRegistiContatore[regista.name] = (regista, 1)
        
    def registi(self):
        '''restituisce un set contenente le istanze di oggetti di tipo Regista,
        con cui l'attore ha girato almeno un film.'''
        # inserite qui il vosto codice
        return set(self.dizionarioRegisti.values())

    def regista_preferito(self):
        '''restituisce un'istanza di un oggetto Regista, che rappresenta il regista con cui l'attore
        ha girato più film.
        In caso di pareggio, viene preso il regista il cui nome viene prima in ordine alfabetico.
        '''
        # inserite qui il vosto codice
        orderedList = list(self.dizionarioRegistiContatore.items())
        
        if not orderedList:
            return None
        orderedList.sort(reverse=True, key=takeSecond)
        maxValue = orderedList[0][1][1]
        registiPreferiti = []
        for regNum in orderedList:
            if regNum[1][1] == maxValue:
                registiPreferiti.append(regNum)
            else:
                break
        registiPreferiti.sort()
        return registiPreferiti[0][1][0]
    
    def coprotagonisti(self):
        '''
        restituisce un set contenente le istanze di oggetti di tipo Attore,
        che rappresentano tutti gli attori con cui l'attore self ha girato almeno un film.
        '''
        # inserite qui il vosto codice
        return set(map(lambda x: x[0], set(self.dizionarioCoprotagonisti.values())))

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
        if partner is None:
            if self.gender == 'M':
                a_m = self
                partnerList = self.lookingForGenderPartner('F')
                if not partnerList:
                    return set([])
                return set(map(lambda x: (a_m, x[0], x[1]), partnerList))
            else:
                a_f = self
                partnerList = self.lookingForGenderPartner('M')
                if not partnerList:
                    return set([])
                return set(map(lambda x: (x[0], a_f, x[1]), partnerList))
        else:
            if partner in self.dizionarioCoprotagonisti:
                # se il partner ha lavorto insieme a self
                partnerFilmList = self.dizionarioCoprotagonisti[partner][0].dizionarioFilm
                if not partnerFilmList:
                    return set([])
                else:
                    selfList = list(self.dizionarioFilm.items())
                    if not partnerFilmList:
                        return set([])
                    partnerFilmListFiltered = list(filter(lambda x: x[0] in partnerFilmList, selfList))
                    return set(map(lambda x: x[1], partnerFilmListFiltered))
            else:
                return set([])
                
    def lookingForGenderPartner(self, gender):
        partnerList = []
        for nome, coprotagonistaTupla in self.dizionarioCoprotagonisti.items():
            if coprotagonistaTupla[0].gender == gender and coprotagonistaTupla[1] > 1:
                partnerList.append(coprotagonistaTupla)
        
        return partnerList
        
    def luogo_preferito(self):
        '''restituisce la stringa con il paese in cui l'attore self ha girato più film.
        In caso di pareggio, viene restituito il luogo che viene prima in ordine alfabetico.
        Se non esiste si torna None
        '''
        countryDic = {}
        maxCountryPresence = 0
        for film in self.dizionarioFilm.values():
            for country in film.country:
                presence = 0
                if country in countryDic:
                    presence = countryDic[country]
                countryDic[country] = presence + 1
                if presence + 1 > maxCountryPresence:
                    maxCountryPresence = presence + 1
        
        countryList = countryDic.items()
        if not countryList or len(countryList) == 0:
            return None
        # revert, chiave l'occorrenza e valore il nome del luogo, in questo modo sfruttiamo l'ordine naturale delle tuple
        countryList = list(filter(lambda x: x [1] == maxCountryPresence, countryList))
        countryList.sort()
        return countryList[0][0]
            
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
        outputList = []
        for name, film in self.dizionarioFilm.items():
            if not film.runtimeMin or film.runtimeMin < inf:
                continue
            
            if not sup or film.runtimeMin <= sup:
                outputList.append(film)

        # sort di una tupla(durata, titolo), ordina in automatico per durata e poi per titolo
        outputList.sort(key=lambda film: (film.runtimeMin, film.title))
        return outputList;

##################################################################################################
# Esempio di voce json che descrive un film estratta dal file films.json
##################################################################################################
# "10 Things I Hate About You;1999": {
#     "TITLE": [
#         "10 Things I Hate About You",
#         "1999"
#     ],
#     "ACTORS": [
#         "Heath Ledger",
#         "Julia Stiles",
#         "Joseph Gordon-Levitt",
#         "Larisa Oleynik",
#         "David Krumholtz",
#         "Andrew Keegan",
#         "Susan May Pratt",
#         "Gabrielle Union",
#         "Larry Miller",
#         "Daryl Mitchell",
#         "Allison Janney",
#         "David Leisure",
#         "Greg Jackson",
#         "Kyle Cease",
#         "Terence Heuston"
#     ],
#     "DIRECTORS": [
#         "Gil Junger"
#     ],
#     "WRITERS": [
#         "Karen McCullah Lutz",
#         "Kirsten Smith",
#         "and 1 more credit"
#     ],
#     "GENRES": [
#         "Comedy",
#         "Romance"
#     ],
#     "COUNTRY": ["USA"],
#     "LANGUAGE": [
#         "English",
#         "French"
#     ],
#     "RUNTIME": ["97 min"],
#     "IMDB_URL": ["http://www.imdb.com/title/tt0147800/"],
#     "POSTER": [ "http://ia.media-imdb.com/images/M/MV5BMTI4MzU5OTc2MF5BMl5BanBnXkFtZTYwNzQxMjc5._V1._SY317_CR4,0,214,317_.jpg"]
# },


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
        # inserite qui il vosto codice
        self.dizionarioAttori = {}
        self.dizionarioRegistri = {}
        self.country = data['COUNTRY']
        minMaxRuntime = self.calcolaDurataMinimaMassima(data['RUNTIME'])
        self.runtimeMin = None if not minMaxRuntime else minMaxRuntime[0]
        self.runtimeMax = None if not minMaxRuntime else minMaxRuntime[1]
        self.title = data['TITLE'][0]
        self.year = data['TITLE'][1]
        
    def calcolaDurataMinimaMassima(self, runTimeAsList):
        if not runTimeAsList or len(runTimeAsList) == 0:
            return None
            # raise ValueError('RunTime non presente')
        minRuntime = None
        maxRuntime = None
        for item in runTimeAsList:
            patternMatch = patternDigit.findall(item)
            if len(patternMatch) >= 1:
                time = int(patternMatch[0])
                if minRuntime is None or time < minRuntime:
                    minRuntime = time
                if maxRuntime is None or time > maxRuntime:
                    maxRuntime = time
        
        return (minRuntime, maxRuntime)
    
    def attori(self):
        '''torna l'insieme di istanze di tipo Attore che hanno lavorato al film'''
        # inserite qui il vosto codice
        return set(self.dizionarioAttori.values())

    def registi(self):
        '''torna l'insieme di istanze di tipo Regista che hanno diretto il film'''
        # inserite qui il vosto codice
        return set(self.dizionarioRegistri.values())

    def luoghi(self):
        '''torna l'insieme di luoghi in cui è stato fatto il film (campo "COUNTRY" dei dati json)'''
        # inserite qui il vosto codice
        return self.country

    def durata(self):
        '''torna la durata minima in minuti (intero) del film (campo "RUNTIME" dei dati json)'''
        # inserite qui il vosto codice
        return self.runtimeMin

    def titolo(self):
        '''torna il titolo del film'''
        # inserite qui il vosto codice
        return self.title

    def anno(self):
        '''torna l'anno di produzione del film (dal campo "TITLE" dei dati json)'''
        # inserite qui il vosto codice
        return None if not self.year else int(self.year)

##################################################################################################


class Regista:
    '''
    La classe Regista rappresenta la scheda di un regista.
    Gli attributi di istanza della classe Regista sono quelli necessari ad implementare i seguenti metodi.
    '''

    def __init__(self, nome):
        '''Il costruttore assegna il nome.'''
        # inserite qui il vosto codice
        self.name = nome
        self.dizionarioFilm = {}
        self.dizionarioAttori = {}

    def aggiungiFilm(self, film):
        self.dizionarioFilm[film.title] = film
        for nome, attore in film.dizionarioAttori.items():
            if nome in self.dizionarioAttori:
                presenze = self.dizionarioAttori[nome][1]
                self.dizionarioAttori[nome] = (attore, presenze + 1)
            else:
                self.dizionarioAttori[nome] = (attore, 1)
        
    def films(self):
        '''torna l'insieme delle istanze dei Film in cui il regista ha lavorato'''
        # inserite qui il vosto codice
        return set(self.dizionarioFilm.values())

    def nome(self):
        '''torna il nome del regista'''
        # inserite qui il vosto codice
        return self.name

    def attori(self):
        '''torna l'insieme di attori che hanno lavorato col regista'''
        # inserite qui il vosto codice
        return set(map(lambda x : x[0], self.dizionarioAttori.values()))

    def attore_preferito(self):
        '''torna l'istanza di tipo Attore che ha lavorato più volte col regista
            In caso di parità si torni l'attore più giovane (vedi metodo Attore.eta())
            In caso di parità si torni l'attore di genere femminile
            In caso di parità quello col vero nome (campo "REALNAME") che viene prima in ordine alfabetico.
            Se il campo REALNAME nel dizionario json non è presente o non contiene un valore usate il campo NAME.
        '''
        # inserite qui il vosto codice
        # for nome, attore in self.dizionarioAttori:
        if not self.dizionarioAttori:
            return None
        
        attoriList = list(map(lambda x: (x[1], x[0]), self.dizionarioAttori.values()))
        attoriList.sort(key=takeFirst, reverse=True)
        
        papabile = attoriList[0]
        for attore in attoriList:
            if attore[0] < papabile[0]:
                break
            if attore[0] > papabile[0]:
                papabile = attore
            if attore[0] == papabile[0]:
                if attore[1].eta() < papabile[1].eta():
                    papabile = attore
                    continue
                elif attore[1].genere() == 'F' and papabile[1].genere() == 'M':
                    papabile = attore
                    continue
                elif not papabile[1].vero_nome() and attore[1].vero_nome():
                    papabile = attore
                    continue
                elif attore[1].vero_nome() and attore[1].vero_nome() < papabile[1].vero_nome():
                    papabile = attore
                    continue
                elif attore[1].nome() < papabile[1].nome():
                    papabile = attore
                    continue
        return papabile[1]

    def anni_di_lavoro(self):
        '''torna per quanti anni ha lavorato il regista a partire dal primo film prodotto all'ultimo
        compresi (vedi Film.anno())
        '''
        # inserite qui il vosto codice
        primoFilm = None
        ultimoFilm = None
        for nome, film in self.dizionarioFilm.items():
            if primoFilm is None:
                primoFilm = film
                continue
            if ultimoFilm is None:
                ultimoFilm = film
                continue
            if  film.anno() < primoFilm.anno():
                primoFilm = film
                continue
            if film.anno() > ultimoFilm.anno():
                ultimoFilm = film
                continue
        return ultimoFilm.anno() - primoFilm.anno() +1
            

##################################################################################################


if __name__ == '__main__':
    # inserite qui il vosto codice personale di test
    catalogo_attori = leggi_archivio_attori('actors.json')
    catologhi = leggi_archivio_film('films.json', catalogo_attori)
    catalogo_film = catologhi[0]
    catalogo_registi = catologhi[1]
    
    print(catalogo_attori['Marilyn Monroe'].regista_preferito())
    print(catalogo_attori['Ada May'].coprotagonisti())
    output = catalogo_attori['Scarlett Johansson'].film_durata(90, 120)
    inCoppiaList = catalogo_attori['Marilyn Monroe'].in_coppia('Cary Grant')
    print(inCoppiaList)
    
    print(catalogo_attori['Marcello Mastroianni'].luogo_preferito())
    
    print(catalogo_registi['Michelangelo Antonioni'].attore_preferito().nome())
    
