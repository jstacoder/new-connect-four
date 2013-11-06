# coding: utf-8
import sys
import os

#def get_move(board,symbol,

#def make_move(

def get_first_choice():
    clear()
    print 'Would you like to be "X" or "O"?\nenter choice --> ',
    choice = raw_input().upper()
    
    if not choice in ['X','O']:
        raise InputError
    else:
        if choice == 'X':
            rtn = ('X','O')
        else:
            rtn = ('O','X')
    return rtn

def clear():
    x = os.system('clear')

def get_new_board(size):
    b = [][:]
    for x in range(size[0]):
        b.append([' ']*size[1])
    return b

def print_top_screen(size):
    print '  ',
    for x in range(1, size[0]):
        print(' %s ' % x),
    print ''
    print '  +---+' + ('---+' * (size[0]-2))
    

def print_bottom_screen(size):
    print '',
    print ' +---+' + ('---+' * (size[0]-2))

def print_board(board, size):
    print_top_screen(size)
    for y in range(size[1]):
        for x in range(size[0]):
            print(' %s|' % board[x][y]),
        print ''
        print_bottom_screen(size)
        
def add_to_board(board,column,symbol):
    row = range(len(board[column]))
    for spot in reversed(row):
        if board[column][spot] == ' ':
            board[column][spot] = symbol
            break
            
def get_column_choice(board):
    while True:
        clear()
        print ''
        print 'What Column would you like to choose?\npress q to quit\n(1-10): ',
        choice = raw_input()
        if choice.lower().startswith('q'):
            sys.exit()
        if not choice.isdigit() or int(choice) > 10:
            print 'INVALID INPUT!!'
            raw_input()
            continue
        move = int(choice) 
        if is_valid(board,move):
            return move

def is_valid(board, spot):
    if spot < 0 or spot > len(board):
        return False
    if board[spot-1][0] != ' ':
        return False

    return True


def test():
    s = (11,9)
    b = get_new_board(s)
    add_to_board(b,get_column_choice(b),'X')
    #print get_first_choice()
    #print get_column_choice(b)
    print_board(b,s)

if __name__ == "__main__":
    test()


