def greeting(s):
    global s
    s = "Happy " + s
    print(s)
res = greeting(s)
print(res)