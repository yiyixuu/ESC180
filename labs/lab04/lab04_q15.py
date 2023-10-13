def duplicates(list):
    for i in range(len(list)-1):
        if list[i] == list[i+1]:
            return True
    return False

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(duplicates(list1))

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

print(duplicates(list1))