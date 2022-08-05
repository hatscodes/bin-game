from tkinter import * 
game = Tk()

game.geometry('500x400')
game.title("bin game")

title = Label(game, text="bin game",)
title.config()
title.pack()

#button commands
def start_game_command() :
    win = Tk()
    win.mainloop()

def quit_command() :
    game.destroy()
    game.quit()

#buttons
start_game_button = Button(text="start game", padx = 50, command = start_game_command)
start_game_button.pack()

quit_game_button = Button(text="Quit", padx = 70, command = quit_command)
quit_game_button.config()
quit_game_button.pack()

game.mainloop()
