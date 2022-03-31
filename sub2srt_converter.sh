#!/bin/bash

for file in downloaded_subs/*.sub; do
  filename=${file::-4}
  echo ffmpeg -i "$file" "${filename}.srt"
  ffmpeg -i "$file" "${filename}.srt"
done

rm downloaded_subs/*.sub