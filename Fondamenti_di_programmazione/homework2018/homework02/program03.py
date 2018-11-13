def es3(fmappa):
    with open(fmappa, 'r', encoding='utf-8') as file:
        file_lines = file.read().strip().splitlines()

        p1 = []
        p2 = []
        insieme_I = dict()

        p1 = get_percorso_robottino(file_lines, p1)
        p2 = get_percorso_robottino(file_lines, p2)

        tuples_string = ''.join(file_lines).strip()

        get_tuple_dict(insieme_I, tuples_string)

        spostamento_p1 = get_spostamento_robottino(p1)
        spostamento_p2 = get_spostamento_robottino(p2)


        contatore_circoscritti = 0
        for x, rows in insieme_I.items():
            for y in rows:
                if x not in spostamento_p1 or x not in spostamento_p2:
                    continue

                y2_list = spostamento_p1[x]
                y1_list = spostamento_p2[x]

                for y2 in y2_list:
                    if y < y2:
                        for y1 in y1_list:
                            if y > y1:
                                contatore_circoscritti+=1

        return contatore_circoscritti



def get_spostamento_robottino(percorso_primo_robottino):
    x = 1
    y = 1
    mappa_spostamenti_robottino = dict()  # key will be column x, value list of y
    for spostamento in percorso_primo_robottino:
        if spostamento > 0:
            for i in range(1, spostamento + 1):
                y += 1
                if x in mappa_spostamenti_robottino:
                    mappa_spostamenti_robottino[x] += [y]
                else:
                    mappa_spostamenti_robottino[x] = [y]
        elif spostamento < 0:
            spostamento = spostamento * -1
            for i in range(1, spostamento + 1):
                x += 1
                if x in mappa_spostamenti_robottino:
                    mappa_spostamenti_robottino[x] += [y]
                else:
                    mappa_spostamenti_robottino[x] = [y]
    return mappa_spostamenti_robottino


def get_tuple_dict(dict_I, tuples_string):
    while len(tuples_string) > 0:
        first_par_index = tuples_string.find("(")
        second_par_index = tuples_string.find(")")
        try:
            index_ = tuples_string[first_par_index:second_par_index + 1]
            tuple = eval(index_)
            x, y = tuple

            if x in dict_I:
                dict_I[x] += [y]
            else:
                dict_I[x] = [y]
            find_next_par = tuples_string.find("(", second_par_index)
            if find_next_par < 0:
                break
            tuples_string = tuples_string[find_next_par:]
        except:
            break



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


#print(es3("mp2.txt"))
