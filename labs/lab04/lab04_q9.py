def gcd(n, m):
    while n%m != 0:
        n, m = m, n%m
    return m

def simplify_fraction(n, m):
    d = gcd(n, m)
    print(d)
    n//=d
    m//=d
    print(n) if m == 1 else print(str(n) + "/" + str(m))

simplify_fraction(4, 8)