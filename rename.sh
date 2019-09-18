#!/bin/bash

let i=0                               # define an incremental variable
path=/home/gjx/visual-struct/darknet/validateImage               # add your file path here
cd ${path}                             # make a backup directory
for file in *.png          # *.jpg means all jpg files in current directory
do
    
    mv "${file}" "${i}.png"

    echo "${file} renamed as ${i}.png"
    let i=i+1
done
