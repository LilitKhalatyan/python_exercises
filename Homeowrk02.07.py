#Task 1 -- changing character in the string

t1_string = "rewrite"
t1_lenght = len(t1_string)
t1_first_char = t1_string[0]

print(t1_first_char + t1_string[1:t1_lenght].replace(t1_first_char, "$"))

# Task 2 -- adding ing or ly

t2_string = "strongly"
t2_lenght = len(t2_string)
if t2_lenght < 3:
	print(t2_string)
elif t2_string[-3:] == "ing" :
	print(t2_string + "ly")
else:
	print(t2_string + "ing")

#Task 3 -- <not good> - <poor>

t3_string = "The lyrics is not that poor but looks like poor"
find_not = t3_string.find("not")
find_poor = t3_string.find("poor")
print(find_not)
print(find_poor)

if find_not > 0 and find_poor > 0  and find_poor > find_not:
	print(t3_string.replace(t3_string[find_not:find_poor+4], "good"))
else:
	print(t3_string)