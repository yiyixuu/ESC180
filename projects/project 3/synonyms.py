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
    descriptors = {}

    for sentence in sentences:
        pairs = [(a, b) for idx, a in enumerate(sentence) for b in sentence[idx + 1:]]

        for pair in pairs:
            word_1 = pair[0]
            word_2 = pair[1]

            if word_1 not in descriptors:
                descriptors[word_1] = {}
            
            if word_2 not in descriptors:
                descriptors[word_2] = {}

            if word_2 not in descriptors[word_1]:
                descriptors[word_1][word_2] = 1
            else:
                descriptors[word_1][word_2] += 1

            if word_1 not in descriptors[word_2]:
                descriptors[word_2][word_1] = 1
            else:
                descriptors[word_2][word_1] += 1

    return descriptors

def build_semantic_descriptors_from_files(filenames):
    sentences = []

    punct_sentence = [".", "!", "?"]
    punct_word = [",", "-", "--", ":", ";", "(", ")", "'", "\""]

    for filename in filenames:
        with open(filename, "r", encoding="latin1") as file:
            content = file.read()

            for punct in punct_sentence:
                content = content.replace(punct, ".")
            sentences_list = content.split(".")
            sentences_list = [sentence.strip() for sentence in sentences_list if sentence]

            for sentence in sentences_list:
                for punct in punct_word:
                    sentence = sentence.replace(punct, "")
                sentence = sentence.lower()
                sentence = sentence.split(" ")
                sentences.append(sentence)

    return build_semantic_descriptors(sentences)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    semantic_similarity_scores = {}
    for choice in choices:
        if word in semantic_descriptors and choice in semantic_descriptors:
            semantic_similarity_scores[choice] = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
        else:
            semantic_similarity_scores[choice] = -1

    return max(semantic_similarity_scores, key=semantic_similarity_scores.get)

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    correct = 0
    total = 0
    
    with open(filename) as tests:
        for test in tests:
            words = test.split(" ")
            word = words[0]
            answer = words[1]
            choices = [choice.strip() for choice in words[2:]]
            guess = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
            if answer == guess:
                correct += 1
            total += 1

        return correct / total * 100