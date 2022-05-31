#!/bin/bash
# runs SubtitlesPreprocessor for each .srt file in $INPUT_DIR subdirectories

GR='\e[32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

OUTPUT_DIR=../preprocessed_subtitles

INDEX_FILE=../preprocessed_subtitles/index

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

    srt_path="${subfolder}*.srt"
    genre=$(basename "$subfolder") 

    data_output_file="${OUTPUT_DIR}/${genre}.txt"


    for file in $srt_path; do
        
        if grep -q -F "$file" "$INDEX_FILE"; then

            echo -e "${file} ${RED}already preprocessed${NC}"

        else

                if python ../modules/SubtitlesPreprocessor.py "$file" "$data_output_file"; then
                    echo -e "subtitles from file: '${file}' ${GR}appended to >> '${data_output_file}${NC}"
                    echo "$file" >> "$INDEX_FILE"
                else
                    echo -e "${RED}ERROR${NC}"
                fi

        fi

    done

done