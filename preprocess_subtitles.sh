#!/bin/bash
# runs SubtitlesPreprocessor for each .srt file in $INPUT_DIR subdirectories

GR='\e[32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

TEST_DATA_OUTPUT_DIR="test_data"
TRAIN_DATA_OUTPUT_DIR="train_data"

INDEX_FILE=preprocessed_subtitles.txt

INPUT_DIR=

usage() {
    echo "Usage: $0 [options] [-i input_dir -o output_dir -d data_type]"
    echo
    echo "Options:"
    echo "  i input_dir        set input directory"
    echo "  o output_dir       set output directory"
    echo "  d data_type        set data type [" "${AVAIL_DATA_TYPES[@]}" "]"
    echo "  h                  display this message"

}

while getopts "i:h" flag; do
  case "$flag" in
    i) 
        INPUT_DIR="${OPTARG}" 
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

subfolders="${INPUT_DIR}/*/"

for subfolder in $subfolders; do

    echo
    echo "###########################################"
    echo "Preprocessing subtitles inside ${subfolder}"
    echo "###########################################"
    echo 

    counter=0
    srt_path="${subfolder}*.srt"
    genre=$(basename "$subfolder") 

    train_data_output_file="${TRAIN_DATA_OUTPUT_DIR}/${genre}.txt"
    test_data_output_file="${TEST_DATA_OUTPUT_DIR}/${genre}.txt"


    for file in $srt_path; do
        
        if grep -q -F "$file" "$INDEX_FILE"; then

            echo -e "${file} ${RED}already preprocessed${NC}"

        else

            if ! (( counter % 5 )); then

                if python SubtitlesPreprocessor.py "$file" "$test_data_output_file"; then
                    echo -e "subtitles from file: '${file}' ${GR}appended to >> '${test_data_output_file}${NC}"
                    echo "$file" >> "$INDEX_FILE"
                    counter=$((counter + 1))
                else
                    echo -e "${RED}ERROR${NC}"
                fi
                # echo python SubtitlesPreprocessor.py "$file" "$test_data_output_file"
            else 
            
                if python SubtitlesPreprocessor.py "$file" "$train_data_output_file"; then
                    echo -e "subtitles from file: '${file}' ${GR}appended to >> '${train_data_output_file}${NC}"
                    echo "$file" >> "$INDEX_FILE"
                    counter=$((counter + 1))
                else
                    echo -e "${RED}ERROR${NC}"
                fi
                # echo python SubtitlesPreprocessor.py "$file" "$train_data_output_file"
            fi

        fi

    done

done