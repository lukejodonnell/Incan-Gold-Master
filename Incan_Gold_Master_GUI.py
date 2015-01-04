import easygui as gui

treasure = [0,1,1,1,1,2,0,2,0,1,0,2,0,1,1,1,0,1]
treasureOut = 0
# fire,mummies,rock,spider,snake
hazardsGame = [3,3,3,3,3]
hazardsRound = [3,3,3,3,3]
hazardsTable = [0,0,0,0,0]
#craycray
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
		#should this line be:
		#"del copy[x]"?
		del copy[len(master)]
		
#I added this for debugging, it tells what type each variable in a list is		
def tellType(list):
	for x in range(0, len(list)):
		print(type(list[x]))
		
def typeCard():
	turnType = gui.buttonbox("What type of card was turned over?", "Card Type", ["treasure", "hazard", "artifact"])
	global turnType
	gui.msgbox("Okay, so a " + turnType + " was turned over.", "Card Type This Turn")
	#Original code
	#print("What type of card was turned over?  ")
	#	turnType = input("treasure, hazard, or artifact:")
	#	print("Okay, so a " + turnType + " was turned over.")
	#	line(1)
	
def tressureValue():
	tValue = int(gui.integerbox("Enter the value of the treasure card?", "Treasure Value", 1, 0, 17))
	global tValue
	
def hazardValue():
	tValue = int(gui.indexbox("What type of hazard card was turned over?", "Name the Hazard", ["Fire", "Mummies", "Rocks", "Spider", "Snake"]))
	global tValue
	
def confirmation():
	cardMsg = "I will remove a " + str(tValue) + " " + str(turnType) + " card from the virtual draw pile"
	msgList = [cardMsg, "Press cancel to change, otherwise continue"]
	msgText = '\n'.join(msgList)
	return gui.ccbox(msgText, "Confirm the Card this Round")
	
	
def playersTurnBackMsg():
	choiceList = [None]
	global playersLeft
	for x in range(0, playersLeft + 1):
		choiceList.insert(x, str(x))
	for x in range(playersLeft + 1, len(choiceList)):
		del choiceList[x]

	playersLeft = playersLeft - gui.indexbox("How many players turned back this turn?", "What players are left", choiceList)

def playersTurnBackText():	
	print("How many players turned back this turn?")
	playersLeft = playersLeft - int(input("Number:"))
	print("so there are", playersLeft, " players left in this round")
	line(1)
	
	
def textInfoMsg():
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
	
		
def infomessage():
	roundmsg = "Round: " + str(round) + " turn: " + str(turn)
	
	deckTotalMsg = "Deck total:" + str(deckTotal())
	deathSumMsg = "Round ending hazard cards in deck:" + str(deathSum())
	deathPropMsg = "Percent chance of losing this turn:" + str(deathProb() * 100)
	
	wAverageAllMsg = "Expected treasure value:" + str(wAverageAll())
	artifactsMsg = "Artifacts in deck:" + str(artifacts)
	wAverageMsg = "E.T.V. on treasure cards only:" + str(wAverage())
	ETVsplitMsg = "E.T.V. after split with players:" + str(wAverageAll() // playersLeft) + "(" + str(wAverageAll() / playersLeft) + ")"
	
	goldOwnedMsg = "Points you have this round:" + str(goldOwned)
	rtvrMsg = "Risk times value at risk:" + str(goldOwned * deathProb() * 100)
	metricMsg = "Risk * V.A.R. / E.T.V. after split:" + str((goldOwned * deathProb() * 100) / (wAverageAll() / playersLeft))
	
	messageList = [roundmsg, " ", deckTotalMsg, deathSumMsg, deathPropMsg, " ", wAverageAllMsg, artifactsMsg, wAverageMsg, ETVsplitMsg, " ", goldOwnedMsg, rtvrMsg, metricMsg]
	tellType(messageList)
	messageText = '\n'.join(messageList)
	gui.msgbox(messageText, "Statistics for this coming turn")
	 

gui.msgbox("Hello, and welcome to the Incan Gold Master Program", "Welcome")

players = gui.integerbox("How many players", "Set up", 4, 0, 20)

playersLeft = players
global playersLeft

msg = "Okay, there are " + str(players) + " players."
gui.msgbox(msg, "Set up")

for round in range(1,5):
	while roundNotOver():
		if redo:
			print("redo")
		redo = False
		
		textInfoMsg()
		infomessage()
		
		playersTurnBackMsg()
		
		typeCard()
		

		if turnType == "treasure" or turnType == "t":
			tressureValue()
			
		elif turnType == "hazard" or turnType == "h":
			hazardValue()
		elif turnType == "artifact":
			tValue = None
		else:
			print("I'm sorry, ", turnType, " is not a recognized card type, let's start again")
			pressEnter()
			redo = True
			
		line(1)
		
		if not redo:
			if confirmation():
				print("Okay, I will remove a ", tValue, " ", turnType, " card from the virtual draw pile")
				print("  ")
				if turnType == "treasure" or turnType == "t":
					if (treasure[tValue] - 1) >= 0:
						treasure[tValue] = treasure[tValue] - 1
						treasureOut = treasureOut + 1
						goldOwned = goldOwned + (tValue // playersLeft)
						turn = turn + 1
					else:
						msg = "I'm sorry, but a " + str(tValue) + " wasn't in the deck to be turned over, let's start over"
						gui.msgbox(msg)
						gui.msgbox("Redoing turn", "Redoing Turn")
				elif turnType == "hazard" or turnType == "h":
					if (hazardsRound[tValue] - 1) >= 0:
						hazardsRound[tValue] = hazardsRound[tValue] - 1
						hazardsTable[tValue] = hazardsTable[tValue] + 1
						turn = turn + 1
					else:
						gui.msgbox("I'm sorry, but the hazard you selected wasn't in the deck to be turned over")
				elif turnType == "artifact":
					if (artifacts - 1) >= 0:
						artifacts = artifacts - 1
						turn = turn + 1
					else:
						gui.msgbox("I'm sorry, but an artifact wasn't in the deck to be turned over")
						gui.msgbox("Redoing turn", "Redoing Turn")
						
			else: 
				gui.msgbox("Oh, sorry then, let's try this turn over.", "Redoing Turn")	
				
	line(5)
	gui.msgbox("We are starting a new round!", "New Round!")
	goldOwned = 0
	artifacts = artifacts + 1
	treasure = [0,1,1,1,1,2,0,2,0,1,0,2,0,1,1,1,0,1]
	treasureOut = 0	 
	hazardsTable = [0,0,0,0,0]
	listTransfer(hazardsRound, hazardsGame)
	turn = 1
		


