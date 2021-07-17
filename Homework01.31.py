#Task 1
def max_of_three(num1, num2, num3):
	if num1 > num2 and num1 > num3:
		return "Maximum of these numbers is: ", num1
	elif num2 > num1 and num2 > num3:
	    return "Maximum of these numbers is: ", num2
	else:
		return "Maximum of these numbers is: ", num3

print(max_of_three(1, 9, 8))

#Task 2
def fizz_buzz():
	num = int(input("Pelase enter a number: "))
	if (num % 3 == 0) and (num % 5 == 0):
		return "FizzBuzz"
	if num % 3 == 0 and num % 5 != 0:
		return "Fizz"
	if num % 5 == 0 and num % 3 != 0:
		return "Buzz"
	else:
		return num

print(fizz_buzz())

#Task 3
def showNumbers():
	limit = int(input("Pelase enter a number: "))
	for i in range(limit):
		if i % 2 == 0:
			print(str(i) + " EVEN")
		else: 
			print(str(i) + " ODD")

print(showNumbers())

#Task 4
def n_nn_nnn(n):
	nn = str(n)+str(n)
	nnn = str(n)+str(n)+str(n)
	n = n + int(nn) + int(nnn)
	return(n)

print(n_nn_nnn(5))

#Task 5
def x(n):
	n = n**2 + 1
	return(n)

print(x(4))