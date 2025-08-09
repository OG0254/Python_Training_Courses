class Employee:

    ogada = 'learn2code' # class variable (cls.)

    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        self.email = self.generateEmail(Employee)

    def generateEmail(self, cls):
        return f'{self.name}@{cls.ogada}.com'
    
    def showInfo(self):
        print(self.name, self.age, self.salary, self.gender, self.email)

    @classmethod # acts on a class its a decorator
    def changeCompanyName(cls, newName):
        cls.ogada = newName

# Employee.changeCompanyName("learnTOcode")

    @staticmethod # its like a help for displaying what is entails to the user
    def info():
        print('This is a class for creating employee objects and it requires parameters which are name, age, salary, gender')

obj = Employee('Brian', 32, '250000k', 'M')

Employee.info() #helps the static method

obj.showInfo()