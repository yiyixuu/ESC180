def list_to_str(list):
    res = "["
    for i in range(len(list)):
        if i == len(list)-1:
            res += str(list[i])
        else:
            res += (str(list[i]) + ", ")


    res += "]"
    return res

list0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(str(list0))

print(list_to_str(list0))