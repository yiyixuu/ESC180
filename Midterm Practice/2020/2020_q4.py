def match(pattern, text):
    text *= 2
    for i in range(len(text)-len(pattern)+1):
        if pattern == text[i:i+len(pattern)]:
            return True
    return False