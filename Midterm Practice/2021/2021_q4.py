entries = []

def unlock(input):
    entries.append(input)
    return 'unlocked' if entries[-1] == 'pumpkin' and entries[-2] == 'costumes' and entries[-3] == 'costumes' and entries[-4] == 'fall' else 'locked'

print(unlock("ghosts"))
print(unlock("leaves"))
print(unlock("fall"))
print(unlock("costumes"))
print(unlock("costumes"))
print(unlock("pumpkin"))
print(unlock("pumpkin"))
print(unlock("fall"))
print(unlock("costumes"))
print(unlock("costumes"))
print(unlock("pumpkin"))
print(unlock("fall"))