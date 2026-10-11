class Robot:
    def __init__(self, name, age, abilities, personality):
        self.name = name
        self.age = age
        self.abilities = abilities
        self.personality = personality

    def introduce(self):
        print("Hello, everyone!👋")
        print("My name is", self.name)
        print("I am", self.age, "years old.")
        print("My abilities are:", self.abilities)
        print("My personality is:", self.personality)

    def greet(self):
        print("Beep boop! Nice to meet you! Human🤖")
        print("I am happy to be your robot friend!")

my_robot = Robot(
    "Aliimartisna",
    "6 months",
    "Helping people, solving problems, and dancing",
    "Friendly, smart, and helpful"
)

my_robot.introduce()
my_robot.greet()
