from maze_classes import Maze
from generator_RBT import build_recursive
import time

#Crée les murs du labyrinthe selon la taille saisie
sizes = [10,100,150, 175, 200 , 250, 300,350, 400,450, 500]
durations =[]

for size in sizes:
    start = time.time()
    maze1 = build_recursive(Maze(size))
    durations.append(round(time.time()-start,2))

    fichier = open('temps' + '.txt',"w")
    fichier.write(str(sizes) + '\n' + str(durations))