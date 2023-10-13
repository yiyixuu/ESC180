def next_day(y, m, d):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        if d == 31:
            if m == 12:
                return y+1, 1, 1
            else:
                return y, m+1, 1
        else:
            return y, m, d+1
    elif m in [4, 6, 9, 11]:
        if d == 30:
            return y, m+1, 1
        else:
            return y, m, d+1
    else:
        if y%4 == 0 and (y%100 != 0 or y%400 == 0):
            if d == 29:
                return y, m+1, 1
            else:
                return y, m, d+1
        else:
            if d == 28:
                return y, m+1, 1
            else:
                return y, m, d+1
            
print(next_day(2019, 12, 31))
print(next_day(2020, 2, 28))
print(next_day(2019, 2, 28))
print(next_day(2100, 2, 28))
            

