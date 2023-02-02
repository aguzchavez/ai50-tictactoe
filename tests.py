from tictactoe import *
# Testing player()
print("Player X: " + str(player(initial_state())))
board = [[EMPTY, EMPTY, O],
            [EMPTY, X, O],
            [EMPTY, EMPTY, X]]

print("Player X: " + str(player(board)))

board = [[EMPTY, EMPTY, O],
            [EMPTY, X, O],
            [EMPTY, X, X]]

# Testing actions()
for x,y in actions(board):
    print(f"EMPTY x:{x} y:{y}")

print("Player O: " + str(player(board)))

board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

print("Player O: " + str(player(board)))



# Testing result()
print(board)
print(result(board,(0,0)))

board = [[EMPTY, O, O],
            [EMPTY, X, X],
            [EMPTY, EMPTY, EMPTY]]

print("Terminal False: " + str(terminal(board)))
print("Winner None:" + str(winner(board)))

board = [[X, X, X],
            [O, X, O],
            [EMPTY, O, EMPTY]]
print("Terminal True: " + str(terminal(board)))
print("Winner X:" + str(winner(board)))

board = [[O, EMPTY, X],
            [O, X, EMPTY],
            [O, EMPTY, EMPTY]]
print("Terminal True: " + str(terminal(board)))
print("Winner O:" + str(winner(board)))

board = [[O, EMPTY, X],
            [O, X, EMPTY],
            [X, EMPTY, EMPTY]]
print("Terminal True: " + str(terminal(board)))
print("Winner X:" + str(winner(board)))

board = [[X, O, X],
            [X, O, X],
            [O, X, O]]
print("Terminal True: " + str(terminal(board)))
print("Winner None:" + str(winner(board)))
