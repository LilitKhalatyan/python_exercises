'''17. Write a Python program to match key 
values in two dictionaries. 
For example dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}. 
Expected output: key1: 1 is present in both x and y. 
Commit program to git and past the url in answer'''

x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

for i in x.items():
	for j in y.items():
		if i == j:
			print(i, "is present in both x and y")