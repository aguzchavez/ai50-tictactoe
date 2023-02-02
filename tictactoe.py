"""
Tic Tac Toe Player
"""

import copy
import math
from util import Node, StackFrontier, QueueFrontier

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
    countx = 0
    counto = 0
    for row in board:
        for column in row:
            if column == X:
                countx += 1
            elif column == O:
                counto +=1
    if countx == counto:
        return X
    elif countx > counto:
        return O
    else:
        raise ValueError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = list()
    for idr, row in enumerate(board):
        for idc, column in enumerate(row):
            if column == EMPTY:
                actions.append((idr,idc))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = copy.deepcopy(board)
    next_player = player(newboard)
    newboard[action[0]][action[1]] = next_player
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if (row[0] == row[1] == row[2] != EMPTY):
            return row[0] 
    # Check columns
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i] != EMPTY):
            return board[0][i] 
    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] != EMPTY) or (board[0][2] == board[1][1] == board[2][0] != EMPTY):
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return check_full(board) or winner(board) != None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    who_won = winner(board)
    if who_won == X: 
        return 1
    elif who_won == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    next_player = player(board)
    if next_player == X:
        return max_action(board)
    else:
        return min_action(board)

def max_action(board):
    max_score = -100
    next_action = None
    for action in actions(board):
        possible_value = min_value(result(board,action))
        if(possible_value > max_score):
            next_action = action
            max_score = possible_value
    return next_action

def min_action(board):
    min_score = 100
    next_action = None
    for action in actions(board):
        
        possible_value = max_value(result(board,action))
        print("Possible to min " + str(action) + " possible value " + str(possible_value))
        if(possible_value < min_score):
            next_action = action
            min_score = possible_value
    return next_action

def max_value(board):
    if(terminal(board)):
        return utility(board)
    v = -100
    for action in actions(board):
        possible_result = result(board,action)
        v = max(v,min_value(possible_result))
    return v

def min_value(board):
    if(terminal(board)):
        return utility(board)
    v = 100
    for action in actions(board):
        possible_result = result(board,action)
        v = min(v,max_value(possible_result))
    return v

def check_full(board):
    if (board[0].count(EMPTY) == 0 and board[1].count(EMPTY)== 0 and board[2].count(EMPTY) == 0):
        return True
    return False