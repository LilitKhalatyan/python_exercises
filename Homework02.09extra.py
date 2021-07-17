''' 02.09.2020 Extra Homework '''
''' Task 1 -- Write a python function to check 
wether a number is in a given range.'''
num = int(input("Enter a number: "))
def in_range():
	if num in range(0,20):
		print("Your numbr is in range: 0, 20")
	else:
		print("Your numbr is not in range: 0, 20")
print(in_range())

'''Task 2 -- Write a python function that acceptes a string and 
calculates the number of upper case letters and lower case letters.'''
user_string = input("Enter a string here: ")
def low_upp():
	upper = 0
	lower = 0
	for i in user_string:
		if i.isupper():
			upper = upper + 1
		elif i.islower():
			lower = lower + 1
	print("Number of upper case elements is", upper)
	print("Number of lower case elements is", lower)
print(low_upp())

'''Task 3 -- Write a python function that takes a list and returens 
a new list with unique numbers'''

user_list_unique = []
j = 0
for i in user_list:
	if i[j] == i[j+1]:
		j = j+1
	break
	else: 
		user_list.append(i[j])

print(user_list_unique)

'''Task 4 -- Write a Python fucntion that takes a number
as a parametr and checkes the number is prime or not.'''
num = int(input("Input numer you want to check for prime: "))
def prime(num):
    x = 0
    for i in range(2, num) :
        if num % i == 0:
            x = x + 1
    if x == 0:
        print ("This number is Prime ! ")
    else:
        print("This number is nor prime ")
if num >= 1:
    print(prime(num))
else:
    print("Please enter a number that is great than 1: ")