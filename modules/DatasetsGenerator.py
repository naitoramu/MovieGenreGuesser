import os
import random

filenames = os.listdir(os.path.join("preprocessed_subtitles/"))

subtitles = []
train_data = []
validation_data = []
test_data = []

for filename in filenames:
    with open(os.path.join("preprocessed_subtitles/" + filename), 'r') as file:
        subtitles.append(file.read().split('\n'))

for i in range(0, len(filenames)):
    counter = 0

    for row in subtitles[i]:
        if len(row) != 0:
            if counter % 2.5 == 0:
                if counter & 2 == 0:
                    test_data.append(row + "," + filenames[i][:-4])
                else:
                    validation_data.append(row + "," + filenames[i][:-4])
            else:
                train_data.append(row + "," + filenames[i][:-4])
            counter += 1

random.shuffle(train_data)
random.shuffle(validation_data)
random.shuffle(test_data)

with open("./data/train.csv", 'w') as file:
    file.write("Subtitles,Genre\n")
    for row in train_data:
            file.write(row + '\n')
    
with open("./data/validation.csv", 'w') as file:
    file.write("Subtitles,Genre\n")
    for row in validation_data:
        file.write(row + '\n')

with open("./data/test.csv", 'w') as file:
    file.write("Subtitles,Genre\n")
    for row in test_data:
        file.write(row + '\n')

