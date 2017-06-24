# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma
# separated form while n is input by console.
#
# Example:
# If the following n is given as input to the program:
# 100
# Then, the output of the program should be:
# 0,35,70


def generate_numbers_divisible_by_5_and_7(max):
    for x in range(0, max + 1):
        if x % 5 == 0 and x % 7 == 0: yield str(x)

result = []
n = int(input())
for x in generate_numbers_divisible_by_5_and_7(n):
    result.append(x)

print(','.join(result))