from tkinter import *
from pickle import dump , load

def pause_toggle():


def save_game(event):


def load_game(event):


def key_handler(event):


def set_status(status_text , color = 'black'):


def check_finish():


KEY_FORWARD1 = 39
KEY_FORWARD2 = 68
KEY_PAUSE = 19

game_width = 800
game_height = 500
game_over = False
pause = False

player_size = 100
SPEED = 12
x1,y1 = 50,50
x2,y2 = x1,y1 + player_size + 100
player1_color = 'red'
player2_color = 'blue'
x_finish = game_width - 50

window = Tk()
window.title('Догони меня, если сможешь')
canvas = Canvas (window, width=game_width, height=game_height,bg='white')


player1_id = canvas.create_rectangle(x1, y1, x1 + player_size, y1 + player_size,fill=player1_color)

player2_id = canvas.create_rectangle(x2, y2, x2 + player_size, y2 + player_size,fill=player2_color)

finish_id = canvas.create_rectangle(x_finish ,0 ,x_finish + 10, game_height, fill='black')

text_status_id = canvas.create_text(x1, game_height - 50, anchor=SW, font=('Arial', '25'),text='Вперед!')

canvas.pack()
window.bind('<KeyRelease>', key_handler)
window.bind('<Control-Key-s>', save_game)
window.bind('<Control-Key-o>', load_game)
window.mainloop()

