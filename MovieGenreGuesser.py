# import tensorflow as tf
# from tensorflow import keras
# # print(tf.__version__)
import pandas
import re
import sys

if( len(sys.argv)) < 2:
    print("Missed arguments")
    quit()

path_to_subtitles_file = sys.argv[1]

with open(path_to_subtitles_file) as file:
    subtitles = file.read()

subtitles = subtitles.split()
print(subtitles)