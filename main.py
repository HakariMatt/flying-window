from tkinter import Tk, Label
from time import sleep
import random
from PIL import Image, ImageTk
import pygame as pg


# Set your screen resolution and UI scale of your windows.
# You can check it in Settings -> System -> Display -> Scale
# If it's 100% leave it as 1, 125% = 1.25 and so on.
WIDTH, HEIGHT = 1920, 1080
SCALE = 1



window = Tk()
pg.mixer.init()

window.title('Hime')
window.geometry('200x200')
window.resizable(False, False)
window.bind("<Escape>", lambda x: window.destroy())


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
SOUNDS = [
    'sounds/1.mp3',
    'sounds/2.mp3',
    'sounds/3.mp3',
    'sounds/4.mp3',
    'sounds/5.mp3',
    'sounds/6.mp3',
    'sounds/7.mp3',
]


def change_pos(x, y):
    window.geometry('+{}+{}'.format(x,y))


def chose_img(velx):
    if velx > 0:
        return(ImageTk.PhotoImage(random.choice(PICS_R)))
    else:
        return(ImageTk.PhotoImage(random.choice(PICS_L)))


def play():
    pg.mixer.music.load(random.choice(SOUNDS))
    pg.mixer.music.play(loops=0)


if __name__ == "__main__":
    x, y = random.randint(0, int(WIDTH - (WINDOW_SIZE_SCALED*2))), random.randint(0, int(HEIGHT - (WINDOW_SIZE_SCALED*2)))
    velx = vely = random.choice([-2, 2])

    img = chose_img(velx)
    panel = Label(window, image=img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    
    running = True
    while running:
        if x*SCALE + WINDOW_SIZE_SCALED >= WIDTH or x <= 0:
            velx *= -1
            img = chose_img(velx)
            panel.config(image=img)
            play()

        if (y*SCALE + WINDOW_SIZE_SCALED + TITLE_BAR*SCALE) >= HEIGHT - TASK_BAR*SCALE or y <= 0:
            vely *= -1
            img = chose_img(velx)
            panel.config(image=img)
            play()

        x += velx
        y += vely

        change_pos(x, y)
        window.update()
        sleep(1/FPS)

    window.mainloop()
