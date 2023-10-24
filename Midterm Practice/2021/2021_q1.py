# part (a)

for i in range(100,201,2): print(i)

# part (b)

def last_ind(L, e):
    for i in range(len(L)-1, -1, -1):
        if L[i] == e: return i
    return None
