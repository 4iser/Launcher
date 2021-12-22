import tkinter
from tkinter import *
from subprocess import call


def open_snake():
    call(["python", "snake.py"])


def open_flappy():
    call(["python", "flappy.py"])


def open_pac():
    call(["python", "PacManGui.py"])


def open_econ():
    call(["python", "base/econ/econ_game.py"])


def open_tik():
    call(["python", "base/tikTak/Tic_Tac_Toe_Game.py"])


root= Tk()
root.geometry('400x600')
btn1 = tkinter.Button(root, text='Змейка', command=open_snake, width=12, height=6)
btn1.pack(pady=10)
btn2 = tkinter.Button(root, text='Flappy Bird', command=open_flappy, width=12, height=6)
btn2.pack(pady=10)
btn3 = tkinter.Button(root, text='PacMan', command=open_pac, width=12, height=6)
btn3.pack(pady=10)
btn4 = tkinter.Button(root, text='Economy Game', command=open_econ, width=12, height=6)
btn4.pack(pady=10)
btn5 = tkinter.Button(root, text='X and 0', command=open_tik, width=12, height=6)
btn5.pack(pady=10)
root.mainloop()
root.title("МНОГОИГРОВОЧКА")
root.mainloop()