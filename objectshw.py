class Pet: 
    print ("Hi, I am a pet profile class")

pet_object = Pet()

class Petprofile:
    category = "pet"
    def __init__(self, name, type,age, food):
        self.name = name
        self.type = type
        self.age = age
        self.food = food

pet1 = Petprofile("Max", "Dog", 5, "Dog food")
pet2 = Petprofile("Whiskers", "Cat", 3, "Fish")

print( "Max is a {}".format(pet1.category))
print( "Whiskers is a {}".format(pet2.category))
print( "{} is a {} and is {} years old.".format(pet1.name, pet1.type, pet1.age))
print("{} likes eating {}.".format(pet1.name, pet1.food))
print( "{} is a {} and is {} years old.".format(pet2.name, pet2.type, pet2.age))
print("{} likes eating {}.".format(pet2.name, pet2.food))
