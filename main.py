from tkinter import Tk, Label
from time import sleep
import random
from PIL import Image, ImageTk

window = Tk()

window.title('Bounce')
window.geometry('200x200')
window.resizable(False, False)
window.bind("<Escape>", lambda x: window.destroy())

WIDTH, HEIGHT = 1920, 1080
SCALE = 1.25  # CHANGE THIS TO YOUR SCREEN SCALE (Mine is 125%)
WINDOW_SIZE = 200
WINDOW_SIZE_SCALED = int(WINDOW_SIZE * SCALE)
FPS = 60
TASK_BAR = 48
TITLE_BAR = 32
COLORS = ['orchid2', 'pink', 'yellow1', 'green1', 'turquoise1', 'SteelBlue2']
PICS_R = [
    Image.open('img/0R.png').resize((WINDOW_SIZE, WINDOW_SIZE)),
    Image.open('img/1R.png').resize((WINDOW_SIZE, WINDOW_SIZE))
]
PICS_L = [
    Image.open('img/0L.png').resize((WINDOW_SIZE, WINDOW_SIZE)),
    Image.open('img/1L.png').resize((WINDOW_SIZE, WINDOW_SIZE))
]

def change_pos(x, y):
    window.geometry('+{}+{}'.format(x,y))

def chose_img(velx):
    if velx > 0:
        return(ImageTk.PhotoImage(random.choice(PICS_R)))
    else:
        return(ImageTk.PhotoImage(random.choice(PICS_L)))

if __name__ == "__main__":
    x, y = random.randint(0, int(WIDTH - (WINDOW_SIZE_SCALED*2))), random.randint(0, int(HEIGHT - (WINDOW_SIZE_SCALED*2)))
    velx = vely = random.choice([-5, 5])

    img = chose_img(velx)
    panel = Label(window, image=img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    # window['bg'] = random.choice(COLORS)


    
    running = True
    while running:
        if x*SCALE + WINDOW_SIZE_SCALED >= WIDTH or x <= 0:
            velx *= -1

            # window['bg'] = random.choice(COLORS)
            print(window.winfo_x()+WINDOW_SIZE)
            img = chose_img(velx)
            panel.config(image=img)

        if (y*SCALE + WINDOW_SIZE_SCALED + TITLE_BAR*SCALE) >= HEIGHT - TASK_BAR*SCALE or y <= 0:
            # window['bg'] = random.choice(COLORS)
            img = chose_img(velx)
            panel.config(image=img)
            vely *= -1

        x += velx
        y += vely

        # print(window.winfo_geometry())
        change_pos(x, y)
        window.update()
        sleep(1/FPS)

    window.mainloop()