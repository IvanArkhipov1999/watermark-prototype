#!/bin/bash

mkdir tmp
cd tmp
python3 ../main.py apply_watermark ../tests/test.cpp "Test message" gcc
output=$(python3 ../main.py extract_watermark watermarked)
gcc --version
echo $output
failure=1
if [[ "$output" == "Test message" ]]; then
  failure=0
fi
cd ..
rm -r tmp
rm -r __pycache__
exit $failure
