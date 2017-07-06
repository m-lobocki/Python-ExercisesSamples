# Please write a program which count and print the numbers of each character in a string input by console.
#
# Example:
# If the following string is given as input to the program:
# abcdefgabc
# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

string = input()
words_occurency = dict()
for letter in string:
    words_occurency[letter] = words_occurency.get(letter, 0) + 1

print('\n'.join([f'{key},{value}' for key, value in words_occurency.items()]))