'''
Implementation of the TextRank algorithm
'''
import numpy as np
import Preprocessing as pp
import random
import os

def sentenceSimilarity(sentence1, sentence2, embeddings_dict):
    '''
    Calculates the similarity between two sentences.

    @param sentence1 - one sentence to compare
    @param sentence2 - another sentence to compare
    @param embeddings_dict - GloVe embedding dictionary to embed words into vectors

    @return - cosine similarity of the two sentences (based on average embedding of sentence)
    '''

    # Get the average word embedding of each sentence
        # Turn each word into a vector with GloVe, then average all of them
    wordsSentence1 = pp.tokenize_sentence(sentence1)
    wordsSentence2 = pp.tokenize_sentence(sentence2)

    # Get average for sentence 1
    avgSentence1 = calcAverageEmbedding(wordsSentence1, embeddings_dict)

    # Get average for sentence 2
    avgSentence2 = calcAverageEmbedding(wordsSentence2, embeddings_dict)
  
    if len(avgSentence1) == 0 or len(avgSentence2) == 0:
        return 0
    else:
        # Find the cosine similarity between averages
        return np.dot(avgSentence1, avgSentence2) / (np.linalg.norm(avgSentence1) * np.linalg.norm(avgSentence2))


def calcAverageEmbedding(sentence: list, embeddings_dict):
    '''
    Calculates the average embedding of a sentence.

    Skips over words that are not in the embeddings_dict

    @param sentnece - a list of preprocessed tokens representing the sentence as words
    @param embeddings_dict - the dictionary that maps words to their embeddings

    @return - the average embeddings, calculated from the embedding of each word.
    '''

    # Add up all embeddings
    embeddingsCount = 0
    unknownWords = []
    combinedEmbedding = []
    for word in sentence:

        # If word has an embedding, add it to the sentence's average embedding
        if word in embeddings_dict:
            newEmbedding = embeddings_dict[word]

            # For the first embedding, set the total (so that combinedEmbedding is the right size)
            if len(combinedEmbedding) == 0:
                combinedEmbedding = newEmbedding
            else:
                combinedEmbedding = np.add(combinedEmbedding, newEmbedding)

            embeddingsCount += 1

        # Skip over words that do not have embeddings
        else:
            unknownWords.append(word)

    # HANDLE WITH THIS LATER
    if embeddingsCount == 0:
        return []
    else:
        # Return average
        return combinedEmbedding * (1.0 / embeddingsCount)

def updateSentenceGraph(similarityMatrix, sentences):
    '''
    Performs one iteration of the TextRank algorithm to update every sentence's relevancy score.
    Returns a boolean that says if it changed too much or not.
    '''

    has_changed = False
    D = 0.85
    sentence_score = {}

    for sentence_id in sentences.keys():
        total = 0
        # Loop through every neighbor (every sentence except for self)
        for neighbor_id in sentences.keys():
            if sentence_id  == neighbor_id:
                continue

            denominator = sum(similarityMatrix[neighbor_id])
            numerator = similarityMatrix[sentence_id][neighbor_id]
            total += numerator / denominator * sentences[neighbor_id][1]

        total *= D
        total += (1-D)

        if abs(sentences[sentence_id][1] - total) >= 0.001:
            has_changed = True

        sentence_score[sentence_id] = total

    for sentence_id in sentences.keys():
        sentences[sentence_id][1] = sentence_score[sentence_id]

    return has_changed

def textRank(similarityMatrix, sentences):
    '''
    Repeatedly updates sentence relevancy scores until they converge and do not change by much.
    Returns a summary (top 3 sentences put together).
    '''

    changing = True
    while(changing):
        changing = updateSentenceGraph(similarityMatrix, sentences)

    sorted_sentences = sorted(sentences.items(), key=lambda x: x[1][1], reverse=True)

    print("\nThese are the top three sentences:")
    for sentence_id, (sentence, score) in sorted_sentences[:3]:
        print(f"{sentence}: {score:.3f}")


def buildSimilarityMatrix(sentences):
    '''
    Builds a similarity matrix between every sentence.
    This matrix represents the edges between sentences in a fully connected graph, where each vertex is a sentence, and each edge
    is the similarity between two sentences, from 0 to 1.

    @param sentences - a list of sentences. Each sentence is a list whose first element is a string containing the sentence

    @return - a similarity matrix for all of the sentences. To get the similarity/edge between two sentences,
    index into this matrix with the indices of the sentences
    
    Example: to get the similarity between sentence 5 and 7, access matrix[5][7]. This is also the same as matrix[7][5].
    '''

    # Create word embedding dictionary
    in_file = 'data/glove.6B.50d.txt'

    embeddings_dict = {}
    
    # Obtain the pretrained data
    with open(in_file, 'r', encoding = 'utf-8') as file:
        for line in file:
            values = line.split()
            word = values[0]    # The word is the first token in each line
            vector = np.asarray(values[1:], 'float32')  # The rest of tokens are vector values
            embeddings_dict[word] = vector

    # Create full empty matrix
    matrix = []
    for i in range(len(sentences)):
        matrix.append([0] * len(sentences))

    # Calculate the similarity for every combination of sentences
    for row in range(len(sentences)):

        sentence1 = sentences[row][0]
        
        # Every sentence is similar to itself
        matrix[row][row] = 1

        '''
        Sim Matrix  Sentence:  0  1  2  3  4
                            0: 1 .5 .2 .6 .1
                            1:    1 .5 .1 .8
                            2:       1 .9 .1
                            3:          1 .0
                            4:             1
        
   
        '''
        for col in range(row + 1, len(sentences)):
            sentence2 = sentences[col][0]

            similarity = sentenceSimilarity(sentence1, sentence2, embeddings_dict)

            # Create both sides of matrix ( 0,2 is the same as 2,0 )
            matrix[row][col] = similarity
            matrix[col][row] = similarity

    return matrix

def main():

    example_sentences = {
        0: ["Apples are in Stardew valley and sell for gold.", 0.1],
        1: ["Stardew valley is a game.", 0.1],
        2: ["Cats!", 0.1],
        3: ["Apples are in Stardew valley and sell for gold and cute cats.", 0.1],
        4: ["Without the energy of the sun, scientists cannot find the sun.", 0.1],
        5: ["Stardew valley is a farming and life simulator with town NPCs and lots of interactions.", 0.1]
    }

    # TO TEST IT WITH THE EXAMPLE SENTENCES UNCOMMENT IT
    exampleSimilarityMatrix = buildSimilarityMatrix(example_sentences)
    #  textRank(exampleSimilarityMatrix, example_sentences)


    # Open text file
    rootDir = "Corpus"
    file_list=[]

    # add the file path in a list so you can reach all the file paths
    for file in os.listdir(rootDir):
        if(file[-4:] == ".txt"):
            file_list.append( os.path.join(rootDir, file))

    # go through the file list and find the similarity matrix for all of them
    for i in file_list:
        with open(i, mode = "r", encoding="utf-8") as file:
            sentences = build_dictionary(pp.preprocess(file.read()))
            similarityMatrix = buildSimilarityMatrix(sentences)
            textRank(similarityMatrix, sentences)

def build_dictionary(sentences):
    dictionary = {}
    for i in range(len(sentences)):
        dictionary[i] = [sentences[i], (1 / len(sentences))]

    return dictionary

if __name__ == "__main__":
    main()