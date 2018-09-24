def space(stringa,n_spaces):
    '''Scrivere una funzione space(s, k) che prende in input una stringa s e un intero k e ritorna una nuova
stringa che ha i caratteri di s separati da k spazi. Ad esempio
space('ciao ciao', 1) ritorna la stringa 'c i a o c i a o'''
    return_string = ''
    for char in stringa:
        if char != ' ':
            return_string+=char+n_spaces*' '
 #       else:
 #           return_string+=char
    return return_string
    


