print("Basic Emoji Pattern \n")
emojis = ["😀", "🌸", "⭐", "🎱", "🦋", "🍀", "🦊"] 
for i in range(1, 8 ):
  for j in range(i):
    print(emojis[i-1], end="")
  print('\n')

print("Inverted Emoji Pattern \n")
for i in range(7, 0, -1):
  for j in range(i, 1, -1):
    print(emojis[i-1], end="")
  print('\n')