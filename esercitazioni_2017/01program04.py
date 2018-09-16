'''Scrivere la funzione stringa_for_if(s) che,presa una stringa s contenente numeri interi separati da spazi,
ritorna la somma dei valori positivi presenti in s.

Ad esempio stringa_for_if('3 0     2  -6   ') restituisce 5


'''
import sys
import re


def stringa_for_if(s):
    print("removing non numeric characters in string: ", s)
    s = re.sub("[^0-9]"," ",s)
    print("after non numeric chars removal: ",s)
    summation = 0
    i= 0
    while i in range(len(s)):
        char = s[i]
        print("extracted: ",char,"at iteration ",i)
        if char=="-":
            i=jumped_space_index(s, i)
            print("jumping next iteration to avoid negative number, next space index at: ",i+1)
            continue
        if char.isdigit() and int(char)>0:
            print("current converted number is: ",char)
            summation+=int(get_whole_number(s,i))
        if(i==(len(s)-1)):
            break
        i=jumped_space_index(s, i)
        print("found positive number, moving to next number, next space index at: ",i+1)
    return summation

def get_whole_number(s,i):
    next_space_index = s.find(' ',i)
    if(next_space_index!=-1):
       whole_number = s[i:next_space_index]
    else:
        whole_number=s[i:]

    return whole_number


def jumped_space_index(s, i):
    for char in range(len(s)):
        spaceIndex =  s.find(' ',i)
        if(spaceIndex!=-1):
            print("next space index found at", spaceIndex)
            return spaceIndex+1
        else:
            return len(s)-1




if __name__ == "__main__":
    arg = sys.argv[1]
    print("you have entered",arg)
    print("the positive integer entered sum is:",stringa_for_if(arg))
