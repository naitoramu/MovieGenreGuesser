#!/bin/bash
# runs SubtitlesPreprocessor for each .srt file in $INPUT_DIR
# usage:
#   ./preprocess_subtitles.sh <movie_genre> <directory_with_genre_folders> <output_directory> 
# example:
#   ./preprocess_subtitles.sh drama srt training_data 

MOVIE_GENRE=$1
INPUT_DIR=$2
OUTPUT_DIR=$3

SRT_LOCATION="${INPUT_DIR}/${MOVIE_GENRE}/*.srt"
OUTPUT_FILE="${OUTPUT_DIR}/${MOVIE_GENRE}.txt"

for file in $SRT_LOCATION; do
    # echo python SubtitlesPreprocessor.py train "$file" $OUTPUT_FILE
    python SubtitlesPreprocessor.py train "$file" $OUTPUT_FILE
done