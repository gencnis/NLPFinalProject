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
for i in range(0, ten_percent):
    j = random.randint(0, len(file_list)-1)
    if j not in random_index and file_list[j] != "TrainingSet": 
        random_index.append(j)
    else:
        while(j in random_index or file_list[j] == "TrainingSet"):
            j = random.randint(0, len(file_list) - 1)
        random_index.append(j)


test_destination = "Corpus/TestSet/"
training_destination = "Corpus/TrainingSet/"

for index in random_index:
    source = source_folder + file_list[index]
    destination = test_destination + file_list[index]
    shutil.move(source, destination)

# create a file name list
for file in os.listdir(source_folder):
    if file != "TraininSet" and file != "TestSet":
        shutil.move(source_folder+file, training_destination)
    
