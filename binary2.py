file = open("binary_file.bin", "wb")

data = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64'

file.write(data)

file.close()
