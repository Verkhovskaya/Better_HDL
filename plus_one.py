import math

def incrementor(inBit, inNumber, outNumber, bit_size):
	print "a[0] <= " + inBit
	print "b <= " + inNumber

	print "inNumber <= " + str(bit_size)
	print
	print "Build:"

	for index in range(bit_size):
		bit = str(index)
		print "\t" + "a[" + bit + "] XOR b[" + bit + "] => out[" + str(index) + "]"
		print "\t" + "a[" + bit + "] & b[" + bit + "] => a[" + str(index+1) + "]"

	print
	print "out => outNumber"

incrementor("inBit", "inNumber", "outNumber", 4)