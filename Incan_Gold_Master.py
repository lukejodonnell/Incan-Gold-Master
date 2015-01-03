treasure = [0,1,1,1,1,2,0,2,0,1,0,2,0,1,1,1,0,1]
treasureOut = 0
# fire,mummies,rock,spider,snake
hazardsGame = [3,3,3,3,3]
hazardsRound = [3,3,3,3,3]
hazardsTable = [0,0,0,0,0]

artifacts = 1
goldOwned = 0
round = 1
turn = 1
redo = False
Enter = None

def pressEnter():
	enterVar = input("press enter")
	

def line(r):
	for x in range(0, r):
		print(" ")

def roundNotOver():
	retval = True
	for x in range(0, 5):
		if hazardsTable[x] == 2:
			retval = False
			hazardsGame[x] = hazardsGame[x] - 1
	return retval
			
			
def deckTotal():
	return (sum(treasure) + sum(hazardsRound) + artifacts)
	
def deathSum():
	deathSum = 0
	for x in range(0,5):
		if hazardsTable[x] == 1:
			deathSum = deathSum + hazardsRound[x] 
	return deathSum
	
def deathProb():
	deathProb = 0
	for x in range(0, 5):
		if hazardsTable[x] == 1:
			deathProb = deathProb + (hazardsRound[x] / deckTotal())
	return deathProb
	
def wAverageAll():
	wAverageAll = 0
	for x in range(0,18):
		wAverageAll = wAverageAll + ( x * (treasure[x] / deckTotal()))
	return wAverageAll
	
def wAverage():
	wAverage = 0
	for x in range(0,18):
		wAverage = wAverage + ( x * (treasure[x] / sum(treasure)))
	return wAverage
	
#listTransfer(list_to_be_copied_from, list_to_be_copied_to)
def listTransfer(master, copy):
	for x in range(0, len(master)):
		copy[x] = master[x]
	for x in range(len(master), len(copy)):
		del copy[len(master)]


line(4)
print("Hello, and welcome to the Incan Gold Master Program")
line(1)

players = int(input("How many players?  "))
playersLeft = players
print("Okay, there are ", players, " players.")

for round in range(1,5):
	while roundNotOver():
		if redo:
			print("redo")
		redo = False
		line(2)
		print("Round: ", round, "turn: ", turn)
		line(3)
		
		print("Deck total.........................:", deckTotal())
		print("Round ending hazard cards in deck..:", deathSum())
		print("Percent chance of losing this turn.:", deathProb() * 100)
		line(1)
		
		print("Expected treasure value............:", wAverageAll())
		print("Artifacts in deck..................:", artifacts)
		print("E.T.V. on treasure cards only......:", wAverage())
		print("E.T.V. after split with players....:", wAverageAll() // playersLeft, "(", wAverageAll() / playersLeft, ")")
		line(1)
		
		print("Points you have this round.........:", goldOwned)
		print("Risk times value at risk...........:", goldOwned * deathProb() * 100)
		print("Risk * V.A.R. / E.T.V. after split.:", (goldOwned * deathProb() * 100) / (wAverageAll() / playersLeft))
		line(1)
		
		print("......Debug.........")
		print("HazardsTable", hazardsTable)
		print("HazardsRound", hazardsRound)
		print("HazardsGame", hazardsGame)
		line(2)
		
		print("How many players turned back this turn?")
		playersLeft = playersLeft - int(input("Number:"))
		print("so there are", playersLeft, " players left in this round")
		line(1)
		
		print("What type of card was turned over?  ")
		turnType = input("treasure, hazard, or artifact:")
		print("Okay, so a " + turnType + " was turned over.")
		line(1)

		if turnType == "treasure" or turnType == "t":
			print("What value treasure card?")
			tValue = input("type the number")
			tValue = int(tValue)
			
		elif turnType == "hazard" or turnType == "h":
			print("What type of hazard card?")
			tValue = input("0 for fire, 1 for mummies, 2 for rocks, 3 for spider, 4 for snake")
			tValue = int(tValue)
		elif turnType == "artifact":
			tValue = None
		else:
			print("I'm sorry, ", turnType, " is not a recognized card type, let's start again")
			pressEnter()
			redo = True
			
		line(1)
		
		if not redo:
			print("So a ", tValue, " ", turnType, " card was turned over this turn.  Is this correct?")
			okay = input("(y or n):")
		

			if okay == "y":
				print("Okay, I will remove a ", tValue, " ", turnType, " card from the virtual draw pile")
				print("  ")
				if turnType == "treasure" or turnType == "t":
					if (treasure[tValue] - 1) >= 0:
						treasure[tValue] = treasure[tValue] - 1
						treasureOut = treasureOut + 1
						goldOwned = goldOwned + (tValue // playersLeft)
						turn = turn + 1
					else:
						print("I'm sorry, but a ", tValue, " wasn't in the deck to be turned over, there must be a mistake, let's start over")
						pressEnter()
				elif turnType == "hazard" or turnType == "h":
					if (hazardsRound[tValue] - 1) >= 0:
						hazardsRound[tValue] = hazardsRound[tValue] - 1
						hazardsTable[tValue] = hazardsTable[tValue] + 1
						turn = turn + 1
					else:
						print("I'm sorry, but a ", tValue, " value hazard wasn't in the deck to be turned over, there must be a mistake, let's start over")
						pressEnter()
				elif turnType == "artifact":
					if (artifacts - 1) >= 0:
						artifacts = artifacts - 1
						turn = turn + 1
					else:
						print("I'm sorry, but an artifact wasn't in the deck to be turned over, there must be a mistake, let's start over")
						pressEnter()
			else: 
				print("Oh, sorry then, let's try this turn over.")	
				
	line(5)
	print("new round!")
	artifacts = artifacts + 1
	treasure = [0,1,1,1,1,2,0,2,0,1,0,2,0,1,1,1,0,1]
	treasureOut = 0	 
	hazardsTable = [0,0,0,0,0]
	listTransfer(hazardsRound, hazardsGame)
	turn = 1
		


