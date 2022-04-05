#!/bin/bash
# runs SubtitlesPreprocessor for each .srt file in $INPUT_DIR subdirectories

declare -a AVAIL_DATA_TYPES
AVAIL_DATA_TYPES[1]="train"
AVAIL_DATA_TYPES[2]="test"

INPUT_DIR=
OUTPUT_DIR=
DATA_TYPE=

usage() {
    echo "Usage: $0 [options] [-i input_dir -o output_dir -d data_type]"
    echo
    echo "Options:"
    echo "  i input_dir        set input directory"
    echo "  o output_dir       set output directory"
    echo "  d data_type        set data type [" "${AVAIL_DATA_TYPES[@]}" "]"
    echo "  h                  display this message"

}

while getopts "i:o:d:h" flag; do
  case "$flag" in
    i) 
        INPUT_DIR="${OPTARG}" 
        # echo "${OPTARG}"
        ;;
    o)
        OUTPUT_DIR="${OPTARG}" 
        # echo "${OPTARG}"
        ;;
    d)
        DATA_TYPE="${OPTARG}"
        # echo "${OPTARG}"
        ;;
    h)
        usage
        exit 1 ;;
    :)  
        echo "Missing option argument for -$OPTARG" >&2
        usage
        exit 1;;
    *)
        echo "Unimplemented option: -$OPTARG" >&2
        usage
        exit 1 ;;
  esac
done

available_data_type=false

for data_type in "${AVAIL_DATA_TYPES[@]}"; do
    [[ "$data_type" == $DATA_TYPE ]] && available_data_type=true
done

if ! $available_data_type; then
    echo "Syntax: invalid data type"
    usage
    exit 1
fi

subfolders="${INPUT_DIR}/*/"

for subfolder in $subfolders; do

    srt_path="${subfolder}*.srt"
    genre=$(basename $subfolder) 

    output_file="${OUTPUT_DIR}/${genre}.txt"

    for file in $srt_path; do
        # echo python SubtitlesPreprocessor.py "$DATA_TYPE" "$file" $output_file
        
        python SubtitlesPreprocessor.py train "$file" $output_file
    done

done