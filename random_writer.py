import os.path
import random
import sys

def main():
	script, filename, order, output_length = sys.argv
	order = int(order)
	output_length = int(output_length)
	# distinguishes between numbers as strings and numbers
	# as integers

	if order <= 10: 
		print "Perfect! Let's proceed."
	else:
		print "Please choose a number between 1 and 10."

	# open the file in read mode
	# note: f is a file object

	f = open(filename, 'r')

	#initialize an empty dictionary
	my_map = {}

	sequence = f.read(order)

	next_character = f.read(1)
	# using index value to indicate next character

	while next_character:

		if sequence in my_map:
			# if my_map recognizes this sequence of characters,
			# it will give us back an array of all off the characters
			# that have followed the sequence (f.read(order))
			my_map[sequence].append(next_character)
		else:
			my_map[sequence] = [next_character]

		f.seek(-order, 1)

		sequence = f.read(order)
		next_character = f.read(1)

	f.close()

	# above yields a map containing all unique k-character
	# sequences in the input text file

	# next, need to find the most frequently occuring key
	# in my_map

	max_occurences = 0 
	mfk = "" # mfk == most frequent key in .txt file
	key_list = my_map.keys() # list of all of the keys
	for key in key_list:
		num_occurences = len(my_map[key])
		if num_occurences > max_occurences:
			max_occurences = num_occurences
			mfk = key

	print "The most frequent %d-character is \"%s\"." % (order, mfk)
	print "The sequence is followed by the following characters:", my_map[mfk]
	print "Get ready to giggle. The output is text: "

	current_key = mfk
	output = current_key
	for i in xrange(len(current_key), output_length):
		next_character = random.choice(my_map[current_key])
		output += next_character
		current_key = current_key[1:] + next_character

	print output

	print "Mazel tov! You have reformulated", filename

if __name__ == '__main__'
	main()