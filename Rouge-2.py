import TextRank
import nltk
from collections import Counter

def getSummary():
    '''Gets the reference summary of the document. (In our case it is the first 3 sentences of the document)'''
    return NotImplemented

def rouge_2(summary, output):
    
    summary_bigram = nltk.bigrams( nltk.word_tokenize(summary))
    output_bigram = nltk.bigrams( nltk.word_tokenize(output))

    summary_count = Counter(summary_bigram)
    output_count = Counter(output_bigram)

    matching_bigrams = 0
    total_summary_bigrams = 0
    # Count bigram overlap
    for bigram, count in output_count.items():
        if bigram in summary_count:
            matching_bigrams += min(output_count[bigram], summary_count[bigram])

    # Add up reference bigrams
    for bigram, count in summary_count.items():
        total_summary_bigrams += count

    return matching_bigrams / total_summary_bigrams
    

def main():

    testSummary = "Stardew valley is a cool game. Stardew valley is a farming game. Apples are cool."
    testOutputPerfect = testSummary
    testOutputMedium = "Stardew Valley is a cool game. Apples have red skin. Apples can be sold for gold."
    testOutputBad = "According to all known laws of aviation, there is no way a bee should be able to fly."

    print("Perfect Summary: ", rouge_2(testSummary, testOutputPerfect))
    print("Medium Summary: ", rouge_2(testSummary, testOutputMedium))
    print("Bad Summary: ", rouge_2(testSummary, testOutputBad))

if __name__ == "__main__":
    main()