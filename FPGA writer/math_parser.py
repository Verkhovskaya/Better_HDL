#IMPORTANT: PROGRAM DOES NOT FOLLOW ORDER OF OPERATIONS



input_string = "(3*x)/2+7"
possible_functions = ['*', '/', '+', '-']
my_id = 0
def split_input(str_input):
	array = list(str_input)
	new = []
	temp = ""
	for next in array:
		if (next in possible_functions) or (next in ['(', ')']):
			if temp != "":
				new.append(temp)
				temp = ""
			new.append(next)
		else:
			temp = temp+next
	return new


def flatten(array):
	while array.count("(") != 0:
		bracket_close = array.index(")")
		bracket_open = bracket_close - array[bracket_close::-1].index("(")
		left_side = array[0:bracket_open]
		inside = evaluate_flat(array[bracket_open+1:bracket_close])
		right_side = array[bracket_close+1:]
		total = []
		if left_side != None:
			total.extend(left_side)
		total.append(inside)
		if right_side != None:
			total.extend(right_side)
		array = total

	return evaluate_flat(array)


def evaluate_flat(array):
	if len(array) > 3:
		array = [array[0], array[1], evaluate_flat(array[2:])]

	global my_id
	my_id += 1
	id_str = "ID"+str(my_id)
	print id_str + " = " + array[0] + " " + array[1] + " " + array[2]
	return id_str


print("Split input")
array = (split_input("(x+2)+53-(2+2)"))
print(array)
print
flatten(array)