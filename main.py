from graphics import Window
from cell import Cell
from maze import Maze

def main():
    num_rows = 5
    num_cols = 5
    margin = 50
    screen_width = 800
    screen_height = 600
    cell_size_x = (screen_width - 2 * margin) / num_cols
    cell_size_y = (screen_height - 2 * margin) / num_rows
    win = Window(800, 600)
    
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")

    win.wait_for_close()

main()
