import TextRank
import nltk
from collections import Counter

def getSummary():
    '''Gets the reference summary of the document. (In our case it is the first 3 sentences of the document)'''
    return NotImplemented

def rouge_2(summary, output):

    summary_bigram = nltk.bigram( nltk.word_tokenize(summary))
    output_bigram = nltk.bigram( nltk.word_tokenize(output))


    summary_count = Counter(summary_bigram)
    output_count = Counter(output_bigram)

    rouge_sum = 0

    for bigram, count in output_count.items():
        rouge_sum += count / summary_count[bigram]

    rouge_2 = rouge_sum / 2

    return rouge_2