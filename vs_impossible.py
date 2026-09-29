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
    global player, turns

    if player == players[1] and check_winner() is False:

        window.update()

        move = get_computer_move()
        row = move[0]
        column = move[1]

        buttons[row][column]['text'] = player

        turns += 1

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

        # IF x 0 0
        #    0 0 0
        #    0 0 x
        diagonals = [[buttons[0][0], buttons[2][2]], [buttons[0][2], buttons[2][0]]]

        # IF x 0 0
        #    0 0 0
        #    0 x 0
        corner_patterns = [
            [[buttons[0][0]['text'], buttons[2][1]['text']], [buttons[1][0]['text'], buttons[2][2]['text']]], 
            [[buttons[0][2]['text'], buttons[2][1]['text']], [buttons[1][2]['text'], buttons[2][0]['text']]], 
            [[buttons[0][2]['text'], buttons[1][0]['text']], [buttons[0][1]['text'], buttons[2][0]['text']]], 
            [[buttons[0][0]['text'], buttons[1][2]['text']], [buttons[0][1]['text'], buttons[2][2]['text']]]
            ]
        
        # IF 0 0 0
        #    x 0 0
        #    0 x 0
        edge_patterns = [
            [buttons[0][1]['text'], buttons[1][2]['text']],
            [buttons[1][2]['text'], buttons[2][1]['text']],
            [buttons[2][1]['text'], buttons[1][0]['text']],
            [buttons[1][0]['text'], buttons[0][1]['text']]
            ]

        if turns == 1 and buttons[1][1]['text'] != "":


            corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
            
            return random.choice(corners)

        elif buttons[1][1]['text'] == "":
            return [1, 1]
        
        if  2 <= turns <= 3:

            edges = [[0, 1], [1, 2], [2, 1], [1, 0]]
            corner_patterns_answ = [
                            [[0, 0], [0, 1], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]],
                            [[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]],
                            [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1]],
                            [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 1], [2, 2]]
                           ]
            edge_patterns_answ = [
                            [0, 2],
                            [2, 2],
                            [2, 0],
                            [0, 0]
                            ]

            if diagonals[0][0]['text'] == players[0] and diagonals[0][1]['text'] == players[0]:
                return random.choice(edges)
            
            elif diagonals[1][0]['text'] == players[0] and diagonals[1][1]['text'] == players[0]:
                return random.choice(edges)
            
            for i in range(4):
                for j in range(2):
                    
                    if corner_patterns[i][j][0] == players[0] and corner_patterns[i][j][1] == players[0]:

                        move = random.choice(corner_patterns_answ[i])

                        while buttons[move[0]][move[1]]['text'] != "":
                            move = random.choice(corner_patterns_answ[i])

                        return move
                    
                if edge_patterns[i][0] == players[0] and edge_patterns[i][1] == players[0]:

                    move = edge_patterns_answ[i]

                    if buttons[move[0]][move[1]]['text'] == "":
                        return move


        row = random.randint(0, 2)
        column = random.randint(0, 2)
        repeat = True

        while buttons[row][column]['text'] != "" or repeat == True:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            if buttons[row][column]['text'] == "":
                buttons[row][column]['text'] = players[1]
                if can_win('player')[0] != True:
                    buttons[row][column]['text'] = ""
                    repeat = False

        return [row, column]

def can_win(who):

    if who == 'computer':
        check_who = players[1]

    elif who == 'player':
        check_who = players[0]
        
    for i in range (3):
        for j in [0, 2]:
            if buttons[i][1]['text'] == check_who and buttons[i][j]['text'] == check_who:
                if j == 0: 
                    if buttons[i][2]['text'] == "":
                        return [True, [i, 2]]
                else:
                    if buttons[i][0]['text'] == "":
                        return [True, [i, 0]]
        
        if buttons[i][0]['text'] == check_who and buttons[i][2]['text'] == check_who:
            if buttons[i][1]['text'] == "":
                return [True, [i, 1]]
        
    for i in range (3):
        for j in [0, 2]:
            if buttons[1][i]['text'] == check_who and buttons[j][i]['text'] == check_who:
                if j == 0: 
                    if buttons[2][i]['text'] == "":
                        return [True, [2, i]]
                else:
                    if buttons[0][i]['text'] == "":
                        return [True, [0, i]]
        
        if buttons[0][i]['text'] == check_who and buttons[2][i]['text'] == check_who:
            if buttons[1][i]['text'] == "":
                return [True, [1, i]]
        
    if buttons[0][0]['text'] == check_who and buttons[2][2]['text'] == check_who:
        if buttons[1][1]['text'] == "":
            return [True, [1, 1]]
    
    elif buttons[0][2]['text'] == check_who and buttons[2][0]['text'] == check_who:
        if buttons[1][1]['text'] == "":
            return [True, [1, 1]]
    
    for i in [0, 2]:
        for j in [0, 2]:
            if buttons[i][j]['text'] == check_who and buttons[1][1]['text'] == check_who:
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

    global player, turns

    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""
            buttons[row][column].config(bg="white")
    
    player = random.choice(players)
    turns = 1
    if player == players[1]:
        computer_turn()

window = Tk()
window.title("Tic-Tac-Toe - imp")
players = ["x", "o"]
player = random.choice(players)
buttons = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
turns = 1

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