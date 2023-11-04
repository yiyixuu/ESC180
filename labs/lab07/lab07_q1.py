L = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

def modify_list(L):
    L[0] = [10, 11, 12] 
    L[0][0] = 100 

modify_list(L)
print(L)

