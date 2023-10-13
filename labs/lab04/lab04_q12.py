def comp(l1, l2):
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [1, 2, 3]

print(comp(l1, l2))
print(comp(l1, l3))
print(comp(l2, l3))
