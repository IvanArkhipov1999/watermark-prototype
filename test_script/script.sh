#!/bin/bash

failure=0

mkdir tmp
cd tmp

for test in $(ls ../tests)
do
	python3 ../main.py apply_watermark ../tests/test.cpp "Test message" gcc
	output=$(python3 ../main.py extract_watermark watermarked)
	echo "----------"

	if [[ "$output" == "Test message" ]]; then
  		(( failure |= 0 ))
		echo "OK"
	else
		(( failure |= 1 ))
		echo "FAILURE"
	fi

	echo $test
	echo $output
done
echo "----------"

cd ..
rm -r tmp
rm -r __pycache__
exit $failure
