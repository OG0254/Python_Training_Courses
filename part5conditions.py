# for condition
# Compare student marks
# minMarks = 30
# studentMarks = float(input('Enter your marks: '))

# if   studentMarks >= minMarks:
#    print("You are eligible")
# elif studentMarks >= 25:
#    print("You are in waiting list")
# else:
#    print("You are not eligible")

# Age = 60
# userAge = int(input('Enter your age: '))

# if userAge <= 0:
#   print('Invalid age!')
# elif userAge != 1-12:
#   print('You are a child')
#elif userAge != 13-19:
#    print('You are a teenager')
#elif userAge != 20-59:
#   print('You are an adult')
#else: 
#   userAge >60
#   print('You are a senior citizen')

   # OR


userAge = int(input('Enter your age: '))

if userAge <= 0:
   print('Invalid age!')
elif userAge <= 12:
   print('You are a child')
elif userAge <= 19:
   print('You are a teenager')
elif userAge <= 59:
   print('You are an adult')
else: 
   userAge >60
   print('You are a senior citizen')
