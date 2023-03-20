import sys

from apply_watermark import *
from extract_watermark import *

if __name__== "__main__":
	if len(sys.argv) < 3:
		print("Not enough arguments")	
		sys.exit()

	path_to_source_file = sys.argv[1]
	watermark_message = sys.argv[2]

	apply_watermark(path_to_source_file, watermark_message, "gcc")
	#extract_watermark()
