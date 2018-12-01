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
            image_row_column = image_row[c]
            if c + 3 < lunghezza and is_black(image_row_column) and is_black(image_row[c + 3]):
                c += 4
                continue

            if is_white(image_row_column):
                rect_corners = []
                get_rectangle_from_pixel(r, c, image, lunghezza, altezza, final_solution, rect_corners)
                if not len(rect_corners) == 0:
                    c = rect_corners[0][1]
                    continue

            c += 1

    for rect in final_solution:
        writeGreen(rect, image)
        writeRed(rect, image)

    immagini.save(image, fimg1)
    return len(final_solution)


def writeGreen(rect, image):
    left_up_corner = rect[0]
    right_up_corner = rect[1]
    left_down_corner = rect[2]
    right_downd_corner = rect[3]

    GREEN = (0, 255, 0)

    # lato sopra
    left_up_corner_x = left_up_corner[0]
    for c in range(left_up_corner[1], right_up_corner[1] + 1):
        image[left_up_corner_x][c] = GREEN

    # lato sotto
    left_down_corner_x = left_down_corner[0]
    left_downn_corner_y = left_down_corner[1]
    right_down_corner_y = right_downd_corner[1]
    for c in range(left_downn_corner_y, right_down_corner_y + 1):
        image[left_down_corner_x][c] = GREEN

    # LATO SINISTRO
    for r in range(left_up_corner_x, left_down_corner_x + 1):
        image[r][left_up_corner[1]] = GREEN

    # LATO DESTRO
    for r in range(right_up_corner[0], right_downd_corner[0] + 1):
        image[r][right_up_corner[1]] = GREEN


def writeRed(rect, image):
    RED = (255, 0, 0)
    left_up_corner = rect[0]
    right_up_corner = rect[1]
    left_down_corner = rect[2]

    for c in range(left_up_corner[1] + 1, right_up_corner[1]):
        for r in range(left_up_corner[0] + 1, left_down_corner[0]):
            # SCRIVO COLONNE
            image[r][c] = RED


def get_rectangle_from_pixel(r, c, image, lunghezza, altezza, final_solution, rect_corners):
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

    for y in range(left_up_corner_y + 1, lunghezza):
        current_pixel = image[left_up_corner_x][y]
        if is_black(current_pixel):
            return False
        # se il pixel nell'ultima colonna e' bianco quindi la riga continua verifichiamo se sotto e' bianco in tal caso e' un angolo in alto a destra e ci fermiamo
        # (left_up_corner[0] + 1) < altezza controlla che sotto sia presente una riga
        elif is_white(current_pixel) and (left_up_corner_x + 1) < altezza and is_white(image[left_up_corner_x + 1][y]):
            right_up_corner = (left_up_corner_x, y)
            rect_corners.append(right_up_corner)
            break

    if right_up_corner == -1:
        return False

    right_up_corner_y = right_up_corner[1]
    rect_length = right_up_corner_y - left_up_corner_y + 1
    # confrontiamo le colonne per capire la lunghezza
    if rect_length < min_length:
        # TOO SMALL
        return False

    # LETS GO DOWN NOW

    # scoperta la base di sopra scendiamo a destra e a sinistra verticalmente fino a che non troviamo 
    # un nero o la fine dell'immagine, se anche dall'altra parte e' nero allora abbiamo trovato i lati
    for x in range(left_up_corner_x + 1, altezza):
        left_pixel = image[x][left_up_corner_y]
        right_pixel = image[x][right_up_corner_y]

        if is_white(left_pixel) and is_white(right_pixel):
            # se sono entrambi bianchi allora va bene, controlliamo solo che non sia una potenziale riga bianca
            left_pixel_inner = image[x][left_up_corner_y + 1]
            right_pixel_inner = image[x][right_up_corner_y - 1]
            if is_white(left_pixel_inner) and is_white(right_pixel_inner):
                # e' una possibile riga bianca quindi e' la base del rett
                left_down_corner = (x, left_up_corner_y)
                right_down_corner = (x, right_up_corner_y)
                break
            elif is_black(left_pixel_inner) and is_black(right_pixel_inner):
                # se gli inner sono entrambi neri allora dobbiamo proseguire, prima pero' controlliamo che la riga sia nera
                #if not rect_length == min_length:
                    for y in range(left_up_corner_y + 2, right_up_corner_y - 1):
                        if is_white(image[x][y]):
                            return False
                        else:
                            continue
            else:
                # se sono uno bianco e uno nero allora non va bene
                return False
        else:
            # se sono entrambi neri o uno bianco e uno nero allora non puo' essere un rettangolo
            return False

    # if left_up_corner == -1 or right_up_corner == -1 or left_down_corner == -1 or right_down_corner == -1:
    #     return False

    if left_down_corner[0] - left_up_corner_x + 1 < min_length:
        # print("Rettangolo troppo poco alto")
        return False

    # controlliamo la base sia interamente bianca
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


if __name__ == '__main__':
    es1('e1_f5.png', 'test5.png');
