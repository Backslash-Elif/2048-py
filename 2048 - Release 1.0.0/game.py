import random, vars
print("game.py: random, vars(.py) have been imported.")

def shortenGame(): #cuts off any values that are after the index 15 in "game"
    if len(vars.game)> 16:
        del vars.game[15:len(vars.game)-1]

def setupGame(): #prepares the game for the start
    #2/4 random modifiers
    modList = []
    for i in range(3):
        mod = random.randint(1,10)
        if mod == 1:
            modList.append(4)
        else:
            modList.append(2)

    #pick 3 random fields, there MUST be 3 fields picked.
    ran = [0, 0, 0]
    while ran[0]==ran[1] or ran[1]==ran[2] or ran[2]==ran[0]:
        ran = []
        for i in range(3):
            ran.append(random.randint(0,15))
    ran.sort()
    #setting the playfield
    for i in range(3):
        vars.game.insert(ran[i], int(modList[i]))
    shortenGame()

def addNum(): #adds a random 2 or 4 to a random free(value=0) space in "game"
    found = True
    for i in range(16): #check for softlock
        if vars.game[i]==0:
            found = False
    while found == False:
        select = random.randint(0,15)
        if vars.game[select]==0:
            found = True
            insert = random.randint(1,2)
            vars.game[select]= insert*2

def swipeUp(): #moves and merges numbers upwards
    for repeats in range(4):
        workingGame = []
        for i in range(4):
            vars.game.append(0)
        for i in range(1,5):
            for i2 in range(4):
                if vars.game[((i-1)*4)+i2]==0 and repeats!=2:
                    workingGame.append(vars.game[(i*4)+i2])
                    vars.game[(i*4)+i2] = 0
            
                elif vars.game[((i-1)*4)+i2]==vars.game[(i*4)+i2] and repeats ==2:
                    workingGame.append(vars.game[(i*4)+i2]*2)
                    vars.game[(i*4)+i2] = 0
                    vars.points = vars.points + vars.game[((i-1)*4)+i2]*2
            
                else:
                    workingGame.append(vars.game[((i-1)*4)+i2])
        vars.game = workingGame
    addNum()

def swipeLeft(): #rotates the game, calls "swipeUp()", and reverses the rotation
    orientation = [12, 8, 4, 0, 13, 9, 5, 1, 14, 10, 6, 2, 15, 11, 7, 3]
    workingGame = []
    for i in range(16):
        workingGame.append(vars.game[orientation[i]])
    vars.game = workingGame
    swipeUp()
    orientation.reverse()
    workingGame = []
    for i in range(16):
        workingGame.append(vars.game[orientation[i]])
    vars.game = workingGame

def swipeRight(): #rotates the game, calls "swipeUp()", and reverses the rotation
    orientation = [3, 7, 11, 15, 2, 6, 10, 14, 1, 5, 9, 13, 0, 4, 8, 12]
    workingGame = []
    for i in range(16):
        workingGame.append(vars.game[orientation[i]])
    vars.game = workingGame
    swipeUp()
    orientation.reverse()
    workingGame = []
    for i in range(16):
        workingGame.append(vars.game[orientation[i]])
    vars.game = workingGame

def swipeDown(): #inverts the game, calls "swipeUp()", and reverses the invertion
    orientation = [12, 13, 14, 15, 8, 9 ,10, 11, 4, 5, 6, 7, 0, 1, 2, 3]
    workingGame = []
    for i in range(16):
        workingGame.append(vars.game[orientation[i]])
    vars.game = workingGame
    swipeUp()
    workingGame = []
    for i in range(16):
        workingGame.append(vars.game[orientation[i]])
    vars.game = workingGame


#==========================Game Over detection==========================

def checkGameOver():
    workingShadow = vars.game
    workingShadow2 = vars.game
    didSomething = []
    if 0 in workingShadow:
        didSomething.append(1)
    for row in range(4):
        for i in range(3):
            if workingShadow[i+row*4] == workingShadow[i+1+row*4] or workingShadow[i+row*4] == 0:
                didSomething.append(1)
    for row in range(4):
        for i in range(1,4):
            if workingShadow[i+row*4] == workingShadow[i-1+row*4] or workingShadow[i-1+row*4] == 0:
                didSomething.append(1)
    
    orientation = [12, 8, 4, 0, 13, 9, 5, 1, 14, 10, 6, 2, 15, 11, 7, 3]
    workingShadow2 = []
    for i in range(16):
        workingShadow2.append(workingShadow[orientation[i]])
    
    workingShadow = workingShadow2
    
    for row in range(4):
        for i in range(3):
            if workingShadow[i+row*4] == workingShadow[i+1+row*4] or workingShadow[i+row*4] == 0:
                didSomething.append(1)
    for row in range(4):
        for i in range(1,4):
            if workingShadow[i+row*4] == workingShadow[i-1+row*4] or workingShadow[i-1+row*4] == 0:
                didSomething.append(1)
    
    if len(didSomething) == 0:
        result = True
    else:
        result = False
    return result