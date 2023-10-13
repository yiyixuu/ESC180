def list1_start_with_list2(list1, list2):

    if len(list2) > len(list1):
        return False

    for i in range(len(list2)):
        if list1[i] != list2[i]:
            return False

    return True

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3]

print(list1_start_with_list2(list1, list2))

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 9, 3]

print(list1_start_with_list2(list1, list2))
