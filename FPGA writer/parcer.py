

input_file_name = "HelloWorldNand.txt"
program = [line.strip(' \t\n\r') for line in open(input_file_name)]
key_words = ["BUILD", "DEFINE", "END"]


def remove_comments(program):
	multiline_comment = False
	current_line_index = 0
	while current_line_index < len(program):
		line = program[current_line_index]
		if line.find("#") != -1:
			if line.find("##") == -1:
				program[current_line_index] = line[0:line.find("#")-1]
			else:
				if multiline_comment:
					program[current_line_index] = line[line.find("##")+2:len(line)]
				else:
					program[current_line_index] = line[0:line.find("##")]
				multiline_comment = not multiline_comment
		else:
			if multiline_comment:
				program[current_line_index] = ""
			current_line_index += 1


def reformat(program):
	new_program = []

	for line in program:
		line = line.replace(","," ").replace('\t', " ").strip()
		new_line = []
		for command in line.split(" "):
			if command in key_words:
				if new_line != []:
					new_program.append(new_line)
				new_program.append([command])
			else:
				if command != '':
					new_line.append(command)
		if (new_line != ['']) & (new_line != []):
			new_program.append(new_line)
	return new_program


remove_comments(program)
program = reformat(program)


"""
print "Cleaned program"
for line in program:
	print line
print
print

"""

class Block:
	def __init__(self, name):
		self.name = name
		self.vars = []
		self.commands = []
		self.nodes = []

	def __str__(self):
		info = self.name + '\n' + str(self.vars) + '\n'
		info += str(self.commands)
		return info

outer_block = Block("MAIN")
current_block = outer_block
current_state = "BUILD"
blocks = [outer_block]

for line in program:
	if line[0] == "DEFINE":
		current_state = "DEFINE"
		continue
		print "HIHIHI"

	if line[0] == "BUILD":
		current_state = "BUILD"
		continue

	if current_state == "BUILD":
		if line[0] == "END":
			current_block = outer_block
		else:
			current_block.commands.append(line)
		continue

	if current_state == "DEFINE":
		if line[0].istitle:
			current_block = Block(line[0])
			blocks.append(current_block)
			for index in range(1,len(line)):
				current_block.vars.append(line[index])
		else:
			for var in line:
				current_block.vars.append(var)
		continue

	print "ERROR IN PARSER"
	print(line)

for block in blocks:
	print block