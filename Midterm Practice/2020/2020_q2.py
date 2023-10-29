def sum_cubes_num_terms(n):
    sum = 0
    for i in range(1, n+1):
        if sum + i*i*i >= n:
            return i
        else:
            sum += i*i*i
