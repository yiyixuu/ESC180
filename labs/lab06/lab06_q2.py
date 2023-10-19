def get_nums(L):
    res = []
    for i in L:
        for j in i:
            if type(j) == int:
                res.append(j)
    return res


print(get_nums([["CIV", 92], ["180", 98], ["103", 99], ["194", 95]]))
