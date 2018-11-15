#NOTA!
'''

PREVEDI LA POSSIBILITà CHE SU UNA RIGA LA STESSA PAROLA SIA PRESENTE PIù DI UNA VOLTA!!!!
ora con quello che ho fatto funzoina solo se è presente una volta
'''


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

            end_index_first_word = 0
            count = colonna_diagramma.count(parola)
            if count > 0:
                lista_coordinate = find_in_i_j(colonna_diagramma, count, end_index_first_word, j, lista_coordinate,
                                               parola)

            else:
                parola_reversed = parola[::-1]
                count = colonna_diagramma.count(parola_reversed)
                lista_coordinate = find_in_i_j(colonna_diagramma, count, end_index_first_word, j, lista_coordinate,
                                               parola_reversed)

    return lista_coordinate


def find_in_i_j(colonna_diagramma, count, end_index_first_word, j, lista_coordinate, parola_reversed):
    if count > 0:
        for n in range(count):
            word_start_index = colonna_diagramma.index(parola_reversed, n + end_index_first_word)
            end_index_first_word = word_start_index + len(parola_reversed)
            coordinate_parola = [(i, j) for i in range(word_start_index, len(parola_reversed) + word_start_index)]
            lista_coordinate += coordinate_parola
    return lista_coordinate


def find_parole_in_righe(diagramma, lista_coordinate, lista_parole):
    for i, riga_diagramma in enumerate(diagramma):

        for parola in lista_parole:

            if parola in riga_diagramma:
                indice_riga = riga_diagramma.find(parola)
                coordinate_parola = [(i, j) for j in range(indice_riga, len(parola) + indice_riga)]
                lista_coordinate += coordinate_parola
                count = riga_diagramma.count(parola)
                find_in_i_j

            else:
                parola_reversed = parola[::-1]
                if parola_reversed in riga_diagramma:
                    indice_riga = riga_diagramma.find(parola_reversed)
                    coordinate_parola = [(i, j) for j in range(indice_riga, len(parola) + indice_riga)]
                    lista_coordinate += coordinate_parola
                    count = riga_diagramma.count(parola)

    return lista_coordinate


# da alto a sinistra in giu
def find_diagonal_forward_slash(diagramma, lista_parole, forward):
    return_list = diags_mio(diagramma)
    range_list = []

    for sub in return_list:
        diagonal_word = ''
        temp_list = []
        for tupl in sub:
            i,j = tupl
            temp_list.append(tupl)
            try:
                diagonal_word+=diagramma[i][j]
            except:
                pass
        word_in_list , indexes = is_word_in_list(diagonal_word, lista_parole, temp_list)
        if word_in_list:
            range_list += [xy for xy in indexes]
    return range_list


def is_word_in_list(diagonal_string, list_words, index_list):
    word_index = []
    found = False

    if len(diagonal_string)<=1:
        return False, None

    for w in list_words:

        lenght_word = len(w)
        count = diagonal_string.count(w)
        if count > 0:
            found, word_index = find_word_in_generic_string(count, diagonal_string, found, index_list, lenght_word, w,
                                                            word_index)

        else:
            word_reversed = w[::-1]
            count = diagonal_string.count(word_reversed)
            if count > 0:
                found, word_index = find_word_in_generic_string(count, diagonal_string, found, index_list, lenght_word,
                                                                word_reversed,
                                                                word_index)
    return found, word_index


def find_word_in_generic_string(count, diagonal_string, found, index_list, lenght_word, w, word_index):
    end_index_first_word = 0
    for n in range(count):
        word_start_index = diagonal_string.index(w, n + end_index_first_word)
        end_index_first_word = word_start_index + lenght_word
        word_index += index_list[word_start_index:end_index_first_word]
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
                pass
        lista_colonne.append(colonna_string)
    return lista_colonne









def diags(mat):
    width, height = len(mat[0]), len(mat)
    def diag(sx, sy):
        for x, y in zip(range(sx, height), range(sy, width)):
            yield mat[x][y]
    for sx in range(height):
        yield list(diag(sx, 0))
    for sy in range(1, width):
        yield list(diag(0, sy))


def diags_mio(mat):
    width, height = len(mat[0]), len(mat)
    return_list = []
    for j in range(width):
       # print("J =", j)

        # "/"
        i_list_fw = [i for i in range(j+1)]
        j_list_fw = [n for n in reversed(range(j+1))]
        list1 = list(zip(i_list_fw, j_list_fw))
        # print("forward:" , list1)
        return_list.append(list1)
        # "\"
        i_list_bk = [i for i in reversed(range(height))]
        j_list_bk = [n for n in reversed(range(j+1))]
        list2 = list(zip(i_list_bk, j_list_bk))
        return_list.append(list2)
        # print("backward:", list2)

    for i in range(height):
        #print("I = ", i)

        i_list_fw = [i for i in range(i, height)]
        j_list_fw = [n for n in reversed(range(width))]
        list3 = list(zip(i_list_fw, j_list_fw))
        return_list.append(list3)
        # print(list3)

        i_list_bk = [i for i in reversed(range(i+1))]
        j_list_bk = [n for n in reversed(range(width))]
        list4 = list(zip(i_list_bk, j_list_bk))
        # print("backward", list4)
        return_list.append(list4)


    return return_list



#mat = [[1,2,3,4,5],[5,6,7,8,5],[9,10,11,12,5],[13,14,15,16,5],[13,14,15,16,5],[13,14,15,16,5]]
#print(diags_mio(mat))
#print(list(diags(mat)))
#print(find_diagonal_forward_slash_p(mat,False))
print(es1("cp6_Pensiero.txt"))