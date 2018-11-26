def es3(fmappa):
    with open(fmappa, 'r', encoding='utf-8') as file:
        file_lines = file.read().strip().splitlines()

        p1 = []
        p2 = []

        
        p1 = get_percorso_robottino(file_lines, p1)
        p2 = get_percorso_robottino(file_lines, p2)
        
        insieme_I = dict()

        tuples_string = ''.join(file_lines).strip()

        get_tuple_dict(insieme_I, tuples_string)


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
    mappa_spostamenti_robottino = dict()  # key will be column x, value list of y
    for spostamento in percorso_primo_robottino:
        if spostamento > 0:
            y = build_mappa_spostamenti(mappa_spostamenti_robottino, spostamento, x, y)
        else:
            x = build_mappa_spostamenti_negativi(mappa_spostamenti_robottino, spostamento*-1, x, y)
    return mappa_spostamenti_robottino


def build_mappa_spostamenti_negativi(mappa_spostamenti_robottino, spostamento, x, y):
    for i in range(1, spostamento + 1):
        x += 1
        if x in mappa_spostamenti_robottino:
            mappa_spostamenti_robottino[x] += [y]
        else:
            mappa_spostamenti_robottino[x] = [y]
    return x


def build_mappa_spostamenti(mappa_spostamenti_robottino, spostamento, x, y):
    for i in range(1, spostamento + 1):
        y += 1
        if x in mappa_spostamenti_robottino:
            mappa_spostamenti_robottino[x] += [y]
        else:
            mappa_spostamenti_robottino[x] = [y]
    return y


def get_tuple_dict(dict_I, tuples_string):
    tuple_list = tuples_string.replace("),",");").split(";")
    
    for tuple_str in tuple_list:
        x, y = eval(tuple_str)
        if x in dict_I:
            dict_I[x] += [y]
        else:
            dict_I[x] = [y]
        


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

if __name__ == "__main__":
    print(es3("mp3.txt"))