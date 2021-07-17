#Task 1
persons_name = input("Please enter your name")
persons_age = input("Please enter your age")
persons_age = int(persons_age)
yyyy_dob = 2020 - persons_age
yyyy_100yo_before = yyyy_dob + 100
yyyy_100yo_after = yyyy_dob + 99

print("Dear ", persons_name)
print("If you have already celcbrated you birthday this year, then You will turn 100 in ", yyyy_100yo_before)
print("If not, then You will turn 100 in ", yyyy_100yo_after)

#Task 2
iinput_1 = input("Please enter anything you want (1st entry)")
iinput_2 = input("Please enter anything you want (2nd entry)")
iinput_3 = input("Please enter anything you want (3rd entry)")

print("The fact that all entries are equal is ", bool(iinput_1 == iinput_2 and iinput_2 == iinput_3 and iinput_1 == iinput_3))
print("The fact that any of two entries are equal is ",bool(iinput_1 == iinput_2 or iinput_2 == iinput_3 or iinput_1 == iinput_3))

#Task 3
t3_number_1 = int(input("Please enter any numer"))
t3_number_2 = int(input("Please enter any number"))
the_sum = t3_number_1 + t3_number_2

print("The fact that the sum of your entered numbers is greater than 5 is ", bool(the_sum > 5))
print("The fact that the sum of your entered numbers is less than 5 is ", bool(the_sum < 5))
print("The fact that the sum of your entered numbers is equal than 5 is ", bool(the_sum == 5))

#Task 4
t4_mark = int(input("Please enter your grade"))

print("The fact that you completed the subject is: ", bool(t4_mark >= 35))