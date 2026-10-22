class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health

    def show_info(self):
        print(f"🐾 Pet Name: {self.name}")
        print(f"❤️ Health Level: {self.__health}%")
        print(f"📊 Health Status: {self.get_health_status()}")

    def get_health_status(self):
        if self.__health >= 80:
            return "🟢 Excellent"
        elif self.__health >= 60:
            return "🟡 Good"
        elif self.__health >= 40:
            return "🟠 Fair"
        else:
            return "🔴 Needs Attention"

    def care_action(self):
        print(f"🩺 {self.name} needs general care.")

    def set_health(self, new_health):
        if (
            isinstance(new_health, (int, float))
            and not isinstance(new_health, bool)
            and 0 <= new_health <= 100
        ):
            self.__health = new_health
            print(
                f"✅ {self.name}'s health updated "
                f"to {self.__health}%."
            )
        else:
            print("❌ Error: Health must be between 0 and 100.")


class Dog(Pet):
    def care_action(self):
        print(f"🦴 {self.name} needs a walk and playtime. 🎾")


class Cat(Pet):
    def care_action(self):
        print(
            f"🧶 {self.name} needs grooming, food, "
            "and quiet rest. 💤"
        )


class Rabbit(Pet):
    def care_action(self):
        print(
            f"🥕 {self.name} needs fresh hay "
            "and a clean cage. 🏡"
        )


dog = Dog("Buddy", 85)
cat = Cat("Misty", 75)
rabbit = Rabbit("Snowy", 65)

pets = [dog, cat, rabbit]

print("🐾 ===== MY PET CARE DASHBOARD ===== 🐾\n")

for pet in pets:
    pet.show_info()
    pet.care_action()
    print("─" * 35)

print("\n💖 ===== UPDATING PET HEALTH ===== 💖\n")

dog.set_health(95)
cat.set_health(80)
rabbit.set_health(70)

print("\n⚠️ ===== TESTING HEALTH VALIDATION ===== ⚠️\n")
dog.set_health(120)

print("\n🐾 ===== FINAL PET CARE SUMMARY ===== 🐾\n")

for pet in pets:
    pet.show_info()
    print("─" * 35)

print("❤️ Keep your pets happy and healthy! 🐶🐱🐰")
