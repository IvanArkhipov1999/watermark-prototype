from compile import *
from insert import *

# -----------------------------------------------------------
# Inserts given message to binary, compiled from source file.
#
# Parameters:
#
# source_file: path to source file in which binary message should be watermarked
# watermark_message: message to be inserted
# compiler: path to compiler
# marked_sequence: sequence for marking
# -----------------------------------------------------------
def apply_watermark(source_file, watermark_message, compiler, marked_sequence):
	# Number of bytes to store sequence for marking.
	marked_sequence_space_in_bytes = (marked_sequence.bit_length() + 7) // 8
	# Number of bytes to store size of message.
	message_size_space_in_bytes = (len(watermark_message).bit_length() + 7) // 8
	# Full size in bytes for watermark: bytes for marked sequence + bytes for size of message + message
	watermark_space_in_bytes = marked_sequence_space_in_bytes + message_size_space_in_bytes + len(watermark_message)

	# Compiling source file to assembler. We use only gcc because of sequence.
	compile_file(source_file, "origin.s", compiler, ["-S"])
	# Insert nop commands to assembler files
	insert_nop_commands("origin.s", watermark_space_in_bytes, "inserted_commands.s")
	# Compile file with nops to binary. We use only gcc because of sequence.
	compile_file("inserted_commands.s", "inserted_commands", "gcc", [])
	# Insert watermark to binary
	insert_watermark("inserted_commands", watermark_message, watermark_space_in_bytes, marked_sequence, "watermarked")
