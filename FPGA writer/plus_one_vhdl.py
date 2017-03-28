import math

def incrementor(inBit, inNumber, outNumber, bit_size):
	print "ENTITY Incrementor IS \n \tPORT (inBit, inNumber: IN SIGNAL_TYPE;"
	print "\t \t" + "outNumber :OUT SIGNAL_TYPE); \nEND Incrementor"
	print

	print "ARCHITECTURE Incrementor_main is"
	print "\tSIGNAL a IS array[8]"
	print "\tCOMPONENT ANDGate PORT(bit1, bit2: IN bit; and_out:OUT BIT);"
	print "\tEND COMPONENT;"
	print "\tCOMPONENT XORGate PORT(bit1, bit2: IN bit; xor_out:OUT BIT);"
	print "\tEND COMPONENT;"
	print "\tBEGIN"

	for index in range(bit_size):
		bit = str(index)
		print "\t\tXORGate (a[" + bit + "],b[" + bit + "],out[" + bit + "]"
		print "\t\tANDGate (a[" + bit + "],b[" + bit + "],a[" + str(index+1) + "]"

	print
	print "out => outNumber"

incrementor("inBit", "inNumber", "outNumber", 4)