#!/bin/bash

rm rnnlm/models/model
rm rnnlm/models/model.output.txt

time ../rnnlm-0.3e/rnnlm -train $1 -valid $2 -rnnlm $3 -hidden $4 -rand-seed 1 -debug 2 -class $5 -bptt $6
mv $3 rnnlm_models/
pre=$3
suf=".output.txt"
MODEL_OUTPUT="${pre}${suf}"
mv $MODEL_OUTPUT rnnlm_models/
