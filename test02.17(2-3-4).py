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

string1 = Pow(2, 5)
print(string1.pow())


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

		# list1 = (self.word).reverse()
		# return list1

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