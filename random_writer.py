# designed to produce somewhat sensible output by generalizing
# from patterns found in the input text

# Markov model: statistical model that describes the future
# state of a system based on the current state and the 
# conditional probabilities of the posible transitions.

# simple improvement: gather information on character frequency
# use that as a weight for choosing the next letter

# order-9 Markov model: predicts that each character occurs with 
# a fixed probability, independent of previous characters

# Using an order-k model, you generate random output by
# choosing the next character based on the probabilities of
# what followed the previous k characters in the input text.
# seed: the string of characters preceding the current point

# Steps for Program
# 1. Prompt the user for the name of a file to read for the
# source text and reprompt as needed until you get a valid name. DONE.
# 2. Ask the user for what order of Markov model to use 
# (a number from 1 to 10). DONE.
# Goal: record the frequency information in such a way that input
# it will be easy to generate random text later without any
# complicated manipulations.
# For the initial seed, choose the sequence that appears most
# frequently in the source. 
# e.g. if you are doing a k=4 analysis, the 4-character 
# sequence that is most often repeated in thes ource is used to 
# start the random writing.

# output the initial seed, then choose the next character based 
# on the probabilities of what followed that seed in the source

# Output that character, update the seed, and the process repeats
# until you have 2,000 characters. 

# prompt user for file

'''
take each 2-character sequence of letters
parse the whole input file
for each 2-character sequence, find most frequent

order of markov process = k 
what is the length of sequence of characters that we use to determine prob of next character
iterate through whole file
for each k-character sequence in the file:
	1. check and see if key already exists in dictionary
	2. if so, see which character comes after k sequence and .append to list of characters for key
	3. else, create a new key for sequence of characters and .append to list of characters
have a dictionary of every k-character sequence in .txt file 
at each one of keys, have array of characters that follow the k-sequence

''' 


import.ospath

filename = raw_input('Enter a filename: ')

while not os.path.isfile(filename):
	print "Try again. Please input a filename."
	filename = raw_input('Enter a filename: ')
print "Okay, let's proceed with that file."

'''
if os.path.isfile(filename):
	print "Perfect! Let's proceed with that file."
else:
	print "Please enter a filename."
'''

# ask user for what order of Markov model
markov = raw_input('User, what order of Markov model would you like?')
markov = int(markov)
print markov

if markov <= 10:
	print "Perfect! Let's proceed."
else:
	print "Please choose a number between 1 and 10."






















