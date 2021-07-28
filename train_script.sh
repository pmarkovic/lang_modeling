#!/bin/bash

rm rnnlm/models/model
rm rnnlm/models/model.output.txt

time ./rnnlm/rnnlm -train $1 -valid $2 -rnnlm model -hidden $3 -rand-seed 1 -debug 2 -class $4 -bptt $5
