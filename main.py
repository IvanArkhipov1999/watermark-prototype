import sys

from apply_watermark import *
from extract_watermark import *

if __name__== "__main__":
	if len(sys.argv) < 2:
		print("Not enough arguments")
		sys.exit()

	path_to_source_file = sys.argv[1]

	apply_watermark(path_to_source_file)
	#extract_watermark()
