from maze_classes import Maze
from explorer_A import Node, shorter_path
from generator_RBT import build_recursive
from jpg_generator import create_jpg

# #Crée les murs du labyrinthe selon la taille saisie
# maze_size = int(input('Input maze size : '))
# maze1 = Maze(maze_size)

# #Génère (RBT) un labyrinthe selon les murs définis
# maze1 = build_recursive(maze1)

# #Ecrit le labyrinthe dans un fichier dont le nom est à saisir
# file_name = input('File name ? ')
# maze1.write(file_name)

# #Résolution A*
# start_nod = Node(maze1,0,0)
# end_nod = Node(maze1,maze_size-1,maze_size-1)
# shorter_path(maze1, start_nod, end_nod)

# #Ecrit le labyrinthe dans un fichier dont le nom est à saisir
# maze1.write(file_name + ' - SOLVED')

maze_size = 30
maze1 = Maze(maze_size)
# create_jpg(maze1)
maze1 = build_recursive(maze1)
maze1.write('TEST')
# create_jpg(maze1)
start_nod = Node(maze1,0,0)
end_nod = Node(maze1,maze_size-1,maze_size-1)
shorter_path(maze1, start_nod, end_nod)
maze1.write('TEST')
create_jpg(maze1)