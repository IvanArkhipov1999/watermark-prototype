import os

def compile_to_assembler(path_to_file):
	compiling_command = "gcc "
	compiling_command = compiling_command + path_to_file
	compiling_command = compiling_command + " -S -o test.s"
	os.system(compiling_command)
