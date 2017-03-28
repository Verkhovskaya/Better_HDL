import math

def incrementor(inBit, inNumber, outNumber, max):
	bit_size = int(math.ceil(math.log(max,2)))
	print "DEFINE PlusOne inBit, b, outNumber, max \n a[8] \n a[0] <= inBit"
	print
	print "Build:"

	for index in range(bit_size):
		bit = str(index)
		#print "\t" + "a[" + bit + "] XOR b[" + bit + "] => out[" + str(index) + "]"
		#print "\t" + "a[" + bit + "] & b[" + bit + "] => a[" + str(index+1) + "]"

	print
	print "out => outNumber"

incrementor("inBit", "inNumber", "outNumber", 4)