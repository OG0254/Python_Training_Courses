class Bird():

    def walk(self): # Every class method you construct in an object-oriented approach will always take "self" as an argument.
        print('hopping around......')

class Mammal():
    def walk(self):
        print('jogging around......')

class Movements:
    @classmethod # we introduce this since movement is a class method
    def move(cls, thing): # we can accept many forms into this class and thats what polymorphism is
        thing.walk()

bird = Bird()
dog = Mammal()

Movements.move(bird)
Movements.move(dog)