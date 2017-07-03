# Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

target = [5, 6, 77, 45, 22, 12, 24]
new_list = [x for x in target if x % 2 != 0]
print(new_list)