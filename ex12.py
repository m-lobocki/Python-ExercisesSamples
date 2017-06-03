# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of
# the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

nums = map(str, range(1000, 3001))
result = []

for num in nums:
    digits = [char if int(char) % 2 == 0 else False for char in num]
    if all(digits):
        result.append(num)

print(','.join(result))
