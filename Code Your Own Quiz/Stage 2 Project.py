
# -*- coding: utf-8 -*-



# A list of blanks to be passed in to the game function.
blanks = ["___1___", "___2___", "___3___", "___4___", "___5___"]

# Questions will be asked to fill in
game_data = {
	'Easy': {
		'quiz': '''A ___1___ is one of the basic things a program works with, like a letter or a number.These ___2___s belong to different types: 2 is an integer, and 'Hello, World!' is a ___3___A ___4___ is a name that refers to a ___5___.''',
		'answers' : ["value", "value", "string", "variable", "value"]
	},
	'Medium': {
		'quiz': '''In the context of programming, a ___1___ is a named sequence of statements that performs a computation.The expression in parentheses is called the ___2___ of the ___3___. It is common to say that a ___4___ “takes”an ___5___ and “returns” a result.''',
		'answers' : ["function", "argument", "function", "function", "argument"]
	},
	'Hard': {
		'quiz': '''A ___1___ expression is an expression that is either true or false. There are three ___2___ operators: and, or, and not.The ___3___ operator works on integers and yields the remainder when the first operand is divided by the second.The == operatoris one of the ___4___ operators. A ___5___ statement gives us to check conditions and change the behavior of the program accordingly.''',
		 'answers' : ["boolean", "logical", "modulus", "relational", "conditional"]
	},
}




def word_in_blanks(word, blanks):
	'''Checks if there is a word in blank list that is a substring of the variable word,
	then return that word in blank list'''
	for blank in blanks:
		if blank in word:
			return blank
	return None

def replace_blanks(word, replaced, blanks, guess, index):
	'''To replace the blanks showed in questions by guess typed by useers'''
	if word_in_blanks(word, blanks) == None:
		if word not in replaced:
			replaced.append(word)
	else:
		replacement = word_in_blanks(word, blanks)
		word = word.replace(replacement, guess)
		if replacement == blanks[index]:
			if replacement not in replaced:
				replaced.append(word)
			else:
				position = replaced.index(replacement)
				replaced[position] = word
		else:
			replaced.append(replacement)

	return replaced

def fill_blanks(questions, blanks, replaced, guess, index):
	'''To replace the blanks showed in questions by guess typed by useers '''
	replaced = []
	questions_split = questions.split()

	for word in questions_split:
		replace_blanks(word, replaced, blanks, guess, index)

	replaced = " ".join(replaced)
	return replaced


def check_answers(choice, questions, answers):
	'''To check the user's guess.'''

	replaced = []
	guess = ''
	index = 0
	for blank in blanks:
		guess = raw_input("Would you like to answer" + blanks[index] + "?")
		while guess != answers[index]:
			print ("Oops! It looks like your answer was wrong. Please try again.")
			guess = raw_input("Type in" + blanks[index] + "here again: ")

		print ("Great! There we go!")

		replaced = fill_blanks(questions, blanks, replaced, guess, index)
		print replaced
		index += 1

	return replaced, index


MESSAGE = """
This game was degisned to help you remember
important vocabulary during your Python study.
Please choose a level to start when you get ready
"""

def game():
	'''The final function to start the fill in blanks game'''

	print (MESSAGE)
	choice = raw_input("$Easy$  $$Medium$$  $$$Hard$$$  ")
	while choice not in ['Easy', 'Medium', 'Hard']:
		print "Would you like to choose a level as indicated? "
		choice = raw_input("$Easy$  $$Medium$$  $$$Hard$$$  ")
	questions = game_data[choice]['quiz']
	answers = game_data[choice]['answers']
	print ('You chose the' + choice + 'one, here we go!')
	print questions
	replaced = check_answers(choice, questions, answers)
	print "Brilliant! You have done a great job"

game()
