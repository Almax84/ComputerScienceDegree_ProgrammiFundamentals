import immagini



def es1(fimg, fimg1):
    image = immagini.load(fimg)
    lunghezza = len(image)
    altezza = len(image[0])
    final_solution = []

    for r in range(lunghezza):
        c = 0
        image_row = image[r]
        while c < altezza:
            if c + 3 < lunghezza and is_black(image_row[c]) and is_black(image_row[c + 3]):
                c += 4
                continue

            currentPixel = image_row[c]
            if (is_white(currentPixel)):
                rect_corners = []
                can_start_rect_from_here(r, c, image, lunghezza, altezza, final_solution, rect_corners)
                if not len(rect_corners) == 0:
                    c = rect_corners[0][1]
                    continue

            c +=1

    for rect in final_solution:
        write_green(rect, image)
        write_red(rect, image)

    immagini.save(image, fimg1)
    return len(final_solution)


def write_green(rect, image):
    left_up_corner = rect[0]
    right_up_corner = rect[1]
    left_down_corner = rect[2]
    right_downd_corner = rect[3]

    GREEN = (0, 255, 0)

    # lato sopra
    left_up_corner_x = left_up_corner[0]
    write_lato_sotto(GREEN, image, left_up_corner_x, left_up_corner[1], right_up_corner[1])

    # lato sotto
    left_down_corner_x = left_down_corner[0]
    left_downn_corner_y = left_down_corner[1]
    right_down_corner_y = right_downd_corner[1]
    write_lato_sotto(GREEN, image, left_down_corner_x, left_downn_corner_y, right_down_corner_y)

    # LATO SINISTRO
    for r in range(left_up_corner_x, left_down_corner_x + 1):
        image[r][left_up_corner[1]] = GREEN

    # LATO DESTRO
    for r in range(right_up_corner[0], right_downd_corner[0] + 1):
        image[r][right_up_corner[1]] = GREEN


def write_lato_sotto(GREEN, image, left_down_corner_x, left_downn_corner_y, right_down_corner_y):
    for c in range(left_downn_corner_y, right_down_corner_y + 1):
        image[left_down_corner_x][c] = GREEN


def write_red(rect, image):
    RED = (255, 0, 0)
    left_up_corner = rect[0]
    right_up_corner = rect[1]
    left_down_corner = rect[2]

    for c in range(left_up_corner[1] + 1, right_up_corner[1]):
        for r in range(left_up_corner[0] + 1, left_down_corner[0]):
            # SCRIVO COLONNE
            image[r][c] = RED


def can_start_rect_from_here(r, c, image, lunghezza, altezza, final_solution, rect_corners):
    # andiamo a destra fino a che troviamo un nero o finisce l'immagine
    # contemporaneamente cerchiamo se nella riga di sotto ci sono pixel bianchi, se si ci fermiamo
    min_length = 3
    left_up_corner = (r, c)
    right_up_corner = -1
    left_down_corner = -1
    right_down_corner = -1

    # scorro verso destra, quindi il range e' da left_up_corner.LEFT+1 fino alla fine della riga
    left_up_corner_y = left_up_corner[1]
    left_up_corner_x = left_up_corner[0]
    for r in range(left_up_corner_y + 1, lunghezza):
        current_pixel = image[left_up_corner_x][r]
        # bottomSideCurrentPixel = fimgAsArray[left_up_corner[0] + 1][r]
        # se nero o alla fine dell'immagine allora OK
        # Se e l'ultima colonna verifico se e' bianco o nero
        if r == (lunghezza - 1):
            if is_black(current_pixel):
                # se all'ultima colonna troviamo nero e ancora non abbiamo individuato un angolo allora non e' un rettangolo
                return False
            elif is_white(current_pixel):
                # questa colonna e' l'ultima
                right_up_corner = (left_up_corner_x, r)
                rect_corners.append(right_up_corner)
                return False
        # se e' nero e al passo precedente non abbiamo trovato un angolo allora non puo' essere un angolo
        if is_black(current_pixel):
            return False
        # se il pixel nell'ultima colonna e' bianco quindi la riga continua verifichiamo se sotto e' bianco in tal caso e' un angolo in alto a destra e ci fermiamo
        # (left_up_corner[0] + 1) < altezza controlla che sotto sia presente una riga
        elif is_white(current_pixel) and (left_up_corner_x + 1) < altezza and is_white(image[left_up_corner_x + 1][r]):
            right_up_corner = (left_up_corner_x, r)
            rect_corners.append(right_up_corner)
            break

    if right_up_corner == -1:
        return False

    right_up_corner_y = right_up_corner[1]
    rectLength = right_up_corner_y - left_up_corner_y + 1
    # confrontiamo le colonne per capire la lunghezza
    if rectLength < min_length:
        # TOO SMALL
        return False

    # LETS GO DOWN NOW

    # scoperta la base di sopra scendiamo a destra e a sinistra verticalmente fino a che non troviamo
    # un nero o la fine dell'immagine, se anche dall'altra parte e' nero allora abbiamo trovato i lati
    for r in range(left_up_corner_x + 1, altezza):
        left_pixel = image[r][left_up_corner_y]
        right_pixel = image[r][right_up_corner_y]

        if r == (altezza - 1):
            # se proprio l ultima riga e' bianca almeno negli inner allora puo essere un rettangolo
            if is_white(left_pixel) and is_white(right_pixel):
                left_pixel_inner = image[r][left_up_corner_y + 1]
                right_pixel_inner = image[r][left_up_corner_y - 1]
                if is_white(left_pixel_inner) and is_white(right_pixel_inner):
                    # e' una possibile riga bianca quindi e' la base del rett
                    left_down_corner = (r, left_up_corner_y)
                    right_down_corner = (r, right_up_corner_y)
                    break
                else:
                    return False
            else:
                # se non sono entrambi bianchi e siamo arrivati alla fine allora non e' un rettangolo, manca la base
                return False
        if is_white(left_pixel) and is_white(right_pixel):
            # se sono entrambi bianchi allora va bene, controlliamo solo che non sia una potenziale riga bianca
            left_pixel_inner = image[r][left_up_corner_y + 1]
            right_pixel_inner = image[r][right_up_corner_y - 1]
            if is_white(left_pixel_inner) and is_white(right_pixel_inner):
                # e' una possibile riga bianca quindi e' la base del rett
                left_down_corner = (r, left_up_corner_y)
                right_down_corner = (r, right_up_corner_y)
                break
            elif is_black(left_pixel_inner) and is_black(right_pixel_inner):
                # se gli inner sono entrambi neri allora dobbiamo proseguire, prima pero' controlliamo che la riga sia nera
                if not rectLength == min_length:
                    for ir in range(left_up_corner_y + 2, right_up_corner_y - 1):
                        if is_white(image[r][ir]):
                            return False
                        else:
                            continue
            else:
                return False
        else:
            return False


    if left_down_corner[0] - left_up_corner_x + 1 < min_length:
        return False

    for i in range(left_down_corner[1], right_down_corner[1] + 1):
        current_pixel = image[left_down_corner[0]][i]
        if is_black(current_pixel):
            return False

    final_solution.append([left_up_corner, right_up_corner, left_down_corner, right_down_corner])
    return True


def is_black(tupla):
    BLACK = (0, 0, 0)
    return tupla == BLACK


def is_white(tupla):
    WHITE = (255, 255, 255)
    return tupla == WHITE

