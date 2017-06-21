# Write a function to compute 5/0 and use try/except to catch the exceptions.

try:
    result = 5/0
except ZeroDivisionError:
    print('Divided by zero!')
except:
    print('An error has been thrown!')