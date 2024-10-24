
import tkinter as tk
from tkinter import filedialog
from tkinter import *

texter = "Over time, your typing speed improves naturally with regular use, but dedicated practice can help you get faster sooner. Tools like typing tests and speed drills are great ways to track your progress and challenge yourself to type quicker. Whether you're a student, a programmer, or someone who frequently writes, fast typing is a valuable asset in our fast-paced world."
reps = 60
def start():
    global reps
    if reps == 60:
        tester.config(text=texter)

        countdown(10)

        # elif secx == 0:
        # result(tester)

def result(text, check):
    score = 0
    text = text.split()
    check = check.split()
    for i in range(0,len(text)):
        if text[i] == check[i]:
            score += 1
    print("score",score)
    return score
def countdown(secx):
    global text

    canvas.itemconfig(time_text, text=secx)
    if secx > 0:
        x = window.after(1000, countdown, secx-1)
    elif secx == 0:
        user_int = text.get("1.0", "end-1c")
        sexy = result(user_int, texter)
        tester.config(text=f"Game over your score is {sexy}")



window=Tk()
window.title("Type tester")
# window.minsize(300, 300)
#
# # Set the maximum window size (width x height)
window.maxsize(700, 1000)
tester = Label(window, text="you will get 60 seconds to type as fast as you can.You will get marks based on number of words written in correctly. Test is not case sensitive.                                    start game ", wraplength=300)

tester.grid(row=0, column=0)

text = Text(window, bg="light cyan", width=50, height=10)
text.grid(column=0, row=1)

buto = Button(window, text="Start", command=start)
buto.grid(column=0, row=2)

canvas = Canvas(bg="red", width=40, height=20)
time_text = canvas.create_text(20, 10, text="60")
canvas.grid(row=0, column=3)
window.mainloop()
