'''Task 1 -- Write a python script to add a key to a dictionary.'''
my_dictionary = {0: 10, 1: 10, 2: 30}
my_dictionary.update({3: 40})
print(my_dictionary)
#Result is: {0: 10, 1: 10, 2: 30, 3: 40}

'''Task 2 -- Write a python script to concatenate dictionries to
create a new one.'''
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)


'''Task 3 -- Write a python script to check whether a given key already 
exist in dictionary or not.'''
sample_dictionary = {"Name": "Lilit", "Surename": "Khalatyan", "Nationality": "Armenian"}
kays = sample_dictionary.keys()
print(kays)
kay = input("Input a key you want to check: ")
if kay in kays:
    print("The given kay already exists in dictionary: ")
else:
    print("The given kay does not exists in dictionary: ")

 '''Task 4 -- Create a dictionary about user and all values should
 be inputed from user.'''
new_dictionary = {}
num = int(input("How many kays do you want to add?: "))
for i in range(num):
    kay = input("Input a kay you want to add: ")
    value = input("Input a value you want to add for the kay: ")
    new_dictionary.update({kay: value})
print(new_dictionary)

'''Task 5 -- Write a python program to get the maximum and 
the minimum value in the dictionary.'''
dict5 = {1: 11, 2: 22, 3: 33, 4: 40}
print("The maximum value is: ", max(dict5.values()))
print("The minimum value is: ",min(dict5.values()))

'''Task 6 -- Write a python program to get to create a dictionary from string.'''
string = "ISTC"
lenght = len(string)
print(string)
dic1 = {}
i = 0
for i in string:
 	dic1.update({i: 1})
print(dic1)