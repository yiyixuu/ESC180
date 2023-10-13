# val = 0

# for n in range(999999):
#     val += ((-1)**n/(2*n+1))

# print(val)

# print(4*val)

val = 0

for i in range(1,99999999,2):
    val += 1/i if i%4 == 1 else -1/i

print(val)
print(val*4)