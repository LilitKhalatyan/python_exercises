# my_tuple = ((1, 2, 3), (4, 5, 6), 2)

# print(my_tuple)
# print(my_tuple[0])
# print(my_tuple[0][2])


# my_lsit = [(1, 2, 3), (4, 5, 6), 2]

# print(my_lsit)
# print(my_lsit[0])
# print(my_lsit[0][0])

market_list = ["item1", "item2", "item 3", "item4"]
user_item_numbers = int(input("Input number of items you want to order"))
user_list = []
user_list_available = []
user_list_na = []
i = 0
for i in range(user_item_numbers):
	user_input = input("What do you want to buy? ")
	if user_input in market_list:
		user_list_available.append(user_input)
print("You can buy these items: ", user_list_available)

		# 	if user_input not in market_list:
		# user_list_na.append(user_input)
		# print("These items are not available in market", user_list_na)

	# user_input = input("What do you want to buy? ")
	# user_list.append(user_input)
	# print("You want to by these items: ", user_list)


