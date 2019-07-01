import random

#Write your game of chance functions here

def cointoss(bet=1):
	guess = ""
	while guess == "":
		userinput = input("Heads [H] or Tails[T]?")
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



#Call your game of chance functions here

money = 100
chosengame = ""
games = {
		"C" : cointoss,
		"A" : "laterputfunctionhere"
		}

while chosengame == "":
	userinput = input(
		"What game would you like to play?\n\
		Coin Toss [C]\n\
		Another [A]\n\
		or choose [F] to finish playing.\n\
		Selection: "
		)
	if userinput == "F":
		break
	chosengame = games.get(userinput, "")
	if chosengame != "":
		# need to put stake choosing in here, poss function?
		money += chosengame(10)
		print("You now have {} money.".format(money))
		chosengame = ""