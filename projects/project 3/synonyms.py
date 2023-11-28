'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math


def norm(vec):
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2):
    numerator = 0.0
    denominator = norm(vec1) * norm(vec2)
    for key in vec1.keys():
        if key in vec2:
            numerator += vec1[key] * vec2[key]
    return numerator/denominator

print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))

def build_semantic_descriptors(sentences):
    d = {}
    for sentence in sentences:
        unique_words = set(sentence)
        for word in unique_words:
            if word not in d:
                d[word] = {}
            for other_word in sentence:
                if other_word != word:
                    if other_word in d[word]:
                        d[word][other_word] += 1
                    else:
                        d[word][other_word] = 1
            else:
                for other_word in sentence:
                    if other_word != word:
                        if other_word in d[word]:
                            d[word][other_word] += 1
                        else:
                            d[word][other_word] = 1
    return d

def build_semantic_descriptors_from_files(filenames):
    sentences = []
    for filename in filenames:
        with open(filename, "r", encoding="latin1") as file:
            content = file.read()

            # Splitting into sentences
            for punct in [".", "!", "?"]:
                content = content.replace(punct, "|")
            sentences_list = content.split("|")

            # Processing each sentence
            for sentence in sentences_list:
                for punct in [",", "-", "--", ":", ";"]:
                    sentence = sentence.replace(punct, " ")
                words = sentence.strip().lower().split()
                if words:
                    sentences.append(words)
    
    return build_semantic_descriptors(sentences)
    
filenames = "/Users/shaanjain/Downloads/ENGSCI/FIRST YEAR/SEM 1/esc180/Projects/ESC180-1/projects/project 3/test.txt"
print(build_semantic_descriptors_from_files([filenames]))

        

        



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass
