user_name_input = input("Tell me your name")
user_surname_input = input("Tell me your surename")
user_age_input = input("tell me your age")
user_gender_input = input("tell me your gender (M or F)")


user_age_input = int(user_age_input)
user_gender_input = bool(user_gender_input)


print(user_name_input)
print(type(user_name_input))

print(user_surname_input)
print(type(user_surname_input))

print(user_age_input)
print(type(user_age_input))

print(user_gender_input)
print(type(user_gender_input))