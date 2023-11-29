# ESC180 Project 3
# David Guo, Hanson Liu
# Emerson Grabke
# 4 December 2021

import math

def norm(vec):
  '''Helper function which returns the norm of a vector stored as a dictionary, as described in the handout for Project 3.
  '''
  sum_of_squares = 0.0
  for x in vec:
      sum_of_squares += vec[x] * vec[x]

  return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2):
  ''' Helper function to calculate the cosine similarity between predefined sparse vectors stored as dictionaries; returns a scalar between 0 and 1'''

  # Define dot product variable
  dot_uv = 0
  # Get the norm of the vectors
  mag_u = norm(vec1)
  mag_v = norm(vec2)

  # Implement version from handout -- only multiply if keys match
  for i in vec1:
    for j in vec2:
      if i == j:
        dot_uv += vec1[i] * vec2[j]

  # Compute similarity based on formula
  cos_similarity = dot_uv/(mag_u*mag_v)

  return cos_similarity

def build_semantic_descriptors(sentences):
  '''Returns a dictionary of semantic descriptors from each sentence'''
  # Define the dictionary to return
  sem_dict = {}

  # Iterate through the sentences of the text
  for sentence in sentences:
    # Iterate through word of the sentence
    for word in sentence:
      # First check if the word has already been added to the dictionary -- we don't want duplicates
      if word not in sem_dict:
      # Create the ssemantic descriptor dictionary for the word
        sem_dict[word] = {}

      # Iterate through the sentence again and compare each word with the 'target' word w_i
      for tracker in sentence:
        # The tracker can't equal the word
        if tracker != word:
          # Create an entry in the dict for the tracker if none exists yet so we don't get an error we spend 3 hours and 5 coffees trying to fix fucking hell
          if tracker not in sem_dict[word]:
            sem_dict[word][tracker] = 0

          # Increment the count of same-sentence occurence for specified word and tracker
          sem_dict[word][tracker] += 1

  return sem_dict

def build_semantic_descriptors_from_files(filenames):
  '''Processess a raw text file into a list of sentences which can be input build_semantic_descriptors, and calls the functino to create a dictionary of semantic descriptors for multiple text files.'''
  # Create sentences list to be passed to the build_semantic_descriptors method
  sentences = []
  # Create a list of delimiters to more easily separate out the sentences
  delimiters = [".", "!", "?"]
  # Create a list of punctuation to remove
  punctuations = [",", "-", "--", ":", ";", "(",")", "'", "\""]

  rawtext = ''
  # Iterate through thee filenames
  for filename in filenames:
    # Open the file
    f = open(filename, "r", encoding="latin1")
    # Some processing to remove not UTF-8 characters which would interfere with our code and joining the files into one big string
    rawtext += "".join(char for char in f.read() if ord(char)<128)

  # Remove non delimiting punctuation
  for punctuation in punctuations:
    rawtext = rawtext.replace(punctuation, "")

  # Separate string into sentences using delimiters
  for delimiter in delimiters:
    rawtext = rawtext.replace(delimiter, ".")

  chunks = (rawtext.lower()).split(".")
  for chunk in chunks:
    sentences += [chunk.split()]

  # Remove empty sentences since they will cause errors
  for s in sentences:
    if len(s) == 0:
      sentences.remove(s)

  return build_semantic_descriptors(sentences)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
  '''Returns the most similar choice from a list of choices to the specified word using a dict of semantic descriptors, and similarity function cosine similarity'''

  # List of similarities between choice i and the word
  similarities = []

  # Iterate through the choices, get the semantic similarity
  for choice in choices:
    # Check if both the word and the choice are in the semantic descriptors dictionary
    if word in semantic_descriptors and choice in semantic_descriptors:
      # Add the computed similarity score
      similarities.append(similarity_fn(semantic_descriptors[word], semantic_descriptors[choice]))

    # Add
    else:
      similarities.append(-1)

  # Return the first instance of the max similarity, effectively np.argmax(), but since there is no argmax function for Python lists for whatever reason, we have to find a workaround
  return choices[max(zip(similarities, range(len(similarities))))[1]]

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
  '''Computes the accuracy of the get most similar word function for a synonym test described in Project 3 handout'''

  # Define variables
  computed_similarity_answers = []
  correct_answers = []
  num_correct = 0

  # Open text file and readlines
  with open(filename, "r", encoding="latin1") as f:
    text = f.readlines()

  # Get the word, correct word, and choices
  for set in text:
    set = (set.replace("\n", "")).split()

    word = set[0]
    correct = set[1]
    choices = set[2:]

    # Get most similar word
    computed_similarity_answers.append(most_similar_word(word, choices, semantic_descriptors, similarity_fn))
    # Get correct answer at location
    correct_answers.append(correct)

  # Calculate total number of correct answers
  for i, j in zip(computed_similarity_answers, correct_answers):
    print(i,j)
    if i == j:
      num_correct += 1

  # Calculate accuracy
  accuracy = float(num_correct/len(text) * 100)

  return accuracy
