# Watermark prototype
This repository contains prototype of watermarking software in code section of elf. 

This is tool for applying and extracting watermark for one-file project.
Usage: <path to python3 interpreter> main.py [arguments].
1) If you want to apply watermark, the arguments are:
	- "apply_watermark"	 -- flag, meaning applying watermark mode
	- path-to-source-file	 -- path to source c\c++ file of program to be watermarked
	- watermark-message	 -- message to be inserted (less than 256 symbols)
	- path-to-compiler	 -- path to c\c++ compiler
2) If you want to extract watermark, the arguments are:
	- "extract_watermark"	 -- flag, meaning extracting watermark mode
	- path-to-watermarked-file	 -- path to executable file with watermark

Prototype is tested on ubuntu 18.04 with compiler gcc version 7.5.0. Work correctness of prototype is not guaranteed with other operating system and compiler.
