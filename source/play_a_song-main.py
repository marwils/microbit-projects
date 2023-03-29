from microbit import *
import music

songs = [
    {
        'tempo': 120,
        'notes': ['g4:2', 'c5:2', 'c5:2', 'g5:2', 'g5:2', 'e5:2', 'e5:2', 'c5:2', 'c5:2', 'd5:2', 'd5:2', 'g4:2', 'g4:2', 'c5:2', 'c5:1', 'e5:1', 'g5:1']
    },
    {
        'tempo': 80,
        'notes': ['g4:2', 'c5:2', 'c5:2', 'c5:2', 'g4:2', 'c5:2', 'c5:2', 'c5:2', 'g4:2', 'd5:1', 'd5:1', 'd5:1', 'd5:1', 'd5:1', 'd5:1', 'e5:1', 'd5:1', 'c5:2', 'c5:2', 'c5:2']
    }
]

posX = 2

def play_song(idx):
    music.set_tempo(bpm=songs[idx]['tempo'])
    music.play(songs[idx]['notes'])

while True:
    display.set_pixel(posX, 2, 9)
    if button_a.was_pressed():
        display.set_pixel(posX, 2, 0)
        posX -= 1
    if button_b.was_pressed():
        display.set_pixel(posX, 2, 0)
        posX += 1

    if posX < 0:
        posX = 2
        display.show(Image.HOUSE)
        play_song(0)
        display.clear()

    if posX > 4:
        posX = 2
        display.show(Image.HAPPY)
        play_song(1)
        display.clear()
