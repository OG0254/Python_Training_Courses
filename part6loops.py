# iteration / for loop
# for i in range(1, 51):
# print(i)

# Conditional / while loop
# i = 1
# while i <=51:
#    print (i)
#    i += 3

# Getting sum

# n = int(input('User enter number :'))
# total = 0
# for i in range (1, n + 1):
#    total += i
#    print(f"The sum from 1 to {n} is {total}") # getting sum

# Multilplication table

# num = int(input("Enter a number:"))

# print(f"\nMultiplication Table of {num}:")
# for i in range(1, 11):
#    print(f"{num} * {i} = {num * i}") # creating multiplication table


# while loop for giving out even numbers between 2 to 20

# num = 2
# while num <= 20:
#     print (num)
#    num += 2

# Nested loop
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1): #outer loop for rows
    for j in range(i):  #inner loop for printing (*)
        print("*", end=" ")
        print() # move to the next line after inner loop