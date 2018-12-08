
import immagini 

################################################################################


class Colore:

    def __init__(self, r=0, g=0, b=0):
        if not Colore.isColorValid(r) or not Colore.isColorValid(g) or not Colore.isColorValid(b):
            raise ValueError('Colore non valido')
        self.r = r
        self.g = g
        self.b = b

    def utilizzo(self, sk):
        if not isinstance(sk, Skyline):
            raise ValueError("Skylines non valido")
        counter = 0


        for position, rect in sk.rect_map.items():
            if self == rect.colore:
                counter +=  1
        return counter

    def to_tuple(self):
        return (self.r, self.g, self.b)

    def brightness(self):
        return self.r + self.g + self.b
    
    @staticmethod #because i'm a java nostalgic
    def static_brightness(tupla):
        return tupla[0] + tupla[1] + tupla[2]
        
    @staticmethod #just for funzies
    def isColorValid(rgb_color):
        try:
            if not isinstance(rgb_color, int):
                return False
        except ValueError:
            return False
           
        if rgb_color < 0 or rgb_color > 255:
            return False;
        else:
            return True
        
################################################################################


class Rettangolo:

    def __init__(self, base, altezza, colore):
        try:
            if not isinstance(base, int):
                raise ValueError("Dimensioni non valide")
            elif not isinstance(altezza, int):
                raise ValueError("Dimensioni non valide")
        except ValueError:
            raise ValueError("Dimensioni non valide")
        
        if base <= 0 or altezza <= 0:
            raise ValueError('Dimensioni non valide')
        
        if not isinstance(colore, Colore):
            raise ValueError("Sfondo Rettangolo non valido")
        self.base = base
        self.altezza = altezza
        self.colore = colore
        self.skyline_ref = []

    def cancella(self):
        for ref in self.skyline_ref:
            local_skyline = ref[0]
            local_position = ref[1]
            if local_position in local_skyline.rect_map:
                del local_skyline.rect_map[local_position]
                local_skyline.to_draw = True
                max_width = 0
                max_height = 0
                #calcolo larghezza ed altezza del nuovo skyline
                for position, rect in local_skyline.rect_map.items():
                    if (position + rect.base) > max_width:
                        max_width = position + rect.base
                    if rect.altezza > max_height:
                        max_height = rect.altezza
                local_skyline.width = max_width
                local_skyline.height = max_height
        self.skyline_ref = []
        
    def brightness(self):
        return self.colore.brightness();

    def aggiungi_skyline_ref(self, skyline, position):
        self.skyline_ref.append((skyline, position))
        
    def to_tuple(self):
        return (self.base, self.altezza, self.colore);

################################################################################


class Skyline:

    def __init__(self, sfondo):
        if not isinstance(sfondo, Colore):
            raise ValueError("Sfondo Skyline non valido")
        self.sfondo = sfondo
        self.to_draw = True
        self.width = 0
        self.height = 0
        self.img_as_pixesl_array = []
        self.rect_map = {}  # dizionario di rettangoli presenti nello skyline, key: posizione (e' univoca) value: rettangolo

    def aggiungi(self, rettangolo, x):
        if not isinstance(rettangolo, Rettangolo):
            raise ValueError("Rettangolo non valido")
        if not isinstance(x, int):
            raise ValueError("Posizione non valida")
        if x < 0:
            raise ValueError("Posizione non valida")
        
        if self.sfondo == rettangolo.colore:
            return

        if x in self.rect_map:
            return

        # aggiungo il rettangolo
        self.rect_map[x] = rettangolo
        
        # ricalcolo massima lunghezza e altezza
        if (x + rettangolo.base) > self.width:
            self.width = x + rettangolo.base
        if rettangolo.altezza > self.height:
            self.height = rettangolo.altezza
        # aggiungo reference
        rettangolo.aggiungi_skyline_ref(self, x)
        self.to_draw = True

    def fondi(self, other):
        if not isinstance(other, Skyline):
            raise ValueError("Skyline non valido")
        for position, rect in other.rect_map.items():
            try:
                self.aggiungi(rect, position)
            except:
                pass
        self.to_draw = True

    def salva(self, fimg):
        if not isinstance(fimg, str):
            raise ValueError("FileImg is not a valid file name")
        if not (fimg.endswith('.png')  or fimg.endswith('.PNG')):
            raise ValueError("FileImg is not a valid file name")
        
        if self.to_draw == True:
            self.disegna()
        
        immagini.save(self.img_as_pixesl_array, fimg)

    def disegna(self):
        lst = [None] * self.width
        for i in range (self.width):
            lst[i] = [self.sfondo.to_tuple()] * self.height
            
        self.img_as_pixesl_array = lst
        # scorro i rettangoli da inserire in ordine di posizione, cosi se trovo stessa brightness comunque non lo inserisco
        for position, rect in sorted(self.rect_map.items()):
            for row in range(position, position + rect.base):
                for col in range(rect.altezza):
                    if self.img_as_pixesl_array[row][col] == self.sfondo.to_tuple():
                        self.img_as_pixesl_array[row][col] = rect.colore.to_tuple()
                    elif rect.colore.brightness() > Colore.static_brightness(self.img_as_pixesl_array[row][col]):
                        self.img_as_pixesl_array[row][col] = rect.colore.to_tuple()

        # rotate 3 times
        self.img_as_pixesl_array = list(zip(*self.img_as_pixesl_array[::-1]))
        self.img_as_pixesl_array = list(zip(*self.img_as_pixesl_array[::-1]))
        self.img_as_pixesl_array = list(zip(*self.img_as_pixesl_array[::-1]))
        
        self.to_draw = False
        
    def larghezza(self):
        return self.width

    def altezza(self):
        return self.height

    def edifici(self):
        return len(self.rect_map)

    def to_tuple(self):
        return (self.sfondo,)


# ################################################################################
