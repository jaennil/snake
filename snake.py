from tkinter import *
from random import randint
import time


def create_field():
    w = 20
    for i in range(row):
        array.append([])
        for j in range(col):
            array[i].append(
                canvas.create_rectangle(20 + j * w, 20 + i * w, 20 + (j + 1) * w, 20 + (i + 1) * w, fill=canvas_color))
            tk.update()
    return array


def up(event):
    global head
    global direction
    if head[0] == 0:
        print('Вы врезались в стену :/')
        game_over()
    elif not game_ended:
        direction.append('up')
        canvas.itemconfig(array[head[0]][head[1]], fill=canvas_color)
        head[0] -= 1
        canvas.itemconfig(array[head[0]][head[1]], fill=snake_color)
        if len(tail) > 1:
            is_in_tail()
            move_tail()
        tk.update()
        delete_and_create_eat()


def down(event):
    global head
    global direction
    if head[0] == row - 1:
        print('Вы врезались в стену :/')
        game_over()
    elif not game_ended:
        direction.append('down')
        canvas.itemconfig(array[head[0]][head[1]], fill=canvas_color)
        head[0] += 1
        canvas.itemconfig(array[head[0]][head[1]], fill=snake_color)
        if len(tail) > 1:
            is_in_tail()
            move_tail()
        tk.update()
        delete_and_create_eat()


def left(event):
    global head
    global direction
    if head[1] == 0:
        print('Вы врезались в стену :/')
        game_over()
    elif not game_ended:
        direction.append('left')
        canvas.itemconfig(array[head[0]][head[1]], fill=canvas_color)
        head[1] -= 1
        canvas.itemconfig(array[head[0]][head[1]], fill=snake_color)
        if len(tail) > 1:
            is_in_tail()
            move_tail()
        tk.update()
        delete_and_create_eat()


def right(event):
    global head
    global direction
    if head[1] == col - 1:
        print('Вы врезались в стену :/')
        game_over()
    elif not game_ended:
        direction.append('right')
        canvas.itemconfig(array[head[0]][head[1]], fill=canvas_color)
        head[1] += 1
        canvas.itemconfig(array[head[0]][head[1]], fill=snake_color)
        if len(tail) > 1:
            is_in_tail()
            move_tail()
        tk.update()
        delete_and_create_eat()


def delete_and_create_eat():
    if head[0] == eat[0] and head[1] == eat[1]:
        eat[0] = randint(0, row - 1)
        eat[1] = randint(0, col - 1)
        canvas.itemconfig(array[eat[0]][eat[1]], fill=eat_color)
        append_tail()
    if head[0] == eat[0] and head[1] == eat[1]:
        canvas.itemconfig(array[eat[0]][eat[1]], fill=snake_color)
        print('self pot spawn fixing')
        delete_and_create_eat()
    for i in range(0, len(tail), 2):
        if tail[i] == eat[0] and tail[i+1] == eat[1]:
            canvas.itemconfig(array[eat[0]][eat[1]], fill=snake_color)
            print('eat in tail fix')
            delete_and_create_eat()


def append_tail():
    global tail
    if len(tail) > 1:
        if direction[-(len(tail) // 2) - 1] == 'up':
            tail.append(0)
            tail.append(0)
            tail[-2] = tail[-4] + 1
            tail[-1] = tail[-3]
            canvas.itemconfig(array[tail[-2]][tail[-1]], fill=snake_color)
        elif direction[-(len(tail) // 2) - 1] == 'left':
            tail.append(0)
            tail.append(0)
            tail[-2] = tail[-4]
            tail[-1] = tail[-3] + 1
            canvas.itemconfig(array[tail[-2]][tail[-1]], fill=snake_color)
        elif direction[-(len(tail) // 2) - 1] == 'down':
            tail.append(0)
            tail.append(0)
            tail[-2] = tail[-4] - 1
            tail[-1] = tail[-3]
            canvas.itemconfig(array[tail[-2]][tail[-1]], fill=snake_color)
        elif direction[-(len(tail) // 2) - 1] == 'right':
            tail.append(0)
            tail.append(0)
            tail[-2] = tail[-4]
            tail[-1] = tail[-3] - 1
            canvas.itemconfig(array[tail[-2]][tail[-1]], fill=snake_color)
    else:
        if direction[-1] == 'up':
            tail.append(0)
            tail.append(0)
            tail[-2] = head[0] + len(tail) // 2
            tail[-1] = head[1]
            canvas.itemconfig(array[tail[-2]][tail[-1]], fill=snake_color)
        elif direction[-1] == 'left':
            tail.append(0)
            tail.append(0)
            tail[-2] = head[0]
            tail[-1] = head[1] + len(tail) // 2
            canvas.itemconfig(array[tail[-2]][tail[-1]], fill=snake_color)
        elif direction[-1] == 'down':
            tail.append(0)
            tail.append(0)
            tail[-2] = head[0] - len(tail) // 2
            tail[-1] = head[1]
            canvas.itemconfig(array[tail[-2]][tail[-1]], fill=snake_color)
        elif direction[-1] == 'right':
            tail.append(0)
            tail.append(0)
            tail[-2] = head[0]
            tail[-1] = head[1] - len(tail) // 2
            canvas.itemconfig(array[tail[-2]][tail[-1]], fill=snake_color)


def move_tail():
    global tail
    canvas.itemconfig(array[tail[-2]][tail[-1]], fill=canvas_color)
    if direction[-1] == 'up':
        tail[0] = head[0] + 1
        tail[1] = head[1]
        canvas.itemconfig(array[tail[0]][tail[1]], fill=snake_color)
    elif direction[-1] == 'left':
        tail[0] = head[0]
        tail[1] = head[1] + 1
        canvas.itemconfig(array[tail[0]][tail[1]], fill=snake_color)
    elif direction[-1] == 'down':
        tail[0] = head[0] - 1
        tail[1] = head[1]
        canvas.itemconfig(array[tail[0]][tail[1]], fill=snake_color)
    elif direction[-1] == 'right':
        tail[0] = head[0]
        tail[1] = head[1] - 1
        canvas.itemconfig(array[tail[0]][tail[1]], fill=snake_color)

    if len(tail) > 2:
        for i in range(2, len(tail), 2):
            if direction[-i // 2 - 1] == 'up':
                tail[i] = tail[i - 2] + 1
                tail[i + 1] = tail[i - 1]
                canvas.itemconfig(array[tail[i]][tail[i + 1]], fill=snake_color)
            elif direction[-i // 2 - 1] == 'left':
                tail[i] = tail[i - 2]
                tail[i + 1] = tail[i - 1] + 1
                canvas.itemconfig(array[tail[i]][tail[i + 1]], fill=snake_color)
            elif direction[-i // 2 - 1] == 'down':
                tail[i] = tail[i - 2] - 1
                tail[i + 1] = tail[i - 1]
                canvas.itemconfig(array[tail[i]][tail[i + 1]], fill=snake_color)
            elif direction[-i // 2 - 1] == 'right':
                tail[i] = tail[i - 2]
                tail[i + 1] = tail[i - 1] - 1
                canvas.itemconfig(array[tail[i]][tail[i + 1]], fill=snake_color)


def is_in_tail():
    for i in range(0, len(tail), 2):
        if head[0] == tail[i] and head[1] == tail[i + 1]:
            print('Вы врезались в собственный хвост :/')
            game_over()


def game_over():
    global game_ended
    game_ended = True
    for i in range(row):
        for j in range(col):
            canvas.itemconfig(array[i][j], fill=end_color)
            time.sleep(0.001)
            tk.update()


row = 32  # пример, работает с любыми значениями
col = 27  # пример, работает с любыми значениями
tk = Tk()
tk.title('ДубровскихНикита_Прог_ДЗ_Змейка')
tk.resizable(False, False)
game_ended = False
direction, array, tail = [], [], []
head = [randint(0, row - 1), randint(0, col - 1)]
eat = [randint(0, row - 1), randint(0, col - 1)]
eat_color = 'green'
snake_color = 'cyan'
canvas_color = 'yellow'
end_color = 'red'

canvas = Canvas(tk, width=(col + 2) * 20, height=(row + 2) * 20)
canvas.pack()

tk.bind('<w>', up)
tk.bind('<a>', left)
tk.bind('<s>', down)
tk.bind('<d>', right)

create_field()
canvas.itemconfig(array[head[0]][head[1]], fill=snake_color)
canvas.itemconfig(array[eat[0]][eat[1]], fill=eat_color)
tk.mainloop()
