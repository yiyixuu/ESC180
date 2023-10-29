primes = []
primes.append(2)

global alive
alive = True

def check_next_prime(n):
    print('called')
    global alive
    start = primes[-1]+1
    print(start)
    is_prime = True
    while True:
        for i in range(2, start):
            print(start)
            if start%i == 0:
                is_prime = False
        if is_prime:
            primes.append(start)
            break
        else:
            start += 1

    print(primes)
    if not alive:
        print('Game is over')
        alive = False
    elif n != primes[-2]:
        print('Incorrect, game over')
    else: print('Correct')

check_next_prime(2)
check_next_prime(3)
check_next_prime(3)