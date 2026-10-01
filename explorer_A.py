from maze_classes import Cell

class Node(Cell):
    def __init__(self,maze,X,Y):
        
        self.cost = 0
        self.dist = 0
        self.heuristic = self.cost + self.dist

        self.X = X
        self.Y = Y

        self.walls = maze.cells[X][Y].walls

        self.maze = maze
        self.symbol = self.maze.cells[X][Y].symbol
        self.visited = self.maze.cells[X][Y].visited

        self.parent = self.maze.cells[0][0]

def dist(node1,node2):
    return abs(node2.X-node1.X) + abs(node2.Y-node1.Y)

def shorter_path(maze, start_nod, end_nod):
    maze.cells[0][0].walls['W'] = True

    closed_list = []
    open_list = []
    
    # Adds START node to OPEN list
    start_nod.heuristic = dist(start_nod,end_nod)
    open_list.append(start_nod)
    maze.cells[start_nod.X][start_nod.Y].symbol = '*'
    
    while open_list != []:
        
        # Priorise la liste par HEURISTIC
        # if len(open_list):
        #     print('liste avant')
        #     for nd in open_list:
        #         print(nd.X,nd.Y,nd.cost,nd.dist,nd.heuristic)

        open_list = sorted(open_list, key=lambda node: node.heuristic)
        
        # if len(open_list):
        #     print('liste apres')
        #     for nd in open_list:
        #         print(nd.X,nd.Y,nd.cost,nd.dist,nd.heuristic)
        #     print(maze)
        
        # Prend le premier noeud de la liste triée (le plus prometteur) et le retire de OPEN
        u = open_list.pop(0)
        
        # Si le noeud est le END, retourne la solution et arrête la recherche
        if u.X == end_nod.X and u.Y == end_nod.Y:
            build_path(u,maze,start_nod)
            break
        
        # Si le noeud n'est pas le END, examine ses voisins
        for v in neighbors(u):

            dist_tmp = dist(v,end_nod)
            cost_tmp = u.cost + 1

            heuristic_tmp = dist_tmp + cost_tmp

            in_open = False
            in_closed = False

            h_open = 0
            h_closed = 0

            for i in range(len(closed_list)):
                if v.X == closed_list[i].X and v.Y == closed_list[i].Y:
                    in_closed = True
                    h_closed = closed_list[i].heuristic
            
            for i in range(len(open_list)):
                if v.X == open_list[i].X and v.Y == open_list[i].Y:
                    in_open = True
                    h_open = open_list[i].heuristic
            
            if not ((in_open and h_open < heuristic_tmp) or (in_closed and h_closed < heuristic_tmp)):
                v.cost = u.cost + 1 
                v.dist = dist_tmp
                v.heuristic = v.cost + v.dist
                v.parent = u
                open_list.append(v)
                maze.cells[v.X][v.Y].symbol = '*'
        
        # Ajoute le noeud u à CLOSED
        closed_list.append(u)

    maze.cells[0][0].walls['W'] = False

def build_path(node,maze,start_nod):
    while not ((node.X == start_nod.X) and (node.Y == start_nod.Y)):
        maze.cells[node.X][node.Y].symbol = 'o'
        node = node.parent
    maze.cells[node.X][node.Y].symbol = 'o'

def neighbors(node):
    neighbors_ls =[]
    
    if node.walls['N'] == False:
        neighbors_ls.append(Node(node.maze,node.X-1,node.Y))

    if node.walls['E'] == False:
        neighbors_ls.append(Node(node.maze,node.X,node.Y+1))

    if node.walls['S'] == False:
        neighbors_ls.append(Node(node.maze,node.X+1,node.Y))

    if node.walls['W'] == False:
        neighbors_ls.append(Node(node.maze,node.X,node.Y-1))
    
    return neighbors_ls