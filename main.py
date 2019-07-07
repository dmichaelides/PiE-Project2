'''

create Hangman in Python.


___________
|         |
|         #
|         #
|         #
|         O
|       ~~|~~
|        / \
|         
|
|
|
|______

# manSequence = ["O","|","~","~","~","~","/","\\"]


'''



#################



def drawGamepPlay():
	for row in range(14):
		if row == 0:
			print("___________")
		if row == 1:
			print("|         |")
		if row > 1 and row < 5:
			print("|         #")
		if row > 4 and row < 8:
			if errorCounter == 0:
				print("|")
			else:
				for col in range(2):
					if col == 0:
						if errorCounter < 2 and row > 5:
							print("|       ")
							break
						if 1 < errorCounter < 7 and row > 6:
							print("|       ")
							break
						else:
							print("|       ",end="")
					if col > 0:
						if row == 5:
							print("  o")
						if row == 6:
							if errorCounter == 2:
								print("  |")
							if errorCounter == 3:
								print("  |~")
							if errorCounter == 4:
								print(" ~|~")
							if errorCounter == 5:
								print(" ~|~~")
							if errorCounter >= 6:
								print("~~|~~")
							continue
						if row == 7:
							if errorCounter == 7:
								print(" /")
							if errorCounter == 8:
								print(" / \\")	
						# print("  o")
		if row > 7 and row < 12:
			print("|")
		if row == 12:
			print("|______")
		if row == 13:
			print("\n\n")
			for i in revealedWord:
				print(i + " ",end="")
			print("\n\n")


################

import os
import time	

Player1 = input("Player 1, please provide your name: \n")
Player2 = input("Player 2, please provide your name: \n")

theWord = input("Great!  Ok, " + Player1 + " what will be the word which " + Player2 + " will need to find?\n\nWrite it down below:\n")


print("Nice! The word you have chosen is '" + theWord + "'.\n\n GOOD LUCK!  \n\nWait for the screen to clear before you passing it on for " + Player2 + " to begin.")
time.sleep(5)

os.system("cls")

print("GOOD LUCK " + Player2 + "!\n")
errorCounter = 0

wordToList = list(theWord)
revealedWord = []

for n in wordToList:
	n = "_"
	revealedWord.append(n)


guessList = {}

while True:
	letIndex = 0	
	exists = 0
	preLetCheck = 0
	totLet = int(len(wordToList))
	if wordToList == revealedWord:
		os.system("cls")
		print("\n\nNICE!  You found the word and saved the man's life!\n\nGood for you",Player2)
		time.sleep(4)
		break
	if errorCounter == 8:
		os.system("cls")
		drawGamepPlay()
		print("\n\nOh no your man has hung!\n\nGAME OVER!\n\nFATALITY!",Player1,"wins.")
		break
	letterChoice = input("Type a letter you think is in the word:\n")
	for gl in guessList:
		if gl == letterChoice:
			preLetCheck += 1
	if preLetCheck > 0:
		os.system("cls")
		drawGamepPlay()
		print("\n\nOops! You have already chosen that letter!  Try again.\n")
		time.sleep(2)
		continue
	for g in wordToList:
		if g == letterChoice:
			revealedWord[letIndex] = g
			guessList[g] = "match"
			exists += 1
			letIndex += 1
			totLet -= 1
			os.system("cls")
			drawGamepPlay()
			if wordToList == revealedWord:
				continue
			else:
				print("\nYEAH! That letter exists in the word.\n\nCheck it out underneath the gallow")
				time.sleep(3)
				os.system("cls")
		else:
			totLet -= 1
			letIndex += 1
			if totLet == 0 and exists == 0:
				guessList[letterChoice] = "nomatch"
				errorCounter += 1
				if errorCounter < 8:
					os.system("cls")
					drawGamepPlay()
					print("\nUnlucky!  You guessed wrong.\n\nTry again, you have", 8 - errorCounter,"tries left.")
					time.sleep(3)
					os.system("cls")
	drawGamepPlay()

