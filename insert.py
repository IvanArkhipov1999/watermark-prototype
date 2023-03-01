def insert_commands(path_to_file):
	with open(path_to_file, "r") as f:
		contents = f.readlines()

	index = contents.index("\tret\n")
	contents.insert(index, "\tjmp\t.L2\n");
	contents.insert(index + 1, "\tnop\n");
	contents.insert(index + 2, "\tnop\n");
	contents.insert(index + 3, "\tnop\n");
	contents.insert(index + 4, "\tnop\n");
	contents.insert(index + 5, ".L2:\n");

	with open(path_to_file, "w") as f:
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

