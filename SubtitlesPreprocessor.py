# SubtitlesPreprocessor
# usage: python SubtitlesPreprocessor.py [.srt file] [destination_directory]*
# destination_directory is not necessary
# example: SubtitlesPreprocessor.py test-subtitles.srt
#           SubtitlesPreprocessor.py test-subtitles.srt training_data/

import re
import os
import sys


class SubtitlesPreprocessor:

    def __init__(self, path_to_subtitles_file):

        self.path_to_subtitles_file = path_to_subtitles_file
        self.filename = ''
        self.file_loaded_successfully = False

        self.preprocessSubtitles()

    def preprocessSubtitles(self):

        self.loadFile(self.path_to_subtitles_file)

        if(self.file_loaded_successfully):
            self.extractSubtitlesWithTime()
            self.removeTimeDataFromSubtitles()
            self.removeTagsFromSubtitles()
            self.removeSoundDescritpionsFromSubtitles()
            self.removeSpecialCharactersFromSubtitles()
            self.toLowerCase()


    def loadFile(self, path_to_subtitles_file):
        try:
            file = open(path_to_subtitles_file, 'r')
            self.file_content = file.read()
            self.file_loaded_successfully = True
                                                                                # os.path.basename(file.name) returns filename without path
            self.filename = os.path.splitext(os.path.basename(file.name))[0]    # os.path.splitext()[] returns filename without extension

        except IOError:
            self.file_loaded_successfully = False

    def extractSubtitlesWithTime(self):
        self.subtitles_with_time = re.findall("(\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+)\s+(.+)", self.file_content)
    
    def removeTimeDataFromSubtitles(self):

        self.subtitles = ''

        for row in self.subtitles_with_time:
            self.subtitles += ' ' + row[1]

    def removeTagsFromSubtitles(self):

        self.subtitles = self.subtitles.replace('<i>', '')
        self.subtitles = self.subtitles.replace('</i>', '')

        self.subtitles = re.sub(r'<font(.)*?font>', '', self.subtitles)

        self.subtitles = re.sub(r'\{\\an8\}', '', self.subtitles)


    def removeSoundDescritpionsFromSubtitles(self):
        self.subtitles = re.sub(r'\[.*?\]', '', self.subtitles)

    def removeSpecialCharactersFromSubtitles(self):
        self.subtitles = re.sub(r'[^\w\s]', '', self.subtitles)

    def toLowerCase(self):
        self.subtitles = self.subtitles.lower()

    def getSubtitles(self):
        return self.subtitles

    def getWordList(self):
        return self.subtitles.split()
    
    def saveSubtitles(self, destination_directory):
        with open(destination_directory + self.filename + '.txt', 'w') as file:
            file.write(self.subtitles)
        print('file saved to >> ' + 'training_data/' + self.filename + '.txt')

subtitles_file = sys.argv[1]
if( len(sys.argv) >= 3):
    destination_directory = sys.argv[2]
else:
    destination_directory = 'training_data/'

subtitles = SubtitlesPreprocessor(subtitles_file)
subtitles.saveSubtitles(destination_directory)


