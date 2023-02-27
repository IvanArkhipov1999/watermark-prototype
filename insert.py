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

	with open("modified.s", "w") as f:
		contents = "".join(contents)
		f.write(contents)
