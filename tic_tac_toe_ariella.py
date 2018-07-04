# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bull_cow.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jfleisch <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/04 13:34:33 by jfleisch          #+#    #+#              #
#    Updated: 2018/07/04 13:34:35 by jfleisch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

player = 1
check_piece = (['1', '2', '3','4', '5', '6', '7', '8', '9']);
xy = 'x'
done = 0
count = 0
def print_board():
    global check_piece
    print('''
          |        |
       ''' + check_piece[0] + '''  |   ''' + check_piece[1] + '''    |  ''' + check_piece[2] + '''
      -------------------
          |        |
       ''' + check_piece[3] + '''  |   ''' + check_piece[4] + '''    |  ''' + check_piece[5] + '''
      ------------------
          |        |
       ''' + check_piece[6] + '''  |   ''' + check_piece[7] + '''    |  ''' + check_piece[8])
def get_input():
    global player
    global xy
    global numchoose
    global check_piece
    global done
    while (done == 0):
        if (player == 1):
            xy  = 'x'
        else:
            xy = 'o'
        numchoose = input("choose a number ")
        choose_piece()
def choose_piece():
    global check_piece
    global numchoose
    global xy
    global player
    global count
    if (check_piece[numchoose - 1] != 'x' and check_piece[numchoose - 1] != 'y'):
        check_piece[numchoose - 1] = xy
        print_board()
        if (player == 1):
            player = 2
        else:
            player = 1
        count += 1
        check_win()
def check_win():
    global check_piece
    global xy
    global count
    if (count == 9):
        win()
    if (check_piece[0] == xy and check_piece[1] == xy and check_piece[2] == xy):
        win()
    elif (check_piece[3] == xy and check_piece[4] == xy and check_piece[5] == xy):
        win()
    elif (check_piece[6] == xy and check_piece[7] == xy and check_piece[8] == xy):
        win()
    elif (check_piece[0] == xy and check_piece[3] == xy and check_piece[6] == xy):
        win()
    elif (check_piece[1] == xy and check_piece[4] == xy and check_piece[7] == xy):
        win()
    elif (check_piece[2] == xy and check_piece[5] == xy and check_piece[8] == xy):
        win()
    elif (check_piece[0] == xy and check_piece[4] == xy and check_piece[8] == xy):
        win()
    elif (check_piece[2] == xy and check_piece[4] == xy and check_piece[6] == xy):
        win()
def win():
    global xy
    global check_piece
    global done
    global count
    if (count < 9):
        print(xy + " WINS!")
    else:
        print("TIE GAME!")
    print_board()
    done = 1
print_board()
get_input()
