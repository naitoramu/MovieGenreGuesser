import numpy as np
import tensorflow as tf

from glob import glob

from tensorflow.keras.preprocessing.sequence import pad_sequences

class Tokenizer:
    def __init__(self):
        self.SEQUENCE_LENGTH = 10000
        self.genres = ('action', 'comedy', 'drama')
        self.genre_to_index = dict((c, i) for i, c in enumerate(self.genres))
        self.index_to_genre = dict((v, k) for k, v in self.genre_to_index.items())
        self.data_files = glob("./preprocessed_subtitles/*.txt")
        self.all_subtitles = self.loadAllSubtitles()
        self.tokenizer = tf.keras.preprocessing.text.Tokenizer()
        self.tokenizer.fit_on_texts(self.all_subtitles)

    def loadFile(self, filename):
        with open(filename, 'rt') as file:
            return file.read()

    def getPaddedSequences(self, subtitles):
        sequences = self.tokenizer.texts_to_sequences(subtitles)
        padded = pad_sequences(sequences, truncating='post',padding='post', maxlen=self.SEQUENCE_LENGTH)
        return padded

    def loadAllSubtitles(self):
        subtitles = []
        for filename in self.data_files:
            words = self.loadFile(filename).split('\n')
            subtitles += words
        return subtitles

    def genresToIds(self, genres):
        return np.array([self.genre_to_index.get(x) for x in genres])

    def getVocabSize(self):
        return len(self.tokenizer.word_index) + 1
    
    def getSequenceLength(self):
        return self.SEQUENCE_LENGTH

    def getSubtitlesCount(self):
        return len(self.all_subtitles)
