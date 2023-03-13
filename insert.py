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

def insert_watermark(noped_file, message, watermark_space_in_bytes, marked_sequence):
	with open(noped_file, "rb") as f:
		file_bytes = bytearray(f.read())
	index = 0

	for byte in file_bytes:
		if byte == 0x90:
			is_found = True
			for i in range(watermark_space_in_bytes):
				if file_bytes[index + i] != 0x90:
					is_found = False
			if is_found:
				break
		index = index + 1

	# TODO: make marked seq not only 2 bytes and size of message not only 1 byte
	file_bytes[index] = marked_sequence // 256
	file_bytes[index + 1] = marked_sequence % 256
	file_bytes[index + 2] = len(message)

	for i in range(len(message)):
		file_bytes[index + i + 3] = ord(message[i])

	with open("watermarked", "wb") as f:
		f.write(file_bytes)

