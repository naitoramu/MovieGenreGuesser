from modules.SubtitlesPreprocessor import SubtitlesPreprocessor
from modules.Tokenizer import Tokenizer

import os
import numpy as np
import tensorflow as tf

from keras_visualizer import visualizer

subtitles_preprocessor = SubtitlesPreprocessor("srt/Zootopia.srt")
subtitles = subtitles_preprocessor.getSubtitles()

tokenizer = Tokenizer()
sequences = tokenizer.getPaddedSequences([subtitles])

model = tf.keras.models.load_model("./models/model_v4/model.h5")

os.system("clear")
prediction = model.predict(np.expand_dims(sequences[0], axis=0))[0]

predicted_genre = tokenizer.index_to_genre[np.argmax(prediction).astype('uint8')]
print("Predicted genre: ", predicted_genre, '\n')

print("Confidence:")
for i in range(len(prediction)):
    genre = tokenizer.index_to_genre[i]
    confidence = round(prediction[i] * 100, 2)
    print("    ", genre, "=", confidence, '%')
