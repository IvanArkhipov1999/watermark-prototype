import os

# -----------------------------------------------------------
# Compiles given source file to output file with given name by 
# given compiler and flags.
#
# Parameters:
#
# source_file: path to source file for compiling
# assembler_file: path to output file, all directories in path should exist
# compiler: compiler for compiling
# flags: list of flags for compiling
# -----------------------------------------------------------
def compile_file(source_file, output_file, compiler, flags):
	# Setting compiler
	compiling_command = compiler + " "
	# Setting flags
	for flag in flags:
		compiling_command = compiling_command + flag + " "
	# Setting path to source file
	compiling_command = compiling_command + source_file
	# Setting path for assembler file
	compiling_command = compiling_command + " -o " + output_file
	# Executing command
	os.system(compiling_command)
