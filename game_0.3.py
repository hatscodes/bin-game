from tkinter import * 
game = Tk()

game.geometry('500x400')
game.title("bin game")

title = Label(game, text="bin game")
title.pack()

button = Button(text="yes")
button.pack()
game.mainloop()
