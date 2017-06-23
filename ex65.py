# Write a program to compute:
#
# f(n)=f(n-1)+100 when n>0
# and f(0)=1
#
# Example:
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 500
#
# In case of input data being supplied to the question, it should be assumed to be a console input.

def f(x):
    return f(x-1) + 100 if x > 0 else x

n = int(input())
print(f(n))