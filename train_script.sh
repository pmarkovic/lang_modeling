#!/bin/bash

rm model
rm model.output.txt

#rnn model is trained here
time ../rnnlm -train $1 -valid $2 -rnnlm model -hidden $3 -rand-seed 1 -debug 2 -class 9999 -bptt $4
