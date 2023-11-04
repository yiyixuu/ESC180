L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def format(L):
    L1 = []
    for i in range(len(L)):
        L1.append(L[i])
    
    L1[0] = [100, 100, 100]
    return L1


print(format(L))
print(L)