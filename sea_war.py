import time
import random
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

menu_field_x = 250  #  field for menu

ships = s_x // 2  # max quant 

ship_type_1 = s_x // 5
ship_type_2 = s_x // 3
ship_type_3 = s_x // 2

enemy_ships = [[0 for i in range(s_x+1)] for i in range(s_x+1)]

list_ids = []

def closing_window():
    global app
    if messagebox.askokcancel("Exit", "Do you want to exit ?"):
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
    for i in range(0, s_x):
        for j in range(0, s_y):
            if enemy_ships[j][i] > 0:
                _id = canvas.create_rectangle(i * step_x, j * step_y, i * step_x + step_x, j * step_y + step_y, fill="red")
                list_ids.append(_id)
    
def start_new_game():
    global list_ids
    for i in list_ids:
        canvas.delete(i)
    list_ids = []
        
btn_1 = Button(tk, text="Show enemy ships", command=show_enemy_ships)
btn_1.place(x=size_canv_x+20, y=30)
btn_2 = Button(tk, text="Start a new game", command=start_new_game)
btn_2.place(x=size_canv_x+20, y=70)

def add_all(event):
    _type = 0
    if event.num == 3:
        _type = 1
        
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    
    cell_x = mouse_x // step_x
    cell_y = mouse_y // step_y
    
canvas.bind_all("<Button-1>", add_all)  # left mouse button
canvas.bind_all("<Button-3>", add_all)  # right mouse button

def gen_enemy_ships():
    global enemy_ships
    list_ships = []
    for i in range(0, ships):
        list_ships.append(random.choice([ship_type_1, ship_type_2, ship_type_3]))

    sum_all_ships = sum(list_ships)
    sum_enemy_ships = 0
    
    while sum_enemy_ships != sum_all_ships:
        enemy_ships = [[0 for i in range(s_x + 1)] for i in
                       range(s_y + 1)]  

        for i in range(0, ships):
            len = ships_list[i]
            horizont_vertikal = random.randrange(1, 3) 

            primerno_x = random.randrange(0, s_x)
            if primerno_x + len > s_x:
                primerno_x = primerno_x - len

            primerno_y = random.randrange(0, s_y)
            if primerno_y + len > s_y:
                primerno_y = primerno_y - len

            if horizont_vertikal == 1:
                if primerno_x + len <= s_x:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y][primerno_x - 1] + \
                                               enemy_ships[primerno_y][primerno_x + j] + \
                                               enemy_ships[primerno_y][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j]
                            # print(check_near_ships)
                            if check_near_ships == 0: 
                                enemy_ships[primerno_y][primerno_x + j] = i + 1  
                        except Exception:
                            pass
            if horizont_vertikal == 2:
                if primerno_y + len <= s_y:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y - 1][primerno_x] + \
                                               enemy_ships[primerno_y + j][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x - 1] + \
                                               enemy_ships[primerno_y + j][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j][primerno_x - 1]
                            
                            if check_near_ships == 0:  
                                enemy_ships[primerno_y + j][primerno_x] = i + 1  
                        except Exception:
                            pass

        sum_1_enemy = 0
        for i in range(0, s_x):
            for j in range(0, s_y):
                if enemy_ships[j][i] > 0:
                    sum_1_enemy = sum_1_enemy + 1
        
gen_enemy_ships()    
    
while app:
    if app:
        tk.update_idletasks()
        tk.update()
        time.sleep(0.005)
