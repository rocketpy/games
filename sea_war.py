import time
from tkinter import *
from tkinter import messagebox


tk = Tk()
app = True

size_canv_x = 500
size_canv_y = 500

def closing_window():
    global app
    if messagebox.askokcancel("Exit Game", "Do you want to exit ?"):
        app = False
        tk.destroy()
        

tk.protocol(WM_DELETE_WINDOW, closing_window)
tk.title("Sea  Buttle")
tk.resizable(0, 0)  # no change window
tk.wm_attributes("-topmost", 1)  # window will upper other windows

canvas = Canvas(tk, width=size_canv_x, height=size_canv_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canv_x, size_canv_y, fill="white")  # fill - white color field
canvas.pack()
tk.update()

while app:
    if app:
        tk.update_idletasks()
        tk.update()
        time.sleep(0.005)
