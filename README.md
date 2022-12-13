# NLPFinalProject: Stardew Summarization

Unsupervised Document Summarization of a Video Game Wiki System

## Description

Topic specific, extractive unsupervised document summarization of a video game (Stardew Valley) wiki website, using TextRank Algorithm and Rouge-2 Score evaluation. (More detail)

## Getting Started

### Dependencies

* **NLTK:** The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English written in the Python programming language. You will need NLTK downloaded in your computer to be able to run TextRank algorithm. [This might help for downloading it.](https://www.nltk.org/install.html)
* **matplotlib.pyplot:** matplotlib.pyplot is a collection of functions that make matplotlib work like MATLAB. You will need matplotlib.pyplot downloaded in your computer to be able to run the dataset analysis code. [This might help for downloading it.](https://matplotlib.org/stable/users/installing/index.html)
* **NumPy:** NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. You will need NumPy downloaded in your computer to be able to run TextRank algorithm. [This might help for downloading it.](https://numpy.org/install/)
* **Beautiful Soup:** Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. You will need Beautiful Soup downloaded in your computer to be able to extract the text from the wiki. [This might help for downloading it.](https://pypi.org/project/beautifulsoup4/)

### Installing

* You can download the project [here.](https://github.com/gencnis/NLPFinalProject)
* You will need to do these modifications:
  * Download the GloVe data [here.](https://www.kaggle.com/datasets/watts2/glove6b50dtxt)
  * Add GloVe data to the data folder.
  * Run CreateCorpus file to populate the Corpus folder. This will extract data from Stardew Valley Wiki and create your dataset. Here is how to run CreateCorpus in your terminal:
```
python3 CreateCorpus.py
```

### Executing program

To execute the program, _make sure you are done with the modifications above._

Here is what you need to do know about the files in the project before you start executing:
* **TextRank.py** is the main file you will be running.
* **Preprocessing.py** will be used in TextRank to preprocess the data.
* **Rouge2.py** will be used in TextRank to evaluate the sentence scores.
* **DatasetAnalysis.py** is to analyze your dataset after you create it. It is optional to use.
* **DistrubuteData.py** is designed to distrubute the dataset for neural network into Training Set and Test Set folders. It is not recommended to use at this step of the project, it will be compatible with future versions.
* **Corpus folder** is where your dataset will be created after you run the CreateCorpus, it extracts 1400 .txt files from the Stardew Valley Wiki.
* **data folder** is where GloVe data will be stored.
* **TestData folder** is where a test dataset is stored. It takes approximately 17 hours for program to finish calculation with Corpus dataset, so we have added a sample TestData folder for you to be able to test the code in around 12 seconds.

**To execute your code, you can use this snippet in your terminal:**
```
python3 TextRank.py [dataset info]
```

**dataset info** : 
* You can chose to run the program with TestData, in this case your command should look like this:
```
python3 TextRank.py TestData
```
* Or you can chose to run the program with Corpus, in this case your command should look like this:
```
python3 TextRank.py TestData
```

**WARNING:** If you do not enter any arguments, the program will run with the Corpus folder by default.

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

* [Nisanur Genc](https://github.com/gencnis) 
* [Alex Wills](https://github.com/AlexWills37)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* UMM IF WE WANT TO CITE THE PAPERS
