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

def insert_watermark(path_to_file):
	with open(path_to_file, "rb") as f:
		file_bytes = bytearray(f.read())
	index = 0

	for byte in file_bytes:
		if byte == 0x90:
			is_found = True
			for i in range(4):
				if file_bytes[index + i] != 0x90:
					is_found = False
			if is_found:
				break
		index = index + 1
	print(hex(index))
		
	file_bytes[index] = 0x77
	file_bytes[index + 1] = 0x6f
	file_bytes[index + 2] = 0x72
	file_bytes[index + 3] = 0x64

	with open("watermarked", "wb") as f:
		f.write(file_bytes)

