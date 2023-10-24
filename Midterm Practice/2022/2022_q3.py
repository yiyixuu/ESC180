cnt = 0

while True:
    order = str(input("What is your order? "))

    if not (order.upper() == "PUMPKIN SPICE LATTE"):
        cnt+=1
    else:
        print(cnt)
        break


