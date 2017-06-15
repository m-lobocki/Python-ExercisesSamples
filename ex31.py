# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

def print_longer(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    if len_str1 > len_str2:
        print(str1)
    elif len_str1 < len_str2:
        print(str2)
    else:
        print(str1 + '\n' + str2)
