def lookup(L, key):
    for i in L:
        if i[1] == key:
            return i[0]

print(lookup([["CIV", 92], ["180", 98], ["103", 99], ["194", 95]], 99))