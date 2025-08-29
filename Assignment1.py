#Q1. VARIABLES AND DATA TYPES
print("Q1. VARIABLES AND DATA TYPES")
# Variables
name = "Umme Aiman"
age = 20
is_student = True

# Print values in single line
print(name, age, is_student)

# Print data types
print(type(name))       # str
print(type(age))        # int
print(type(is_student)) # bool

#Q2. ARITHMETIC OPERATIONS
print("Q2. ARITHMETIC OPERATIONS")
x = 20
y = 6

print("Addition", x + y)
print("Subtraction", x - y)
print("Multiplication", x * y)
print("Division", x / y)
print("Floor Division", x // y)
print("Modulus", x % y)
print("Exponent", x ** y)


# Q3. ASSIGNMENT OPERATORS
print("Q3. ASSIGNMENT OPERATORS")
num = 10
print("Initial value of num =", num)

# Add 5 to num
num += 5
print("After num += 5:", num)

# Subtract 3 from num
num -= 3
print("After num -= 3:", num)

# Multiply num by 2
num *= 2
print("After num *= 2:", num)

# Divide num by 4
num /= 4
print("After num /= 4:", num)

print("final value of num:", num)


#Q4. COMPARISON OPERATORS
print("Q4. COMPARISON OPERATORS")

a = 15
b = 12

# Check if a is bigger than b
print("a > b:", a > b)

# Check if a is smaller than b
print("a < b:", a < b)

# Check if a and b are the same
print("a == b:", a == b)

# Check if a and b not same
print("a != b:", a != b)

# Check if a is bigger or equal to b
print("a >= b:", a >= b)

# Check if a is smaller or equal to b
print("a <= b:", a <= b)


#Q5. LOGICAL OPERATORS
print("Q5. LOGICAL OPERATORS")

# Assign boolean values
p = True
q = False

# AND operator: returns True only if both are True
result = p and q
print("p AND q:", result)

# OR operator: returns True if at least one is True
result2 = p or q
print("p OR q:", result2)

# NOT operator: reverses the value (True -> False, False -> True)
result3 = not p
print("NOT p:", result3)

result4 = not q
print("NOT q:", result4)


#Q6. REAL LIFE EXAMPLE
print("Q6. REAL LIFE EXAMPLE")

notebook_price = 80
total_quantity = 7
money = 600

#if i buy 7 notebook calculate total cost
total_price = notebook_price * total_quantity

#print the total
print("total cost of 7 notebooks will be:",total_price)

if money > total_price:
	print("You have enough money to buy 7 notebooks.")
else:
	print("You do not have enough money to buy 7 notebooks.")
	



    # Take input from user and convert it into integer
print("Q7. BONUS")
num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

# Calculate the sum of both numbers
sum = num1 + num2

# Print the sum
print("Sum of the two numbers is:", sum)

# Check whether the first number is greater than the second number
if num1 > num2:
	print("First Number is greater than Second Number")
else: 
	print("Second Number is greater than First Number")