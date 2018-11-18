def es3(fmappa):
    with open(fmappa, 'r', encoding='utf-8') as file:
        file_lines = file.read().strip().splitlines()

        p1 = []
        p2 = []
        insieme_I = dict()

        tuples_string = ''.join(file_lines).strip()

        get_tuple_dict(insieme_I, tuples_string)

        p1 = get_percorso_robottino(file_lines, p1)
        p2 = get_percorso_robottino(file_lines, p2)


        spostamento_p1 = get_spostamento_robottino(p1,insieme_I)
        spostamento_p2 = get_spostamento_robottino(p2,insieme_I)

        contatore_circoscritti = get_contatore_circoscritti(insieme_I, spostamento_p1, spostamento_p2)

        return contatore_circoscritti


def get_contatore_circoscritti(insieme_I, spostamento_p1, spostamento_p2):
    contatore_circoscritti = 0
    for x, rows in insieme_I.items():
        for y in rows:
            if x not in spostamento_p1 or x not in spostamento_p2:
                break

            y2_list = spostamento_p2[x]
            y1_list = spostamento_p1[x]

            if y in y2_list or y in y1_list:
                continue

            y1_maggiori = list(filter(lambda y1: y1 > y, y1_list))
            y2_minori = list(filter(lambda y2: y2 < y, y2_list))

            if len(y1_maggiori) > 0 and len(y2_minori) > 0:
                contatore_circoscritti += 1
    return contatore_circoscritti


def get_spostamento_robottino(percorso_primo_robottino,insieme_I):
    x = 1
    y = 1
    mappa_spostamenti_robottino = {1:[1]}  # key will be column x, value list of y
    for spostamento in percorso_primo_robottino:
        if spostamento > 0:
            y = get_mappa_spostamenti(mappa_spostamenti_robottino, spostamento, x, y)
        elif spostamento < 0:
            x = get_mappa_spostamenti_neg(mappa_spostamenti_robottino, spostamento, x, y)
    return mappa_spostamenti_robottino


def get_mappa_spostamenti_neg(mappa_spostamenti_robottino, spostamento, x, y):
    spostamento = spostamento * -1
    for i in range(1, spostamento + 1):
        x += 1
        if x in mappa_spostamenti_robottino:
            mappa_spostamenti_robottino[x] += [y]
        else:
            mappa_spostamenti_robottino[x] = [y]
    return x


def get_mappa_spostamenti(mappa_spostamenti_robottino, spostamento, x, y):
    for i in range(1, spostamento + 1):
        y += 1
        if x in mappa_spostamenti_robottino:
            mappa_spostamenti_robottino[x] += [y]
        else:
            mappa_spostamenti_robottino[x] = [y]
    return y


def get_tuple_dict(dict_I, tuples_string):
    while len(tuples_string) > 0:
        first_par_index = tuples_string.find("(")
        second_par_index = tuples_string.find(")")
        try:
            index_ = tuples_string[first_par_index:second_par_index + 1]
            tuple = eval(index_)
            x, y = tuple

            find_next_par = build_dict_I(dict_I, second_par_index, tuples_string, x, y)
            if find_next_par < 0:
                break
            tuples_string = tuples_string[find_next_par:]
        except:
            break


def build_dict_I(dict_I, second_par_index, tuples_string, x, y):
    if x in dict_I:
        dict_I[x] += [y]
    else:
        dict_I[x] = [y]
    find_next_par = tuples_string.find("(", second_par_index)
    return find_next_par


def get_percorso_robottino(file_lines, percorso_rotottino):
    i = 0
    while i < len(file_lines):
        line = file_lines[i]
        if line != '' or len(percorso_rotottino) == 0:
            percorso_rotottino += list(map(lambda x: int(x), line.split()))
            file_lines.pop(i)
            i -= 1
        else:
            break
        i += 1
    return percorso_rotottino

