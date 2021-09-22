import keyboard, mouse, time, datetime
from tkinter import *
from pyscreeze import pixel


def getPix(pos):
    while (True):
        try:
            pix = pixel(pos[0], pos[1])
            return (pix)
        except:
            print('pixGetErr, tryin again...')


def isGreen(p):
    if getPix(p) == (34, 142, 93): return True
    return False

def exec(vk):
    if(times[vk] is None):
        lbl.configure(text='Скрипт работает. (Вкладка #'+str(vk+1)+')')
        window.update()

        mouse.move(data[0][0], data[0][1], True, 0.1)
        mouse.click('left')

        time.sleep(0.3)

        keyboard.press_and_release('BACKSPACE')

        time.sleep(0.3)

        keyboard.write('2')

        time.sleep(0.3)

        mouse.move(data[1][0], data[1][1], True, 0.1)
        mouse.click('left')

        time.sleep(1)

        if(isGreen(data[2])):
            keyboard.press('F5')
            time.sleep(0.5)
            return()
        else:
            times[vk] = datetime.datetime.now()
            return()
    else:
        delta = datetime.datetime.now() - times[vk]
        if(delta.total_seconds() > 40):
            times[vk] = None
            mouse.move(ssilki[vk][0], ssilki[vk][1], True, 0.1)
            mouse.click('left')
            return()
        else:
            lbl.configure(text='Ожидаю покупку в '+str(vk+1)+' вкладке')
            window.update()
            time.sleep(1.0)
            return()

def cycleEnd():
    a = 3
    while (a > 0):
        lbl.configure(text='ESC - выход, F8 - пауза (' + str(a.__round__(1)) + 's)')
        window.update()
        if (keyboard.is_pressed('ESC')):
            lbl.destroy()
            exit(0)
        if (keyboard.is_pressed('F8')):
            lbl.configure(text='На паузе. F8 для продолжения работы.')
            lbl.update()
            time.sleep(0.3)
            while (not keyboard.is_pressed('F8')):
                lbl.update()
            time.sleep(0.3)
        a -= 0.1
        time.sleep(0.09)

window = Tk()
window.wm_attributes("-topmost", 1)
window.title('lolzScriptMenu')
window.geometry('400x50')
lbl = Label(window, text='Сколько окон необходимо поддерживать?')
lbl.grid(column=0, row=0)
window.update()

def clicked():
    global clicked
    clicked = True
    pass

btn = Button(window, text="->", command=clicked)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
btn.grid(column=2, row=0)
window.update()
clicked = False
while(not clicked):
    window.update()
windowcount = int(txt.get())
txt.grid_forget()
btn.grid_forget()

vkladki = []
ssilki = []
data = []
times = [None]*windowcount

for i in range(windowcount):
    lbl.configure(text='Вкладка #'+str(i+1)+ ' (пробел)')
    window.update()
    while True:
        window.update()
        if keyboard.is_pressed('space'):
            vkladki.append(mouse.get_position())
            lbl.configure(text="...")
            window.update()
            time.sleep(0.5)
            break
    lbl.configure(text='Ссылка #' + str(i + 1) + ' (пробел)')
    window.update()
    while True:
        window.update()
        if keyboard.is_pressed('space'):
            ssilki.append(mouse.get_position())
            lbl.configure(text="...")
            window.update()
            time.sleep(0.5)
            break

guitexts = ["окошко с вводом числа", "кнопка покупки", "зелёный цвет для проверки"]

for lp in range(3):
    lbl.configure(text=guitexts[lp] + " (пробел)")
    window.update()
    while True:
        window.update()
        if keyboard.is_pressed('space'):
            data.append(mouse.get_position())
            lbl.configure(text="...")
            window.update()
            time.sleep(0.5)
            break

lbl.configure(text="Ожидаю старта. (F8 - start, ESC - выйти из программы)")
while True:
    if keyboard.is_pressed('F8'): break
    if(keyboard.is_pressed('ESC')):
        lbl.destroy()
        exit(0)
    window.update()

while(True):
    for i in range(windowcount):
        mouse.move(vkladki[i][0], vkladki[i][1], True, 0.1)
        mouse.click('left')
        exec(i)
        time.sleep(2.0)
    cycleEnd()