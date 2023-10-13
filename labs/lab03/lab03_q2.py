def my_sqrt(x):
    sqr = x**0.5
    return sqr

def my_print_square(x):
    sqr = my_sqrt(x)
    print(sqr)

# q4
def display_current_value():
    print("Current value: " + str(val))

# q5
def add(to_add):
    global val
    val += to_add

    stack.append(val)
    stack2.append(val)

#q6
def mult(to_mult):
    global val
    val *= to_mult

    stack.append(val)
    stack2.append(val)


# q7
def div(to_div):
    global val
    val /= to_div

    stack.append(val)
    stack2.append(val)


# q8
def setM():
    global mem, val
    mem = val

def getM():
    global mem, val
    val = mem

# q9
def undo():
    global val
    stack.pop()
    val = stack[len(stack)-1]

def undo2():
    global val
    stack2.pop()
    stack2.pop()
    val = stack[len(stack2)-1]
    
if __name__ == "__main__":
    val = 0
    mem = 0 # q8

    stack = []
    stack2 = []
    res = my_sqrt(25) # sqr is set on this line

    my_print_square(25)
    # print(sqr) doesn't work because sqr is a local variable in my_sqrt(x), not a global variable and it cannot be accessed in main
    # can make sqr a global variable by declaring it outside of the function to make print(sqr) not an error or doing global sqr in the function

    res = my_print_square(25)
    # print(res) doesn't work because my_print_square(25) doesn't return anything, so res does not have a value

    # q3
    print("Welcome to the calculator program.")
    display_current_value()

    add(3) #q5
    display_current_value()

    mult(4) #q6
    display_current_value()

    div(6) #q7
    display_current_value()

    # div(0) div by 0 error
    # display_current_value()

    undo2()
    display_current_value()