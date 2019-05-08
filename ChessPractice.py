import chess
import chess.svg as svg
import copy
import FileIO as io
import random as rand


def reverseArray(arr):
    return list(reversed(arr))


# These arrays allow the algorithm to make decisions based on the position of pieces


pawnEvalWhite = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
    [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
    [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
    [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
    [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
    [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]

pawnEvalBlack = reverseArray(pawnEvalWhite)

knightEval = [
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
    [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
    [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
    [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
    [-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0],
    [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
]

bishopEvalWhite = [
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
    [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
    [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
    [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0],
    [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]

bishopEvalBlack = reverseArray(bishopEvalWhite)

rookEvalWhite = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]
]

rookEvalBlack = reverseArray(rookEvalWhite)

evalQueen = [
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
    [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
    [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
    [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]

kingEvalWhite = [
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
    [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]
]

kingEvalBlack = reverseArray(rookEvalWhite)


# Returns the value of a certain piece based on where it is on the board
# black pieces have a negative value
def get_piece_value(piece, x, y):
    if piece == 'P':
        return 10 + pawnEvalWhite[y][x]
    elif piece == 'p':
        return -1 * (10 + pawnEvalBlack[y][x])
    elif piece == 'R':
        return 50 + rookEvalWhite[y][x]
    elif piece == 'r':
        return -1 * (50 + rookEvalBlack[y][x])
    elif piece == 'N':
        return 30 + knightEval[y][x]
    elif piece == 'n':
        return -1 * (30 + knightEval[y][x])
    elif piece == 'B':
        return 30 + bishopEvalWhite[y][x]
    elif piece == 'b':
        return -1 * (30 + bishopEvalBlack[y][x])
    elif piece == 'Q':
        return 90 + evalQueen[y][x]
    elif piece == 'q':
        return -1 * (90 + evalQueen[y][x])
    elif piece == 'K':
        return 900 + kingEvalWhite[y][x]
    elif piece == 'k':
        return -1 * (900 + kingEvalBlack[y][x])


def get_piece_value_new(piece):
    if piece == 'P':
        return 10
    elif piece == 'p':
        return -10
    elif piece == 'R':
        return 50
    elif piece == 'r':
        return -50
    elif piece == 'N':
        return 30
    elif piece == 'n':
        return -30
    elif piece == 'B':
        return 30
    elif piece == 'b':
        return -30
    elif piece == 'Q':
        return 90
    elif piece == 'q':
        return -90
    elif piece == 'K':
        return 900
    elif piece == 'k':
        return -900


# Returns the piece at a given spot
def get_piece(board, x, y):
    pieces = ['p', 'r', 'n', 'b', 'q', 'k', 'P', 'R', 'N', 'B', 'Q', 'K']
    fen = board.board_fen()
    i = 0
    while x > 0:
        if fen[i] == '/':
            x -= 1
        i += 1
    while y > 0:
        if pieces.__contains__(fen[i]):
            y -= 1
        else:
            y -= int(fen[i])
            if y < 0:
                return -1
        i += 1
    return fen[i]


# Returns the cumulative sum of the values of all the pieces on the board
def evaluate_board(board):
    total_evaluation = 0
    for i in range(0, 8):
        for j in range(0, 8):
            value = get_piece_value_new(get_piece(board, i, j))
            # print(str(value) + '(' + str(i) + ', ' + str(j) + ')')
            if not (value is None):
                total_evaluation = total_evaluation + value
    return total_evaluation


# The recursive minimax function used to determine which options are best
def minimax(depth, board, is_maximizing_player):
    if depth == 0:
        return -1 * evaluate_board(board)
    legal_moves = board.generate_legal_moves()
    if is_maximizing_player:
        best_move = -9999
        for move in legal_moves:
            copy_board = copy.copy(board)
            copy_board.push(move)
            contender = minimax(depth - 1, copy_board, not is_maximizing_player)
            if contender >= best_move:
                best_move = contender
        return best_move
    else:
        best_move = 9999
        for move in legal_moves:
            copy_board = copy.copy(board)
            copy_board.push(move)
            contender = minimax(depth - 1, copy_board, not is_maximizing_player)
            # print('Contender: ' + str(contender))
            if contender != 0:
                print('Contender: ' + str(contender))
            if contender <= best_move:
                if contender != best_move:
                    print('New Best Move: ' + str(contender))
                best_move = contender
        return best_move


def minimax_alpha(depth, board, alpha, beta, is_maximizing_player):
    if depth == 0:
        return -1 * evaluate_board(board)
    legal_moves = board.generate_legal_moves()
    if is_maximizing_player:
        best_move = -9999
        for move in legal_moves:
            copy_board = copy.copy(board)
            copy_board.push(move)
            contender = minimax_alpha(depth - 1, copy_board, alpha, beta, not is_maximizing_player)
            if contender >= best_move:
                best_move = contender
            if best_move >= alpha:
                alpha = best_move
            if beta <= alpha:
                return best_move
        return best_move
    else:
        best_move = 9999
        for move in legal_moves:
            copy_board = copy.copy(board)
            copy_board.push(move)
            contender = minimax_alpha(depth - 1, copy_board, alpha, beta, not is_maximizing_player)
            # print('Contender: ' + str(contender))
            """if contender != 0:
                print('Contender: ' + str(contender))"""
            if contender <= best_move:
                """if contender != best_move:
                    print('New Best Move: ' + str(contender))"""
                best_move = contender
            if best_move <= beta:
                beta = best_move
            if beta <= alpha:
                return best_move
        return best_move


# Evaluates the board and decides on an optimal move
def minimax_root(depth, board, is_maximizing_player):
    moves = board.generate_legal_moves()
    best_move = -9999
    turn = 1
    besti = -1
    moveNum = 1
    move_contenders = []

    for move in moves:
        copy_board = copy.copy(board)
        copy_board.push(move)
        contender = minimax_alpha(depth - 1, copy_board, -9999, 9999, not is_maximizing_player)
        print('Turn: ' + str(turn) + ' - Move: ' + str(moveNum) + ' - Score: ' + str(contender))
        if contender >= best_move:
            if best_move == contender:
                move_contenders.append(move)
            else:
                move_contenders = [move]
            best_move = contender
            best_move_found = move
            besti = moveNum
        moveNum += 1
    print('Best Move: ' + str(besti))
    return move_contenders[rand.randint(0, len(move_contenders) - 1)]


# Prompts the player to enter their move and then pushes the move to the board
def player_move(board):
    rank = ['1', '2', '3', '4', '5', '6', '7', '8']
    file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    legal_moves = board.generate_legal_moves()
    move_from = input('Move From: ')
    from_square = chess.square(file.index(move_from[0]), rank.index(move_from[1]))
    move_to = input('Move To: ')
    to_square = chess.square(file.index(move_to[0]), rank.index(move_to[1]))
    move = chess.Move(from_square, to_square)
    if not (move in legal_moves):
        print('Please enter a legal move!')
        return player_move(board)
    # print('From: ' + str(from_square) + ' To: ' + str(to_square))
    board.push(move)
    return board


# Runs the minimax algorithm and pushes the optimal move to the board
def comp_move(board, depth):
    print('Minimax under way...')
    move = minimax_root(depth, board, True)
    print('Best Move: ' + str(move))
    board.push(move)
    return board

def get_comp_move(board, depth):
    print('Minimax under way...')
    move = minimax_root(depth, board, True)
    print('Best Move: ' + str(move))
    return move


board_fen = io.readBoard("boardInput.txt")
board = chess.Board(board_fen)
print(board)
print(evaluate_board(board))
print(evaluate_board(board))
print()
move = get_comp_move(board, 3)
io.writeSuggestino(move)
board = comp_move(board, 3)
print(board)
print(evaluate_board(board))
print()