import time
from tkinter import *
from tkinter import messagebox


tk = Tk()
app = True

size_canv_x = 500
size_canv_y = 500

s_x = s_y = 10  # size of cells , 10 * 10

step_x = size_canv_x // s_x
step_y = size_canv_y // s_y

# size_canv_x = step_x * s_x  # using this if change size of cells
# size_canv_y = step_y 8 s_y  # same

#  field for menu
menu_field_x = 250

def closing_window():
    global app
    if messagebox.askokcancel("Exit Game", "Do you want to exit ?"):
        app = False
        tk.destroy()
        

tk.protocol(WM_DELETE_WINDOW, closing_window)
tk.title("Sea  Buttle")
tk.resizable(0, 0)  # no change window
tk.wm_attributes("-topmost", 1)  # window will upper other windows

canvas = Canvas(tk, width=size_canv_x+menu_field_x, height=size_canv_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canv_x, size_canv_y, fill="white")  # fill - white color field
canvas.pack()
tk.update()

def create_table():
    for i in range(0, s_x + 1):
        canvas.create_line(step_x * i, 0, step_x * i, size_canv_y)
    for i in range(0, s_y + 1):
        canvas.create_line(0, step_y * i, size_canv_x, step_y * i)
        
create_table()

def show_enemy_ships():
    pass

def start_new_game():
    pass

btn_1 = Button(tk, text="Show enemy ships", command=show_enemy_ships)
btn_1.place(x=size_canv_x+20, y=30)
btn_2 = Button(tk, text="Start a new game", command=start_new_game)
btn_2.place(x=size_canv_x+20, y=70)

while app:
    if app:
        tk.update_idletasks()
        tk.update()
        time.sleep(0.005)
