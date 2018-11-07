import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program02 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, fname, expected):
        '''Implementazione del test
            - fname:    indirizzo del file di testo con i post del forum
            - expected: stringa risultante attesa
        '''
        result   = program.es2(fname)
        self.assertNotEqual( result, None, "La funzione non torna nessun risultato")
        self.check(type(result), list,     None, "il risultato non e' una lista")
        for line in result:
            self.check(type(line), dict,     None, "alcune righe della tabella non sono dizionari")
        self.check(result,       expected, None, "il risultato non e' corretto")
        return 1

    def test_fp1(self):
        '''...'''
        tab1= [ {'parola': 'hw1',       'I1': 6, 'I2': 3, 'I3': (3, '30')},
                {'parola': 'python',    'I1': 3, 'I2': 2, 'I3': (2, '30')},
                {'parola': 'hw2',       'I1': 2, 'I2': 1, 'I3': (2, '1')},
                {'parola': '30',        'I1': 1, 'I2': 1, 'I3': (1, '21')},
                {'parola': 'monti',     'I1': 1, 'I2': 1, 'I3': (1, '30')},
                {'parola': 'spognardi', 'I1': 1, 'I2': 1, 'I3': (1, '1')},
                {'parola': 'sterbini',  'I1': 1, 'I2': 1, 'I3': (1, '21')},
                ]
        return self.do_test('fp1.txt', tab1)

    def test_fp2(self):
        '''file casuale con 5000 post ciascuno con al piu' 200 parole'''
        tab2=[  {'parola': 'h', 'I1': 69312, 'I2': 4991, 'I3': (39, '9533')},
                {'parola': 'd', 'I1': 69250, 'I2': 4979, 'I3': (37, '27312')},
                {'parola': 'b', 'I1': 69032, 'I2': 4984, 'I3': (38, '26089')},
                {'parola': 'c', 'I1': 69001, 'I2': 4990, 'I3': (38, '28149')},
                {'parola': 'a', 'I1': 68929, 'I2': 4980, 'I3': (41, '27893')},
                {'parola': 'f', 'I1': 68829, 'I2': 4981, 'I3': (38, '41778')},
                {'parola': 'e', 'I1': 68760, 'I2': 4984, 'I3': (39, '10436')},
                {'parola': 'g', 'I1': 68391, 'I2': 4987, 'I3': (38, '23016')}]
        return self.do_test('fp2.txt', tab2)
        
    def test_fp3(self):
        '''file casuale con 20000 post ciascuno 10 righe di 10 parole'''
        tab3=[  {'parola': 'f', 'I1': 252020, 'I2': 14805, 'I3': (70, '159467')},
                {'parola': 'b', 'I1': 251050, 'I2': 14736, 'I3': (70, '88881')},
                {'parola': 'c', 'I1': 250370, 'I2': 14778, 'I3': (60, '116575')},
                {'parola': 'd', 'I1': 249680, 'I2': 14723, 'I3': (60, '123864')},
                {'parola': 'h', 'I1': 249390, 'I2': 14778, 'I3': (60, '143501')},
                {'parola': 'a', 'I1': 249360, 'I2': 14713, 'I3': (70, '117737')},
                {'parola': 'g', 'I1': 249190, 'I2': 14688, 'I3': (70, '129128')},
                {'parola': 'e', 'I1': 248940, 'I2': 14698, 'I3': (60, '110325')}]
        return self.do_test('fp3.txt', tab3)

    # def test_fp3b(self):
    #    '''file casuale con 100000 post ciascuno 10 righe di 10 parole'''
    #    tab4=[{'parola': 'h', 'I1': 1254590, 'I2': 73817, 'I3': (70, '30076')},
    #    {'parola': 'b', 'I1': 1251490, 'I2': 73729, 'I3': (70, '134887')},
    #    {'parola': 'e', 'I1': 1250600, 'I2': 73622, 'I3': (70, '313483')},
    #    {'parola': 'a', 'I1': 1250300, 'I2': 73476, 'I3': (80, '702758')},
    #    {'parola': 'd', 'I1': 1249940, 'I2': 73869, 'I3': (70, '431455')},
    #    {'parola': 'c', 'I1': 1249850, 'I2': 73671, 'I3': (80, '170445')},
    #    {'parola': 'f', 'I1': 1247410, 'I2': 73533, 'I3': (70, '114816')},
    #    {'parola': 'g', 'I1': 1245820, 'I2': 73504, 'I3': (70, '258097')}]
    #    return self.do_test('fp3b.txt', tab4)

if __name__ == '__main__':
    Test.main()

