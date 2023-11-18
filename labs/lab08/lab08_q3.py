L = open("/Users/yiyixu/Documents/First Year/Intro to Computer Programming/labs/lab08/text.txt", encoding="latin-1").read().split()

for i in range(len(L)):
    L[i] = L[i].strip(".,?!:;()_-").lower()

def get_word_counts(L):
    word_counts = {}
    for word in L:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

# print(get_word_counts(L))


def top10(L):
    return sorted(L, reverse=True)[:10]


# print(top10([i for i in range(100)]))

def top10words(L):
    # return list(dict(sorted(get_word_counts(L).items(), key=lambda x: x[1], reverse=True)).keys())[:10]
    return list(dict(sorted(get_word_counts(L).items(), key=lambda x: x[1], reverse=True)).items())[:10]

print(top10words(L))