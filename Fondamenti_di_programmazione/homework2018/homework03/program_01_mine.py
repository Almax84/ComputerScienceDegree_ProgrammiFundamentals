
import immagini

def es1(fimg, fimg1):

    original_image = immagini.load(fimg)
    lunghezza = len(original_image)
    altezza = len(original_image)
    finalSolution = []

    loop_counter = 0
    for r in range(lunghezza):
        c = 0
        while c < altezza:
            loop_counter+=1
            if isWhite(original_image[r][c]) and isWhite(original_image[r][c+1]) and isWhite(original_image[r][c+2]):
                print("papabile")
            c+=3
    print(loop_counter)







def isBlack(tupla):
    BLACK = (0, 0, 0)
    return tupla == BLACK


def isWhite(tupla):
    WHITE = (255, 255, 255)
    return tupla == WHITE

if __name__ == '__main__':
    es1('e1_f7.png', 'test7.png')
