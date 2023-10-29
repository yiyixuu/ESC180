def moving_average(measurements):
    list = []
    for i in range(1, len(measurements)-1):
        list.append((measurements[i-1]+measurements[i]+measurements[i+1])/3)
    return list
