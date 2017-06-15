# Define a function which can generate and print a list where the values are square of numbers between 1 and 20
# (both included).

def print_squares():
    list = [x*x for x in range(1,21)]
    print(list)