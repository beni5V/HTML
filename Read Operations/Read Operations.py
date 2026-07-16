file_read = open("Condingal.txt","r")
print("File in read mode-")
print(file_read.read())
file_read.close()

file_write = open("Condingal.txt","w")

file_write.write("File in write mode ..........")
file_write.write("Hi! I am Penguin. I am 1 yr. old")
file_write.close()

file_append = open("Condingal.txt", "a")
file_append.write("\n File in append")
file_append.write("Hi! I am Penguin. I am 1 yr. old")
file_append.close()