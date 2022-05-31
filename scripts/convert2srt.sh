#!/bin/bash
# converts subtitle files from downloaded_subs folder into .srt files
# usage:
#   ./convert2srt <input_files_extension>


if [ -z "$1" ]
  then
    INPUT_FILES_EXTENSION='sub'
  else
    INPUT_FILES_EXTENSION=$1
fi

FILES="downloaded_subs/*.${INPUT_FILES_EXTENSION}"

for file in $FILES; do
  filename=${file::-4}
  echo ffmpeg -i "$file" "${filename}.srt"
  ffmpeg -i "$file" "${filename}.srt"
done

rm $FILES