# import tensorflow as tf
# from tensorflow import keras
# # print(tf.__version__)
import pandas
import re

file = open("test-subtitles.srt")
content = file.read()

result = re.findall("(\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+)\s+(.+)", content)

subtitles = ''

for line in result:
    subtitles += ' ' + line[1]

print(subtitles)

subtitles = subtitles.lower()
subtitles = subtitles.replace('.', '')
subtitles = subtitles.replace(',', '')
subtitles = subtitles.replace('!', '')
subtitles = subtitles.replace('?', '')
subtitles = subtitles.replace('[', '')
subtitles = subtitles.replace(']', '')
subtitles = subtitles.replace('<i>', '')
subtitles = subtitles.replace('</i>', '')
subtitles = subtitles.replace('{\\an8}', '')


words = subtitles.split(' ')

print(words)