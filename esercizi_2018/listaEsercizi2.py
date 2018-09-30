def palindromi_check(s1,s2):
    if len(s1) != len(s2):
        return False

    for i,v in enumerate(s1):
        if s1[i] != s2[-i-1]:
            return False
        
    return True

#print(palindromi_check('anna','anna'))
    

    '''la funzione deve restire True se la  stringa s2 e' un anagramma della
    stringa s1 (False altrimenti)'''

   # anagrams apprently DO NOT take white spaces into consideration. So
   # google says    
def es1(s1,s2):
    if len(s1.replace(" ","")) != len(s2.replace(" ","")):
        return False
   
    for i,v in enumerate(s2):
        if v not in s1 and v!=' ':
            return False
    return True

#print(es1('anna','nana')) #must return True
#print(es1('anna','nani')) #must return False
#print(es1('anna','annna')) #must return False
#print(es1('conversation','voices rant on'))
#print(es1('dormitory','dirty room'))  
#print(es1('dynamite','may it end'))     

#######################################################
def es2(s):
    alfabeto_map={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"l":10,"m":11,"n":12,"o":13,"p":14,"q":15,"r":16,"s":17,"t":18,"u":19,"v":20,"z":21}
    return_string = ''
    counter = 0
    for index,char_in_s in enumerate(s,1):
        if char_in_s != " ":
            char_numeric_value=alfabeto_map.get(char_in_s.lower())
            counter+=char_numeric_value
        else:
            return_string +=str(counter)+" "
            counter = 0
        if index == len(s): #enumerate set to count from 1
            return_string +=str(counter)
    return return_string

#print(es2('Angelo Monti Andrea Sterbini e Angelo Spognardi')) #'48 63 39 88 5 48 93'
#######################################################

def es3(st1,st2):
    '''la funzione stampa le sottostringhe di almeno due caratteri comuni alle due stringhe
    datein input. Le sottostringhe vanno stampate in ordine lessicografico crescente e 
    separate tra loro da un semplice spazio. Nota se una stessa sottostringa 
    compare piu' volte va stampata un'unica volta'''
    len_st1 = len(st1)
    result_list = []
    for i in range(2,len_st1):
        for j in range(len_st1):
            #i = substring length e.g. if i = 2 and j =0 find all substrings of length 2
            st1_substring = st1[j:j+i]
            if st1_substring in st2 and st1_substring not in result_list and len(st1_substring)>=2:
                result_list.append(st1_substring)
    return ' '.join(sorted(result_list))
        
#print(es3('programmazione', 'progettazione'))
    
    
'''  
>>> es3('programmazione', 'progettazione')
az azi azio azion io ion og on pr pro prog ro rog zi zio zion 

>>> es3('ananas','ananas')
an ana anan anana na nan nana 
'''
#######################################################

#in crittografia il cifrario di Cesare e' una delle tecniche di cifratura piu' semplice. 
# Dato il testo in chiaro  ed un intero x>=0 ciascun   carattere c tra 'a' e 'z' che occorre 
# nel  testo viene codificato con c' dove c' e' il carattere 
# che  troviamo x posti a destra di  c nell'ordinamento alfabetico 
# Nota che si considera l'ordinamento circolare (i.e. a destra di 'z' troviamo  'a')
# i caratteri al di fuori dell'intervallo 'a' ..'z' non vanno modificati.

def es4(st, k):
    '''la funzione restituisce la stringa cifrata che si ottiene applicando alla stringa st il codice 
    Cesare con intero k quando l'alfabeto e' quello italiano di 21 lettere
    '''
    alfabeto_map={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"l":10,"m":11,"n":12,"o":13,"p":14,"q":15,"r":16,"s":17,"t":18,"u":19,"v":20,"z":21}
    result_string =''
    index = 0
    if k>21:
        index=k%21
    else:
        index=k
        
    for i,char in enumerate(st,1):
        original_char_index=alfabeto_map.get(char)
        next_index=original_char_index+index
        
        if next_index > 21:
            next_index=next_index%21
            
        for alphabet_char, i in alfabeto_map.items():
            if i == next_index:
                result_string += alphabet_char
                break
    return result_string
    
    
    

#print(es4('america',1))
#print(es4('america',26))
#print(es4('zanna',1))
#print(es4('zanna',200))
'''
>>> es4('america',1)
'bnfsjdb'

>>> es4('america',26)

>>> es4('zanna',1)
'aboob'

>>> es4('zanna',200)
'tuiiu'

>>> es4('Angelo Monti Via Salaria 113 stanza 335',1)
'Aohfmp Mpoul Vlb Sbmbslb 113 tuboab 335'

'''
#################################################

def es5(testo):
    
    splitted_words = testo.split('\n')
    number_of_words = len(splitted_words)
    
    #find longest word
    longest = 0
    for word in splitted_words:
        word_length = len(word)
        if word_length > longest:
            longest = word_length
            
    row_string = ''        
    for i in range(longest):
        
        for j in range(number_of_words):
            if i < len(splitted_words[j]):
                row_string+=splitted_words[j][i]
            else:
                row_string+=' '
        row_string += '\n'
        
   #print(row_string)

test = """fondamenti
di
programmazione"""
es5(test)
    
   # '''la funzione restituisce  un nuovo testo dove ogni riga e diventata una colonna.
   # Ad esempio per il testo:
   # """fondamenti 
  #  di 
  #  programmazione"""
  #  viene restituito il testo:
  #  """
   # fdp
  #  oir
  #  n o
  #  d g
  #  a r
  #  m a
  #  e m
  #  n m
  #  t a
  #  i z
  #    i
  #    o
  #    n
  #    e"""
  #  '''
'''    
>>> testo1='cane\nbue\ncavallo'
>>> testo2=es5(testo1)
>>> testo2
'cbc\naua\nnev\ne a\n  l\n  l\n  o'
>>> print(testo2)
cbc
aua
nev
e a
  l
  l
  o

>>> testo1='Angelo\nMonti\nVia Salaria 133\nRoma'
>>> print(es5(testo1))
AMVR
noio
gnam
et a
liS 
o a 
  l 
  a 
  r 
  i 
  a 
    
  1 
  3 
  3 
'''
#################################################

def es6(ls, c):
    ''' 
    progettare la funzione es6(ls,c) che: 
    - riceve  in input una lista di parole ls ed un carattere c
    - cancella da ls le parole che contengono il carattere c (sia in maiuscolo che in minuscolo)
    - restituisce il numero di parole cancellate da ls. 
    Nota che al termine della funzione la lista passata come parametro deve risultare modificata
    (ricorda che le liste sono mutabili). 
     ESEMPI:
     Se ls=[ 'Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio','Luca', 'Ugo'] e c='a'
     la funzione restituisce 5 e la lista ls diventa ['Lucio','Ugo']  
     Se ls=[ 'Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio', 'Luca','Ugo'] e c='G'
     la funzione restituisce 2 e la lista ls diventa ['Andrea', 'Fabio', 'Francesco', 'Lucio','Luca']
    '''
    # inserisci qui il tuo codice.
    count = 0
    c = c.lower()
    removed_list = []
    
    for word in ls:
        if c in word.lower():
            removed_list.append(word)
            count+=1
            
    for word_removed in removed_list:
        ls.remove(word_removed)
        
    
    return count,ls
        
ls=[ 'Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio', 'Luca','Ugo']
c = 'G'
#print(es6(ls,c))

'''
>>>lista= [ 'Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio','Luca', 'Ugo']    
>>> es6(lista, 'G')
2
>>> print(lista)
['Andrea', 'Fabio', 'Francesco', 'Lucio', 'Luca']

>>> lista= [ 'Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio','Luca', 'Ugo']
>>> es6(lista,'f')
2
>>> print(lista)
['Angelo', 'Andrea', 'Lucio', 'Luca', 'Ugo']
'''    
#################################################

def es7(cs, ds):
    '''Scrivere una funzione es7(cs, ds) che prende in input una lista cs di 
    stringhe che rappresentano codici e una lista ds di stringhe s tali che i primi
    due caratteri di s contengono la lunghezza n di un codice i successivi n caratteri 
    contengono un codice e i successivi 8 caratteri contengono una data nel formato
    ggmmaaaa, la funzione deve modificare la lista cs in modo che per ogni codice di 
    cod in cs se una stringa s di ds ha codice cod allora cod e' sostituito dai tre 
    valori numerici della data di s, altrimenti cod e' rimosso. Per maggiore 
    chiarezza, ogni stringa di ds ha il formato nnc...cggmmaaaa, dove la lunghezza
    del blocco c...c e' uguale al numero specificato da nn. Si assume che non ci sono
    due stringhe in ds con lo stesso codice. 
    Ad esempio:
    '''
    #inserire qui il vostro codice
    return_list = []
    for cs_element in cs:
        for s in ds:
            code_length = int(s[0:2])
            code = s[2:code_length+2]
            if code == cs_element:
                return_list.append(int(s[-8:-6]))
                return_list.append(int(s[-6:-4]))
                return_list.append(int(s[-4:]))
                
                
    lista_cs = return_list
    return lista_cs
                
#lista_ds=['03BBB01122013', '04001B11092011', '10012345678924081999', '03ABC27042005']
#lista_cs=['ABC', '001B', '123', '0123456789']
#print(es7(lista_cs,lista_ds))
#cs = ['0', 'aa', 'bbb', 'cccc', 'bbb', '0']
#print(es7(cs,['01a24121999', '03bbb28081944', '02aa04042003', '04cccC23011977', '01025062002']))
#a = ['A', 'B', 'C', '1', '2', '3', '4', '5']
#print(es7(a,['01E18101987', '01126111995', '02Aa22052009', '01B27081966', '01531031975']))
'''
>>> lista_cs=['ABC', '001B', '123', '0123456789']
>>> lista_ds=['03BBB01122013', '04001B11092011', '10012345678924081999', '03ABC27042005']
>>> es7(lista_cs,lista_ds)
>>> print(lista_cs)
[27, 4, 2005, 11, 9, 2011, 24, 8, 1999]

>>> cs = ['0', 'aa', 'bbb', 'cccc', 'bbb', '0']
>>> es7(cs,['01a24121999', '03bbb28081944', '02aa04042003', '04cccC23011977', '01025062002'])
>>> cs
[25, 6, 2002, 4, 4, 2003, 28, 8, 1944, 28, 8, 1944, 25, 6, 2002]

>>> a = ['A', 'B', 'C', '1', '2', '3', '4', '5']
>>> es7(a,['01E18101987', '01126111995', '02Aa22052009', '01B27081966', '01531031975'])
>>> a
[27, 8, 1966, 26, 11, 1995, 31, 3, 1975]
'''
#################################################

def es8(insi):
    '''
    progettare la funzione es8(insi) che: 
    - riceve  in input un insieme di numeri naturali 
    - trova le coppie di interi nell'insieme che sono tra loro coprimi
    - restituisce l'insieme con tutte le coppie di coprimi trovate. 
      Nell'insieme restituito le coppie di co-primi devono essere  rappresentate tramite tuple.
      Il co-primo piu' piccolo di ciascuna tupla  deve comparire nella prima coordinata della tupla.
     Si ricorda che:.
     Due numeri interi a e b si dicono co-primi, se e solo se essi non hanno nessun 
     divisore comune eccetto 1 e - 1, o, equivalentemente, se il loro massimo comun divisore è 1.
     ESEMPIO:
     se insi={ 6, 35, 49} la funzione restituisce l'insieme contenente le sole due  
     tuple (6,35) e(6,49). Infatti delle 3 coppie di interi che e' possibile formare 
     con gli elementi di insi, la coppia data da 35 e 49 non e' una coppia di coprimi 
     (i due numeri sono entrambi divisibili per 7).
    '''
    # inserisci qui il tuo codice.
    return_list = []
    for index, num in enumerate(insi): #ora definisco le coppie
        for index2, num2 in enumerate(insi,index+1):
            greatest = max(num,num2)
            smallest = min(num,num2)
            divisore_num = []
            divisore_num2 = []
            for index3 in range(2,greatest):
                if num % index3 == 0 and index3 != num:
                    divisore_num.append(index3)
                if num2 % index3 == 0 and index3 != num2:
                    divisore_num2.append(index3)
                hasCommonDivisore = False
            for divisore_num_1 in divisore_num:
                if divisore_num_1 in divisore_num2:
                    hasCommonDivisore = True
            if not hasCommonDivisore and num != num2 and [smallest,greatest]  not in return_list:
                return_list.append([smallest,greatest])
    
    return tuple(return_list)
    
    
print(es8({17,2,13,31}))
print(es8({45,15,30,105} ))


'''    
>>> es8({17,2,13,31})
{(2, 31), (17, 31), (13, 17), (2, 13), (13, 31), (2, 17)}

>>> es8({45,15,30,105} )
set()
'''
#################################################

def es9(la,lb):
    '''Scrivere una funzione es(la, lb) che prende in input due liste contenenti
    uno stesso numero di stringhe, modifica le liste confrontando le stringhe che
    occorrono nella stessa posizione nelle due liste e cancella dalla lista la
    minore delle due,  se  sono uguali, sono cancellate entrambe.
    '''
    # inserisci qui il tuo codice.



'''
>>> a = ['a0', 'b1', 'a2', 'b3', 'a4', 'b5']
>>> b = ['b0', 'a1', 'b2', 'a3', 'b4', 'b5']
>>> es9(a,b)
>>> a
['a0', 'a2', 'a4']
>>> b
['a1', 'a3']


>>> lista1 = ['1', '2', '3', '4', '5', '6']
>>> lista2 = ['4', '5', '6', '1', '2', '3']
>>> es9(lista1,lista2)
>>> lista1
['1','2','3']
>>> lista2
['1','2','3']

>>> la = ['orso', 'tigre', 'lupo', 'balena', 'elefante']
>>> lb = ['cigno', 'gatto', 'cane', 'oca', 'coniglio']
>>> es9(la,lb)
>>> la
['balena']
>>> lb
['cigno', 'gatto', 'cane', 'coniglio']
'''
#################################################

def es10(ls,k):
    '''
    Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
    Scrivere una funzione es(ls,k) che, presa una lista ls di interi  ed un intero 
    non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
    NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

    ad esempio per ls = [121, 4, 37, 441, 7, 16] 
    modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della 
    funzione si avra' che la lista ls=[16]
    ATTENZIONE: Se il programma non termina entro 5 secondi il punteggio dell'esercizio e' zero.
   '''
   #inserite qui il vostro codice




'''
>>> lista=[70,330,293,154,128,113,178]
>>> es10(lista,6)
[293, 113]
>>> print(lista)
[70,154,128]

>>> lista=[340887623,26237927,2491,777923,5311430407,6437635961,82284023]
>>> es10(lista,4)
[26237927]
>>> lista
[]

>>> lista=[10000000116, 10000000431, 10000000469, 10000000548, 10000000697, 10000000711, 10000000768, 10000000924]
>>> es10(lista,16)
[10000000469,10000000711]
>>> lista
[10000000116, 10000000548, 10000000768]
'''