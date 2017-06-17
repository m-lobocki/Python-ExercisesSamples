# Write a program which can map() and filter() to make a list whose elements are square of even number
# in [1,2,3,4,5,6,7,8,9,10].

raw_list = [1,2,3,4,5,6,7,8,9,10]
even_list = list(filter(lambda x: x % 2 == 0, raw_list))
square_list = list(map(lambda x: x * x, even_list))
