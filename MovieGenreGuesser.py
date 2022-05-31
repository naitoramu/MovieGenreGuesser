from modules.SubtitlesPreprocessor import SubtitlesPreprocessor
from modules.Tokenizer import Tokenizer

import numpy as np
import tensorflow as tf

subtitles_preprocessor = SubtitlesPreprocessor("./srt/Zootopia.srt")
subtitles = subtitles_preprocessor.getSubtitles()

tokenizer = Tokenizer()
sequences = tokenizer.getPaddedSequences([subtitles])

model = tf.keras.models.load_model("./models/model_v2/model.h5")
p = model.predict(np.expand_dims(sequences[0], axis=0))[0]

predicted_genre = tokenizer.index_to_genre[np.argmax(p).astype('uint8')]
print("Predicted genre: ", predicted_genre)
