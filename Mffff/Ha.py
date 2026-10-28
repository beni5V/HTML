#Code1
n = int(input("How many charecters to preview?"))
file = open("class-notes.txt","r")
print(file.read(n))
file.close()
print()

#All lines as a list
file = open("class-notes.txt","r")
lines = file.readlines()
file.close()

print("Total lines:",len(lines))
for i in range(len(lines)):
    print(i+1, "->", lines[i].strip())
print()

#Filter Lines
word = input("Skip lines starting with:")
file = open("class-notes.txt","r")
for line in file:
    if line.startswith(word):
        print("skip ->", line.strip())
    else:
        print("keep ->", line.strip())
file.close()
print()

#Copy odd lines to new file
file = open("class-notes.txt","r")
lines = file.readlines()
file.close()
out = open("odd-lines.txt","w")
for i in range(0, len(lines),2):
    out.write(lines[i])
out.close()
print("Odd lines saved tp odd-lines.txt")