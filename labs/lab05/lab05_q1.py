def count_evens(L):
    cnt = 0
    for i in L:
        if i%2 == 0:
            cnt += 1
    return cnt

print(count_evens([1,2,3,4,5,6,7,8,9,10]))