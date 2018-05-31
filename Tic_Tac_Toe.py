from __future__ import print_function
import os  ## to use os.system('cls')
import random ## generate nums to make computer playing

__author__ = "KonINGEL"
__copyright__ = "Copyright (C) 2018 Mostafa Kamal"
__version__ = "1.0"



# This is the main thing in the program without it the program will be failed
board = ["0","1","2","3","4","5","6","7","8","9"]
N = 1 # I need it to name my players

def hello():
    print("============================")
    print("Wellcome to Tic Tac Toe V1.0 :) \n")
    print("Tell me your Opinion about my Tic Tac Toe")
    print("============================")

# clear Terminal
def clear():
    os.system('cls')

def reset_N():
    global N
    N = 1

# display board in cmd
def display():
    clear()
    """
                   ||   row 1  ||  row 2   ||  row 3   ||
                   ======================================
    column 1 -->   || board[1] || board[2] || board[3] ||
                   ======================================
    column 2 -->   || board[4] || board[5] || board[6] ||
                   ======================================
    column 3 -->   || board[7] || board[8] || board[9] ||
                   ======================================
    """
    print( '\n =====================')
    print( ' || ' , board[1] , ' || ' + board[2] , ' || ' , board[3] , '||')
    print( ' =====================')
    print( ' || ' , board[4] , ' || ' + board[5] , ' || ' , board[6] , '||')
    print( ' =====================')
    print( ' || ' , board[7] , ' || ' + board[8] , ' || ' , board[9] , '||')
    print( ' =====================\n')




def check_winner(player):
    #all possible situations to win
  if (board[1]  ==  board[4] ==  board[7] == player) or \
        (board[2] ==  board[5] ==  board[8] == player) or \
        (board[3] ==  board[6] ==  board[9] == player) or \
        (board[1] ==  board[2] ==  board[3] == player) or \
        (board[4] ==  board[5] ==  board[6] == player) or \
        (board[7] ==  board[8] ==  board[9] == player) or \
        (board[7] ==  board[5] ==  board[3] == player) or \
        (board[1] ==  board[5] ==  board[9] == player):

        return True



def draw():
    if (board[1] == 'X' or board[1] =='O')\
       and (board[2] == 'X' or board[2] =='O')\
       and (board[3] == 'X' or board[3] =='O')\
       and (board[4] == 'X' or board[4] =='O')\
       and (board[5] == 'X' or board[5] =='O')\
       and (board[6] == 'X' or board[6] =='O')\
       and (board[7] == 'X' or board[7] =='O')\
       and (board[8] == 'X' or board[8] =='O')\
       and (board[9] == 'X' or board[9] =='O'):
           return True

# reset display to use it when you play again
def reset_display():
    global  board
    board = ["0","1","2","3","4","5","6","7","8","9"]
    clear()


def pc():
 reset_display()
 while True:
    display()
    if draw() == True:
            print( '=====================')
            print ("---- Draw . Good Game for each other :) -----")
            print( '=====================')
            rematch = raw_input('Would you like to play again?  (y/n)  :  ').lower()
            if rematch == 'y':
                  reset_N()
                  play_game()
            else:
                  print ("Thanks for playing!")
                  break
    global N
    if N == 1 :
        global C
        C = raw_input("please write your name  :  ")
        print("\n")
        N = 2


    player = raw_input( C + " , Choose num from (1:9) : ")
    player = int(player)



        # use index list to change nums to X Value
    try:
        if board[player] != 'X' and board[player] != 'O':
            board[player] = 'X'
            check = True

            # check winner if you win it will ask you if you wanna play again
            if  check_winner('X') == True:
                print( '=====================')
                print ("---- X Wins -----")
                print( '=====================')


                rematch = raw_input('Would you like to play again?  (y/n)  :  ').lower()
                if rematch == 'y':
                   reset_N()
                   play_game()
                else:
                  print ("Thanks for playing!")
                  break

            # computer play by generating numbers
            while check:
                random.seed() #generate
                opponent  =  random.randint(0,9)
                if board[opponent] != 'X' and board[opponent] != 'O':
                     board[opponent] = 'O'
                     check = False
                     if  check_winner('O') == True:
                         print( '=====================')
                         print ("---- O Wins -----")
                         print( '=====================')
                         rematch = raw_input('Would you like to play again?  (y/n)  :  ').lower()
                         if rematch == 'y':
                           reset_N()
                           play_game()
                         else:
                            print ("Thanks for playing!")
                            break

        else:
            print ("This spot is taken")
    except:
            print("Sorry sir , :) Choose num from (1:9) only ")
            Sorry = raw_input("Choose (y/n) to continue match or not  :  ").lower()
            if Sorry == "y" :
                continue
            else:
                break
                print("Thanks for Playing")



def two_player():
    reset_display()
    while True:
        display()
        global N
        if N == 1:
           global C
           global D
           C = raw_input("first player  please Write your name :   ")
           D = raw_input("Second player please Write your name :   ")
           N = 2

        player1 = raw_input(  C + ' ,  Choose num from (1:9) : ')
        player1 = int(player1)

        try:
          if board[player1] != 'X' and board[player1] != 'O' :
                board[player1] = 'X'
                check = True
                display()
                if draw() == True :
                        print( '=====================')
                        print ("---- Draw . Good Game for each other :) -----")
                        print( '=====================')
                        rematch = raw_input('Would you like to play again?  (y/n)  :  ').lower()
                        if rematch == 'y':
                                reset_N()
                                play_game()
                        else:
                                print ("Thanks for playing!")
                                break
                if  check_winner('X') == True:
                            print( '=====================')
                            print ("-------  %s  Wins -------  " % C)
                            print( '=====================')
                            rematch = raw_input('Would you like to play again?  (y/n)  :  ').lower()
                            if rematch == 'y':
                                  reset_N()
                                  play_game()
                            else:
                                 print ("Thanks for playing!")
                                 break
                while check:
                    player2 = raw_input( D + ' ,  Choose num from (1:9) : ')
                    player2 = int(player2)


                    if board[player2] != 'X' and board[player2] != 'O':
                        board[player2] = 'O'
                        check = False

                        if  check_winner('O') == True:
                            print( '=====================')
                            print ("-------  %s  Wins -------  " % D)
                            print( '=====================')
                            rematch = raw_input('Would you like to play again?  (y/n)  :  ').lower()
                            if rematch == 'y':
                                  reset_N()
                                  play_game()
                            else:
                                 print("Thanks for playing!")
                                 break
        except:
            print("Sorry sir , :) Choose num from (1:9) only ")
            Sorry = raw_input("Choose (y/n) to continue match or not  :  ").lower()
            if Sorry == "y" :
                continue
            else:
                print("Thanks for Playing")
                break




def play_game():
    print("\n")
    a = raw_input("Would you play with computer or with another player please write (pc / player) \n\nWrite here : ").lower()
    if a == "pc":
        pc()
    elif a == 'player':
        two_player()
    else:
        print('======================')
        print("Please , Write (pc / player) ")
        play_game()


hello()


play_game()
