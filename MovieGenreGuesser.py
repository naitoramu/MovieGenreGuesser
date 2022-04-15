# import tensorflow as tf
# from tensorflow import keras
# # print(tf.__version__)
import pandas
import re
import sys
import matplotlib.pyplot as plt

from collections import Counter

if( len(sys.argv)) < 2:
    print("Missed arguments")
    quit()

path_to_subtitles_file = sys.argv[1]

with open(path_to_subtitles_file) as file:
    subtitles = file.read()

subtitles = subtitles.split()

counts = Counter(subtitles)

most_common = counts.most_common(500)

# print(*zip(*most_common))

plt.bar(*zip(*most_common))
plt.show()