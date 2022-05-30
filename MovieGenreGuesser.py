import pickle
import csv
import pandas
import tensorflow as tf
import numpy as np

from glob import glob

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

SEQUENCE_LENGTH = 10000


def loadFile(filename):
    with open(filename, 'rt') as file:
        return file.read()

def get_padded_sequences(sequences):
    padded = pad_sequences(sequences, truncating='post', padding='post', maxlen=SEQUENCE_LENGTH)
    return padded


def genres_to_ids(genres):
    new_list = []
    for genre in genres:
        print(genre)
        new_list.append(genre_to_index.get(genre))
    return new_list
    # return np.array([genre_to_index.get(x) for x in genres])

data_files = glob("./preprocessed_subtitles/*.txt")
all_subtitles = []

for filename in data_files:
    words = loadFile(filename).split('\n')
    all_subtitles += words


tokenizer = Tokenizer()
tokenizer.fit_on_texts(all_subtitles)
df = pandas.read_csv("./data/train.csv", converters={i: str for i in range(1000)}, index_col=None)
# print(all_subtitles)
# print(df.Subtitles.to_list())
sequences = tokenizer.texts_to_sequences(df.Subtitles.to_list())
# print(len(df.Subtitles.to_list()))

padded_sequences = get_padded_sequences(sequences)
# print(len(padded_sequences))
genres = ('action', 'comedy', 'drama')
genre_to_index = dict((c, i) for i, c in enumerate(genres))
index_to_class = dict((v, k) for k, v in genre_to_index.items())

train_genres = genres_to_ids(df.Genre.to_list())
print(df.Genre.to_list())
print(train_genres)

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(10000, 16, input_length=SEQUENCE_LENGTH),
    tf.keras.layers.Bidirectional(
        tf.keras.layers.LSTM(20, return_sequences=True)
    ),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(20)),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)
