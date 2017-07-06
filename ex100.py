# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do
# we have?

heads = 35
legs = 94
for x in range(heads + 1):
    y = heads - x
    if 2 * x + 4 * y == legs:
        print(f'{x} {y}')
