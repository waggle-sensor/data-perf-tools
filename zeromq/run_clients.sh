#!/bin/bash

n=$1
data_dir=data/$(date +%s)
mkdir -p $data_dir
seq $n | xargs -n 1 -P $n bash -c "python3 broadcaster_client.py > $data_dir/\$0"
