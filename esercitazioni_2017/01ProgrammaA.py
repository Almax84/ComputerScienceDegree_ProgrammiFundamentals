'''Scrivere una funzione hertz(k, m, g) che ritorna il numero di hertz che
equivalgono alla somma di k KHz, m MHz e g GHz. Esempi

hertz(0, 1, 0)  ritorna   1000000
hertz(3, 2, 1)  ritorna   1002003000


'''
def hertz(kh, mh, gh):
    return (kh+mh*1000+gh*1000000)*1000


print(hertz(0, 1, 0))
print(hertz(3, 2, 1))

