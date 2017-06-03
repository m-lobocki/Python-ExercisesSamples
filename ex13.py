# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

letters = 0
digits = 0

sentence = input()
for char in sentence:
    if char.isalpha():
        letters += 1
    if char.isdigit():
        digits += 1

print(f'LETTERS {letters}')
print(f'DIGITS {digits}')