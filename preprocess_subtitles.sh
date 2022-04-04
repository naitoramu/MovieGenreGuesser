#!/bin/bash
# runs SubtitlesPreprocessor for each .srt file in $INPUT_DIR subdirectories
# usage:
#   ./preprocess_subtitles.sh <directory_with_folders_with_srt_files> <output_directory> 
# example:
#   ./preprocess_subtitles.sh srt training_data


INPUT_DIR=$1
OUTPUT_DIR=$2

subfolders="${INPUT_DIR}/*/"

for subfolder in $subfolders; do

    srt_path="${subfolder}*.srt"
    genre=$(basename $subfolder) 

    output_file="${OUTPUT_DIR}/${genre}.txt"

    for file in $srt_path; do
        python SubtitlesPreprocessor.py train "$file" $output_file
    done

done