#Amazing Mazes
# Classes

class Maze:
    def __init__(self,N):
        self.N = N

        self.cells = []
        for row in range(N):
            self.cells.append([])
            for col in range(N):
                self.cells[row].append(Cell(row,col))
    
        self.cells[0][0].walls['W'] = False
        self.cells[N-1][N-1].walls['E'] = False

    def __str__(self):
        wall = {True:'#', False:'.'}
        
        maze_out = ''

        for row in range(self.N):
            
            walls_line = ''
            cells_line = ''

            for col in range(self.N):

                walls_line = walls_line + '#' + wall[self.cells[row][col].walls['N']]
                cells_line = cells_line + wall[self.cells[row][col].walls['W']] + self.cells[row][col].symbol
            
            walls_line = walls_line + "#"
            cells_line = cells_line + wall[self.cells[row][col].walls['E']]
            maze_out = maze_out + '\n' + walls_line + '\n' + cells_line

        walls_line = ''
        for col in range(self.N):
            walls_line = walls_line + '#' + wall[self.cells[row][col].walls['S']]
        walls_line = walls_line + "#"
        
        maze_out = maze_out + '\n' + walls_line            

        return maze_out

    def write(self,file_name):
        fichier = open(file_name + '.txt',"w")
        fichier.write(str(self))

    def available_dir(self,cell):
        dir_list = []
        if not (cell.X == 0 or self.cells[cell.X-1][cell.Y].visited == True):
            dir_list.append('N')
        if not (cell.Y == self.N-1 or self.cells[cell.X][cell.Y+1].visited == True):
            dir_list.append('E')
        if not (cell.X == self.N-1 or self.cells[cell.X+1][cell.Y].visited == True):
            dir_list.append('S')
        if not (cell.Y == 0 or self.cells[cell.X][cell.Y-1].visited == True):
            dir_list.append('W')
        return dir_list

class Cell:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y

        self.walls = {
                        'N' : True,
                        'E' : True,
                        'W' : True,
                        'S' : True
                        }

        self.symbol = '.'
        self.visited = False

    def cell_coords(self):
        return [self.X, self.Y]

    def visit(self):
        self.visited = True

    def break_wall(self,direction):

        self.walls[direction] = False