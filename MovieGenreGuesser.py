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
    return np.array([genre_to_index.get(x) for x in genres])


genres = ('action', 'comedy', 'drama')
genre_to_index = dict((c, i) for i, c in enumerate(genres))
index_to_class = dict((v, k) for k, v in genre_to_index.items())
data_files = glob("./preprocessed_subtitles/*.txt")
all_subtitles = []

for filename in data_files:
    words = loadFile(filename).split('\n')
    all_subtitles += words


tokenizer = Tokenizer()
tokenizer.fit_on_texts(all_subtitles)
df = pandas.read_csv("./data/train.csv", converters={i: str for i in range(len(all_subtitles))}, index_col=None)
sequences = tokenizer.texts_to_sequences(df.Subtitles.to_list())

train_sequences = get_padded_sequences(sequences)
train_genres = genres_to_ids(df.Genre.to_list())
# print(train_genres)

df = pandas.read_csv("./data/validation.csv", converters={i: str for i in range(len(all_subtitles))}, index_col=None)
sequences = tokenizer.texts_to_sequences(df.Subtitles.to_list())

validation_sequences = get_padded_sequences(sequences)
validation_genres = genres_to_ids(df.Genre.to_list())

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(
        len(tokenizer.word_index)+1, 
        16, 
        input_length=SEQUENCE_LENGTH
    ),
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

h = model.fit(
    train_sequences, train_genres,
    validation_data=(validation_sequences, validation_genres),
    epochs=20,
    callbacks=[tf.keras.callbacks.EarlyStopping(
        monitor='val_accuracy', patience=2   
    )]
)

model.save("./models/model_v1/model_v1.h5")

df = pandas.read_csv("./data/test.csv", converters={i: str for i in range(len(all_subtitles))}, index_col=None)
sequences = tokenizer.texts_to_sequences(df.Subtitles.to_list())

test_sequences = get_padded_sequences(sequences)
test_genres = genres_to_ids(df.Genre.to_list())
model.evaluate(test_sequences, test_genres)