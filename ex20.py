# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n


class Generator:
    @staticmethod
    def nums_divisible_by_7(max):
        return (x for x in range(0, max + 1) if x % 7 == 0)

max = int(input())
for num in Generator.nums_divisible_by_7(max):
    print(num)