# Import necessary Modules
from abc import ABC, abstractmethod

# Create base class
class Absclass(ABC):

    # Function to print a value
    def print(self, x):
        print("Passed value: ", x)

    # Abstract Method
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")

# Object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)


from abc import ABC, abstractmethod

# Create a base class
class Animal(ABC):

    # Abstract method
    # Should be implemented by all sub-classes
    @abstractmethod
    def move(self):
        pass


# Sub classes
class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
   def move(self):
    print("I can roar")

# Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()