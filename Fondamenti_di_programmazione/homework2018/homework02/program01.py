def es1(ftesto):
    lista_coordinate = []
    with open(ftesto, 'r', encoding='utf-8') as file:
        testo = file.read().splitlines()

        diagramma_n = list(map(lambda el: el.split("\t"), list(filter(lambda line: '\t' in line, testo))))
        lista_parole = list(filter(lambda line: '\t' not in line and len(line) > 0, testo))
        diagramma = list(map(lambda x: ''.join(list(map(lambda word: word, x))), diagramma_n))

        # controllo parole su righe da dx e sx
        lista_coordinate = find_parole_in_righe(diagramma, lista_coordinate, lista_parole)

        # controllo parola su colonna
        lista_colonne = find_colonne(diagramma)
        lista_coordinate = find_parole_in_colonne(lista_colonne, lista_coordinate, lista_parole)

        # cerco nelle diagonali ed anti diagonali
        lista_coordinate += find_diagonal_forward_slash(diagramma, lista_parole, True)
        lista_coordinate += find_diagonal_forward_slash(diagramma, lista_parole, False)


        return_string = ''
        coordinate = coordinate_i_j(diagramma_n)
        for coordinata in coordinate:
            if coordinata[1] not in lista_coordinate:
                return_string += coordinata[0]

        return return_string


def coordinate_i_j(diagramma_n):
        for i, stringa_riga in enumerate(diagramma_n):
            for j, char in enumerate(stringa_riga):
                yield char, tuple((i, j))

def find_parole_in_colonne(lista_colonne, lista_coordinate, lista_parole):
    for j, colonna_diagramma in enumerate(lista_colonne):
        for parola in lista_parole:

            if parola in colonna_diagramma:
                indice_colonna = colonna_diagramma.find(parola)
                coordinate_parola = [(i, j) for i in range(indice_colonna, len(parola) + indice_colonna)]
                lista_coordinate += coordinate_parola
            else:
                parola_reversed = parola[::-1]

                if parola_reversed in colonna_diagramma:
                    indice_colonna = colonna_diagramma.find(parola_reversed)
                    coordinate_parola = [(i, j) for i in range(indice_colonna, len(parola_reversed) + indice_colonna)]
                    lista_coordinate += coordinate_parola
    return lista_coordinate


def find_parole_in_righe(diagramma, lista_coordinate, lista_parole):
    for i, riga_diagramma in enumerate(diagramma):
        for parola in lista_parole:

            if parola in riga_diagramma:
                indice_riga = riga_diagramma.find(parola)
                coordinate_parola = [(i, j) for j in range(indice_riga, len(parola) + indice_riga)]
                lista_coordinate += coordinate_parola
            else:
                parola_reversed = parola[::-1]
                if parola_reversed in riga_diagramma:
                    indice_riga = riga_diagramma.find(parola_reversed)
                    coordinate_parola = [(i, j) for j in range(indice_riga, len(parola) + indice_riga)]
                    lista_coordinate += coordinate_parola
    return lista_coordinate


# da alto a sinistra in giu
def find_diagonal_forward_slash(diagramma, lista_parole, forward):
    h = len(diagramma)
    w = len(diagramma[0])
    range_list = []

    verso = 0
    verso_fatt_molt = 1
    n = 1
    if not forward:
        verso = h - 1
        verso_fatt_molt = -1

    for k in range(h + w - 1):
        if k < w:
            diagonal_word = ''
            temp_list = []
            for l in range(k + 1):
                i = verso + l * verso_fatt_molt
                j = k - l
                try:
                    temp_list.append(tuple((i, j)))
                    diagonal_word += diagramma[i][j]
                except:
                    pass
            word_in_list, indexes = is_word_in_list(diagonal_word, lista_parole, temp_list)
            if word_in_list:
                range_list += [xy for xy in indexes]


        else:
            diagonal_word = ''
            temp_list = []
            for l in range(k - w + 1, k + 1 - n):
                i = verso + l * verso_fatt_molt
                if i == h:
                    break
                j = k - l
                if j == w:
                    break
                try:
                    temp_list.append(tuple((i, j)))
                    diagonal_word += diagramma[i][j]
                except Exception as e:
                    print("find diagonale: (i,j)", i, j, "  ", e)

            word_in_list, indexes = is_word_in_list(diagonal_word, lista_parole, temp_list)
            n+=1
            if word_in_list:
                range_list += [xy for xy in indexes]

    return range_list


def is_word_in_list(diagonal_string, list_words, index_list):
    word_index = []
    found = False
    for w in list_words:

        lenght_word = len(w)
        if w in diagonal_string:
            word_start_index = diagonal_string.index(w)
            word_index += index_list[word_start_index:word_start_index + lenght_word]
            found = True
        else:
            word_reversed = w[::-1]
            if word_reversed in diagonal_string:
                word_start_index = diagonal_string.index(word_reversed)
                word_index += index_list[word_start_index:word_start_index + lenght_word]
                found = True
    return found, word_index


def find_colonne(diagramma_upper):
    lista_colonne = []
    n_colonne = len(diagramma_upper[0])
    n_righe = len(diagramma_upper)
    for j in range(n_colonne):
        colonna = []
        colonna_string = ''
        for i in range(n_righe):
            try:
                colonna.append(diagramma_upper[i][j])
                colonna_string = ''.join(colonna)
            except Exception as e:
                print("find colonne: (i,j)",i,j, "  ",e)
        lista_colonne.append(colonna_string)
    return lista_colonne

mat = [[1,2,3,4,5,6,7,8,9,10,1,1,1,1,1],
       [11,12,13,14,15,16,17,18,19,20,1,1,1,1,1],
       [11,12,13,14,15,16,17,18,19,20,1,1,1,1,1],
[11,12,13,14,15,16,17,18,19,20,1,1,1,1,1],
[11,12,13,14,15,16,17,18,19,20,1,1,1,1,1],
[11,12,13,14,15,16,17,18,19,20,1,1,1,1,1],
[11,12,13,14,15,16,17,18,19,20,1,1,1,1,1],
[11,12,13,14,15,16,17,18,19,20,1,1,1,1,1],
[11,12,13,14,15,16,17,18,19,20,1,1,1,1,1],
[11,12,13,14,15,16,17,18,19,20,1,1,1,1,1],
[11,12,13,14,15,16,17,18,19,20,1,1,1,1,1],
[11,12,13,14,15,16,17,18,19,20,1,1,1,1,1],
[11,12,13,14,15,16,17,18,19,20,1,1,1,1,1],
[11,12,13,14,15,16,17,18,19,20,1,1,1,1,1]


       ]


'''
1   2   3   4  5 
6   7   8   9  10 
11  12  13  14  15
16  17  18  19  20


'''


# da alto a sinistra in giu
def find_diagonal_forward_slash_p(diagramma,forward):
    h = len(diagramma)
    w = len(diagramma[0])
    range_list = []
    diagonal_list = []
    verso = 0
    verso_fatt_molt = 1
    if not forward:
        verso = h - 1
        verso_fatt_molt = -1
        n = 1
    for k in range(h + w - 1):
        if k < w:
            diagonal_word = ''
            temp_list = []
            for l in range(k + 1):
                i = verso + l * verso_fatt_molt
                j = k - l
                try:
                    temp_list.append(diagramma[i][j])
                    #diagonal_word += diagramma[i][j]
                except:
                    pass
            diagonal_list.append(temp_list)
            #word_in_list, indexes = is_word_in_list(diagonal_word, lista_parole, temp_list)
            #if word_in_list:
            #    range_list += [xy for xy in indexes]


        else:
            diagonal_word = ''
            temp_list = []
            for l in range(k - w + 1, k + 1 - n):
                i = verso + l * verso_fatt_molt
                j = k - l
                try:
                    temp_list.append(diagramma[i][j])
                    #diagonal_word += diagramma[i][j]
                except Exception as e:
                    print("find diagonale: (i,j)", i, j, "  ", e)
            diagonal_list.append(temp_list)
            n +=1
            #word_in_list, indexes = is_word_in_list(diagonal_word, lista_parole, temp_list)
            #if word_in_list:
            #    range_list += [xy for xy in indexes]

    return diagonal_list




def diags(mat):
    width, height = len(mat[0]), len(mat)
    def diag(sx, sy):
        for x, y in zip(range(sx, height), range(sy, width)):
            yield mat[x][y]
    for sx in range(height):
        yield list(diag(sx, 0))
    for sy in range(1, width):
        yield list(diag(0, sy))

#print(list(diags(mat)))
#print(find_diagonal_forward_slash_p(mat,False))
#print(es1("cp6_Pensiero.txt"))