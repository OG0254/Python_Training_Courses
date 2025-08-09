# class Employee:

 #   def showEmployeeData(self):
 #       print('Brian', '32' , '250000') # This is when you have data

# object = Employee()
# object.showEmployeeData()

# now you don't have specific data

#    def __init__(self, name, age, salary, gender):
#        self.name = name
#        self.age = age
#        self.salary = salary
#        self.gender = gender
#        self.email = self.generateEmail()

#    def generateEmail(self):
#        return f'{self.name}@ogada.com'
    
#    def showInfo(self):
#        print(self.name, self.age, self.salary, self.gender, self.email)

#obj = Employee('Brian', 32, '250000k', 'M')

#obj.showInfo()

# Need user input

class Employee:
    def __init__(self, name, age, salary, gender): 
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        self.email = self.generate_email()

    def generate_email(self):
        return f"{self.name.lower().replace(' ', '.')}" + "@ogada.com"
    
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: ${self.salary}, Gender: {self.gender}, Email: {self.email}")

# List to store multiple employees
employees = []

# Ask how many employees to add
num_of_employees = int(input("How many employees do you want to add? "))

# Collect employee details
for _ in range(num_of_employees):
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    salary = float(input("Enter Salary: "))
    gender = input("Enter Gender (M/F): ")

    # Create Employee object and add to list
    emp = Employee(name, age, salary, gender)
    employees.append(emp)

# Display all employees
print("\nEmployee List:")
for emp in employees:
    emp.show_info()
