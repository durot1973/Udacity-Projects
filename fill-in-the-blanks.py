
# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!


import string


# first we define the functions necessary for the code to run.

def introduction():
	'''This function introduces the program and points in the next direction'''
	level_chosen = ''

	while level_chosen !='easy' or level_chosen != 'medium' or level_chosen !='hard':
		print 'Please select a game difficulty by typing it in!'
		print 'Possible choices include easy, medium and hard'
		levels = ['easy', 'medium', 'hard']
		level_chosen = raw_input()
		level_chosen = level_chosen.lower()
		if level_chosen in levels:
			return level_chosen
		else:
			print "That's not an option!"


def isSubstituted(paragraph):
	'''
	Checks if the words have been substituted into the paragraphs
	'''
	if '__' in paragraph:
			return False
	return True


def toSubstitute(replacement, space, paragraph):
	'''
	This function replaces space with word in the paragraph
	replacement is the the word the user has inputed that is correct
	space is what is to be substituted
	'''
	assert '__' in space
	if space in paragraph:
		sub_paragraph = string.replace(paragraph, space, replacement)
	return sub_paragraph


def identifySubstitute(paragraph):
	'''
	This is to be used to find the next word to be substituted
	e.g __1__.
	'''
	index = paragraph.index('___')
	substitute_length = 7
	return paragraph[index: index + substitute_length]


def game(paragraph, answers, level_chosen):
	'''This function accepts values from the either easy, medium or hard and runs with that giving the user feedback 
	for each guess made'''
	guesses, user_input, substitute_paragraph, words_to_be_substituted = 5, '', paragraph[:], answers.copy()
	print 'You have chosen ' + level_chosen + '!' + '\n  ' + '\nYou will get ' + str(guesses) + ' guesses per problem' + '\n '
	
	while not isSubstituted(paragraph):
		substitute_word = identifySubstitute(paragraph)
		print 'The current paragraph reads as such:' + '\n' + substitute_paragraph + '\n' 
		user_input = (raw_input('What should be substituted in for ' + substitute_word + '?')).lower()
		
		if user_input in words_to_be_substituted:
			print '\nCorrect!'
			substitute_paragraph, paragraph = toSubstitute(user_input, substitute_word, paragraph), toSubstitute(user_input, substitute_word, paragraph)
			words_to_be_substituted.discard(user_input)
		else:
			guesses -= 1
			if guesses < 1:
				break
			else:
				print "\nThat's not the correct answer: Let's try again; you have %g try left" %guesses

	if isSubstituted(paragraph):
		print substitute_paragraph + '\nYou won!'

# Then the games variables for the diffrent levels.


game_levels = {'easy': { 'phrase': '''A common first thing to do in a language is display
 	 'Hello ___1___!' In ___2___ this is particularly easy; all you have
 	 to do is type in: ___3___ "Hello ___1___!". Of course, that isn't a
 	very useful thing to do. However, it is an example of how to output 
 	to the user using the ___3___ command, and produces a program which 
 	does something, so it is useful in that capacity. It may seem a bit 
 	odd to do something in a Turing complete language that can be done 
 	even more easily with an ___4___ file in a browser, but it is a step
 	 in learning ___2___ and that is really it's purpose''',
 	  'answers': {'world', 'python', 'print', 'html'}},
 
 'medium': {'phrase': '''A ___1___ is created with the def keyword. You specify 
 	the inputs a ___1___ takes by adding ___2___ separated by commas between
 	 the parentheses. ___1___s by default return ___3___ if you don't specify
 	 the value to return. ___2___ can be standard data types such as string,
 	 number, dictionary, tuple, and ___4___ or can be more complicated such
 	 as objects and lambda functions.''', 
 	'answers': {'function', 'argument', 'none', 'list'}},
 
 'hard': {'phrase': '''When you create a ___1___, certain ___2___ are 
 	automatically generated for you if you don't make them manually. An 
 	object is an ___3___ of a class is. Binary operators can also be 
 	created for the class e.g ___4___ which lets '+' be used on the class''', 
 	'answers': {'class', 'methods', 'instance', 'add'}}}

def progress_game(level_chosen):
	game_level = game_levels[level_chosen]
	return game(game_level['phrase'], game_level['answers'], level_chosen)


# Initialize the game.
level_chosen = introduction()

if level_chosen != None:
	progress_game(level_chosen)