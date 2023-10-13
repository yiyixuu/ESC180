def gcd(n, m):
    i = min(n, m)

    while i > 0:
        if n%i == 0 and m%i == 0:
            return i
        i -= 1

def simplify_fraction(n, m):
    d = gcd(n, m)
    n//=d
    m//=d
    print(n) if m == 1 else print(str(n) + "/" + str(m))

simplify_fraction(20, 7)