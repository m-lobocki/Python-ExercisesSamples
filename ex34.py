# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys.

def print_squares():
    dictionary = {x: x*x for x in range(1,21)}
    print(dictionary)
