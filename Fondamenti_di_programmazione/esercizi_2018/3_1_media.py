def media(vals):
    '''Scrivere una funzione media(vals) che prende in input una lista vals (i cui valori si assume siano
numeri) e ritorna la media dei suoi valori.'''
    base = len(vals)
    somma = 0
    for num in vals:
        somma+=num
    return somma / base
        
        