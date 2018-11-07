import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program03 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, fname, expected):
        '''Implementazione del test
            - fname:    indirizzo del file di testo con percorsi ed insieme di quadrati
            - expected: numero intero atteso
        '''
        result   = program.es3(fname)
        self.assertNotEqual( result, None, "La funzione non torna nessun risultato")
        self.check(type(result), int,     None, "il risultato non e' un intero")
        self.check(result,       expected, None, "il risultato non e' corretto")
        return 1

    def test_mp1(self):
        '''...'''
        return self.do_test('mp1.txt', 4)

    def test_mp2(self):
        '''istanza in cui la zona circoscritta e' un rettangolo di base 10000 e altezza 20
        e l'insieme contiene 9000 quadrati interni equispaziati ad altezza 5 e 10 e 15
        e 1000 quadrati esterni equispaziati ad altezza 25 '''
        return self.do_test('mp2.txt', 3000)
        
    def test_mp3(self):
        '''istanza in cui 
        -il primo cammino e' formato da una un'alternanza di 2 passi 
        in alto e due passi a destra per 5000 volte. 
        -Il secondo cammino parte con 4 passi a destra e poi ha un alternanza di due passi 
        in alto e due a destra per 5000-2 volte e 4 passi in alto per finire.
        L'insieme contiene 3000 quadrati (x,x-4),(x,x),(x,x+4) dove x e' qualunque multiplo di 10
        fino a 10000.
        '''
        return self.do_test('mp3.txt', 1000)
        
    def test_mp4(self):
        '''istanza in cui 
        la zona circoscritta e' un rettangolo di base 4 e altezza 100000
        l'insieme dei quadrati e' composto da quadrati del tipo (3,x) e (5,x) e (8,x)
        con x multiplo di 1000 e non superiore a 100000
        '''
        return self.do_test('mp4.txt', 200)




if __name__ == '__main__':
    Test.main()

