from nltk import word_tokenize, sent_tokenize
import os
import re

def preprocess(document):
    # Casefold
    text = document.casefold()

    # Get sentences
    sentences = sent_tokenize(text)

    # First sentence is expected to be mixed with header, so we isolate it
    firstSentence = re.findall(r"\n.+\.", sentences[0]) 
    if len(firstSentence) > 0:
        sentences[0] = firstSentence[-1][1:]    # True first sentence is the last line that ends with a "."
    
    return sentences



def tokenize_sentence(sentence):
    sentence = sentence.casefold()

    words = []

    # Remove punctuation
    punc = '''!()-[]{};:'"’“”\,<>./?@#$%^&*_~'''
    for character in punc:
        sentence.replace(character, "")
        words = word_tokenize(sentence)

    return words


def main():
    
    # open file for testing purposes
    rootDir = os.path.dirname(__file__)

    with open(os.path.join(os.path.dirname(__file__), "Corpus/Abigail.txt"), mode = "r", encoding="utf-8") as file:
        document = preprocess(file.read())
        print("hi")

if __name__ == "__main__":
    main()