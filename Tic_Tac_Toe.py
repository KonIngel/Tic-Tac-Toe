from __future__ import print_function
import os  ## to use os.system('cls')
import random ## generate nums to make computer playing

board = ["0","1","2","3","4","5","6","7","8","9"]



# clear Terminal
def clear():
    os.system('cls')



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


# reset display to use it when you play again
def reset_display():
    global  board
    board = ["0","1","2","3","4","5","6","7","8","9"]
    clear()


def play_game():
 reset_display()
 while True:
    display()
    player = raw_input("Choose num from (1:9) : ")
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

play_game()
