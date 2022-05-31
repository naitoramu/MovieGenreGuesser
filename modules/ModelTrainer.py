from statistics import mode
import pandas
import tensorflow as tf
import numpy as np
import random

from Tokenizer import Tokenizer


tokenizer = Tokenizer()
df = pandas.read_csv("./data/train.csv", converters={i: str for i in range(tokenizer.getSubtitlesCount())}, index_col=None)

train_sequences = tokenizer.getPaddedSequences(df.Subtitles.to_list())
train_genres = tokenizer.genresToIds(df.Genre.to_list())
# print(train_genres)

df = pandas.read_csv("./data/validation.csv", converters={
                     i: str for i in range(tokenizer.getSubtitlesCount())}, index_col=None)

validation_sequences = tokenizer.getPaddedSequences(df.Subtitles.to_list())
validation_genres = tokenizer.genresToIds(df.Genre.to_list())

# model = tf.keras.models.Sequential([
#     tf.keras.layers.Embedding(
#         len(tokenizer.word_index)+1, 
#         16, 
#         input_length=SEQUENCE_LENGTH
#     ),
#     tf.keras.layers.Bidirectional(
#         tf.keras.layers.LSTM(20, return_sequences=True)
#     ),
#     tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(20)),
#     tf.keras.layers.Dense(3, activation='softmax')
# ])

# model.compile(
#     loss='sparse_categorical_crossentropy',
#     optimizer='adam',
#     metrics=['accuracy']
# )

# h = model.fit(
#     train_sequences, train_genres,
#     validation_data=(validation_sequences, validation_genres),
#     epochs=20,
#     callbacks=[tf.keras.callbacks.EarlyStopping(
#         monitor='val_accuracy', patience=2   
#     )]
# )

# model.save("./models/model_v3/model.h5")
model = tf.keras.models.load_model("./models/model_v2/model.h5")

df = pandas.read_csv("./data/test.csv", converters={
                     i: str for i in range(tokenizer.getSubtitlesCount())}, index_col=None)

test_sequences = tokenizer.getPaddedSequences(df.Subtitles.to_list())
test_genres = tokenizer.genresToIds(df.Genre.to_list())
# model.evaluate(test_sequences, test_genres)

i = random.randint(0,len(test_sequences)-1)

print('Subtitles:', test_sequences[i])
print('Genre:', tokenizer.index_to_genre[test_genres[i]])

p = model.predict(np.expand_dims(test_sequences[i], axis=0))[0]

predicted_genre = tokenizer.index_to_genre[np.argmax(p).astype('uint8')]

print("Predicted genre: ", predicted_genre)
