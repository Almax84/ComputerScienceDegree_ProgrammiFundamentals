'''Scrivere una funzione last(s, n) che ritorna una stringa che inizia con la
stringa s e finisce con n ripetizioni dell'ultimo carattere di s. Si assume
che s non e' vuota. Esempi:

last('ciao', 4)    ritorna  'ciaooooo'
last('ciao', 0)    ritorna  'ciao'
last('PYTHON', 3)  ritorna  'PYTHONNNN'

'''

def last(s, n):
	return s+s[len(s)-1:]*n
print(last('ciao', 4))
print(last('ciao', 0))
print(last('PYTHON', 3))
