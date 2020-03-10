import random
class Die(object):
    def __init__(self):
        self.num = random.randint(1, 6)
    def roll(self):
        self.num = random.randint(1, 6)
class Player(object):
    def __init__(self):
        self.Ones = -1
        self.Twos = -1
        self.Threes = -1
        self.Fours = -1
        self.Fives = -1
        self.Sixes = -1
        self.TOK = -1
        self.FOK = -1
        self.FH = -1
        self.SS = -1
        self.LS = -1
        self.Y = -1
        self.C = -1
        self.filled = []
    def playTurn(self):
        print("Your first roll is:")
        firstRoll()
        printDice()
        askForRerolls()
        self.possiblePoints()
        self.assignPoints()
        self.showCard(False)
    def possiblePoints(self):
        print("Your roll would score the following numbers:")
        if(self.Ones<0):
            print("0  Ones: " + str(calcOnes()))
        else:
            print("0  Ones: " + "FILLED: " + str(self.Ones))
        if(self.Twos<0):
            print("1  Twos: " + str(calcTwos()))
        else:
            print("1  Twos: " + "FILLED: " + str(self.Twos))
        if(self.Threes<0):
            print("2  Threes: " + str(calcThrees()))
        else:
            print("2  Threes: " + "FILLED: " + str(self.Threes))
        if(self.Fours<0):
            print("3  Fours: " + str(calcFours()))
        else:
            print("3  Fours: " + "FILLED: " + str(self.Fours))
        if(self.Fives<0):
            print("4  Fives: " + str(calcFives()))
        else:
            print("4  Fives: " + "FILLED: " + str(self.Fives))
        if(self.Sixes<0):
            print("5  Sixes: " + str(calcSixes()))
        else:
            print("5  Sixes: " + "FILLED: " + str(self.Sixes))
        if(self.TOK<0):
            print("6  3 of a kind: " + str(calcTOK()))
        else:
            print("6  3 of a kind: " + "FILLED: " + str(self.TOK))
        if(self.FOK<0):
            print("7  4 of a kind: " + str(calcFOK()))
        else:
            print("7  4 of a kind: " + "FILLED: " + str(self.FOK))
        if(self.FH<0):
            print("8  Full House: " + str(calcFH()))
        else:
            print("8  Full House: " + "FILLED: " + str(self.FH))
        if(self.SS<0):
            print("9  Small Straight: " + str(calcSS()))
        else:
            print("9  Small Straight: " + "FILLED: " + str(self.SS))
        if(self.LS<0):
            print("10 Large Straight: " + str(calcLS()))
        else:
            print("10 Large Straight: " + "FILLED: " + str(self.LS))
        if(self.Y<0):
            print("11 Yahtzee: " + str(calcY()))
        else:
            print("11 Yahtzee: " + "FILLED: " + str(self.Y))
        if(self.C<0):
            print("12 Chance: " + str(calcC()))
        else:
            print("12 Chance: " + "FILLED:" + str(self.C))
    def assignPoints(self):
        notPicked = True
        slotIsNum = False
        while(notPicked):
            while(slotIsNum==False):
                slot = input("Which slot would you like to fill? ")
                if(slot.isdigit()):
                    slotIsNum = True
                else:
                    print("Please enter a number")
            same = False
            for num in self.filled:
                if(num==int(slot)):
                    same = True
            if(same==True):
                print("That slot has already been filled. Please pick again.")
            else:
                self.filled.append(int(slot))
                if(int(slot)==0):
                    self.Ones = calcOnes()
                elif(int(slot)==1):
                    self.Twos = calcTwos()
                elif(int(slot)==2):
                    self.Threes = calcThrees()
                elif(int(slot)==3):
                    self.Fours = calcFours()
                elif(int(slot)==4):
                    self.Fives = calcFives()
                elif(int(slot)==5):
                    self.Sixes = calcSixes()
                elif(int(slot)==6):
                    self.TOK = calcTOK()
                elif(int(slot)==7):
                    self.FOK = calcFOK()
                elif(int(slot)==8):
                    self.FH = calcFH()
                elif(int(slot)==9):
                    self.SS = calcSS()
                elif(int(slot)==10):
                    self.LS = calcLS()
                elif(int(slot)==11):
                    self.Y = calcY()
                elif(int(slot)==12):
                    self.C = calcC()
                notPicked = False
    def showCard(self, final):
        if(final):
            print("This is your final card:")
        else:
            print("This is your current card:")
        if(self.Ones>=0):
            print("Ones: " + str(calcOnes()))
        else:
            print("Ones: " + "0 ")
        if(self.Twos>=0):
            print("Twos: " + str(calcTwos()))
        else:
            print("Twos: " + "0 ")
        if(self.Threes>=0):
            print("Threes: " + str(calcThrees()))
        else:
            print("Threes: " + "0 ")
        if(self.Fours>=0):
            print("Fours: " + str(calcFours()))
        else:
            print("Fours: " + "0 ")
        if(self.Fives>=0):
            print("Fives: " + str(calcFives()))
        else:
            print("Fives: " + "0 ")
        if(self.Sixes>=0):
            print("Sixes: " + str(calcSixes()))
        else:
            print("Sixes: " + "0 ")
        if(self.TOK>=0):
            print("3 of a kind: " + str(calcTOK()))
        else:
            print("3 of a kind: " + "0")
        if(self.FOK>=0):
            print("4 of a kind: " + str(calcFOK()))
        else:
            print("4 of a kind: " + "0")
        if(self.FH>=0):
            print("Full House: " + str(calcFH()))
        else:
            print("Full House: " + "0")
        if(self.SS>=0):
            print("Small Straight: " + str(calcSS()))
        else:
            print("Small Straight: " + "0")
        if(self.SS>=0):
            print("Large Straight: " + str(calcLS()))
        else:
            print("Large Straight: " + "0")
        if(self.Y>=0):
            print("Yahtzee: " + str(calcY()))
        else:
            print("Yahtzee: " + "0")
        if(self.C>=0):
            print("Chance: " + str(calcC()))
        else:
            print("Chance: " + "0")
    def calcFinalScore(self):
        bonus = 0
        if(self.Ones+self.Twos+self.Threes+self.Fours+self.Fives+self.Sixes>=63):
            bonus = 35
        return self.Ones+self.Twos+self.Threes+self.Fours+self.Fives+self.Sixes+self.TOK+self.FOK+self.FH+self.SS+self.LS+self.Y+self.C+bonus
def reroll():
    dice.clear()
    for die in rerollDice:
        die.roll()
    for die in keepDice:
        dice.append(die)
    for die in rerollDice:
        dice.append(die)
    keepDice.clear()
    rerollDice.clear()
def firstRoll():
    for die in dice:
        die.roll()
def printDice():
    print("Die Num     Roll")
    i = 0
    for die in dice:
        print("   " + str(i) + "         " + str(die.num))
        i += 1
def askForRerolls():
    rrCount = 0
    rrContinue = True
    rrAsk = ""
    while(rrContinue):
        rrAsk = input("Would you like to reroll? You have rolled " + str(rrCount+1) + " times. (Y/N): ")
        if(rrAsk.upper()=="Y"):
            chooseKeep()
            reroll()
            print("Your new roll is:")
            printDice()
            rrCount += 1
        else:
            rrContinue = False
        if(rrCount>1):
            rrContinue = False
def chooseKeep():
    inputNum = "-2"
    inputNumInt = -2
    zeroChosen = False
    oneChosen = False
    twoChosen = False
    threeChosen = False
    fourChosen = False
    while(inputNumInt!=-1):
        inputNum = input("Insert the die number followed by enter for the dice you would like to keep, when done type -1: ")
        inputNumInt = int(inputNum)
        if((inputNumInt==0 and zeroChosen == False) or (inputNumInt==1 and oneChosen == False) or (inputNumInt==2 and twoChosen == False) or (inputNumInt==3 and threeChosen == False) or (inputNumInt==4 and fourChosen == False)):
            if(inputNumInt==0):
                keepDice.append(dice[0])
                zeroChosen = True
            elif(inputNumInt==1):
                keepDice.append(dice[1])
                oneChosen = True
            elif(inputNumInt==2): 
                keepDice.append(dice[2])
                twoChosen = True
            elif(inputNumInt==3):
                keepDice.append(dice[3])
                threeChosen = True
            elif(inputNumInt==4):
                keepDice.append(dice[4])
                fourChosen = True
        elif(inputNumInt!=-1):
            print("Please insert a value from 0-4 that has not already been chosen or -1 to stop")
    for die in dice:
        inboth = False
        for kdie in keepDice:
            if(die==kdie):
                inboth = True
        if(inboth==False):
            rerollDice.append(die)
def createArrays():
    global dice
    dice = []
    global keepDice
    keepDice = []
    global rerollDice
    rerollDice = []
    global players
    players = []
def createDice():
    for i in range(0,5):
        dice.append(Die())
def createPlayers():
    numPlayers = int(input("How many players are there? "))
    for i in range(0, numPlayers):
        players.append(Player())
def calcOnes():
    points = 0
    for die in dice:
        if(die.num==1):
            points += 1
    return points
def calcTwos():
    points = 0
    for die in dice:
        if(die.num==2):
            points += 2
    return points
def calcThrees():
    points = 0
    for die in dice:
        if(die.num==3):
            points += 3
    return points
def calcFours():
    points = 0
    for die in dice:
        if(die.num==4):
            points += 4
    return points
def calcFives():
    points = 0
    for die in dice:
        if(die.num==5):
            points += 5
    return points
def calcSixes():
    points = 0
    for die in dice:
        if(die.num==6):
            points += 6
    return points
def calcTOK():
    points = 0 
    for die in dice:
        points += die.num
    for die in dice:
        count = 0
        for die2 in dice:
            if(die.num==die2.num):
                count += 1
        if(count>=3):
            return points 
    return 0
def calcFOK():
    points = 0 
    for die in dice:
        points += die.num
    for die in dice:
        count = 0
        for die2 in dice:
            if(die.num==die2.num):
                count += 1
        if(count>=4):
            return points 
    return 0
def calcFH():
    hasThree = False
    hasTwo = False
    for die in dice:
        count = 0
        for die2 in dice:
            if(die.num==die2.num):
                count += 1
        if(count==3):
            hasThree = True
        if(count==2):
            hasTwo = True
    if(hasThree and hasTwo):
        return 25
    else:
        return 0
def calcSS():
    unsortedArr = []
    for die in dice:
        unsortedArr.append(die.num)
    sortedArr = list(dict.fromkeys(unsortedArr))
    sortedArr.sort()
    if(len(sortedArr)<4):
        return 0
    elif(len(sortedArr)==4):
        startNum = sortedArr[0]
        if(startNum+1==sortedArr[1] and startNum+2==sortedArr[2] and startNum+3==sortedArr[3]):
            return 30
        else:
            return 0
    elif(len(sortedArr)==5):
        startNum = sortedArr[0]
        startNum2 = sortedArr[1]
        if((startNum+1==sortedArr[1] and startNum+2==sortedArr[2] and startNum+3==sortedArr[3]) or (startNum2+1==sortedArr[2] and startNum2+2==sortedArr[3] and startNum2+3==sortedArr[4])):
            return 30
        else:
            return 0
def calcLS():
    unsortedArr = []
    for die in dice:
        unsortedArr.append(die.num)
    sortedArr = list(dict.fromkeys(unsortedArr))
    sortedArr.sort()
    if(len(sortedArr)<5):
        return 0
    elif(len(sortedArr)==5):
        startNum = sortedArr[0]
        if(startNum+1==sortedArr[1] and startNum+2==sortedArr[2] and startNum+3==sortedArr[3] and startNum+4==sortedArr[4]):
            return 40
        else:
            return 0
def calcY():
    if(dice[0].num==dice[1].num==dice[2].num==dice[3].num==dice[4].num):
        return 50
    else:
        return 0
def calcC():
    points = 0 
    for die in dice:
        points += die.num
    return points
def finishGame():
    finalScorecards()
    annouceWinner()
def finalScorecards():
    n = 1
    for player in players:
        print("Player " + str(n) + ":")
        player.showCard(True)
        n += 1
def annouceWinner():
    playerRanks = []
    playerScores = []
    for player in players:
        playerScores.append(player.calcFinalScore())
    playerScores.sort()
    for score in playerScores:
        n = 1
        for player in players:
            if(player.calcFinalScore()==score):
                playerRanks.append(n)
            n += 1
    print("The final rankings are:")
    i = len(players)
    for rank in playerRanks:
        print(str(i) + ". Player " + str(playerRanks[i-1]) + " with a score of " + str(playerScores[i-1]))
        i -= 1
createArrays()
createDice()
createPlayers()
for i in range(0, 2):
    n = 1
    for player in players:
        print()
        print("Player " + str(n) + ", turn " + str(i + 1))
        player.playTurn()
        n += 1
finishGame()
 No newline at end of file
 No newline at end of file