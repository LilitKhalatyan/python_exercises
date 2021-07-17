#Task 1
t1_user_input = int(input("Input any number: "))
for i in range (1, 10):
	print(t1_user_input, " * ", i, " = ", t1_user_input * i)

#Task 2
for i in range (0, 6):
	print("*" * i)
for i in range (4, 0, -1):
	print("*" * i)

#Task 3
t3_user_input = int(input("Input any number: "))
for i in range (0, t3_user_input):
	if (i % 2) == True:
		print(i)