#!/bin/bash

cd paths
for f in $(ls | sort -n);do
    clear
    cat $f
    sleep 0.5
done