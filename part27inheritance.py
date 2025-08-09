class A:

    def __init__(self):
        print('a') # it will print 'a' if its using 'a' initializor
        
    def method1(self):
        print('method1')
    def method2(self):
        print('method2')

class B: # No inheritance here
# class B(A): # this is where inheritance happens where it will inherit all methods from A

    def __init__(self):
        print('b') # it will print 'b' if its using 'b' initializor
    def method3(self):
        print('method3')
    def method4(self):
        print('method4')

class C(A, B): # this is where inheritance happens where it will inherit all methods from A , and B
    def __init__(self):
        super().__init__() # used when you want run the __init__ from the class you inherited from also known as method reolution order by taking the 1st class for instance here it's 'a'
        print('c') # it will print 'c' if its using 'c' initializor
    def method5(self):
        print('method5')

a = A()
b = B()
c = C()

a.method1() # 'a' can use method 1 and 2 only while now 'b' can use method 1, 2, 3 and 4
a.method2()
c.method() # 'c' can use method 1, 2, 3, 4 and 5