#Amazing Mazes
# Recursive Backtrack
import random

def build_recursive(maze):
    prev_wall = {
                'N' : 'S',
                'S' : 'N',
                'E' : 'W',
                'W' : 'E'
                }

    path = []
    cell = maze.cells[0][0]
    path.append(cell.cell_coords())
    cell.visit()

    cells_nb = maze.N * maze.N

    while len(path) < cells_nb:
        prev_X = cell.X
        prev_Y = cell.Y
        cell = next_cell(maze,cell)
        
        if cell == 'END':
            i = -1
            while maze.available_dir(maze.cells[path[i][0]][path[i][1]]) == []:
                i = i - 1
            
            prev_X = path[i][0]
            prev_Y = path[i][1]
            cell = next_cell(maze,maze.cells[path[i][0]][path[i][1]])
        
        if cell.X == prev_X:
            if cell.Y > prev_Y:
                direction = 'W'
            else:
                direction = 'E'

        elif cell.Y == prev_Y:
            if cell.X > prev_X:
                direction = 'N'
            else:
                direction = 'S'

        path.append(cell.cell_coords())
        cell.visit()
        cell.break_wall(direction)
        maze.cells[prev_X][prev_Y].break_wall(prev_wall[direction])
    
    return maze

def next_cell(maze,cell):

    next_list = maze.available_dir(cell)
    if next_list != []:
        direction = random.choice(next_list)

        if direction == 'N' and cell.X > 0:
            return maze.cells[cell.X-1][cell.Y]

        elif direction == 'E' and cell.Y < maze.N - 1:
            return maze.cells[cell.X][cell.Y+1]

        elif direction == 'S' and cell.X < maze.N - 1:
            return maze.cells[cell.X+1][cell.Y]

        elif direction == 'W' and cell.Y > 0:
            return maze.cells[cell.X][cell.Y-1]

        else:
            return next_cell(maze,cell)

    else:
        return 'END'