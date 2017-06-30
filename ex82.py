# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

import zlib
string = "hello world!hello world!hello world!hello world!"
compressed = zlib.compress(string.encode('utf-8'))
decompressed = zlib.decompress(compressed)
print(compressed)
print(decompressed)