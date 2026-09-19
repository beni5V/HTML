import datetime

print("🌈 WELCOME TO MY DAILY MOOD ADVISOR 🌈")
print("------------------------------------------")

name = input("Enter your name: ")

mood = input(
    "How are you feeling today? "
    "(happy/sad/tired/stressed/excited): "
).lower()

energy = int(input("Enter your energy level from 1 to 10: "))

if energy < 3:
    print("\n⚠️ Alert: Your energy is very low today.")
    print("Take some rest and give yourself time to recharge.")

if energy >= 5:
    print("\n💪 You have enough energy to be productive today!")
else:
    print("\n🌿 Take it slow today and do something relaxing.")

if mood == "happy":
    advice = "Keep smiling and spreading your positive energy! 😊"
    emoji = "😄"

elif mood == "sad":
    advice = "Talk to someone you trust or do something that makes you happy. 💙"
    emoji = "😢"

elif mood == "tired":
    advice = "Drink some water, take a break, and give your mind some rest. 😴"
    emoji = "😴"

elif mood == "stressed":
    advice = "Take some deep breaths and focus on one small task at a time. 🌿"
    emoji = "😰"

elif mood == "excited":
    advice = "Use your excitement to start something fun and creative! 🎨"
    emoji = "🤩"

else:
    advice = "Every mood is okay. Take care of yourself today. 💚"
    emoji = "🙂"

today = datetime.datetime.now()

print("\n==========================================")
print("          🌟 MOOD ADVISOR REPORT 🌟")
print("==========================================")

print("👤 Name:", name)
print("💭 Mood:", mood, emoji)
print("⚡ Energy Level:", energy, "/ 10")
print("📅 Date and Time:", today.strftime("%d-%m-%Y %I:%M %p"))

print("------------------------------------------")
print("💡 Your Advice:")
print(advice)

print("------------------------------------------")

if energy >= 8:
    print("🔥 Amazing energy! Make the most of your day!")
elif energy >= 5:
    print("🌟 Good energy! You can accomplish something great today!")
else:
    print("💙 Remember: Rest is also productive.")

print("==========================================")
print("       Thank you for using Mood Advisor! 😊")
print("==========================================")
