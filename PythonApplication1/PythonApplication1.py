import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import random as rand
import pygame
from pygame import mixer

root = tk.Tk();
root.title("atom's dice app")

canvas = tk.Canvas(root, width = 400, height = 300, bg = "black")
canvas.pack()
canvas.create_rectangle(20, 20, 180, 180, outline="white", width=2)
canvas.create_rectangle(220, 20, 380, 180, outline="white", width=2)

mixer.init()
def playSound():
    mixer.music.load("diceRoll.wav")
    mixer.music.play()

def getImage(imgVal):
    img = Image.open(f"dice{imgVal}.png")
    img = img.resize((155, 155))
    tk_img = ImageTk.PhotoImage(img)
    return tk_img


def getValue():
    value3 = rand.randint(1,6)
    return value3

def dot(x, y):
    canvas.create_oval(x-10, y-10, x+10, y+10, fill="pink")

positions = {
        "center1": (100,100),
        "center2": (300,100),
        "topLeft1": (50,50),
        "topLeft2": (250,50),
        "topRight1": (150,50),
        "topRight2": (350,50),
        "bottomLeft1": (50,150),
        "bottomLeft2": (250,150),
        "bottomRight1": (150,150),
        "bottomRight2": (350,150),
        "centerLeft1": (50,100),
        "centerLeft2": (250,100),
        "centerRight1": (150,100),
        "centerRight2": (350,100),
    }    

def draw_dice1(value):
    if value == 1:
        dot(*positions["center2"])
        #l.place(x=20, y=20)

    if value == 2:

        dot(*positions["topLeft2"])
        dot(*positions["bottomRight2"])

    if value == 3:
        dot(*positions["topLeft2"])
        dot(*positions["center2"])
        dot(*positions["bottomRight2"])

    if value == 4:
        dot(*positions["topLeft2"])
        dot(*positions["topRight2"])
        dot(*positions["bottomLeft2"])
        dot(*positions["bottomRight2"])

    if value == 5:
        dot(*positions["topLeft2"])
        dot(*positions["topRight2"])
        dot(*positions["center2"])
        dot(*positions["bottomLeft2"])
        dot(*positions["bottomRight2"])

    if value == 6:
        dot(*positions["topLeft2"])
        dot(*positions["topRight2"])
        dot(*positions["centerLeft2"])
        dot(*positions["centerRight2"])
        dot(*positions["bottomLeft2"])
        dot(*positions["bottomRight2"])

def draw_dice2(value):
    if value == 1:
        dot(*positions["center1"])

    if value == 2:
        dot(*positions["topLeft1"])
        dot(*positions["bottomRight1"])

    if value == 3:
        dot(*positions["topLeft1"])
        dot(*positions["center1"])
        dot(*positions["bottomRight1"])

    if value == 4:
        dot(*positions["topLeft1"])
        dot(*positions["topRight1"])
        dot(*positions["bottomLeft1"])
        dot(*positions["bottomRight1"])

    if value == 5:
        dot(*positions["topLeft1"])
        dot(*positions["topRight1"])
        dot(*positions["center1"])
        dot(*positions["bottomLeft1"])
        dot(*positions["bottomRight1"])

    if value == 6:
        dot(*positions["topLeft1"])
        dot(*positions["topRight1"])
        dot(*positions["centerLeft1"])
        dot(*positions["centerRight1"])
        dot(*positions["bottomLeft1"])
        dot(*positions["bottomRight1"])

def drawImg1(value):
    img = getImage(value)
    l.config(image=img)
    l.image = img   
    l.place(x=20, y=20)

def drawImg2(value):
    img = getImage(value)
    l2.config(image=img)
    l2.image = img  
    l2.place(x=220, y=20)

def rollDice():
    canvas.delete("all")
    l.place_forget()
    l2.place_forget()

    canvas.create_rectangle(20, 20, 180, 180, outline="white", width=2)
    canvas.create_rectangle(220, 20, 380, 180, outline="white", width=2)

    value1 = getValue()
    value2 = getValue()

    #draw_dice1(value1)
    #draw_dice2(value2)

    drawImg1(value1)
    drawImg2(value2)

    print(value1)
    print(value2)
    print("")

    playSound()

    if value1 > value2:
        print("1 wins")
        print("")

        canvas.create_text(
            200, 210, 
            text="One Wins!", 
            fill="pink", 
            font=("Helvetica", 24, "bold")
        )

    elif value1 < value2:
        print("2 wins")
        print("")

        canvas.create_text(
            200, 210, 
            text="Two Wins!", 
            fill="pink", 
            font=("Helvetica", 24, "bold")
        )

    else:
        canvas.create_text(
            200, 210, 
            text="Tie!", 
            fill="pink", 
            font=("Helvetica", 24, "bold")
        )

        print("")
        print("tie")

    canvas.create_window(200, 250, window=button)

button = tk.Button(root,
                   text = "Roll Dice",
                   command = rollDice)

canvas.create_window(200, 250, window=button)

img = Image.open("dice1.png")
img = img.resize((155, 155))  # width, height

tk_img = ImageTk.PhotoImage(img)
l = tk.Label(image=tk_img)
l2 = tk.Label(image=tk_img)

root.mainloop()