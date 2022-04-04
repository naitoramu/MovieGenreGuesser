# Movie Genre Guesser
## An application written in python that uses machine learning to recognize the genre of a movie based on its subtitles

This application is the implementation of the semstral project in the subject "Machine Learning"

## Subtitles preprocessing
To preprocess subtitles, place them in the appropriate directory in srt dir, and then run script preprocess_subtitles.sh

If downloaded subtitles aren't in .srt format, you can place them in downloaded_subs dir, and run script convert2srt.sh

### preprocess_subtitles.sh
#### Runs SubtitlesPreprocessor for each .srt file in $INPUT_DIR
#### usage:
./preprocess_subtitles.sh <movie_genre> <directory_with_genre_folders> <output_directory> 
#### usage example:
./preprocess_subtitles.sh drama srt training_data 


### convert2srt.sh
#### Converts subtitle files from downloaded_subs folder into .srt files

#### usage:
./convert2srt <input_files_extension>

#### usage example:
./convert2srt sub