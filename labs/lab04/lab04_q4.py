val = 0

n = 0
while n < 999999:
    val += ((-1)**n/(2*n+1))
    n += 1

# print(val)
# print(val*4)






val = 0

i = 1

while i <= 6:
    val += 1/i if i%4 == 1 else -1/i
    i+=2

# print(val)
print(val*4)