from tkinter import Tk, Label
from time import sleep
import random
from PIL import Image, ImageTk
import argparse
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame.mixer as pmixer


parser = argparse.ArgumentParser()
parser.add_argument('--resolution', type=str, required=True,
                    help='Screen resolution in the format WIDTHxHEIGHT (e.g., 1920x1080)')
parser.add_argument('--scale', type=float, default=1.0,
                    help='UI scale (e.g., 1.0, 1.25, 2.0)')
parser.add_argument('--super', action='store_true',
                    help='Enable Super Hime')
args = parser.parse_args()


window = Tk()
pmixer.init()


window.title('Hime')
window.geometry('200x200')
window.resizable(False, False)
window.bind("<Escape>", lambda x: window.destroy())


# constants 
WIDTH, HEIGHT = map(int, args.resolution.split('x'))
SCALE = args.scale
VOLUME = 0.5
IS_SUPER = args.super
MOVE_SPD = 4 if IS_SUPER else random.randint(1, 2)
WINDOW_SIZE = 200
WINDOW_SIZE_SCALED = int(WINDOW_SIZE * SCALE)
FPS = 60
TASK_BAR = 48
TITLE_BAR = 32
PICS_R = [
    Image.open('img/0R.png').resize((WINDOW_SIZE, WINDOW_SIZE)),
    Image.open('img/1R.png').resize((WINDOW_SIZE, WINDOW_SIZE))
]
PICS_L = [
    Image.open('img/0L.png').resize((WINDOW_SIZE, WINDOW_SIZE)),
    Image.open('img/1L.png').resize((WINDOW_SIZE, WINDOW_SIZE))
]
SUPER_HIME = [
    Image.open('img/2R.png').resize((WINDOW_SIZE, WINDOW_SIZE)),
    Image.open('img/2L.png').resize((WINDOW_SIZE, WINDOW_SIZE))
]
SOUNDS = [
    'sounds/1.mp3',
    'sounds/2.mp3',
    'sounds/3.mp3',
    'sounds/4.mp3',
    'sounds/5.mp3',
    'sounds/6.mp3',
    'sounds/7.mp3',
    'sounds/8.mp3',
    'sounds/9.mp3',
    'sounds/10.mp3',
    'sounds/11.mp3',
    'sounds/12.mp3',
    'sounds/13.mp3',
    'sounds/14.mp3',
    'sounds/15.mp3',
    'sounds/16.mp3'
]


def change_pos(x, y):
    window.geometry(f'+{int(x/SCALE)-8}+{int(y/SCALE)}')


def random_choice_no_repeat(options, last_choice):
    # Filter out the last choice if it exists and there are other options available
    available_options = [option for option in options if option != last_choice] if last_choice in options else options
    return random.choice(available_options) if available_options else last_choice


def chose_img(velx, last_img, super: bool):
    if super:
        return SUPER_HIME[0] if velx > 0 else SUPER_HIME[1]
    else:
        return random_choice_no_repeat(PICS_R if velx > 0 else PICS_L, last_img)


def play(sound):
    pmixer.music.load(sound)
    pmixer.music.set_volume(VOLUME)
    pmixer.music.play(loops=0)


if __name__ == "__main__":
    x, y = random.randint(0, int(WIDTH - (WINDOW_SIZE_SCALED*2))), random.randint(0, int(HEIGHT - (WINDOW_SIZE_SCALED*2)))
    velx = vely = random.choice([-2, 2])
    last_sound = None

    last_img = chose_img(velx, None, IS_SUPER)
    img = ImageTk.PhotoImage(last_img)
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    
    running = True
    while running:
        if x + WINDOW_SIZE_SCALED >= WIDTH or x <= 0:
            velx *= -1
            last_img = chose_img(velx, last_img, IS_SUPER)
            img = ImageTk.PhotoImage(last_img)
            panel.config(image=img)
            last_sound = random_choice_no_repeat(SOUNDS, last_sound)
            play(last_sound)

        if (y + WINDOW_SIZE_SCALED + TITLE_BAR*SCALE) >= HEIGHT - TASK_BAR*SCALE or y <= 0:
            vely *= -1
            last_img = chose_img(velx, last_img, IS_SUPER)
            img = ImageTk.PhotoImage(last_img)
            panel.config(image=img)
            last_sound = random_choice_no_repeat(SOUNDS, last_sound)
            play(last_sound)

        x += velx * MOVE_SPD
        y += vely * MOVE_SPD

        change_pos(x, y)
        window.update()
        sleep(1/FPS)

    window.mainloop()
