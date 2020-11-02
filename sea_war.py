from tkinter import *
from tkinter import messagebox


tk = Tk()
app_run = True

size_canv_x = 800
size_canv_y = 800

def closing_window():
    pass

tk.protocol(WM_DELETE_WINDOW, closing_window)
tk.title("Sea  Buttle")
tk.resizable(0, 0)  # no change window
tk.wm_attributes("-topmost", 1)  # window will upper other windows


