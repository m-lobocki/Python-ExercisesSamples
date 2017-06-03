# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

lower_case = 0
upper_case = 0

sentence = input()
for char in sentence:
    if char.islower():
        lower_case += 1
    if char.isupper():
        upper_case += 1

print(f'UPPER CASE {upper_case}')
print(f'LOWER CASE {lower_case}')