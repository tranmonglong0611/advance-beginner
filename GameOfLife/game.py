import random
import numpy as np
import time

width = 50
height = 50
symbol = u"\u2588"

def dead_state(width, height):
    return np.zeros((width, height))

def random_state(width, height):
    matrix = dead_state(width, height)
    states = [0, 1]
    for rowIdx in range(len(matrix)):
        matrix[rowIdx] = list(map(lambda x: random.choice(states), matrix[rowIdx]))

    return matrix

def render(board):
    render_matrix = np.zeros_like(dead_state(len(board[0]), len(board)), dtype=str)
    for rowIdx in range(len(board)):
        render_matrix[rowIdx] = list(map(lambda x: symbol if x == 1 else ' ', board[rowIdx]))

    print('-' * (width * 3 + 2))
    for rowIdx in range(len(board)):
        print('|', end="")
        for colIdx in range(len(board[0])):
            print(render_matrix[rowIdx][colIdx], end="")
            print(render_matrix[rowIdx][colIdx], end="")
            print(render_matrix[rowIdx][colIdx], end="")
        print('|', end="")
        print("\n")
    print('-' * (width * 3 + 2))

def next_board_state(board):
    next_board = dead_state(len(board[0]), len(board))
    for rowIdx in range(len(board)):
        for colIdx in range(len(board[0])):
            next_board[rowIdx][colIdx] = next_cell_state(board[rowIdx][colIdx], board, rowIdx, colIdx)
    return next_board

def next_cell_state(current_state, board, rowIdx, colIdx):
    list_neighbor = get_list_neighbor(rowIdx, colIdx, len(board) - 1, len(board[0]) - 1)
    list_neighbor_live_count = sum(map(lambda x: board[x[0]][x[1]], list_neighbor))

    if current_state == 1:
        if (list_neighbor_live_count <= 1) or (list_neighbor_live_count > 3):
            return 0
        else:
            return 1
    else:
        if (list_neighbor_live_count == 3):
            return 1
    return current_state


def get_list_neighbor(rowIdx, colIdx, height, width):
    list_neighbor = []
    for i in range(rowIdx - 1, rowIdx + 2):
        for j in range (colIdx - 1, colIdx + 2):
            if is_valid(i, j, height, width) and ((i != rowIdx) or (j != colIdx)):
                list_neighbor.append((i, j))
    return list_neighbor

def is_valid(rowIdx, colIdx, height, width):
    if (rowIdx >= 0) and (rowIdx <= height) and (colIdx >= 0) and (colIdx <= width):
        return True
    return False

def run_forever(init_board):
    next_board = init_board
    while(True):
        render(next_board)
        next_board = next_board_state(next_board)
        time.sleep(1)


a = random_state(width, height)
run_forever(a)
