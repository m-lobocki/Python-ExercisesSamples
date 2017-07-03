# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in
# [12,24,35,70,88,120,155].

target = [12, 24, 35, 70, 88, 120, 155]
new_list = [x for (x, i) in enumerate(target) if i % 2 != 0]
print(new_list)
