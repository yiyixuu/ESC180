L = [[[1, 2], [3, 4]]]
L1 = L[:]
L1[0][0] = 5
L1[0][1][0] = 6
print(L1)
print(L)