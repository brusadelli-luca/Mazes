from maze_classes import Maze
from explorer_A import Node, shorter_path
from generator_RBT import build_recursive
from jpg_generator import create_jpg

maze_size = 30
maze1 = Maze(maze_size)
maze1 = build_recursive(maze1)
maze1.write('TEST')
start_nod = Node(maze1,0,0)
end_nod = Node(maze1,maze_size-1,maze_size-1)
shorter_path(maze1, start_nod, end_nod)
maze1.write('TEST')
create_jpg(maze1)