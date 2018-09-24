def invest(capitale,interesse,numero_anni):
    '''Scrivere una funzione invest che prende in input un capitale C , un interesse annuale i e un numero di
anni n e ritorna il capitale maturato dopo un investimento di n anni all'interesse i . Ad esempio, se C
= 1000 , i = 10 e n = 2 , la funzione ritorna 1210 .'''
    for i in range(numero_anni):
        capitale +=capitale*interesse/100
    return capitale