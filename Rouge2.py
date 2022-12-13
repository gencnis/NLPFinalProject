'''
This document 'Rouge2.py' creates a baseline summary to compare it with candidate sentences from the document using rouge-n
scores which uses bigrams and computes the rouge-2 score per document.

@author: Nisanur Genc
@author: Alex Wills
'''

import TextRank
import nltk
from collections import Counter

def get_baseline(candidate):
    '''
    Gets the reference baseline of the document. (In our case it is the first 3 sentences of the document)

    @param candidate - a dictionary of sentences. Each sentence is a list whose first element is a string containing the sentence

    @return - a string that contains the first three sentences in the document.
    '''
    
    baseline = ""

    # Gets the first three sentences in the document
    for i in range(min(3, len(candidate))):
        baseline += candidate[i][0]

    return baseline

def rouge_2(baseline, candidate):
    '''
    Computes the rouge-n score using bigrams.

    @param candidate - a dictionary of sentences. Each sentence is a list whose first element is a string containing the sentence
    @param baseline - a string that contains the first three sentences in the document (the summary)

    @return - the computed rouge-2 score
    '''

    # Creates the bigrams for baseline string and the candidate sentences
    baseline_bigram = nltk.bigrams( nltk.word_tokenize(baseline))
    candidate_bigram = nltk.bigrams( nltk.word_tokenize(candidate))

    # Counts the biagrams
    baseline_count = Counter(baseline_bigram)
    candidate_count = Counter(candidate_bigram)

    matching_bigrams = 0
    total_baseline_bigrams = 0
    # Count bigram overlaps
    for bigram, count in candidate_count.items():
        if bigram in baseline_count:
            matching_bigrams += min(candidate_count[bigram], baseline_count[bigram])

    # Add up reference bigrams
    for bigram, count in baseline_count.items():
        total_baseline_bigrams += count

    if(total_baseline_bigrams == 0):
        total_baseline_bigrams = 1

    return matching_bigrams / total_baseline_bigrams


def main():

    # Main function for testing the ROUGE measure
    testBaseline = "Stardew valley is a cool game. Stardew valley is a farming game. Apples are cool."
    testCandidatePerfect = testBaseline
    testCandidateMedium = "Stardew Valley is a cool game. Apples have red skin. Apples can be sold for gold."
    testCandidateBad = "According to all known laws of aviation, there is no way a bee should be able to fly."

    print("Perfect summary: ", rouge_2(testBaseline, testCandidatePerfect))
    print("Medium summary: ", rouge_2(testBaseline, testCandidateMedium))
    print("Bad summary: ", rouge_2(testBaseline, testCandidateBad))

if __name__ == "__main__":
    main()