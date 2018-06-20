'''
Define a class Person and its two child classes: Male and Female.
All classes have a method "getGender" which can print "Male" for
Male class and "Female" for Female class.
'''

class Person(object):
	def getGender(self):
		return "Unknown"

class Male(Person):
	def getGender(self):
		return "Male"

class Female(Person):
	def getGender(self):
		return "Female"

male = Male()
female = Female()

print(male.getGender())
print(female.getGender())
