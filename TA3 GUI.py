from tkinter import *
import random

root = Tk()
root.title("Guess The Number")
root.geometry("400x400")

msgLabel = Label(root)
input=Entry(root)
guessBtn = Button(root)

r = random.randint(1,100)
chances = 3

def check():
    global chances
    chances = chances - 1
    number = int(input.get())
    print(number, r)
    if(number!=r):
            if(number<r):
                outputLabel["text"]="Guess a bigger number"
                input.delete(0, END)
            else:
                outputLabel["text"]="Guess a smaller number"
                input.delete(0, END)
    else:
            outputLabel["text"]="You guessed it right. Congrats!"
            guessBtn.destroy()
            win=1

    if chances==0 and win==0:
        outputLabel["text"]="You lost! Try again!"
        guessBtn.destroy()

def create():
    global msgLabel
    global input
    global guessBtn

    msgLabel = Label(root,text="Enter your guess")
    msgLabel.place(relx=0.2, rely=0.3,anchor=CENTER)

    input=Entry(root)
    input.place(relx=0.6, rely=0.3,anchor=CENTER)

    guessBtn = Button(root,text="Check", command=check)
    guessBtn.place(relx=0.85, rely=0.3,anchor=CENTER)


def start():
    create()
    startButton.destroy()

    
titleLabel = Label(root, text="Guess the Number")
titleLabel.place(relx=0.5, rely=0.1,anchor=CENTER) 

startButton = Button(root, text="Start", command = start)
startButton.place(relx=0.5, rely=0.4,anchor=CENTER)

outputLabel = Label(root, text="")
outputLabel.place(relx=0.5, rely=0.5,anchor=CENTER) 


root.mainloop()
