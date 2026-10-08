class student1:
	grade = 10
	name = "Penguin"
	
	def introduction(self):
		print("Hi I am a student")

	def details(self):
		print("My name is", self.name)
		print("I study in Grade", self.grade)

ob = student1()
ob.introduction()
ob.details()