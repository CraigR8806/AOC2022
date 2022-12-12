#!/bin/bash

next=$(($(ls src | sort -n | tail -1)+1))

mkdir src/$next

head -7 src/1204/main.py > src/$next/main.py

touch src/$next/input.data src/$next/sampleInput.data