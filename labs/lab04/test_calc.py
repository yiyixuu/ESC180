import lab02

if __name__ == '__main__':
    lab02.initialize()

    lab02.add(42)
    lab02.subtract(17)

    if lab02.get_current_value() == 42-17:
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    lab02.initialize()
    lab02.add(5)
    lab02.subtract(10)
    lab02.multiply(2)

    if lab02.get_current_value() == (5-10)*2:
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    lab02.initialize()
    lab02.add(10)
    lab02.divide(0)

    if lab02.get_current_value() == 'ERROR':
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    