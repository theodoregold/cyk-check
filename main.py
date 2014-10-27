#!/usr/bin/python

import os

word = ""
word_length = 0
max_steps = word_length * 2 - 1

# production rules
start_symbol = "P" # <-- CHANGE THIS HERE
productions = { # <-- ENTER YOUR OWN PRODUCTIONS

	# works perfect with this simple grammer
	# "S": ("SA", "AB"),
	# "A": ("AB", "a"),
	# "B": ("BB", "b"),
	# remember to change start_symbol to S

	"P": ("HV", "HZ", "EI", "HH", "S1", "FD", "BC", "AC", "AO", "FN", "EQ", "EG"), 

	"A": ("EC", "ER", "EL"), 
	"B": ("HH", "S1", "BC", "AC", "AO", "EQ", "FN", "EG", "HV", "HZ", "EI", "FD"), 
	"C": ("BC", "AC", "EQ", "AO"), 
	"D": ("FN", "EG"),
	"E": ("a"), 
	"F": ("ET", "HW", "EC", "EL", "ER"), 
	"G": ("FK", "c"),
	"H": ("b"),
	"I": ("EJ"),
	"J": ("AM", "HH"),
	"K": ("c"), 
	"L": ("EA", "a"), 
	"M": ("HH"),
	"N": ("EG"),
	"O": ("EQ"), 

	"R": ("EB"), 	
	"S": ("HV", "HZ", "EI", "HH", "S1", "FD", "BC", "AC", "AO", "FN", "EQ", "EG"), 
	"T": ("EU"),
	"U": ("EC"), 
	"V": ("CA", "BC", "AC", "AO", "EQ"), 
	"Z": ("HC"), 

	"1": ("HH"), 
	"W": ("HH"),  
	"Q": ("BX"), 
	"X": ("HK"), 
}

# table to store calculations
table = []

# function to test weather a word is part of grammar
def check_grammar(): 
	global word
	global table
	global productions
	global word_length

	# initialize table for calculations (wheather it will be 4x4 or 5x5 or ..)
	for i in range(0, word_length):
		table.append([])
		for j in range(0, word_length):
			table[i].append([])

	# place first terminal symbol in diognal
	for i in range(0, word_length):
		for j in productions: # go through all productions
			for symbols in productions[j]: # go through all production results
				if symbols == word[i]: 
					table[i][i].append(j) 
					continue

	# the real magic
	for k in range(1, word_length): 
		for j in range(k, word_length): # first two loops jump through empty squares in table
			for l in range(j-k, j): # third loops is number of previus table squares to calculate from and squares themselves
				for list_item in find_production(table[j-k][l], table[l+1][j]): # select terminal symbols in squares and find current square production 
					if list_item not in table[j-k][j]: # place found non duplicate symbols in current square
						table[j-k][j] += list_item	

	print_table() # for debug

	if start_symbol in table[0][word_length - 1]: return 1 # should add the be
	else: return 0
	

def find_production(list1, list2): # function for finding productions
	global productions

	new_list = []

	if not list1 or not list2:
		return new_list

	for x in list1:
		for y in list2:
			for i in productions:
				for j in range(0, len(productions[i])):
					if (x+y) == productions[i][j] and i not in new_list:
						new_list.append(i)
	return new_list

def print_table():
	global table
	global word_length

	for i in range(0, word_length):
		for j in range(0, word_length):
			print(table[i][j]),
		print ('\n'),
	print ('\n'),


# UI
os.system('cls' if os.name == 'nt' else 'clear')

word = raw_input("Enter a word to be tested: ")
word_length = len(word)
print "Testing! \n"

if (check_grammar()): # initialize check
	print "Your word \"" + word + "\" is part of grammer!"

else:
	print "Sorry, your word \"" + word + "\" is NOT part of grammer!"


# TO-DO:
# check for bad input
# add JSON support
