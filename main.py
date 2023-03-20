import sys

from apply_watermark import *
from extract_watermark import *

# -----------------------------------------------------------
# Help function.
# -----------------------------------------------------------
def print_help():
	print("This is tool for applying and extracting watermark for one-file project.")
	print("Usage: <path to python3 interpreter> main.py [arguments].")
	print("1) If you want to apply watermark, the arguments are:")
	print("\t- \"apply_watermark\"\t -- flag, meaning applying watermark mode")
	print("\t- path-to-source-file\t -- path to source c\c++ file of program to be watermarked")
	print("\t- watermark-message\t -- message to be inserted (less than 256 symbols)")
	print("\t- path-to-compiler\t -- path to c\c++ compiler")
	print("2) If you want to extract watermark, the arguments are:")
	print("\t- \"extract_watermark\"\t -- flag, meaning extracting watermark mode")
	print("\t- path-to-watermarked-file\t -- path to executable file with watermark")

if __name__== "__main__":
	# If there is no argument, help information should be printed.
	if len(sys.argv) < 2:
		print_help()
		sys.exit()

	# For marked sequence is chosen 1111001101. Suffix 011110 is random values.
	# It is needed so that the length of the sequence is a multiple of 16.
	# It should store full number of bytes.
	marked_sequence = int('0b1111001101011110', 2)

	# Applying watermark mode
	if sys.argv[1] == "apply_watermark":
		# If there is not enough arguments
		if len(sys.argv) < 5:
			print("Not enough arguments for applying watermark.")
			print("Help information:")
			print_help()
			sys.exit()
		# Reading arguments
		path_to_source_file = sys.argv[2]
		watermark_message = sys.argv[3]
		compiler = sys.argv[4]

		# Applying watermark
		apply_watermark(path_to_source_file, watermark_message, compiler, marked_sequence)
	# Extracting watermark mode
	elif sys.argv[1] == "extract_watermark":
		# If there is not enough arguments
		if len(sys.argv) < 3:
			print("Not enough arguments for extracting watermark.")
			print("Help information:")
			print_help()
			sys.exit()
		# Reading arguments
		path_to_watermarked_file = sys.argv[2]

		# Printing the result of extracting
		print(extract_watermark(path_to_watermarked_file, marked_sequence))
	# Another cases
	else:
		print_help()
