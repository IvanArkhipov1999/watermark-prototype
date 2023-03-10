from compile import *
from insert import *

def apply_watermark(source_file):
	compile_file(source_file, "origin.s", "gcc", ["-S"])
	# TODO: count number of commands
	insert_nop_commands("origin.s", 8, "inserted_commands.s")
	compile_file("inserted_commands.s", "inserted_commands", "gcc", []);
	#insert_watermark("./modified")
