# By using list comprehension, please write a program to print the list after removing the value 24 in
# [12,24,35,24,88,120,155].

target = [12,24,35,24,88,120,155]
result = [x for x in target if x != 24]
print(result)