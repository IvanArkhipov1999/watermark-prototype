# -----------------------------------------------------------
# Extracts watermark message from given file by given sequence 
# for marking. If sequense is not found, function returns empty
# string. It may return false watermark message, it depends on 
# sequence for marking.
#
# Parameters:
#
# path_to_watermarked_file: path to file with watermark
# marked_sequence: sequence for marking
# -----------------------------------------------------------
def extract_watermark(path_to_watermarked_file, marked_sequence):
	# Marked sequence takes 2 bytes
	first_marked_byte = marked_sequence // 256
	second_marked_byte = marked_sequence % 256

	# Reading content of watermarked file
	with open(path_to_watermarked_file, "rb") as f:
		file_bytes = bytearray(f.read())

	# Searching watermark by sequence for marking. Index is a begining of watermark.
	index = 0
	is_first_marked_byte_found = False
	is_found_watermark = False
	for byte in file_bytes:
		# Checking if this is first byte of sequence for marking
		if byte == first_marked_byte:
			is_first_marked_byte_found = True
		# Checking if it is sequence for marking
		if byte == second_marked_byte and is_first_marked_byte_found:
			index = index + 1
			is_found_watermark = True
			break
		index = index + 1

	# If there is no sequence for marking, then return empty string
	if not is_found_watermark:
		return ''

	# Reading size of watermark text
	message_size = file_bytes[index]
	index = index + 1

	# Converting result to string and return
	return ''.join(map(chr, file_bytes[index:(index + message_size)]))

