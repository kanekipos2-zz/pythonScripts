import pkgutil
from tkinter import filedialog, messagebox
from tkinter import *
import os
from tkinter.ttk import Combobox
from shutil import copytree

def askPath():
    def clicked():
        path = filedialog.askdirectory()
        if (path.endswith('Steam')):
            global p
            p = path
            window.destroy()
        else: txt.configure(text="Its not a steam folder, try again...")
    window = Tk()
    window.title("path?")
    window.geometry('220x25')
    window.resizable(0, 0)
    btn = Button(window, text="path", command=clicked)
    btn.grid(column=0, row=0)
    txt = Label(window, text="Select steam folder...")
    txt.grid(column=1, row=0)
    window.mainloop()
    return(p)

def getPath():
    if os.path.exists('C:/Program Files (x86)/Steam'):
        return 'C:/Program Files (x86)/Steam'
    else:
        return askPath()

def copyCFG():
    global idFrom, idTo, path, ids, window
    path += '/userdata/'
    if not idFrom.get() or not idTo.get() or not idFrom.get() in ids or not idTo.get() in ids:
        messagebox.showerror('err', 'u selected wrong id')
    else:
        for i in ['/7/', '/570/', '/config/', '/ugc/', '/ugcmsgcache/']:
            try:
                copytree(path+idFrom.get()+i, path+idTo.get()+i, dirs_exist_ok=True)
            except PermissionError:
                messagebox.showerror("cfgTransmittor by kanekipos2", "Permission denied!")
                return

        messagebox.showinfo('cfgTransmittor by kanekipos2', 'Success!')
        window.destroy()


path = getPath()
ids = os.listdir(path + '/userdata')

window = Tk()
window.title("cfgTransmittor by kanekipos2")
window.geometry('400x60')
window.resizable(0, 0)

Label(window, text="copy from").grid(column=0, row=0)
Label(window, text="to").grid(column=1, row=0)

idFrom = Combobox(window)
idFrom['values'] = ids
idFrom.grid(column=0, row=1, padx = 8)

idTo = Combobox(window)
idTo['values'] = ids
idTo.grid(column=1, row=1, padx = 8)

eButton = Button(window, text="execute", command=copyCFG).grid(column=2, row=1, padx = 8)

window.mainloop()

