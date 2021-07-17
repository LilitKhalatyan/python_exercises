######## 02.09.2020 Homework
#Task 1 -- Write a python program to count the number of strings where
#the string lenght is 2 or more and the first and the last chcaracters
#are same from a given list of strings

list1 = ["abc", "abba", "xyz", "12221", "121", "aa"]
num1 = len(list1)
sum1 = 0
for i in range(num1):
    if len(list1[i]) > 2 and list1[i][0] == list1[i][-1]:
        sum1 += 1
print(sum1)

#Task 2 -- Write a python program to check if the list is empty or not.

list2 = []
if not list2:
    print("Your list is empty")
else:
    print("Your list is not empty")

#Task 3 -- Write a python program to find the losngest word in the list.

list3 = ["This", "list", "longest", "word"]
num3 = len(list3)
lenght3 = 0
id3 = 0
if not list3:
    print("Your list is empty")
for i in range(num3):
    if len(list3[i]) > lenght3:
        lenght3 = len(list3[i])
        id3 = i
print("The longest word in list is", list3[id3])

#Task 4 -- Write a python function that takes two lists and
#returnes True if they have at least one common member

list_a = ["abs", "aa", "bb", "cc"]
list_b = ["abs", "dd", "ee", "ff"]

def common_element(list_a, list_b):
    for i in list_a:
        for j in list_b:
            if i == j:
                return "True"
print(common_element(list_a, list_b))