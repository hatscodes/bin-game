from tkinter import * 
game_title_screen = Tk()
game_title_screen.geometry('500x400')
game_title_screen.title("bin game")
title = Label(game_title_screen, text="bin game",)
title.config()
title.pack()
#button commands
def start_game_command() :
     game = Tk()
     game.title("")
     game.geometry('700x650')
     
     game.mainloop()
def quit_command() :
    game_title_screen.destroy()
    game_title_screen.quit()
#buttons
start_game_button = Button(text="start game", padx = 50, command = start_game_command)
start_game_button.pack()

quit_game_button = Button(text="Quit", padx = 70, command = quit_command)
quit_game_button.config()
quit_game_button.pack()

game_title_screen.mainloop()
