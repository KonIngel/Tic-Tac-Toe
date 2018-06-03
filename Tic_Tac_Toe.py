from __future__ import print_function
from colorama import init
from termcolor import colored
import os  ## to use os.system('cls')
import random ## generate nums to make computer playing

__author__ = "KonINGEL"
__copyright__ = "Copyright (C) 2018 Mostafa Kamal"
__version__ = "1.0"



# This is the main thing in the program without it the program will be failed
board = ["0","1","2","3","4","5","6","7","8","9"]
N = 1 # I need it to name my players
init() # to make colors support cmd



def hello():
    clear()
    print(colored("============================",'cyan'))
    print(colored("Wellcome to Tic Tac Toe V1.0 :) \n",'cyan'))
    print(colored("Tell me your Opinion about my Tic Tac Toe",'cyan'))
    print(colored("============================",'cyan'))

# clear Terminal
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
       os.system('clear')

def reset_N():
    global N
    N = 1

# display board in cmd
def display():
    clear()
    """
                   ||   col 1  ||  col 2   ||  col 3   ||
                   ======================================
    raw1 -->       || board[1] || board[2] || board[3] ||
                   ======================================
    raw2 -->       || board[4] || board[5] || board[6] ||
                   ======================================
    raw3 -->       || board[7] || board[8] || board[9] ||
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
            print(colored('=============================================','green'))
            print (colored("---- Draw . Good Game for each other :) -----",'white','on_green'))
            print(colored('=============================================','green'))
            rematch = raw_input(colored('Would you like to play again?  (y/n)  :  ','yellow')).lower()
            if rematch == 'y':
                  reset_N()
                  play_game()
            else:
                  print(colored("Thanks for playing! ^_^",'green'))
                  break
    global N
    if N == 1 :
        global C
        C = raw_input(colored("please write your name :",'white','on_blue'))
        if C == '': #* to use default username
            C = "Anonymous"
        print("\n")
        N = 2

    try:
       player = raw_input( C + " , Choose num from (1:9) : ")
       player = int(player)
    except:
        print(colored("\nValue Error\n",'white','on_red'))


        # use index list to change nums to X Value
    try:
        if board[player] != 'X' and board[player] != 'O':
            board[player] = 'X'
            check = True

            # check winner if you win it will ask you if you wanna play again
            if  check_winner('X') == True:
                print(colored( '=====================', 'green'))
                print (colored("---- X Wins -----", 'white','on_green' ))
                print( colored('=====================', 'green' ))


                rematch = raw_input(colored('Would you like to play again?  (y/n)  :  ','yellow')).lower()
                if rematch == 'y':
                   reset_N()
                   play_game()
                else:
                  print(colored("Thanks for playing! ^_^",'green'))
                  break

            # computer play by generating numbers
            while check:
                random.seed() #generate
                opponent  =  random.randint(0,9)
                if board[opponent] != 'X' and board[opponent] != 'O':
                     board[opponent] = 'O'
                     check = False
                     if  check_winner('O') == True:
                         print( colored('=====================','green'))
                         print(colored("---- O Wins -----",'white','on_green'))
                         print(colored( '=====================','green'))
                         rematch = raw_input(colored('Would you like to play again?  (y/n)  :  ','yellow')).lower()
                         if rematch == 'y':
                           reset_N()
                           play_game()
                         else:
                            print(colored("Thanks for playing! ^_^",'green'))
                            break

        else:
            print(colored("This spot is taken",'yellow'))
    except:
            print(colored("Sorry sir , :) Choose num from (1:9) only ",'red'))
            Sorry = raw_input(colored("Choose (y/n) to continue match or not  :  ",'red')).lower()
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
           C = raw_input(colored("first player  please Write your name : ",'white','on_blue'))
           D = raw_input(colored("Second player  your name : ",'white','on_blue'))
           if N == 1:
               if C == '':
                   C = 'Anonymous1'
                   if D == '':
                       D = 'Anonymous2'
               elif D == '' :
                   D = 'Anonymous2'
                   if C == '':
                       C = 'Anonymous1'

           N = 2
        try:
            player1 = raw_input(  C + ' ,  Choose num from (1:9) : ')
            player1 = int(player1)
        except:
            print(colored("\nValue Error\n",'white','on_red'))
        try:
          if board[player1] != 'X' and board[player1] != 'O' :
                board[player1] = 'X'
                check = True
                display()
                if draw() == True :
                        print(colored('=============================================','green'))
                        print (colored("---- Draw . Good Game for each other :) -----",'white','on_green'))
                        print(colored('=============================================','green'))
                        rematch = raw_input(colored('Would you like to play again?  (y/n)  :  ','yellow')).lower()
                        if rematch == 'y':
                                reset_N()
                                play_game()
                        else:
                                print(colored("Thanks for playing! ^_^",'green'))
                                break
                if  check_winner('X') == True:
                            print( colored('=====================','green'))
                            print(colored("-------  %s  Wins -------  " % C ,'white','on_green'))
                            print(colored( '=====================','green'))
                            rematch = raw_input(colored('Would you like to play again?  (y/n)  :  ','yellow')).lower()
                            if rematch == 'y':
                                  reset_N()
                                  play_game()
                            else:
                                 print(colored("Thanks for playing! ^_^",'green'))
                                 break
                while check:
                    player2 = raw_input( D + ' ,  Choose num from (1:9) : ')
                    player2 = int(player2)


                    if board[player2] != 'X' and board[player2] != 'O':
                        board[player2] = 'O'
                        check = False

                        if  check_winner('O') == True:
                            print( colored('=====================','green'))
                            print(colored("-------  %s  Wins -------  " % D ,'white','on_green'))
                            print(colored( '=====================','green'))
                            rematch = raw_input(colored('Would you like to play again?  (y/n)  :  ','yellow')).lower()
                            if rematch == 'y':
                                  reset_N()
                                  play_game()
                            else:
                                 print(colored("Thanks for playing! ^_^",'green'))
                                 break

        except:
            print(colored("Sorry sir , :) Choose num from (1:9) only ",'red'))
            Sorry = raw_input(colored("Choose (y/n) to continue match or not  :  ",'red')).lower()
            if Sorry == "y" :
                continue
            else:
                print(colored("Thanks for Playing! ^_^",'green'))
                break




def play_game():
    print("\n")
    a = raw_input(colored("Would you play with computer or with another player  (pc / player) \n\nWrite here : ",'cyan')).lower()
    if a == "pc":
        pc()
    elif a == 'player':
        two_player()
    else:
        clear()
        print(colored('\n=================================================================','red'))
        print(colored("you didn't choose  (pc / player) please choose one of it to play ",'yellow','on_red'))
        print(colored('=================================================================','red'))
        play_game()

hello()



try:
   play_game()
except KeyboardInterrupt:
   print(colored("==================="))
   print(colored("Thanks for playing See you Later ^_^"))
   print(colored("==================="))
