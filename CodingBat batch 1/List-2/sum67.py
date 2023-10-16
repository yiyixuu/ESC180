def sum67(nums): 
    return (lambda l: sum([l[i] if l.index(7, i+1) < l.index(6, i) else 0 for i in range(len(nums))]))(nums[::-1] + [7,6])