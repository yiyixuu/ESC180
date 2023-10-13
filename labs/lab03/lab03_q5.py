def gcd(n, m):
    gcd = 0

    for i in range(1, min(n, m)+1):
        if n%i == 0 and m%i == 0:
            gcd = max(gcd, i)

    return gcd

print(gcd(20, 30))