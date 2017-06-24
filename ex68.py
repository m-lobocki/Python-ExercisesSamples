# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is
# input by console.
#
# Example:
# If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10


def generate_even_numbers(max):
    for x in range(0, max + 1):
        if x % 2 == 0: yield str(x)

result = []
n = int(input())
for x in generate_even_numbers(n):
    result.append(x)

print(','.join(result))