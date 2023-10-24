# part a

def prod(L):
    product = 1
    for i in L:
        product *= i
    return product

# part b

def duplicates(list0):
    for i in range(len(list0)-1):
        if list0[i] == list0[i+1]:
            return True
    return False