# Mazes

Génération et résolution de labyrinthes en Python.

- **Génération** : algorithme *Recursive Backtracker* (parcours en profondeur avec retour en arrière).
- **Résolution** : algorithme *A\** (recherche du plus court chemin).

## Prérequis

- Python 3
- La bibliothèque Pillow (pour créer l'image) :

```
python -m pip install pillow
```

## Utilisation

```
python main.py
```

Le programme génère un labyrinthe de 30 x 30 cases, le résout, puis crée deux fichiers dans le dossier :

- `TEST.txt` : le labyrinthe en texte
- `TEST.jpg` : le labyrinthe en image (elle s'ouvre aussi automatiquement)

Pour changer la taille, modifier la valeur de `maze_size` dans `main.py`.

### Lecture du résultat

Dans `TEST.txt` :

| Symbole | Signification |
|---|---|
| `#` | mur |
| `.` | passage libre |
| `o` | chemin le plus court trouvé |
| `*` | case explorée par l'algorithme |

L'entrée est en haut à gauche et la sortie en bas à droite. Dans l'image, le chemin est tracé en vert et les cases explorées sont marquées en jaune.

## Les fichiers

| Fichier | Rôle |
|---|---|
| `main.py` | programme principal |
| `maze_classes.py` | classes `Maze` (labyrinthe) et `Cell` (case) |
| `generator_RBT.py` | génération du labyrinthe |
| `explorer_A.py` | résolution avec A* |
| `jpg_generator.py` | création de l'image |
| `timer.py` | mesure du temps de génération selon la taille (résultat dans `temps.txt`) |

## Limites connues

- Les labyrinthes générés n'ont qu'un seul chemin possible entre l'entrée et la sortie.
- Au-delà d'environ 100 x 100 cases, la résolution devient lente, et l'image devient très grande.
