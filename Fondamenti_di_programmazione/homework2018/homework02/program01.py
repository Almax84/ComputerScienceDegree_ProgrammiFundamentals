
def es1(ftesto):
    lista_coordinate = []
    with open(ftesto, 'r', encoding='utf-8') as file:
        testo = file.read().splitlines()
        
        
        diagramma_n = list(map(lambda el: el.split("\t"),list(filter(lambda line : '\t' in line ,testo))))
        lista_parole = list(filter(lambda line: '\t' not in line and len(line) > 0, testo))
        diagramma = list(map(lambda x: ''.join(list(map(lambda word: word, x))), diagramma_n))

        
                #controllo parole su righe da dx e sx
        lista_coordinate = find_parole_in_righe(diagramma, lista_coordinate, lista_parole)

        # controllo parola su colonna
        lista_colonne = find_colonne(diagramma)   
        lista_coordinate = find_parole_in_colonne(lista_colonne, lista_coordinate, lista_parole)

        #cerco nelle diagonali ed anti diagonali
        lista_coordinate += find_diagonal_forward_slash(diagramma, lista_parole, True)
        lista_coordinate += find_diagonal_forward_slash(diagramma, lista_parole, False)

        diagramma_by_char = [list(riga) for riga in diagramma ]

        '''
        #print(diagramma_by_char)
        #print(lista_coordinate)
        return_string = ''.join([char for i, stringa_riga in enumerate(diagramma_by_char)
                                    for j, char in enumerate(stringa_riga)
                                        if tuple((i,j)) not in lista_coordinate])
        '''
    
        return_string = ''
        for i,stringa_riga in enumerate(diagramma_by_char):
            for j, char in enumerate(stringa_riga):
                if tuple((i,j)) not in lista_coordinate:
                    #print("coordinate non in lista coordinate ", i," ",j, char)
                    return_string += char

        return return_string


def find_parole_in_colonne(lista_colonne, lista_coordinate, lista_parole):
    for j, colonna_diagramma in enumerate(lista_colonne):
        for parola in lista_parole:
            parola_reversed = parola[::-1]
            if parola in colonna_diagramma:
                indice_colonna = colonna_diagramma.find(parola)
                coordinate_parola = [(i, j) for i in range(indice_colonna, len(parola) + indice_colonna)]
                lista_coordinate += coordinate_parola
            elif parola_reversed in colonna_diagramma:
                indice_colonna = colonna_diagramma.find(parola_reversed)
                coordinate_parola = [(i, j) for i in range(indice_colonna, len(parola_reversed) + indice_colonna)]
                lista_coordinate += coordinate_parola
    return lista_coordinate


def find_parole_in_righe(diagramma, lista_coordinate, lista_parole):
    for i, riga_diagramma in enumerate(diagramma):
        for parola in lista_parole:
            parola_reversed = parola[::-1]
            if parola in riga_diagramma:
                indice_riga = riga_diagramma.find(parola)
                coordinate_parola = [(i, j) for j in range(indice_riga, len(parola) + indice_riga)]
                lista_coordinate += coordinate_parola
            elif parola_reversed in riga_diagramma:
                indice_riga = riga_diagramma.find(parola_reversed)
                coordinate_parola = [(i, j) for j in range(indice_riga, len(parola) + indice_riga)]
                lista_coordinate += coordinate_parola
    return lista_coordinate


#da alto a sinistra in giu
def find_diagonal_forward_slash(diagramma,lista_parole, forward):
    h = len(diagramma)
    w = len(diagramma[0])
    range_list = []
    
    verso = 0
    verso_fatt_molt = 1
    if not forward:
        verso = h - 1 
        verso_fatt_molt = -1
    
    
    for k in range(h+w-1):
        if k == 0:
            i = 0 + verso
            j = 0
        elif k < w:
            diagonal_word = ''
            temp_list = []
            for l in range(k+1):
                i = verso + l * verso_fatt_molt
                j = k-l
                try:
                    temp_list.append(tuple((i,j)))
                    diagonal_word+=diagramma[i][j]
                except:
                    #print(i,j)
                    pass
            #print(diagonal_word)
            word_in_list, indexes = is_word_in_list(diagonal_word, lista_parole, temp_list)
            if word_in_list:
                #print("trovata:", diagonal_word)
                range_list += [xy for xy in indexes]
            
                            
        else:
            diagonal_word = ''
            temp_list = []
            for l in range(k-w+1,k+1):
                i = verso + l * verso_fatt_molt
                j = k-l
                try:
                    if i < 0 or j < 0:
                        break
                    
                    temp_list.append(tuple((i,j)))
                    diagonal_word+=diagramma[i][j]
                except:
                    pass
                
                
            #print(diagonal_word)
            word_in_list, indexes = is_word_in_list(diagonal_word, lista_parole, temp_list)
            if word_in_list:
                #print("trovata:", diagonal_word, " ", indexes)
                range_list += [xy for xy in indexes]
                
            #print(range_list)
    return range_list
        

                
def is_word_in_list(diagonal_string, list_words,index_list):
        #print("is word in list: ",diagonal_string)
        word_index = []
        found = False
        for w in list_words:
            #diagonal_reversed = diagonal_string[::-1]
            word_reversed = w[::-1]
            if w in diagonal_string :
                word_start_index = diagonal_string.index(w)
                word_index += index_list[word_start_index:word_start_index+len(w)]
                #return True, word_index
                found = True
            elif word_reversed in  diagonal_string :
                word_start_index = diagonal_string.index(word_reversed)
                #print("index_list ",index_list)
                word_index += index_list[word_start_index:word_start_index+len(w)]
                #word_index= [x[::-1] for _,x in enumerate(index_list[word_start_index:word_start_index+len(w)]) ]
                #print("indexes for word: ", w, " ", word_index)
                #return True,word_index
                found = True
        return found, word_index       
        #return False, []


def find_colonne(diagramma_upper):
        lista_colonne = []
        for j in range(len(diagramma_upper[0])):
            colonna = []
            colonna_string = ''
            for i in range(len(diagramma_upper)):
                try:
                    colonna.append(diagramma_upper[i][j])
                    colonna_string = ''.join(colonna)
                except:
                    pass
            lista_colonne.append(colonna_string)
        return lista_colonne
            

#print(es1("cp1_Tisana.txt"))