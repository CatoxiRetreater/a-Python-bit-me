file = open("binary_file.bin", "ab")

data = b'\x20\x41\x70\x70\x65\x6e\x64'

file.write(data)

file.close()
