from microbit import *
import music

# All built-in images
ALL_IMAGES = [
    Image.HEART,
    Image.HEART_SMALL,
    Image.HAPPY,
    Image.SMILE,
    Image.SAD,
    Image.CONFUSED,
    Image.ANGRY,
    Image.ASLEEP,
    Image.SURPRISED,
    Image.SILLY,
    Image.FABULOUS,
    Image.MEH,
    Image.YES,
    Image.NO,
    Image.CLOCK12,
    Image.CLOCK11,
    Image.CLOCK10,
    Image.CLOCK9,
    Image.CLOCK8,
    Image.CLOCK7,
    Image.CLOCK6,
    Image.CLOCK5,
    Image.CLOCK4,
    Image.CLOCK3,
    Image.CLOCK2,
    Image.CLOCK1,
    Image.ARROW_N,
    Image.ARROW_NE,
    Image.ARROW_E,
    Image.ARROW_SE,
    Image.ARROW_S,
    Image.ARROW_SW,
    Image.ARROW_W,
    Image.ARROW_NW,
    Image.TRIANGLE,
    Image.TRIANGLE_LEFT,
    Image.CHESSBOARD,
    Image.DIAMOND,
    Image.DIAMOND_SMALL,
    Image.SQUARE,
    Image.SQUARE_SMALL,
    Image.RABBIT,
    Image.COW,
    Image.MUSIC_CROTCHET,
    Image.MUSIC_QUAVER,
    Image.MUSIC_QUAVERS,
    Image.PITCHFORK,
    Image.XMAS,
    Image.PACMAN,
    Image.TARGET,
    Image.TSHIRT,
    Image.ROLLERSKATE,
    Image.DUCK,
    Image.HOUSE,
    Image.TORTOISE,
    Image.BUTTERFLY,
    Image.STICKFIGURE,
    Image.GHOST,
    Image.SWORD,
    Image.GIRAFFE,
    Image.SKULL,
    Image.UMBRELLA,
    Image.SNAKE,
    Image.SCISSORS,
]

# All built-in songs
ALL_SONGS = [
    music.BA_DING,
    music.BADDY,
    music.BIRTHDAY,
    music.BLUES,
    music.CHASE,
    music.DADADADUM,
    music.ENTERTAINER,
    music.FUNERAL,
    music.FUNK,
    music.JUMP_DOWN,
    music.JUMP_UP,
    music.NYAN,
    music.ODE,
    music.POWER_DOWN,
    music.POWER_UP,
    music.PRELUDE,
    music.PUNCHLINE,
    music.PYTHON,
    music.RINGTONE,
    music.WAWAWAWAA,
    music.WEDDING,
]

display.show(ALL_IMAGES[0])

current_image = 1
current_song = 0

while True:
    if button_a.was_pressed():
        display.show(ALL_IMAGES[current_image])
        current_image += 1
        if current_image >= len(ALL_IMAGES):
            current_image = 0

    if button_b.was_pressed():
        music.play(ALL_SONGS[current_song], wait=False)
        current_song += 1
        if current_song >= len(ALL_SONGS):
            current_song = 0

    sleep(100)
