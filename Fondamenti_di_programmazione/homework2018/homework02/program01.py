# NOTA!
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

        len_parola_piu_corta = len(min(lista_parole, key=len))

        # controllo parole su righe da dx e sx
        lista_coordinate = find_parole_in_righe(diagramma, lista_coordinate, lista_parole, len_parola_piu_corta)

        # controllo parola su colonna
        lista_colonne = find_colonne(diagramma)
        lista_coordinate = find_parole_in_colonne(lista_colonne, lista_coordinate, lista_parole)

        # cerco nelle diagonali ed anti diagonali
        lista_coordinate += search_diagonally(diagramma, lista_parole)
        lista_coordinate += search_diagonally(diagramma, lista_parole)

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
            count = colonna_diagramma.count(parola)
            lista_coordinate = find_in_i_j(colonna_diagramma, count, j, lista_coordinate,
                                           parola, True)
            parola_reversed = parola[::-1]
            count = colonna_diagramma.count(parola_reversed)
            lista_coordinate = find_in_i_j(colonna_diagramma, count, j, lista_coordinate,
                                           parola_reversed, True)

    return lista_coordinate


def find_in_i_j(stringa, count, m, lista_coordinate, parola, isColonna):
    end_index_first_word = 0
    for n in range(count):
        word_start_index = stringa.index(parola, n + end_index_first_word)
        end_index_first_word = word_start_index + len(parola)
        if isColonna:
            coordinate_parola = [(i, m) for i in range(word_start_index, len(parola) + word_start_index)]
        else:
            #inverto nel caso di righe, in modo da usare sempre la stessa funzione
            coordinate_parola = [(m, j) for j in range(word_start_index, len(parola) + word_start_index)]
        lista_coordinate += coordinate_parola
    return lista_coordinate


def find_parole_in_righe(diagramma, lista_coordinate, lista_parole, len_parola_piu_corta):
    for i, riga_diagramma in enumerate(diagramma):

        for parola in lista_parole:

            count = riga_diagramma.count(parola)
            lista_coordinate = find_in_i_j(riga_diagramma, count, i, lista_coordinate,
                                           parola, False)
            parola_reversed = parola[::-1]
            count = riga_diagramma.count(parola_reversed)
            lista_coordinate = find_in_i_j(riga_diagramma, count, i, lista_coordinate,
                                           parola_reversed, False)

    return lista_coordinate


# da alto a sinistra in giu
def search_diagonally(diagramma, lista_parole):
    return_list = get_diagonals_indexes(diagramma)
    range_list = []

    for sub in return_list:
        diagonal_word = ''
        temp_list = []
        for tupl in sub:
            i, j = tupl
            temp_list.append(tupl)
            try:
                diagonal_word += diagramma[i][j]
            except:
                pass
        word_in_list, indexes = is_word_in_list(diagonal_word, lista_parole, temp_list)
        if word_in_list:
            range_list += [xy for xy in indexes]
    return range_list


def is_word_in_list(diagonal_string, list_words, index_list):
    word_index = []
    found = False

    if len(diagonal_string) <= 1:
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



def get_diagonals_indexes(mat):
    width, height = len(mat[0]), len(mat)
    return_list = []
    for j in range(width):

        # "/"
        i_list_fw = [i for i in range(j + 1)]
        j_list_fw = [n for n in reversed(range(j + 1))]
        list1 = list(zip(i_list_fw, j_list_fw))
        return_list.append(list1)
        # "\"
        i_list_bk = [i for i in reversed(range(height))]
        j_list_bk = [n for n in reversed(range(j + 1))]
        list2 = list(zip(i_list_bk, j_list_bk))
        return_list.append(list2)

    for i in range(height):

        i_list_fw = [i for i in range(i, height)]
        j_list_fw = [n for n in reversed(range(width))]
        list3 = list(zip(i_list_fw, j_list_fw))
        return_list.append(list3)

        i_list_bk = [i for i in reversed(range(i + 1))]
        j_list_bk = [n for n in reversed(range(width))]
        list4 = list(zip(i_list_bk, j_list_bk))
        return_list.append(list4)

    return return_list


