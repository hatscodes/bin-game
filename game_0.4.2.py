from tkinter import * 
game_title_screen = Tk()
game_title_screen.geometry('700x650')
game_title_screen.title("bin game")
title = Label(game_title_screen, text="bin game",)
title.config()
title.pack()
#button commands

def start_game_command() :
     game = Tk()
     game.title("")
     game.geometry('700x650')
     input_box = Text(game, height = 1)
     input_box.pack()
     
     def back_out() :
         game.destroy()
         game.quit()   
     start_button = Button(game, text="start", command=game_a)
     start_button.pack()
     back_button = Button(game,text="title screen", command = back_out,)
     back_button.pack()
     game.mainloop()
def quit_command() :
    sure = Tk()
    sure_screen = Label(sure, text = "are you sure you want to quit")
    sure_screen.pack()
    sure.geometry('200x85')
    def yes_funtion() :
        sure.destroy()
        game_title_screen.destroy()
    def no_funtion() :
        sure.destroy()
    yes_button =  Button(sure, text = "yes", command = yes_funtion)
    yes_button.pack()
    no_button = Button(sure, text = "no", command = no_funtion)
    no_button.pack()
    sure.mainloop()
#buttons
start_game_button = Button(text="start game", padx = 50, command = start_game_command)
start_game_button.pack()

quit_game_button = Button(text="Quit", padx = 70, command = quit_command)
quit_game_button.config()
quit_game_button.pack()

def game_a() :
    error = Tk()
    error_404 = Label(error,text="work in progress")
    error_404.pack()
    error.pack()

game_title_screen.mainloop()
