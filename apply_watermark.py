from compile import *
from insert import *

def apply_watermark(source_file):
	compile_to_assembler(source_file, "origin.s", "gcc", [])
	# TODO: count number of commands
	insert_nop_commands("origin.s", 8, "inserted_commands.s")
	#compile_to_binary("./modified.s");
	#insert_watermark("./modified")
