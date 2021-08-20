#!/bin/bash 

for i in {1,2,3,4,5,6,7}
do
    len=$((10 ** $i))
    file_path="$1$len.txt"
    
    ../rnnlm-0.3e/rnnlm -rnnlm $2 -gen $len -debug 0 > $file_path
done