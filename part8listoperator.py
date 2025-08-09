#characters = ["a","b","d","c"]
# list = [1, 2, 4, 3, 9, 8, 5, 6]
# print(characters) # prints the characters
# characters.append("F") # prints and add the character F
# print(characters)
# characters.remove("d") # prints after removing "d"
# print(characters)
# characters.pop(3) # prints after poping what you have instructed
# print(characters)
#list.sort() # prints after correcting any errors
# print(list)
# characters.reverse() # prints after the reversing the way words were written
# print(characters)
# characters= len(characters) # prints the lenght of the characters given
# print(characters)

# Merge operator

# list1 = [1, 2, 3, 4, 5]
#list2 = [6, 7, 8, 9, 10]

# using + operator 
# merged_list = list1 + list2
# list1 = len(list1) # length operator len()
# print(list1)
# print(list2)
# print("Merged List:" , merged_list)

# Repeating operator (*)
# numbers = [0, 1, 2]

# using * operator
# repeated_list = numbers * 3

# print("Repeated List:", repeated_list)

# in operator (in)

# Names = ["Brian", "Owen", "Samuel", "James"]

# using in operator
# user_name = input("Enter Name: ")

# if user_name in Names:
#    print("Name found")
# else:
#    print("Name not found")

# max () and min () operators
# numbers = [15, 42, 8, 23, 56, 91, 3, 78]

# max_num = max(numbers)
# min_num = min(numbers)

# print(f"List of numbers: {numbers}")
# print(f"Maximum number: {max_num}")
# print(f"Minimum number: {min_num}")

# max and min when you ask user to enter values

numbers = list(map(int, input("Enter numbers seperated by spaces: ").split())) # splits does split the input into a list of strings and map(int,....) converts the strings into integers

total_sum = sum(numbers)
max_num = max(numbers)
min_num = min(numbers)

print(f"\nList of numbers: {numbers}")
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
print(f"\nSum of numbers: {total_sum}")
print(f"\nMaximum number: {max_num}")
print(f"\nMinimum number: {min_num}\n")
sum = max_num + min_num
print(f"\nSum of max & min numbers: {sum}")







        