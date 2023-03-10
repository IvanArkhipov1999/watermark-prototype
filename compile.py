import os

# -----------------------------------------------------------
# Compiles given source file to assembler file with given name by 
# given compiler and flags.
#
# Parameters:
#
# source_file: path to source file for compiling
# assembler_file: path to assembler file, all directories in path should exist
# compiler: compiler for compiling
# flags: list of flags for compiling
# -----------------------------------------------------------
def compile_to_assembler(source_file, assembler_file, compiler, flags):
	# Setting compiler
	compiling_command = compiler + " "
	# Setting flags
	for flag in flags:
		compiling_command = compiling_command + flag + " "
	# Setting path to source file
	compiling_command = compiling_command + source_file
	# Setting path for assembler file
	compiling_command = compiling_command + " -S -o " + assembler_file

	os.system(compiling_command)

def compile_to_binary(path_to_file):
	compiling_command = "gcc "
	compiling_command = compiling_command + path_to_file
	compiling_command = compiling_command + " -o modified"
	os.system(compiling_command)
