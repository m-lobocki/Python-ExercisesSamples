# Define a function that can accept an integer number as input and print the "It is an even number"
# if the number is even, otherwise print "It is an odd number".

def print_parity(num):
    print("Is is an even number") if num % 2 == 0 else print("It is an odd number")

print_parity(2)
print_parity(4)
print_parity(5)