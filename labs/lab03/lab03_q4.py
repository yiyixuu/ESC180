import sys

val = 0

for n in range(999999):
    val += ((-1)**n/(2*n+1))

print(val)

print(4*val)