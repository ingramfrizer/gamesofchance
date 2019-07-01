import random

#Write your game of chance functions here

def choosestake(money):
	stake = 0
	while stake == 0:
		userinput = input("Your bankroll is {}. How \
much would you like to stake?".format(money))
		try:
			if not float(userinput) > 0:
				print("You must stake more than zero")
			elif money - float(userinput) < 0:
				print("You cannot stake more than you have!")
			else:
				stake = float(userinput)
		except ValueError:
			print("You must enter a number")
	return stake

def cointoss(bet):
	print("The coin is in the air ...")
	guess = ""
	while guess == "":
		userinput = input("Do you call Heads [H] or Tails[T]?")
		if userinput == "H" or userinput == "T":
			if userinput == "H":
				guess = 0
			else:
				guess = 1
	sides = ("Heads","Tails")
	print("You called ... {}".format(sides[guess]))
	result = random.randint(0,1)
	print("The coin comes down ... {}".format(sides[result]))
	if guess == result:
		print("You won {} money!".format(bet))
		outcome = bet
	else:
		print("Sorry, you lost {} money :(".format(bet))
		outcome = -bet
	return outcome

def chohan(bet):
	print("The (two) dice are rolled ...")
	guess = ""
	while guess == "":
		userinput = input("Will their total be Cho(Even)[E] or Han(Odd)[O]?")
		if userinput == "E" or userinput == "O":
			if userinput == "E":
				guess = 0
			else:
				guess = 1
	sides = ("Cho(Even)", "Han(Odd)")
	print("You called ... {}".format(sides[guess]))
	dice1 = random.randint(1, 6)
	dice2 = random.randint(1, 6)
	dice = dice1 + dice2
	result = dice % 2
	print("The dice read {} and {} for a total of {} - it is ... {}".\
		format(dice1, dice2, dice, sides[result]))
	if guess == result:
		print("You won {} money!".format(bet))
		outcome = bet
	else:
		print("Sorry, you lost {} money :(".format(bet))
		outcome = -bet
	return outcome

def highcard(bet):
	cardnames = dict(list(enumerate(range(2, 11))))
	facecards = {9 : "Jack", 10 : "Queen", 11 : "King", 12 : "Ace"}
	cardnames.update(facecards)
	deck = [i for i in range(13)] * 4
	dealercard = deck[random.randint(0, len(deck) - 1)]
	deck.remove(dealercard)
	print("The dealer draws {} ...".format(cardnames[dealercard]))
	input("Press Enter to draw your card ...")
	playercard = deck[random.randint(0, len(deck) - 1)]
	if playercard > dealercard:
		print("You draw {} - you won {} money!".format(cardnames[playercard], bet))
		outcome = bet
	elif dealercard > playercard:
		print("You draw {} - you lost {} money :(".format(cardnames[playercard], bet))
		outcome = -bet
	else:
		print("you draw {} - ooooohh a tie, you don't win or lose your {} money."\
			.format(cardnames[playercard], bet))
		outcome = 0
	return outcome


cointoss.longname = "Coin Toss"
chohan.longname = "Cho Han"
highcard.longname = "High Card"

#Call your game of chance functions here

money = 100
chosengame = ""
games = {
		"T" : cointoss,
		"C" : chohan,
		"H"	: highcard
		}

while chosengame == "":
	userinput = input(
		"What game would you like to play?\n\
		Coin Toss [T]\n\
		Cho Han [C]\n\
		High Card [H]\n\
		or choose [F] to finish playing.\n\
		Selection: "
		)
	if userinput == "F":
		if money > 100:
			endmessage = "Well done!"
		else:
			endmessage = "Bad luck."
		print("You finished playing with {}. {}".format(money, endmessage))
		break
	chosengame = games.get(userinput, "")
	if chosengame != "":
		#print("You chose to play {}.".format(chosengame.longname))
		stake = choosestake(money)
		print("You chose to stake {} on {}".format(stake, chosengame.longname))
		money += chosengame(stake)
		if money == 0:
			print("You have done all your money, bad luck, good bye!!")
			break
		print("You now have {} money.".format(money))
		chosengame = ""