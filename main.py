import sys

from apply_watermark import *
from extract_watermark import *

if __name__== "__main__":
	if len(sys.argv) < 1:
		print("Not enough arguments")	
		sys.exit()

	# For marked sequence is chosen 1111001101. Suffix 011110 is random values.
	# It is needed so that the length of the sequence is a multiple of 16.
	# It should store full number of bytes.
	marked_sequence = int('0b1111001101011110', 2)

	if sys.argv[1] == "apply_watermark":
		if len(sys.argv) < 4:
			print("Not enough arguments for applying watermark")	
			sys.exit()
		path_to_source_file = sys.argv[2]
		watermark_message = sys.argv[3]
		compiler = sys.argv[4]

		apply_watermark(path_to_source_file, watermark_message, compiler, marked_sequence)
	elif sys.argv[1] == "extract_watermark":
		path_to_watermarked_file = sys.argv[2]

		print(extract_watermark(path_to_watermarked_file, marked_sequence))
	else:
		print("Incorrect arguments")
