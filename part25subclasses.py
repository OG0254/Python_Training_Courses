class Employee:

    def __init__(self, name, age, salary, gender, desig, dept):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        self.email = self.generateEmail()
        self.Job =  self.Job(desig, dept)

    def generateEmail(self):
        return f'{self.name}@ogada.com'
    
    def showInfo(self):
        print(self.name, self.age, self.salary, self.gender, self.email)

# here is a subclass
    class Job:

        def __init__(self, designation, department):
            self.designation = designation
            self.department = department
        
        def showInfo(self):
            print(self.designation, self.department)

obj = Employee('Brian', 32, '250000k', 'M', 'Manager', 'ICT') # will shoe desig and dpt

obj.showInfo() # will show till the email
obj.Job.showInfo() # will shoe desig and dpt

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