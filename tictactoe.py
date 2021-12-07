"""
Tic Tac Toe Player
"""
#This work is done by Amani Touihri (Software Engineering)

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcounter=0
    Ocounter=0
    
    for row in board:
        for element in row:
            if element == "X":
                Xcounter+=1
            elif element == "O":
                Ocounter+=1
    
    if Xcounter>Ocounter:
        return O
    else:
         return X
     

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions=[]
    
    for i in range (3):
        for j in range(3):
            if board[i][j]== None: #i designates the row and j the column
                action=(i,j)
                possible_actions.append(action)
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action(board) == 2:
        raise Exception
    new_board= copy.copydeep(board)
    if new_board[action[0]][action[1]]is EMPTY:
        new_board[action[0]][action[1]] = player(board)
    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # row winner
    for row in board:
        xcount=row.count(X)
        ocount=row.count(O)
        if xcount == 3:
            return X
        elif ocount == 3:
            return O
    #column winner
    lengthcol=len(board)
    for i in range(lengthcol):
        column = [row[i] for row in board]
        if EMPTY not in column:
            if column.count(X) == 3:
                return X
            elif column.count(O) == 3:
                return O

    #diagonal winner
    if board[0][0] is not EMPTY:
        if board[0][0] == board [1][1] == board [2][2]:
            return board[1][1]
        elif board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) is X:
            return 1
        elif winner(board) is O:
            return -1
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # the board is terminal
    if terminal(board):
       return None
    optimal_val = None

    #the max will picks an action that produces the highest val of min_value and min will picks an actions that produces lowest val of max_value
    a = - math.inf
    b = math.inf
    if player(board) == X:
        if board == initial_state():
            optimal_val = (0,0)
            return optimal_val

    minval = -math.inf
    for action in actions(board):
        w = min_value(result(board, action), a, b)
        a = max(a,w)
        if w > minval:
            minval = w
            optimalval = action
        
    
    else:
        minval = math.inf
        for action in actions(board):
            w = max_value(result(board,action), a, b)
            b=min(b,w)
            if w < minval:
                w = b
                optimalval = action

    return optimalval

def min_value(board, a, b):
    if terminal(board):
        return utility(board)
    w = math.inf
    acts = actions(board)
    for action in acts: 
        w = min(w, max_value(board, action), a, b)
        b = min(b, w)
        if b<=a:
            break
    return w



def max_value(board, a , b):
    if terminal(board):
        return utility(board)
    w = - math.inf
    acts = actions(board)
    for action in acts: 
        w = max(w, min_value(board, action), a, b)
        a = max(a, w)
        if b<=a:
            break
    return w


