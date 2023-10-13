def string_match(a, b):
    return sum([1 for i in range(min(len(a), len(b)) - 1) if a[i:i+2] == b[i:i+2]])