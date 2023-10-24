def get_perfect_squares(n):
    result = []
    for i in range(n+1):
        if i**2 <= n: result.append(i**2)
    return result


print(get_perfect_squares(4))