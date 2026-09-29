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

    if player == players[1] and check_winner() is False:

        window.update()

        move = get_computer_move()
        row = move[0]
        column = move[1]

        buttons[row][column]['text'] = player

        if check_winner() is False:
            player = players[0]
            label.config(text=(players[0] + " turn"))
            
        elif check_winner() is True:
            label.config(text=(players[1] + " wins"))

        elif check_winner() == "Tie":
            label.config(text=("It's a tie"))

def get_computer_move():
    global player

    computer_win = can_win('computer')
    player_can_win = can_win('player')

    if computer_win[0] == True:
        return computer_win[1]
    
    elif player_can_win[0] == True:
        return player_can_win[1]
    
    else:

        row = random.randint(0, 2)
        column = random.randint(0, 2)

        while buttons[row][column]['text'] != "":
            row = random.randint(0, 2)
            column = random.randint(0, 2)

        return [row, column]

def can_win(who):

    if who == 'computer':

        for i in range (3):
            for j in [0, 2]:
                if buttons[i][1]['text'] == player and buttons[i][j]['text'] == player:
                    if j == 0: 
                        if buttons[i][2]['text'] == "":
                            return [True, [i, 2]]
                    else:
                        if buttons[i][0]['text'] == "":
                            return [True, [i, 0]]
            
            if buttons[i][0]['text'] == player and buttons[i][2]['text'] == player:
                if buttons[i][1]['text'] == "":
                    return [True, [i, 1]]
            
        for i in range (3):
            for j in [0, 2]:
                if buttons[1][i]['text'] == player and buttons[j][i]['text'] == player:
                    if j == 0: 
                        if buttons[2][i]['text'] == "":
                            return [True, [2, i]]
                    else:
                        if buttons[0][i]['text'] == "":
                            return [True, [0, i]]
            
            if buttons[0][i]['text'] == player and buttons[2][i]['text'] == player:
                if buttons[i][1]['text'] == "":
                    return [True, [i, 1]]
            
        if buttons[0][0]['text'] == player and buttons[2][2]['text'] == player:
            if buttons[1][1]['text'] == "":
                return [True, [1, 1]]
        
        elif buttons[0][2]['text'] == player and buttons[2][0]['text'] == player:
            if buttons[1][1]['text'] == "":
                return [True, [1, 1]]
        
        for i in [0, 2]:
            for j in [0, 2]:
                if buttons[i][j]['text'] == player and buttons[1][1]['text'] == player:
                    if i == 0 and j == 0:
                        if buttons[2][2]['text'] == "":
                            return [True, [2, 2]]
                    elif i == 0 and j == 2:
                        if buttons[2][0]['text'] == "":
                            return [True, [2, 0]]
                    elif i == 2 and j == 0:
                        if buttons[0][2]['text'] == "":
                            return [True, [0, 2]]
                    elif i == 2 and j == 2:
                        if buttons[0][0]['text'] == "":
                            return [True, [0, 0]]
        
    elif who == 'player':

        for i in range (3):
            for j in [0, 2]:
                if buttons[i][1]['text'] == players[0] and buttons[i][j]['text'] == players[0]:
                    if j == 0: 
                        if buttons[i][2]['text'] != player:
                            return [True, [i, 2]]
                    else:
                        if buttons[i][0]['text'] != player:
                            return [True, [i, 0]]
            
            if buttons[i][0]['text'] == players[0] and buttons[i][2]['text'] == players[0]:
                if buttons[i][1]['text'] != player:
                    return [True, [i, 1]]
            
        for i in range (3):
            for j in [0, 2]:
                if buttons[1][i]['text'] == players[0] and buttons[j][i]['text'] == players[0]:
                    if j == 0: 
                        if buttons[2][i]['text'] != player:
                            return [True, [2, i]]
                    else:
                        if buttons[0][i]['text'] != player:
                            return [True, [0, i]]
            
            if buttons[0][i]['text'] == players[0] and buttons[2][i]['text'] == players[0]:
                if buttons[1][i]['text'] != player:
                    return [True, [1, i]]
            
        if buttons[0][0]['text'] == players[0] and buttons[2][2]['text'] == players[0]:
            if buttons[1][1]['text'] != player:
                return [True, [1, 1]]
        
        elif buttons[0][2]['text'] == players[0] and buttons[2][0]['text'] == players[0]:
            if buttons[1][1]['text'] != player:
                return [True, [1, 1]]
            
        for i in [0, 2]:
            for j in [0, 2]:
                if buttons[i][j]['text'] == players[0] and buttons[1][1]['text'] == players[0]:
                    if i == 0 and j == 0:
                        if buttons[2][2]['text'] != player:
                            return [True, [2, 2]]
                    elif i == 0 and j == 2:
                        if buttons[2][0]['text'] != player:
                            return [True, [2, 0]]
                    elif i == 2 and j == 0:
                        if buttons[0][2]['text'] != player:
                            return [True, [0, 2]]
                    elif i == 2 and j == 2:
                        if buttons[0][0]['text'] != player:
                            return [True, [0, 0]]


    return [False, 0]

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

    global player

    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""
            buttons[row][column].config(bg="white")
    
    player = random.choice(players)
    if player == players[1]:
        computer_turn()

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

