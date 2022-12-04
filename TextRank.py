'''
Implementation of the TextRank algorithm
'''
import numpy as np

import random

def sentenceSimilarity(sentence1, sentence2) -> float:
    '''
    Calculates the similarity between two sentences.
    '''

    # Get the average word embedding of each sentence
        # Turn each word into a vector with GloVe, then average all of them

    # Find the cosine similarity between averages
    
    return 


def updateSentenceGraph():
    '''
    Performs one iteration of the TextRank algorithm to update every sentence's relevancy score.
    '''

def textRank():
    '''
    Repeatedly updates sentence relevancy scores until they converge and do not change by much.
    '''
    return


def buildSimilarityMatrix(sentences):
    

    # Create full empty matrix
    matrix = []
    for i in range(len(sentences)):
        matrix.append([0] * len(sentences))

    for row in range(len(sentences)):

        sentence1 = sentences[row]
        
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
            sentence2 = sentences[col]

            similarity = sentenceSimilarity(sentence1, sentence2)

            # Create both sides of matrix ( 0,2 is the same as 2,0 )
            matrix[row][col] = similarity
            matrix[col][row] = similarity



    return matrix

def main():



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


    sentences = {
        0: ["Apples are in Stardew valley and sell for gold.", 0.1],
        1: ["Stardew valley is a game.", 0.1],
        2: ["Cats are cool and cute", 0.1],
        3: ["Stardew Valley has trees and stuff.", 0.1]
    }

    similarityMatrix = buildSimilarityMatrix(sentences)

    # Open text file
    
    # Get list of sentences

    # Add each sentence to dictionary with ID and starting score


    return


if __name__ == "__main__":
    main()