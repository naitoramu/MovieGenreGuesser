# SubtitlesPreprocessor
# usage: python SubtitlesPreprocessor.py [input file] [output file]
# example: SubtitlesPreprocessor.py srt/test-subtitles.srt train_data/sitcom.txt

import re
import os
import sys
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class SubtitlesPreprocessor:

    def __init__(self, path_to_subtitles_file):

        self.path_to_subtitles_file = path_to_subtitles_file
        self.filename = ''
        self.file_loaded_successfully = False
        self.stopwords  = stopwords.words('english')        #stopwords[0:10] = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're"]
        self.wordnet_lemmatizer = WordNetLemmatizer()

        self.preprocessSubtitles()

    def preprocessSubtitles(self):

        self.loadFile(self.path_to_subtitles_file)

        if(self.file_loaded_successfully):
            self.extractSubtitlesWithTime()
            self.removeTimeDataFromSubtitles()
            self.toLowerCase()
            self.removeURLsFromSubtitles()
            self.removeTagsFromSubtitles()
            self.removeDigitsFromSubtitles()
            self.removeSoundDescritpionsFromSubtitles()
            self.removePunctuationFromSubtitles()
            self.removeStopwordsFromSubtitles()
            self.extractOnlyWordsFromSubtitles()
            self.lemmatizeSubtitles()

    def loadFile(self, path_to_subtitles_file):
        try:
            with open(path_to_subtitles_file, 'r', encoding="ISO-8859-1") as file:
                self.file_content = file.read()
                self.file_loaded_successfully = True

                # os.path.basename(file.name) returns filename without path
                # os.path.splitext()[] returns filename without extension
                self.filename = os.path.splitext(
                    os.path.basename(file.name))[0]

        except IOError:
            self.file_loaded_successfully = False

    def extractSubtitlesWithTime(self):
        self.subtitles_with_time = re.findall(
            "(\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+)\s+(.+)", self.file_content)

    def removeTimeDataFromSubtitles(self):

        self.subtitles = ''

        for row in self.subtitles_with_time:
            self.subtitles += ' ' + row[1]

    def toLowerCase(self):
        self.subtitles = self.subtitles.lower()

    def removeURLsFromSubtitles(self):
        self.subtitles = re.sub(
            r'(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+', '', self.subtitles)

    def removeTagsFromSubtitles(self):

        self.subtitles = re.sub(r'<(.)*?>', '', self.subtitles)
        self.subtitles = re.sub(r'\{(.)*?\}', '', self.subtitles)

    def removeSoundDescritpionsFromSubtitles(self):
        self.subtitles = re.sub(r'\[.*?\]', '', self.subtitles)

    def removeDigitsFromSubtitles(self):
        self.subtitles = re.sub(r'[0-9]+', '', self.subtitles)

    def removePunctuationFromSubtitles(self):
        self.subtitles = re.sub(r'[.,?!:-]', '', self.subtitles)


    def removeStopwordsFromSubtitles(self):
        without_stopwords = [i for i in self.getWordList() if i not in self.stopwords]
        self.subtitles = " ".join(without_stopwords)
        

    def extractOnlyWordsFromSubtitles(self):
        self.subtitles = re.sub(r'[^a-z\s]', '', self.subtitles)

    def lemmatizeSubtitles(self):
        lemmatized_subtitles = [self.wordnet_lemmatizer.lemmatize(word) for word in self.getWordList()]
        self.subtitles = " ".join(lemmatized_subtitles)

    def getSubtitles(self):
        return self.subtitles

    def getWordList(self):
        return self.subtitles.split()

    def saveSubtitles(self, output_filename):

        with open(output_filename, 'at') as file:
            file.write(self.subtitles + '\n')



if(len(sys.argv)) < 3:
    print("Missed arguments")
    quit()

subtitles_file = sys.argv[1]
output_filename = sys.argv[2]


subtitles = SubtitlesPreprocessor(subtitles_file)
subtitles.saveSubtitles(output_filename)
# print(subtitles.getSubtitles())
# print(len(subtitles.getSubtitles()))
