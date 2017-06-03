# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
# ??
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

cash = 0

while True:
    user_input = input()
    if not user_input:
        break
    operation, amount = user_input.split()
    if(not operation or not amount):
        break
    if operation == 'D':
        cash += int(amount)
    if operation == 'W':
        cash -= int(amount)

print(cash)