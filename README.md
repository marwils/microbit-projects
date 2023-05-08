# microbit-projects
A collection of small projects written in MicroPython to be run on micro:bit.

## Introduction
You'll need an micro:bit V2 to execute these projects. If you don't have a micro:bit, you could
visit https://python.microbit.org/ and run the code in the web emulator.

## Projects
A short description of the projects.

### baby_toy
A very simple project where only the default images and songs were accessed. This could also be a nice showcase for many of the built-in stuff. And yes, my 1,5 y/o daughter loves it. :D

- Button A: Show next image
- Button B: Play next song

### find_me_by_brightness
You are a spot on the 5x5 LED matrix and have to find a hidden target position. The brightness of the spot increases as you get closer to the target.

**Controls:**
- Button A: Move spot by one step
- Button B: Turn spot right

This is my very first micro:bit project.

### nicer_dicer
A dicing simulation that rolls a dice while the device is shaking. While rolling some random sounds are played. After that it changes it's eyes until it stops.

**Controls:**
- Shake: Roll dice
- Keep shaking: Accelerate dice

### play_a_song
Move a spot to the left or to the right to play a song.

**Controls:**
- Button A: Move left
- Button B: Move right

### spirit_level
A smooth visualization of the accelerometer's x and y position in form of a spot on the LED matrix. Nearby LEDs will also be affected when a given distance from the center of mass is exceeded.

**Controls:**
- Tilt: Move spot around
- Button A (hold): Decrease the maximal distance to nearby LED
- Button B (hold): Inrease the maximal distance to nearby LED
