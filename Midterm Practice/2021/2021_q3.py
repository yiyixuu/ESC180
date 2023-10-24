import sys

def lcm(a,b,c,d):
    for i in range(max(a,b,c,d), sys.maxsize):
        if i%a == i%b == i%c == i%d == 0: return i
