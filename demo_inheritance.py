class Person:
	def __init__(self, name):
		self.name = name
	def say_hello(self):
		print('Hello, ' + self.name)

class Student(Person):
	def __init__(self, name, school):
		super().__init__(name)
		self.school = school
	def sing_school_song(self):
		print('Ode to ' + self.school)

student = Student('Christopher', 'UVM')
student.say_hello()
student.sing_school_song()
# What are you?
print(f'Is this a student? {isinstance(student, Student)}')
print(f'Is this a Person? {isinstance(student, Person)}')
print(f'Is Student a Person? {issubclass(Student, Person)}')

# Overriding ___str___

class Person:
	def __init__(self, name):
		self.name = name
	def say_hello(self):
        # Let the parent do some work
        super().say_hello()     # Override the parent
        # Add on my custom code
		#print('Hello, ' + self.name)
        print('I am kind of tire')
    def ___str___(self):    
        return f'{self.name} attends {self.school}'

presenter = Presernter('Christopher')
print(presenter)
