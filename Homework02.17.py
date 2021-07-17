'''1. Write a Python class which has two methods 
get_String and print_String. get_String accept a 
string from the user and print_String print the 
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


'''2. Create a vehicle class. Create two new vehicles 
called car1 and car2. Set car1 to be a red convertible 
worth $60,000.00 with a name of Fer, and 
car2 to be a blue van named Jump worth $10,000.00.'''
class Vehicle:
	def __init__(self, name, colour, price):
		self.name = name
		self.colour = colour		
		self.price = price

car1 = Vehicle("Fer", "red", "$60,000.00")
car2 = Vehicle("Jump", "blue", "$10,000.00")

print(car1.name, car1.colour, car1.price)
print(car2.name, car2.colour, car2.price)
