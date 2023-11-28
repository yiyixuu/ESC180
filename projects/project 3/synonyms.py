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

def build_semantic_descriptors(sentences):
    d = {}

    for sentence in sentences:
        pairs = [(a, b) for idx, a in enumerate(sentence) for b in sentence[idx + 1:]]

        for pair in pairs:
            word_1 = pair[0]
            word_2 = pair[1]

            if word_1 not in d:
                d[word_1] = {}
            
            if word_2 not in d:
                d[word_2] = {}

            if word_2 not in d[word_1]:
                d[word_1][word_2] = 1
            else:
                d[word_1][word_2] += 1

            if word_1 not in d[word_2]:
                d[word_2][word_1] = 1
            else:
                d[word_2][word_1] += 1

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

filenames = ['projects/project 3/war_and_peace.txt', 'projects/project 3/swanns_way.txt']
d = build_semantic_descriptors_from_files(filenames)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass
