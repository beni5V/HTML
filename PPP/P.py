file_read = open("Condingal.txt","r")
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open("Condingal.txt","w")
file_write.write("Hi!I am Sarah. I am 11 years old")
file_write.close()

file_append = open("Condingal.txt","a")
file_append.write("\n File in append mode......")
file_append.write("Hi! I am Sarah. I am 11 years old")
file_append.close()