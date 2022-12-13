'''
This document 'DatasetAnalysis.py' analyzes the lengths of files in the Corpus folder and plots them.
The methods in this file can be used at any time to generate statistics for the dataset.
'''
import Preprocessing as pp
import os
import matplotlib.pyplot as plt


def build_length_dict():
    '''
    Creates a dictionary for the lengths of each file.
    The key of each entry is the name of the text file, and the value is the number of sentences
    in the file.

    @return - a dictionary containing the lengths of every text file.
    '''
    # Open text file
    rootDir = "Corpus"

    file_list = []

    # add the file path in a list so you can reach all the file paths
    for file in os.listdir(rootDir):
        if(file[-4:] == ".txt"):
            file_list.append( os.path.join(rootDir, file))


    lengths = {}



    for i in file_list:
        with open(i, mode = 'r', encoding='utf-8') as file:
            sentences = pp.preprocess(file.read())

            lengths[i] = len(sentences)

    return lengths


def analyze_dataset():
    '''
    Generates and prints summary statistics for the corpus based on document length in sentences.

    Prints the number of files, the maximum length of a file, the minimum length of a file,
    and the average length of a file.
    '''
    # Open text file
    rootDir = "Corpus"

    file_list = []

    # add the file path in a list so you can reach all the file paths
    for file in os.listdir(rootDir):
        if(file[-4:] == ".txt"):
            file_list.append( os.path.join(rootDir, file))


    lengths = []


    # Build a list of lengths 
    for i in file_list:
        with open(i, mode = 'r', encoding='utf-8') as file:
            sentences = pp.preprocess(file.read())

            l = len(sentences)

            if len(sentences) >= 617:
                print(i)
            lengths.append(len(sentences))

    # Sort the lengths to gather summary statistics
    lengths = sorted(lengths)
    
    print("File count: " + str(len(lengths)))
    print("Max len: " + str(lengths[-1]))
    print("Min length: " + str(lengths[0]))
    print("Average length: " + str(sum(lengths) / len(lengths)))

    print("Length of every file:")
    print(lengths)# Open text file
    


def plot_distribution():
    '''
    Graphically plots the distribution of lengths of documents in a histogram.
    '''

    lengths = build_length_dict().values()
    lengths = sorted(lengths)
    lengths = lengths[:-10]   # Exclude outliers
    width = max(lengths) - min(lengths)
    bin_count = 200

    plt.xlabel("Size of Document (# Sentences)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Document Size")
    plt.hist(lengths, bin_count)
    plt.show()


def main():
    plot_distribution()
    # analyze_dataset()





if __name__ == "__main__":
    main()