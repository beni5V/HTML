class Parrot:
    #class attribute
    species = "bird"
    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#instance of the Parrot class
killy = Parrot("Killy", 3)
army = Parrot("Army", 5)

#accessing the class attributes
print("Killy is a {}".format(killy.__class__.species))
print("Army is also a {}".format(army.__class__.species))

#acces the instance attributes
print("{} is {} years old".format(killy.name, killy.age))
print("{} is {} years old".format(army.name, army.age))