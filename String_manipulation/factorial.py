number = 4
original_number = number
factorial = 1

# Using a while loop to calculate the factorial
while number > 0:
    factorial *= number
    number -= 1
print(f"The factorial of {original_number} is {factorial}")

# Calculate number of zeros in the factorial result
zeros = 0
factorial_str = str(factorial)
for digit in reversed(factorial_str):
    if digit == '0':
        zeros += 1
    else:
        break

print(f"The number of zeros in the factorial of {original_number} is {zeros}")

# Using a for loop to calculate the factorial
# for i in range(1, original_number + 1):
#     factorial *= i
# print(f"The factorial of {original_number} is {factorial}")