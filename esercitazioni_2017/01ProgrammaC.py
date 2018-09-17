'''Scrivere una funzione bkm(s) che presa in input una stringa s che contiene 
numeri interi non negativiseparati tra loro da una virgola ed uno spazio, ritorna una nuova stringa in cui   ogni numero in s
e' espresso in  B, KBe  MB nel formato illustrato dal seguente le varie rappresentaizoni sono separate nella stringa da una virgola e uno spazio
esempio:
    
bkm( '500, 1024, 2000, 1100000' )  ritorna
     '0MB 0KB 500B, 0MB 1KB 0B, 0MB 1KB 976B, 1MB 50KB 224B'
    
'''

def bkm(lst):
    stringList = lst.split(',')
    kb = 2**10
    mb = 2**20
    result = ''
    for s in stringList:
        remainder = 0
        number = int(s.strip())
        megabytes = number/mb
        megaAsInt = int(megabytes)
        result+= str(megaAsInt) + 'MB' + ' '
        remainder = convert(mb, megaAsInt, megabytes, number, remainder)


        kilobytes = remainder/kb
        kiloAsInt = int(kilobytes)
        result+= str(kiloAsInt) + 'KB' + ' '

        remainder = convert(kb, kiloAsInt, kilobytes, number, remainder)

        
        result+=str(int(remainder))+'B'+','

    return result


def convert(kb, kiloAsInt, kilobytes, number, remainder):
    if kiloAsInt != 0:
        remainder = (kilobytes - kiloAsInt) * kb
    else:
        remainder = number
    return remainder


print(bkm( '500, 1024, 2000, 1100000' ))
