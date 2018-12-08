# -*- coding: utf-8 -*-

import json, re

def leggi_archivio_attori(archivio_attori_json):
    # inserite qui il vosto codice
    with open(archivio_attori_json,"r", encoding="utf-8") as f:
       
        actors_json = json.load(f)


        catalogo_attori = dict()

        for nome, dati in actors_json.items():
            attore = Attore(dati)
            name_attore = ''.join(dati["NAME"])
            catalogo_attori[name_attore] = attore
            
        
        return catalogo_attori




def leggi_archivio_film(archivio_film_json, catalogo_attori):
    # inserite qui il vosto codice
    catalogo_film = dict()
    catalogo_registi = dict()
    with  open(archivio_film_json, "r", encoding = "utf-8") as f:
        film_json = json.load(f)
        
        
        for nome_film, dati_film in film_json.items():
            
        #trova i nomi degli attori nel film
            actor_names_in_film = dati_film["ACTORS"]
            #crea una lista di attori da mettere nella classe film
            lista_attori = {catalogo_attori[actor_name] for actor_name in actor_names_in_film}
            dati_film["LISTA_ATTORI"] = lista_attori
            film = Film(dati_film)



            #genero l'oggetto regista
            directors = dati_film["DIRECTORS"]
            film_directors = set()
            for director in directors:
                # ogni regista deve avere i suoi film
                if director in catalogo_registi:
                    regista = catalogo_registi[director]
                    regista.lista_film.add(film)
                    film_directors.add(regista)
                    film.lista_registi |= film_directors
                else:
                    #se il regista non è già stato creato, lo creo
                    regista = Regista(director)
                    catalogo_registi[director] = regista
                    regista.lista_film.add(film)
                    film_directors.add(regista)
                    #ogni oggetto film deve avere i suoi registi
                    film.lista_registi |= film_directors



        # aggiungi il film all'attore
            for attore in lista_attori:
                attore.lista_film.add(film)
            nome_film = dati_film["TITLE"]
            catalogo_film[nome_film[0]] = film

        for attore_name, attore_obj in catalogo_attori.items():
            attore_obj.directors_catalogue = catalogo_registi

    return catalogo_film, catalogo_registi
        
        

class Attore():
    

    def __init__(self, data):
        self.lista_film = set()
        self.directors_catalogue = None
        self.attori_coprotagonisti_dict = None
        
        value = data["NAME"]
        if len(value) > 0:
            self.name = value[0]
        else:
            self.name = ""        
        
        self.last_first = data["LASTFIRST"]
        
        value = data["REALNAME"]
        if len(value) > 0:
            self.real_name = value[0]
        else:
            self.real_name = ""
            
            
        self.nick_names = data["NICKNAMES"]
        
        value = data["GENDER"]
        if len(value) > 0:
            self.gender = value[0]
        else:
            self.gender = ""
        
        value = data["BIRTH"]
        if len(value) > 0:
            self.birth = value[0]
        else:
            self.birth = ""
            
        value = data["DIED"]
        if len(value) > 0:
            self.died = value[0]
        else:
            self.died = ""
        

        self.registi_occurrences = None

    def nome(self):
        return self.name

    def genere(self):
        return self.gender

    def vero_nome(self):
        return self.real_name

    def eta(self):
        # inserite qui il vosto codice
        regex_anno = "[1-9][0-9][0-9][0-9]"
        if self.birth == None or self.birth == '':
            return None
        if self.died == None or self.died == '':
                anno_nascita = int(re.findall(regex_anno, self.birth)[0])
                return 2018 - anno_nascita +1
        else:
            
            anno_morte = int(re.findall(regex_anno, self.died)[0])
            anno_nascita = int(re.findall(regex_anno, self.birth)[0])
            return anno_morte - anno_nascita+1

    def films(self):
        return self.lista_film

    def registi(self):
        registi_con_cui_ha_lavorato = set()
        registi_occurrences = dict()
        #TODO OTTIMIZZARE
        for regista_nome, regista_value in self.directors_catalogue.items():
            for film in self.lista_film:
                #se l'attore non compare nel film skippare
                if regista_nome not in film.directors:
                    continue
                
                registi_con_cui_ha_lavorato.add(regista_nome)

                self.buid_registi_occurrences(regista_nome, registi_occurrences)


        self.registi_occurrences = registi_occurrences

        return_list = {self.directors_catalogue[regista] for regista in registi_con_cui_ha_lavorato}



        return return_list

    def buid_registi_occurrences(self, regista_nome, registi_occurrences):
        if regista_nome in registi_occurrences:
            registi_occurrences[regista_nome] = registi_occurrences[regista_nome] + 1
        else:
            registi_occurrences[regista_nome] = 1

    def regista_preferito(self):
        if self.registi_occurrences == None:
            # this sets the attori_dict if it's none
            self.registi()

        max_value = self.registi_occurrences[max(self.registi_occurrences, key=self.registi_occurrences.get)]

        max_registi = [k for k, v in self.registi_occurrences.items() if v == max_value]

        if len(max_registi) > 1:
            return self.directors_catalogue[min(max_registi)]
        elif len(max_registi) == 1:
            return self.directors_catalogue[max_registi[0]]
        else:
            return None


    def coprotagonisti(self):
        attori_coprotagonisti_dict = dict()
        attori_coprotagonisti = set()
        for film in self.lista_film:
            attori = film.attori()
            for attore in attori:
                if attore.nome() == self.name:
                    attori_coprotagonisti = attori_coprotagonisti | attori
                    for attore_cop in attori:
                        if attore_cop in attori_coprotagonisti_dict:
                            attori_coprotagonisti_dict[attore_cop]+=1
                        else:
                            attori_coprotagonisti_dict[attore_cop]=1


        attori_coprotagonisti.remove(self)
        self.attori_coprotagonisti_dict = attori_coprotagonisti_dict
        return attori_coprotagonisti




    def in_coppia(self, partner=None):
        if self.attori_coprotagonisti_dict == None:
            self.coprotagonisti()

        self_gender = self.genere()
        return_set = set()
        attori_coprotagonisti = self.attori_coprotagonisti_dict
        if partner == None:
            self.find_all_coppie(attori_coprotagonisti, return_set, self_gender)
        else:
            for attore, numero_film in attori_coprotagonisti.items():

                if self_gender == attore.genere() or self_gender == '' or attore.genere() == '':
                    continue
                for film in self.lista_film:
                    for attore in film.attori():
                        if attore.nome() == partner: #ok hanno fatto lo stesso film insieme
                            return_set.add(film)

        return return_set

    def find_all_coppie(self, attori_coprotagonisti, return_set, self_gender):
        for attore, numero_film in attori_coprotagonisti.items():
            if self_gender == attore.genere() or numero_film <= 1 or self_gender == '' or attore.genere() == '':
                continue

            a_f, a_m, n_f = self.build_tuple(attore, numero_film, self_gender)

            return_set.add(tuple((a_m, a_f, n_f)))

    def build_tuple(self, attore, numero_film, self_gender):

        if self_gender == "M":
            a_m = self
            a_f = attore
        elif self_gender == "F":
            a_m = attore
            a_f = self
        n_f = numero_film
        return a_f, a_m, n_f

    def luogo_preferito(self):
        country_dict = dict()
        for film in self.lista_film:
            lista_luoghi = film.luoghi()
            for luogo in lista_luoghi:
                if luogo in country_dict:
                    country_dict[luogo]+=1
                else:
                    country_dict[luogo] = 1

        if len(country_dict) == 0:
            return None

        luogo_preferito = sorted(country_dict, key= lambda x: tuple((-country_dict[x], x)) ,reverse=False)

        return luogo_preferito[0]



    def film_durata(self, inf=0, sup=None):
        lista_film_attore = self.lista_film
        return_list = list()
        for film in lista_film_attore:
            durata_film = film.durata()
            if durata_film == None or durata_film == 0:
                continue

            if sup != None :
                if durata_film >= inf and durata_film <= sup:
                    return_list.append(film)
            elif durata_film >= inf:
                    return_list.append(film)
        return sorted(return_list, key=lambda x: (x.durata(), x.titolo()))



    def catalogo_registi(self, catalogo_registi):
        self.directors_catalogue = catalogo_registi




class Film():
    def __init__(self, data):

        if "LISTA_ATTORI" in data:
            self.lista_attori = data["LISTA_ATTORI"]
        else:
            self.lista_attori = set()
        self.lista_registi = set()
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

        return self.lista_attori
        

    def registi(self):

        return self.lista_registi

    def luoghi(self):
        return set(self.countries) #lista di stringhe

    def durata(self):
        regex = "[0-9]+"
        runtime_string = self.runtime
        runtimes = re.findall(regex, runtime_string)
        runtimes_int_list = list(map(lambda x: int(x), runtimes))

        return min(runtimes_int_list)
        

    def titolo(self):
        return self.title
        

    def anno(self):
        return int(self.year)
    def catalogo_attori(self, catalogo_attori):
        self.catalogo_attori = catalogo_attori
    def catalogo_registi(self, catalogo_registi):
        self.catalogo_registi = catalogo_registi

##################################################################################################

class Regista:
    def __init__(self, nome):
        self.lista_film = set()
        self.name = nome
        self.attori_dict = None
        self.catalogo_film = None

    def films(self):
        films_set = self.lista_film
        return films_set



    def nome(self):
        return self.name

    def attori(self):
        attori_set = set()
        attori_dict = dict()
        for  film_value in self.lista_film:
            registi_film = film_value.registi()
            for regista in registi_film:
                if regista.nome() == self.name:
                    film_attori = film_value.attori()
                    for attore in film_attori:
                        attori_set.add(attore)
                        self.build_attori_dict(attore, attori_dict)
        #mappa necessaria per attore preferito
        self.attori_dict = attori_dict
        return attori_set

    def build_attori_dict(self, attore, attori_dict):
        if attore.birth != "":
            if attore in attori_dict:
                attori_dict[attore] = attori_dict[attore] + 1
            else:
                attori_dict[attore] = 1

    def attore_preferito(self):

        
        if self.attori_dict == None:
            # this sets the attori_dict if it's none
            self.attori()

        max_value = self.attori_dict[max(self.attori_dict, key=self.attori_dict.get)]

        max_actors = [k for k,v in self.attori_dict.items() if v == max_value]


        if len(max_actors) > 1:
            return sorted(max_actors, key=self.max_attore_preferito)[0]
        elif len(max_actors) == 1:
            return max_actors[0]
        else:
            return None


    def max_attore_preferito(self,attore):
        eta_attore = attore.eta()
        gender_attore = attore.genere()
        vero_nome_attore = attore.vero_nome()
        if vero_nome_attore == "":
            vero_nome_attore = attore.nome()

        if eta_attore != None and gender_attore != None and vero_nome_attore != None:
            return  eta_attore, gender_attore, vero_nome_attore
        # if eta_attore != None and gender_attore != None:
        #     return -eta_attore, -ord(gender_attore)
        # if eta_attore != None and vero_nome_attore != None:
        #     return -eta_attore, vero_nome_attore
        # if gender_attore != None and vero_nome_attore != None:
        #     return gender_attore, vero_nome_attore

        if eta_attore != None:
            return -eta_attore
        if gender_attore != None:
            return ord(gender_attore)
        if vero_nome_attore != None:
            return vero_nome_attore


        return eta_attore, -ord(gender_attore), vero_nome_attore




    def anni_di_lavoro(self):
        set_anni = {film.anno() for film in self.lista_film for regista in film.registi() if regista.nome() == self.name}
        return max(set_anni)-min(set_anni)+1


    def catalogo_attori(self, catalogo_attori):
        self.catalogo_attori = catalogo_attori
    def catalogo_film(self, catalogo_film):
        self.catalogo_film = catalogo_film



    
        