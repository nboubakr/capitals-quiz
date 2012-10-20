#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: quiz.py

# The Quiz of Country and Their Capital
# University of Djillali Liabes (UDL) - Sidi Bel Abbes
# Faculty of Sciences - Computer Science (LMD1) 2011/2012 
# Student: Boubakr NOUR <n.boubakr@gmail.com>

# License: Academic Free License (AFL)

import os
import time
from random import choice, shuffle

import sqlite3 as SQLite

from data import Continent

# Conecting to scores' database
connection = SQLite.connect("scores.db")
with connection:
    cursor = connection.cursor()
    cursor.executescript("""CREATE TABLE IF NOT EXISTS Data(Player STRING, Score INT);""")

# Answers that can quit the quiz
farewell = ['quit', 'exit', 'close', 'end', 'stop']

def clear():
	"""Function to clear the Terminal (Console), works under Windows, Mac OS, *Unix"""
	os.system(['clear', 'cls'][os.name == 'nt'])

def main_menu():
	"""Display the main menu"""
	clear()
	print """
	| * * * * WELCOME TO THE QUIZ OF COUNTRY AND THEIR CAPITAL * * * * |
	 ___________________________ MAIN MENU ____________________________
	|                                                                  |
	|                                                                  |
	|    (*) To view the quiz instructions, Press <I>                  |
	|    (*) To start a new quiz, Press <C>                            |
	|    (*) To view the top scores, Press <S>                         |
	|    (*) To quit the quiz, Press <Q>                               |
	|                                                                  |
	|__________________________________________________________________|
	"""

def quiz_instructions():
	"""Display the quiz instructions."""
	clear()
	print """
	 ______________________ THE QUIZ INSTRUCTIONS _____________________
	|                                                                  |
	|                                                                  |
	|    (*) You can play in three levels.                             |
	|    (*) The rating of 100 (percentage).                           |
	|    (*) The response time is calculated on each answer.           |
	|    (*) You can reset all scores to 0.                            |
	|    (*) You can quit the quiz with the answer:                    |
	|        (Quit, Exit, Close, End, Stop)                            |
	|                                                                  |
	|__________________________________________________________________|
	"""

def new_quiz():
	"""Display the new quizz."""
	clear()
	print """
	 ____________________________ NEW QUIZ ____________________________
	|                                                                  |
	|                                                                  |
	|    (*) Good Luck !                                               |
	|                                                                  |
	|__________________________________________________________________|
	"""

def continent_menu():
	"""Display continent menu."""
	clear()
	print """
	 ________________________ SELECT A CONTINENT ______________________
	|                                                                  |
	|                                                                  |
	|    (*) For Africa, Press  (1)                                    |
	|    (*) For America, Press (2)                                    |
	|    (*) For Asia, Press    (3)                                    |
	|    (*) For Europe, Press  (4)                                    |
	|    (*) For Oceania, Press (5)                                    |
	|    (*) For All the World, Press (6)                              |
	|                                                                  |
	|__________________________________________________________________|
	"""

def levels_menu():
	"""Display the levels menu."""
	clear()
	print """
	 _________________________ SELECT A LEVEL _________________________
	|                                                                  |
	|                                                                  |
	|    (*) For Beginner Level, Press (1)                             |
	|    (*) For Average Level, Press (2)                              |
	|    (*) For Expert Level, Press (3)                               |
	|                                                                  |
	|__________________________________________________________________|
	"""

def levels(data, data_txt, player, level, all_questions, mark):
	"""
	Procedure that will ask questions on special level.
	
	data: The chosen continent
	data_txt: The continent name
	player: The player name
	level: The chosen level to play
	all_question: The number of questions that will be asked
	mark: A mark for each correct answer
	"""

	clear()
	answer = ''
	questions = 0
	score = 0
	
	try:
		while answer not in farewell:
			questions += 1  # Count the questions
			question = choice(data) # Choice a random question
			
			if level == 1:
				# Some information about the current position.
				print '  Level: Beginner      Continent: %s      Question: %s/%s      Score: %s\n' % (data_txt, questions, all_questions, int(score))
				
				print 'What is the capital of: %s' % question[0].capitalize() # The question
				
				suggestions = [choice(data)[1].capitalize(), question[1].capitalize(), choice(data)[1].capitalize()] # Suggestions
				shuffle(suggestions) # Shuffle the suggestions
				s1, s2, s3 = suggestions
				print "\n- %s          - %s          - %s" % (s1, s2, s3) # Display the suggestions
				
			elif level == 2:
				print '  Level: Average      Continent: %s      Question: %s/%s      Score: %s\n' % (data_txt, questions, all_questions, int(score))
				
				print 'What is the capital of: %s' % question[0].capitalize()
				
				if len(question) == 3: # If there is a help, print it
					print '\n\t- Help:', question[2]

				else: # else print the first character of the correct answer
					print '\n\t- Help: Its capital begins with:', question[1][0].upper()

			elif level == 3:
				print '  Level: Expert      Continent: %s      Question: %s/%s      Score: %s\n' % (data_txt, questions, all_questions, int(score))
				
				print 'What is the capital of: %s' % question[0].capitalize()

			before_answer = time.time() # Time before type the answer
			answer = raw_input('\n--> Enter your answer: ').lower().strip()
			answer_time = int(time.time() - before_answer) # Answer time
				
			if answer == question[1]: # Correct answer
				score += mark # Add one point to the score
				print '\n   Correct !     - Answer time: %s seconds' % answer_time
				raw_input('\nPress <Enter> to continue...')
				clear()

			elif answer in farewell: # Quit the quiz
				clear()
				print '\n\tYou have stopped the quiz !'
				raw_input('\nPress <Enter> to view your final score...')
				break # Stop the questions

			else: # Wrong answer
				print '\n    Wrong !	 - The correct answer: %s	 - Answer time: %s seconds' % (question[1].capitalize(), answer_time)
				raw_input('\nPress <Enter> to continue...')
				clear()

			if questions == all_questions: # We finished asking all the questions
				print ' * * * * * * * * * * END * * * * * * * * * *\n'
				raw_input('Press <Enter> to view your final score...')
				break # End the quiz
	
	except KeyboardInterrupt:
		clear()
		print '\n\tYou have stopped the quiz !'
		raw_input('\nPress <Enter> to view your final score...')
	
	clear()	
	print '\nYour score:', int(score), '%\n' # View the final score
	save_score(player, int(score)) # Save score
	raw_input('Press <Enter> to return to the main menu... ')
	quiz()

def save_score(player, score):
	"""
	Save the score.

	player: The player naùe
	score: The final score
	"""
	data = ((player, score))
	with connection:
		cursor.execute("INSERT INTO Data VALUES(?, ?)", data)

def reset_db():
	"""Reset scores."""
	with connection:
		cursor.executescript("""
			DROP TABLE IF EXISTS Data;
			CREATE TABLE Data(Player STRING, Score INT);
			INSERT INTO Data VALUES('Boubakr', 99);
			INSERT INTO Data VALUES('Mohamed', 49);
		""")

def view_scores():
	"""View the scores."""
	clear()
	print "     _______________________ TOP SCORES _______________________\n\n"
	try:
		cursor.execute("SELECT * FROM Data ORDER BY Score Desc")
		rows = cursor.fetchall()

		if rows:
			try:
				for i in range(0, 5):
					if rows[i][1] == 0:  # Don't show player that have score = 0
						continue

					print "\t%s\t\t%s" % (rows[i][0], rows[i][1])
			except Exception, e:
				pass
		else:
			print '\tThere is no score !\n'
	
	except SQLite.Error, e:
		print "Error: %s" % e.args[0]
	
	print '\n\nTo reset all scores to 0, Press <O> otherwise press <Enter> !\n'
	score_choice = raw_input('--> Enter your choice: ').lower().strip()
	
	if score_choice == 'o' or score_choice == '0': # Reset all scores.
		reset_db()	# Reset Database
		clear()
		raw_input("\nAll scores was reset to 0\n\nPress <Enter> to return to the main menu...")
		quiz()
	else:
		quiz()

def quit():
	"""Display quit message."""
	clear()
	print """
	 __________________________ QUIT THE QUIZ _________________________
	|                                                                  |
	|                                                                  |
	|    THANK YOU FOR USING THIS QUIZ !                               |
	|    -------------------------------                               |
	|                                                                  |
	|    (*) University of Djillali Liabes (UDL) - Sidi Bel Abbes      |
	|                                                                  |
	|    (*) Faculty of Sciences - Computer Science (LMD1) 2011/2012   |
	|                                                                  |
	|    (*) Student: Boubakr NOUR <n.boubakr@gmail.com>               |
	|                                                                  |
	|__________________________________________________________________|
	"""

def error(msg):
	"""
	Display an error message.

	msg: Error message
	"""
	clear()
	print """
	 ______                        _ 
	|  ____|                      | |
	| |__   _ __ _ __ ___  _ __   | |
	|  __| | '__| '__/ _ \| '__|  | |
	| |____| |  | | | (_) | |     |_|
	|______|_|  |_|  \___/|_|     (_)
	
	%s\n               
	""" % msg

def quiz():
	"""Start the quiz"""

	main_menu()
	
	try:
		main_choice = raw_input('[+] Enter your choice: ').lower().strip()
	except:
		quiz()
	
	if main_choice == 'i':  # Quiz instructions
		quiz_instructions()
		raw_input('Press <Enter> to return to the main menu... ')
		quiz()
	
	elif main_choice == 'c':  # New quiz
		while True:
			new_quiz()
			player_name = raw_input('[+] If you are ready, Enter your name: ').strip() # Ask the player for his name

			if len(player_name) < 3:
				error('Enter a valid name (3 digits at least) !')
				raw_input('Press <Enter> to try again...')
			elif len(player_name) > 10:
				error('Enter a valid name (9 digits at most) !')
				raw_input('Press <Enter> to try again...')
			else:
				break
		
		continent_choice = 0
		continent = []     # Reset all the continents
		
		while continent_choice not in range(1, 7):
			try:
				continent_menu()
				continent_choice = int(raw_input('[+] Enter your choice (1 ~ 6): '))

				if continent_choice == 1:
					continent = Continent.africa
					continent_txt = 'Africa'
				elif continent_choice == 2:
					continent = Continent.america
					continent_txt = 'America'
				elif continent_choice == 3:
					continent = Continent.asia
					continent_txt = 'Asia'
				elif continent_choice == 4:
					continent = Continent.europe
					continent_txt = 'Europe'
				elif continent_choice == 5:
					continent = Continent.oceania
					continent_txt = 'Oceania'
				elif continent_choice == 6:
					continent = Continent.world
					continent_txt = 'All the World'
			except:
				error('Enter a valid choice !')
				raw_input('Press <Enter> to try again...')
			
		max_questions_number = len(continent) # The maximum number of questions possible.
		questions_number_txt = '[+] Choose the number of questions between 1 and %s: ' % max_questions_number
		number_of_questions = 0
		
		while number_of_questions not in range(1, max_questions_number + 1):
			try:
				clear()
				number_of_questions = int(raw_input(questions_number_txt))
			except:
				error('Enter a valid number of questions !')
				raw_input('Press <Enter> to try again...')
		
		point = 100. / number_of_questions # Point for each correct answer
		level_choice = 0
		
		while level_choice not in range(1, 4):
			try:
				levels_menu()
				level_choice = int(raw_input('[+] Enter your choice (1 / 2 / 3): '))
			except:
				error('Enter a valid level !')
				raw_input('Press <Enter> to try again...')
		
		if level_choice == 1:
			levels(continent, continent_txt, player_name, 1, number_of_questions, point)
		elif level_choice == 2:
			levels(continent, continent_txt, player_name, 2, number_of_questions, point)
		elif level_choice == 3:
			levels(continent, continent_txt, player_name, 3, number_of_questions, point)
		
	elif main_choice == 's':  # Top scores
		view_scores()
	
	elif main_choice == 'q':  # Quit quiz
		quit()
		connection.close()	  # Close the connection to database
		raw_input("	--------------------------------------------------------------------")
		exit()
	
	else: # Unknown selection
		error("I didn't understand your choice !")
		raw_input('Press <Enter> to try again... ')
		quiz()

if __name__ == '__main__':
	quiz()