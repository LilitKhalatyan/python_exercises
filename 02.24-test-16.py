'''16. Write a python program which will take a number from user 
and return user inputed lyrics line of 
"The Beatles - I wanna hold your hand"'''


file1 = open("TheBeatles.txt", "r")

number = int(input("Entere a number of the line, that you want to get from 'I wanna hold your hand' song: "))

print(file1.readlines(number))

file1.close()