import math


def figs(n):
    terms = 0
    i = 1
    val = 0
    
    while int(math.pi*(10**(n-1))) != int((4*val)*(10**(n-1))):

        val += 1/i if i%4 == 1 else -1/i
        i+=2
        terms += 1

    return terms

print(figs(2))


    

