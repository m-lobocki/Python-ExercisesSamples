# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed
# of digits only.

import re

sequence = input()
words_with_digits = re.findall('\d+', sequence)
print(words_with_digits)