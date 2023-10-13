def drink_coffee():
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global too_much_coffee

    if current_time - last_coffee_time2 <= 120:
        too_much_coffee = True
    else:
        last_coffee_time2 = last_coffee_time
        last_coffee_time = current_time

def study(minutes):
    global current_time
    global knols
    global last_coffee_time
    global too_much_coffee

    if not too_much_coffee:
        if last_coffee_time == current_time:
            knols += 10 * minutes
        else:
            knols += 5 * minutes

    current_time += minutes

def initialize():
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols
    global i

    too_much_coffee = False
    current_time = 0
    knols = 0
    last_coffee_time = -100
    last_coffee_time2 = -100
    i=0


def debug():
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols
    global i

    # print("i: " + str(i))
    # print("too_much_coffee: " + str(too_much_coffee))
    # print("current_time: " + str(current_time))
    # print("last_coffee_time: " + str(last_coffee_time))
    # print("last_coffee_time2: " + str(last_coffee_time2))
    print("knols: " + str(knols))
    # print("")

    i+=1

if __name__ == "__main__":
    initialize()
    debug()
    study(60) # knols = 300
    debug()
    study(20) # knols = 400
    debug()
    drink_coffee() # knols = 400
    debug()
    study(10) # knols = 500
    debug()
    drink_coffee() # knols = 500
    debug()
    study(10) # knols = 600
    debug()
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes
    debug()
    study(10) # knols = 600
    debug()