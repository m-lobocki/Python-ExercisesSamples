# Please write assert statements to verify that every number in the list [2,4,6,8] is even.


numbers = [2,4,6,8]
assert all(x % 2 == 0 for x in numbers)