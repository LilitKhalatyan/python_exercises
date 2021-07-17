#Task 1
my_string = input("Please enter your text")
x = (" " in my_string)

print("You have entered a sentence: " , x)
print("You have entered a word: " , not x)

#Task 2
my_number = input("Please enter any number")
my_number = int(my_number)
result = my_number % (5 * 11)

print("It is ", not bool(result), " that the number you have entered is divisible by 5 and 11" )	

#Task 3
year = input("Please enter a year you want to check")
leap = int(year) % 4 

print("It is ", not bool(leap), " that the year you have entered is leap")