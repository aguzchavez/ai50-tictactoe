from tictactoe import *

# Testing player initial state
def test_initial_state():
    assert str(player(initial_state())) == "X"

# Testing player X
def test_player():
    board = [[EMPTY, EMPTY, O],
                [EMPTY, X, O],
                [EMPTY, EMPTY, X]]
    assert str(player(board)) == "X"

# Testing player O
def test_player_o():
    board = [[EMPTY, X, O],
                [EMPTY, X, O],
                [EMPTY, EMPTY, X]]
    assert str(player(board)) == "O"
    
# Testing actions()
def test_actions():
    board = [[EMPTY, EMPTY, O],
                [EMPTY, X, O],
                [EMPTY, X, X]]


    possible_actions = actions(board)

    assert len(possible_actions) == 4


# Testing result()
def test_result():
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    next_board = result(board,(0,0))

    assert next_board[0][0] == O

# Testing Terminal false
def test_termina_false():
    board = [[EMPTY, O, O],
            [EMPTY, X, X],
            [EMPTY, EMPTY, EMPTY]]
    assert terminal(board) == False

# Testing Terminal true
def test_termina_true():
    board = [[X, X, X],
            [O, X, O],
            [EMPTY, O, EMPTY]]
    assert terminal(board) == True

# Testing Winner None
def test_winner_none():
    board = [[EMPTY, O, O],
            [EMPTY, X, X],
            [EMPTY, EMPTY, EMPTY]]
    
    assert winner(board) == None

# Testing Winer X horizontal
def test_winner_x():
    board = [[X, X, X],
            [O, X, O],
            [EMPTY, O, EMPTY]]
    assert winner(board) == X

# Testing Winner O vertical
def test_winner_o():
    board = [[O, EMPTY, X],
                [O, X, EMPTY],
                [O, EMPTY, EMPTY]]
    assert winner(board) == O

# Testing Winner X diagonal
def test_winner_x_diagonal():
    board = [[O, EMPTY, X],
            [O, X, EMPTY],
            [X, EMPTY, EMPTY]]
    assert winner(board) == X

# Testing End Game Winner None
def test_winner_none():
    board = [[X, O, X],
            [X, O, X],
            [O, X, O]]

    assert winner(board) == None