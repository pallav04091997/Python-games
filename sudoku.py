board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False





def valid(board, num, pos):
    i, j = pos
    # checking col
    for z in range(len(board[0])):
        if board[i][z] == num and j != z:
            return False
    # checking row
    for z in range(len(board)):
        if board[z][j] == num and i != z:
            return False
    # checking box
    box_x = i//3 #row
    box_y = j //3 #col
    for p in range(box_x*3, box_x*3 +3):
        for q in range(box_y*3, box_y*3+3):
            if board[p][q] == num and (p,q)!= pos:
                return False

    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")





def find_empty(bo):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return False
print_board(board)
solve(board)
print()
print()
print_board(board)