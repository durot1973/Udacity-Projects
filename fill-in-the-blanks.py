
# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!


import string

def introduction():
	'''This function introduces the program and points in the next direction'''
	level_chosen = ''

	while level_chosen !='easy' or level_chosen != 'medium' or level_chosen !='hard':
		print 'Please select a game difficulty by typing it in!'
		print 'Possible choices include easy, medium and hard'
		level_chosen = raw_input()
		level_chosen = level_chosen.lower()
		if level_chosen == 'easy':
			return 'easy'
		elif level_chosen == 'medium':
			return 'medium'
		elif level_chosen == 'hard':
			return 'hard'
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
	index = paragraph.index('__')
	substitute_length = 7
	return paragraph[index: index + substitute_length]

def game(paragraph, words_to_be_substituted, level_chosen):
	'''This is the game.
	accepts values from the either easy, medium or hard and runs with that'''
	guesses, user_input, substitute_paragraph = 5, '', paragraph[:]
	print 'You have chosen ' + level_chosen + '!' + '\n  ' + '\nYou will get ' + str(guesses) + ' guesses per problem' + '\n '
	
	while not isSubstituted(paragraph):
		substitute_word = identifySubstitute(paragraph)
		print 'The current paragraph reads as such:' + '\n' + substitute_paragraph + '\n' 
		question = 'What should be substituted in for ' + substitute_word + '?'
		user_input = (raw_input(question)).lower()
		
		if user_input == words_to_be_substituted[substitute_word]:
			print 'Correct!'
			substitute_paragraph, paragraph = toSubstitute(user_input, substitute_word, paragraph), toSubstitute(user_input, substitute_word, paragraph)
		else:
			guesses -= 1
			if guesses < 1:
				break
			else:
				print "\nThat's not the correct answer: Let's try again; you have %g try left" %guesses
	if isSubstituted(paragraph):
		print substitute_paragraph + '\nYou won!'

#Each function from here is a level that the user chooses, each runs game based on some prebuilt values.
def easy():
	'''easy level'''
	paragraph = '''A common first thing to do in a language is display 'Hello ___1___!' In ___2___ this is
	particularly easy; all you have to do is type in: ___3___ "Hello ___1___!". Of course, that isn't a
	very useful thing to do. However, it is an example of how to output to the user using the ___3___ command,
	and produces a program which does something, so it is useful in that capacity. It may seem a bit
	odd to do something in a Turing complete language that can be done even more easily with an ___4___ file
	in a browser, but it is a step in learning ___2___ and that is really it's purpose'''
	
	words_to_be_substituted = {'___1___': 'world', '___2___':'python', '___3___':'print', '___4___':'html'}

	return game(paragraph, words_to_be_substituted, 'easy')

def medium():
	'''medium level'''
	paragraph = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
	adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
	don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
	tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
	
	words_to_be_substituted = {'___1___': 'function', '___2___':'argument', '___3___':'none', '___4___':'list'}

	return game(paragraph, words_to_be_substituted, 'medium')

def hard():
	'''hard level'''
	paragraph = '''When you create a ___1___, certain ___2___s are automatically generated for you if you don't make them manually. An
	object is an __3__ of a class is. Binary operators can also be created for the class e.g __4__ which lets '+' be used on the class'''
	
	words_to_be_substituted = {'___1___': 'class', '___2___':'method', '___3___':'instance', '___4___':'add'}

	return game(paragraph, words_to_be_substituted, 'hard')

level_chosen = introduction()

if level_chosen == 'easy':
	easy()
elif level_chosen == 'medium':
	medium()
elif level_chosen == 'hard':
	hard()
