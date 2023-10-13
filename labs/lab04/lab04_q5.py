def gcd1(n, m):
    gcd = 0

    for i in range(1, min(n, m)+1):
        if n%i == 0 and m%i == 0:
            gcd = max(gcd, i)

    return gcd


def gcd2(n, m):
    i = min(n, m)

    while i > 0:
        if n%i == 0 and m%i == 0:
            return i
        i -= 1

print(gcd1(20, 30))
print(gcd2(20, 30))
