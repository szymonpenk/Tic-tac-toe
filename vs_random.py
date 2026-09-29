from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        buttons[row][column]['text'] = player
        
        if check_winner() is False:
            player = players[1]
            label.config(text=(players[1] + " turn"))
            computer_turn()
            
        elif check_winner() is True:
            label.config(text=(players[0] + " wins"))

        elif check_winner() == "Tie":
            label.config(text=("It's a tie"))

def computer_turn():
    global player

    if check_winner() is False:

        row = random.randint(0, 2)
        column = random.randint(0, 2)

        while buttons[row][column]['text'] != "":
            row = random.randint(0, 2)
            column = random.randint(0, 2)


        buttons[row][column]['text'] = player

        if check_winner() is False:
            player = players[0]
            label.config(text=(players[0] + " turn"))
            
        elif check_winner() is True:
            label.config(text=(players[1] + " wins"))

        elif check_winner() == "Tie":
            label.config(text=("It's a tie"))

def check_winner():
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            for i in range(3):
                buttons[row][i].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            for i in range(3):
                buttons[i][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        for i in range(3):
            buttons[i][i].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False

def new_game():
    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""
            buttons[row][column].config(bg="white")
    
    player = random.choice(players)

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)
buttons = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack()

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2, bg="white", command= lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

if player == players[1]: 
    computer_turn()

window.mainloop()

