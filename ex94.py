# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all
# duplicate values with original order reserved.

target = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

set = set()
result = list()

for item in target:
    if item not in set:
        set.add(item)
        result.append(item)

print(result)