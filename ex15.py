# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

num = int(input())
result = num + (num * 11) + (num * 111) + (num * 1111)
print(result)