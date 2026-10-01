classmates = ["Zarmeen","Falisha","Yashfa","Qasim","Nafay","Zainab"]
print("Class list:", classmates)

print("Total students:", len(classmates))
print("First student:", classmates[0])
print("Last student:", classmates[-1])
print("First three students:", classmates[:3])

classmates.append("Salar")
print("\nAfter adding Salar:", classmates)  
classmates.remove("Yashfa")
print("After removing Yashfa:", classmates)
classmates.sort()
print("Sorted alphabetically:", classmates)
classmates.reverse()
print("Reversed order:", classmates)

teacher = {"name": "Ms.Javeeria", "subject": "Geography and History", "experience": 20}
print("\nTeacher details:", teacher)

print("Subject:", teacher["subject"])
print("Experience:", teacher["experience"], "Not found")
teacher["experience"] = 21
teacher["email"] = "javeeria8242@gmail.com"
teacher.pop("experience")
print("Updated teacher details:", teacher)

roll_numbers = [1, 2, 3, 4, 5]
names = ["Chae-won", "Nafay", "Falisha", "Yashfa", "Qasim"]
students_directory = dict(zip(roll_numbers, names))
print("\nStudents directory:", students_directory)
print("Roll number 3:", students_directory.get(3))
