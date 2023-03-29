from microbit import *
import music
import audio
import audio as Sound
import random
import math

posX = 2
posY = 2
goalX = -1
goalY = -1
direction = 0

def go_right():
    global posX
    posX += 1

def go_down():
    global posY
    posY += 1

def go_left():
    global posX
    posX -= 1

def go_up():
    global posY
    posY -= 1

movements = [go_right, go_down, go_left, go_up]

def is_on_goal():
    global posX, posY, goalX, goalY
    return posX == goalX and posY == goalY

def shuffle():
    global posX, posY, goalX, goalY
    while True:
        goalX = random.randint(0, 4)
        goalY = random.randint(0, 4)
        if not is_on_goal():
            break

def get_distance(aX, aY, bX, bY):
    return math.sqrt((bX - aX)**2 + (bY - aY)**2 )

def playIntro():
    for i in range(3):
        for p in range(100,1000, 20):
            music.pitch(p)
            sleep(5)
    for p in range(100,4000, 30):
        music.pitch(p)
        sleep(5)
    music.stop()

def do_clock():
    for x in range(0, len(Image.ALL_CLOCKS)):
        display.show(Image.ALL_CLOCKS[x])
        sleep(20)
    display.show(Image.CLOCK12)
    sleep(20)
    display.clear()

playIntro()
do_clock()
shuffle()

while True:
    dist = get_distance(posX, posY, goalX, goalY) - 1
    brightness = 9 - (dist / 5.0) * 9
    display.set_pixel(posX, posY, int(brightness))
    if button_a.was_pressed():
        display.set_pixel(posX, posY, 0)
        movements[direction]()
    if button_b.was_pressed():
        direction += 1

    posX = max(0, min(posX, 4))
    posY = max(0, min(posY, 4))

    if direction >= len(movements):
        direction = 0

    if is_on_goal():
        display.show(Image.HAPPY)
        audio.play(Sound.HAPPY)
        sleep(500)
        do_clock()
        display.clear()
        shuffle()
