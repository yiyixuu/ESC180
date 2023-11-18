import time

def binary_search(L, e):
    low = 0
    high = len(L)-1
    cnt = 0
    while high-low >= 2:
        cnt += 1
        mid = (low+high)//2 #e.g. 7//2 == 3
        # print(L[low], L[mid], L[high])
        if L[mid] > e:
            high = mid-1
        elif L[mid] < e:
            low = mid+1
        else:
            return mid, cnt
    if L[low] == e:
        return low, cnt
    elif L[high] == e:
        return high, cnt
    else:
        return None
        
# print(binary_search([1,2,3,4,5,6,7,8,9,10], 5)) # prints (4, 1)

# 2c
# make a list where e is always the middle element

def create_best_case_list(e, length):
    L = []
    for i in range(length):
        if i < length // 2:
            L.append(e - length // 2 + i)
        elif i > length //2:
            L.append(e + i - length // 2)
        else:
            L.append(e)
    return L

def create_worse_case_list(e, length):
    L = [i for i in range (e, length+e)]
    return L


e = 0
length = 10
# L = create_best_case_list(e, length)
# print(L)
# print(binary_search(L, e))

# for i in range(7):
#     L = create_worse_case_list(e, length)
#     # print(L)
#     start = time.time()
#     # print(binary_search(L, e))
#     binary_search(L, e)
#     end = time.time()
#     print(f'runtime for length {length}, {end-start}')
#     length*=10

