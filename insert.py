# -----------------------------------------------------------
# Inserts nop commands to the content of given origin file.
# Inserts commands before return command. Inserts as many commands,
# as it is given in parameters. Writes content with nop commands
# to new file with given name.
#
# Parameters:
#
# origin_file: path to file with content for inserting nop commands
# num_of_commands: number of commands to insert
# inserted_commands_file: path to file to write content with nop commands, all directories in path should exist
# -----------------------------------------------------------
def insert_nop_commands(origin_file, num_of_commands, inserted_commands_file):
	# Reading content of origin file
	with open(origin_file, "r") as f:
		contents = f.readlines()

	# Finding return command
	index = contents.index("\tret\n")
	# Inserting jump command to label after inserted commands
	contents.insert(index, "\tjmp\t.FORWATERMARK\n");
	
	# Inserting nop commands
	for i in range(1, num_of_commands + 1):
		contents.insert(index + i, "\tnop\n");

	# Inserting label after nop commands
	contents.insert(index + num_of_commands + 1, ".FORWATERMARK:\n");

	# Writing changed content to the file
	with open(inserted_commands_file, "w") as f:
		contents = "".join(contents)
		f.write(contents)

# -----------------------------------------------------------
# Inserts watermark information to the given file with allocated memory for it.
# Allocated memory contains nop commands. Inserts in this space given sequence
# for marking, size of watermark text and watermark text. Marked sequence takes
# 2 bytes, size of watermark text takes 1 byte (size of text is less than 256 symbols).
# Watermarked file is located in given path.
#
# Parameters:
#
# noped_file: path to file with inserted nop commands
# message: text of message
# watermark_space_in_bytes: number of bytes for watermark information
# marked_sequence: sequence for marking
# watermarked_file: path to watermarked file
# -----------------------------------------------------------
def insert_watermark(noped_file, message, watermark_space_in_bytes, marked_sequence, watermarked_file):
	# Reading content of file with nop commands
	with open(noped_file, "rb") as f:
		file_bytes = bytearray(f.read())

	# Searching space for watermark by nop commands. Index is a begining of this space.
	index = 0
	for byte in file_bytes:
		# 0x90 is an opcode of nop command
		if byte == 0x90:
			is_found = True
			# Checking number of nop commands
			for i in range(watermark_space_in_bytes):
				if file_bytes[index + i] != 0x90:
					is_found = False
			if is_found:
				break
		index = index + 1

	# Putting watermark information: marked sequence, size of message and text of message
	# Marked sequence takes 2 bytes
	file_bytes[index] = marked_sequence // 256
	file_bytes[index + 1] = marked_sequence % 256
	# Length of message is less than 256 symbols
	file_bytes[index + 2] = len(message)

	# Writing text of message
	for i in range(len(message)):
		file_bytes[index + i + 3] = ord(message[i])

	# Writing changed content to the file
	with open(watermarked_file, "wb") as f:
		f.write(file_bytes)

