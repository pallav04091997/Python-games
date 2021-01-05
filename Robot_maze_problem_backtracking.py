#maze path is list of list
# . represents valid path
# x represents invalid path
# maze[-1][-1] represents the home

maze = [
    [".",".",".","."],
    [".","x","x","x"],
    [".",".",".","x"],
    ["x","x",".","."]
]
def print_maze(maze):
    for row in maze:
        row_print = ""
        for value in row:
            row_print+= value + " "
        print(row_print)

def solve_maze(maze):
    return solve_maze_helper(maze, [], 0, 0)


def solve_maze_helper(maze, sol, pos_row, pos_col):
    # already home
    if pos_row == len(maze)-1 and pos_col == len(maze[0])-1:
        return sol

    #out of bound
    if pos_row >= len(maze) or pos_col >= len(maze[0]):
        return None
    #is on an obstacle
    if maze[pos_row][pos_col] == "x":
        return None

    sol.append('r')
    sol_going = solve_maze_helper(maze, sol, pos_row, pos_col+1)
    if sol_going is not None:
        return sol_going
    sol.pop()
    sol.append('d')
    sol_down = solve_maze_helper(maze, sol, pos_row+1, pos_col)
    if sol_down is not None:
        return sol_down
    sol.pop()
    return None





print_maze(maze)
print(solve_maze(maze))