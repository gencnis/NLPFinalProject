'''
This document 'DistributeData.py' distrubes the data after the dataset created in the Corpus folder into Test Set folder
and the Training Set folder. It takes the 10% of the files randomly and moves it into the Test Set folder. The remaining
of the files is being moved to the Training Set folder. 

@author: Nisanur Genc
@author: Alex Wills
'''

import shutil
import os
import random

# Open text file
source_folder = "Corpus/"
file_list=[]

# create a file name list
for file in os.listdir(source_folder):
    file_list.append(file)

# 10% of the length of the file list taken as an integer
ten_percent = int(len(file_list) / 100 * 10)

random_index = []
# generates random indexes between 0 and the 10 percent of number of the documents in the dataset 
for i in range(0, ten_percent):
    j = random.randint(0, len(file_list)-1)
    # checks if the random index generated from the file list
    # is in the Training Set index list, if not it adds to the random index list
    if j not in random_index and file_list[j] != "TrainingSet": 
        random_index.append(j)
    else:
        while(j in random_index or file_list[j] == "TrainingSet"):
            j = random.randint(0, len(file_list) - 1)
        random_index.append(j)

# creates destination paths for both Test Set and the Training Set 
test_destination = "Corpus/TestSet/"
training_destination = "Corpus/TrainingSet/"

# for each index in the random index list, it adds to the source path and moves it to the destination path
# which is the test set folder
for index in random_index:
    source = source_folder + file_list[index]
    destination = test_destination + file_list[index]
    shutil.move(source, destination)

# for each file left after random indexes moved to the test set folder, 
# it moves the remaining files to the training set folder
for file in os.listdir(source_folder):
    if file != "TraininSet" and file != "TestSet":
        shutil.move(source_folder+file, training_destination)
    
