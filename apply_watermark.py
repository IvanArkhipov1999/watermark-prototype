from compile import *
from insert import *

def apply_watermark(path_to_file):
	compile_to_assembler(path_to_file)
	insert_commands("./test.s")
	compile_to_binary("./modified.s");
	insert_watermark("./modified")
