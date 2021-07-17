'''1. Write a Python class to find the three elements 
that sum to zero from a set of n real numbers. - Go to the editor
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]'''
d = []
class TripleSumZero:
	def __init__(self, m):
		self.m = m
		lenght = len(m)
		for i in range(lenght):
			for j in range(1,lenght):
				for f in range(2, lenght):
					x = m[i] + m[j] + m[f]
					if x == 0:
						d.append([m[i], m[j], m[f]])
		print(d)

m = TripleSumZero([-25, -10, -7, -3, 2, 4, 8, 10])


'''2. Write a Python Class to implement pow(x, n)'''
class Pow:
	def __init__(self, x, n):
		self.x = x
		self.n = n

	def pow(self):
		x = int(self.x)
		n = int(self.n)
		x = x ** n
		return x

pow1 = Pow(2, 5)
print(pow1.pow())


'''3. Write a Python class to reverse a string word by word.'''
empty = " "
class Reverse:
	def __init__(self, word):
		self.word = word

	def reversed(self):
		list1 = self.word.split()
		list1_reversed = list1[-1::-1]
		return empty.join(list1_reversed)
		print(list1)

word1 = Reverse("hello .py")
print(word1.reversed())

'''4. Write a Python class which has two methods get_String and print_String.
get_String accept a string from the user and print_String print the 
string in upper case.'''
class UserGetPrint:
	def __init__(self, string):
		self.string = string

	def get_string(self):
		self.string = input("Enter Your string here: ")

	def print_string(self):
		print(self.string.upper())

string = UserGetPrint("string")
string.get_string()
string.print_string()

'''5. Write a Python class named Rectangle constructed by a length and width 
and a method which will compute the area of a rectangle'''
class Rectangle:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def eq(self):
		a = int(self.a)
		b = int(self.b)
		x = a * b
		return x

rectangle1 = Rectangle(2, 5)
print(rectangle1.eq())