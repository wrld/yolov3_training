#!/bin/bash

let i=376                               # define an incremental variable
path=/home/gjx/picture/dancer/2020.1.24/jpg               # add your file path here
cd ${path}                             # make a backup directory
for file in *.jpeg           *.jpg means all jpg files in current directory
do
    
    mv "${file%.*}.txt" "newimage_${i}.txt"
    mv "${file}" "newimage_${i}.jpeg"
   
    echo "${file} renamed as newimage_${i}.jpeg"
    

    let i=i+1
done
