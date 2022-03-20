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
subtitles = subtitles.replace('color=', '')
subtitles = subtitles.replace('<font', '')
subtitles = subtitles.replace('</font>', '')
subtitles = re.sub(r'>[a-z]*', '', subtitles)
subtitles = re.sub(r'"#[0-9a-f]{6}"', '', subtitles)

words = subtitles.split(' ')
print(words)
words = filter(None, words) #Usuwam puste slowa

#Zapis do pliku
with open('testCategory.txt', 'w') as f:
    for item in words:
        f.write("%s\n" % item)

#Sposob czytania pliku 1
with open('testCategory.txt') as file:
    lines = [line.rstrip() for line in file]
    print(lines)

#Sposob czytania pliku 2
#with open('testCategory.txt') as file:
#   for line in file:
#      print(line.rstrip())
