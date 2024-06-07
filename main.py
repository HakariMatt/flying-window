from tkinter import Tk
from time import sleep
import random

window = Tk()

window.title('Bounce')
window.geometry('200x200')

WIDTH, HEIGHT = 1920, 1080
SCALE = 1.25  # CHANGE THIS TO YOUR SCREEN SCALE (Mine is 125%)
FPS = 60
TB = 72
COLORS = ['orchid2', 'pink', 'yellow1', 'green1', 'turquoise1', 'SteelBlue2']

def change_pos(x, y):
    window.geometry('+{}+{}'.format(x,y))


if __name__ == "__main__":
    window_size = 200 * SCALE
    window['bg'] = random.choice(COLORS)

    x, y = random.randint(0, int(WIDTH-window_size)), random.randint(0, int(HEIGHT-window_size))
    velx = vely = 5

    
    running = True
    while running:
        if x*SCALE + window_size >= WIDTH or x <= 0:
            window['bg'] = random.choice(COLORS)
            velx *= -1
        if y*SCALE + window_size >= HEIGHT or y <= 0:
            window['bg'] = random.choice(COLORS)
            vely *= -1

        x += velx
        y += vely

        # print(window.winfo_geometry())
        change_pos(x, y)
        window.update()
        sleep(1/FPS)

    window.mainloop()