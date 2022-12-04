from nltk import word_tokenize, sent_tokenize
import os
import re

def preprocess(document: str) -> list:
    # Casefold
    text = document.casefold()

    # Get sentences
    sentences = sent_tokenize(text)

    # First sentence is expected to be mixed with header, so we isolate it
    firstSentence = re.findall(r"\n.+\.", sentences[0]) 
    if len(firstSentence) > 0:
        sentences[0] = firstSentence[-1][1:]    # True first sentence is the last line that ends with a "."
    

    tokenList = []

    # Remove punctuation
    punc = '''!()-[]{};:'"’“”\,<>./?@#$%^&*_~'''
    for i in range(len(sentences)):

        for character in punc:
            sentences[i] = sentences[i].replace(character, "")

        # REMOVE STOP WORDS?????
        # DONT FORGET ABOUT THIS COMMENT
        # THIS COMMENT RIGHT HERE
        # IT EVEN TAKES UP 4 LINES
        words = word_tokenize(sentences[i])
        tokenList.append(words)

    
    return tokenList


def tokenizeSentence(sentence):
    sentence = sentence.casefold()

    words = []

    # Remove punctuation
    punc = '''!()-[]{};:'"’“”\,<>./?@#$%^&*_~'''
    for character in punc:
        sentence.replace(character, "")
        words = word_tokenize(sentence)

    return words



def main():
    
    rootDir = os.path.dirname(__file__)

    with open(os.path.join(os.path.dirname(__file__), "Corpus/Abigail.txt"), mode = "r", encoding="utf-8") as file:
        document = preprocess(file.read())
        print("hi")

main()