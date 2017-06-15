# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the
# values are square of keys. The function should just print the values only.

def print_squares():
    dictionary = {x: x*x for x in range(1,21)}
    for key, value in dictionary.items():
        print(value)
