def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    
    return a + multiply(a, b-1)

def exponent(base, exp):
    if exp == 0 or base == 1:
        return 1
    
    return base * exponent(base, exp-1)

def print_numbers(n):
    if n == 0:
        print(0)
    else:
        print(n)
        print_numbers(n-1)

def print_numbers_reverse(n):
    if n == 0:
        print(0)
    else:
        print_numbers_reverse(n-1)
        print(n)

def reverse_string(s):
    if len(s) == 1:
        return s
    return s[-1] + reverse_string(s[:-1])

def is_prime(n, i=1):
    if n <= 2:
        return n == 2
    if n%i == 0 and i != 1 and i != n:
        return False
    if n == i:
        return True
    
    return is_prime(n, i+1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)