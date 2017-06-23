# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
#
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 3.55
#
# In case of input data being supplied to the question, it should be assumed to be a console input.

max = int(input())
result = 0

for x in range(1, max + 1):
    result += x / (x + 1)
    print(f"{x} / {x + 1}")

print(result)
