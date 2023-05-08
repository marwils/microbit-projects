from microbit import *
import random
import music

numbers = {
    1: Image("00000:"
             "00000:"
             "00900:"
             "00000:"
             "00000"),
    2: Image("00000:"
             "00000:"
             "90009:"
             "00000:"
             "00000"),
    3: Image("00009:"
             "00000:"
             "00900:"
             "00000:"
             "90000"),
    4: Image("90009:"
             "00000:"
             "00000:"
             "00000:"
             "90009"),
    5: Image("90009:"
             "00000:"
             "00900:"
             "00000:"
             "90009"),
    6: Image("90009:"
             "00000:"
             "90009:"
             "00000:"
             "90009")
}

notes = ['c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4', 'c5', 'd5', 'e5']

def dice():
    velocity = 20
    number = 0
    last_number = 0
    note = ''
    last_note = ''
    while (velocity < 400):
        sleep(velocity)

        while (last_note == note):
            note = notes[random.randint(0, len(notes)-1)]
        last_note = note

        music.play(note, wait=False)

        while (last_number == number):
            number = random.randint(1, 6)
        last_number = number

        display.show(numbers[number])

        if accelerometer.is_gesture('shake'):
            velocity /= 2
            if velocity < 20:
                velocity = 20
        else:
          velocity *= 1.2

    music.play(music.BA_DING)

while True:
    if accelerometer.is_gesture('shake'):
        dice()
