#================================imports, checks and pre-configs================================
import threading, turtle, time, random, vars
print("misc.py: threading, turtle, time, random, vars(.py) were imported.")

t = turtle

try:
    from pynput import keyboard
    import pygame
    from pygame.locals import *
    t.forward(20)
except:
    from install import installModules
    print("misc.py: installModules was imported.")
    installModules("misc")
    from pynput import keyboard
    import pygame
    from pygame.locals import *
print("misc.py: keyboard, pygame have been imported.")

def saveScore():#saves the current score
    vars.scoreFile = open(vars.pathToSave, "w")
    vars.scoreFile.write(vars.high_score+" "+str(vars.high_score_points)+" "+cy(vars.high_score_points))
    vars.scoreFile.close()
    print("misc.py: Score was saved.")

def saveSettings():#saves the current settings
    vars.scoreFile = open(vars.pathToSettings, "w")
    vars.scoreFile.write(str(vars.music)+" "+str(vars.sound)+" "+str(vars.colors)+" "+str(vars.motion))
    vars.scoreFile.close()
    print("misc.py: Settings were saved.")


lastKey = ""
#looping thread

def keydet():#key input detection
    def on_press(key):
        try:
            global lastKey
            lastKey=('{0}'.format(
                key.char))
        except AttributeError:
            lastKey=('{0}'.format(
                key))

    def on_release(key):
        lastKey=('{0}'.format(
            key))
        return False

    while True: #keyboard press detection
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

def startKeyDetect():#starts "keydet()" in another thread
    thread = threading.Thread(target=keydet)
    thread.start()
    print("misc.py: NOTE: Key detection has been started.")

def gamepad():#gamepad initialisation and detection
    global lastKey
    pygame.init()
    pygame.joystick.init()
    print("misc.py: Connected and available gamepads have been initialized.")

    if pygame.joystick.get_count() > 0:
        gamepad = pygame.joystick.Joystick(0)
        gamepad.init()
    
    joystick_centered_x = True
    joystick_centered_y = True

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                import sys
                sys.exit()

            if event.type == JOYBUTTONDOWN:
                if event.button == 0:
                    lastKey = "Key.enter"
                elif event.button == 1:
                    lastKey = "Key.esc"
                elif event.button == 2:
                    lastKey = "s"
                elif event.button == 3:
                    lastKey = "t"
            
            if event.type == JOYAXISMOTION:
                if event.axis == 1:
                    if event.value < -0.5 and joystick_centered_y == True:
                        lastKey = "Key.up"
                        joystick_centered_y = False
                    elif event.value > 0.5 and joystick_centered_y == True:
                        lastKey = "Key.down"
                        joystick_centered_y = False
                    elif event.value > -0.3 and event.value < 0.3:
                        joystick_centered_y = True
                elif event.axis == 0:
                    if event.value < -0.5 and joystick_centered_x == True:
                        lastKey = "Key.left"
                        joystick_centered_x = False
                    elif event.value > 0.5 and joystick_centered_x == True:
                        lastKey = "Key.right"
                        joystick_centered_x = False
                    elif event.value > -0.3 and event.value < 0.3:
                        joystick_centered_x = True
        time.sleep(0.01)

def startGamepad():#starts "gamepad()" in another thread
    gp = threading.Thread(target=gamepad)
    gp.start()
    print("misc.py: NOTE: Gamepad detection has been started.")

def turtleTitle():#gives the turtle windows a title with some information during gameplay
    while True:
        while vars.gameOver== True:
            time.sleep(0.01)
            startime = round(time.time())
        
        currentTime = round(time.time())
        sec = (startime - currentTime)
        min = sec/60
        hrs = min/60
        sec = sec%60
        min = min%60
        hrs = hrs%24
        if sec == 0:
            sec = "00"
        if min == 0:
            min = "00"
        if hrs == 0:
            hrs = "00"
        t.title("2048 - Highscore: "+str(vars.high_score_points)+" - Time: "+str(hrs)+":"+str(min)+":"+str(sec))
        time.sleep(1)

def startTurtleTitle():#starts "turtleTitle()" in another thread
    thread = threading.Thread(target=turtleTitle)
    thread.start()
    print("misc.py: NOTE: Turtle window titler has been started.")

def cy(input1): #shhhhh! This is a secret!
    random.seed(input1)
    r = random.randint(1000000000000000, 9999999999999999)
    a = list(str(r))
    b = ""
    c = 0
    for i in range(19):
        if i==4 or i==9 or i==14:
            b = b + "-"
        else:
            b = b + a[c]
            c = c+1
    return b