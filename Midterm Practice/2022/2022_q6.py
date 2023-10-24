import math

global pi
pi = math.pi

def next_digit_pi():
    global pi
    result = int(pi)
    pi -= result
    pi *= 10
    return result

print(next_digit_pi())
print(next_digit_pi())
print(next_digit_pi())
print(next_digit_pi())
print(next_digit_pi())
print(next_digit_pi())
