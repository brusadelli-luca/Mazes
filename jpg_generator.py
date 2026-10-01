from PIL import Image, ImageDraw

CELL_SIZE = 30   # taille d'une cellule en pixels
LINE_WIDTH = 10  # épaisseur des traits

def create_jpg(maze):
    size = maze.N
    image_size = CELL_SIZE * size
    img = Image.new('RGB', (image_size, image_size), (255, 255, 255))
    cell_size = image_size//size
    draw = ImageDraw.Draw(img)
    draw.line((0, 0, image_size-1, 0), fill=(0, 0, 0), width=LINE_WIDTH)
    draw.line((image_size-1, 0, image_size-1, image_size-1-cell_size), fill=(0, 0, 0), width=LINE_WIDTH)
    draw.line((0, image_size-1, image_size-1, image_size-1), fill=(0, 0, 0), width=LINE_WIDTH)
    draw.line((0, cell_size, 0, image_size-1), fill=(0, 0, 0), width=LINE_WIDTH)

    for row in range(size):
        for col in range(size):
            if maze.cells[row][col].walls['S']:
                draw.line((cell_size*col, cell_size*(row+1), cell_size*(col+1), cell_size*(row+1)), fill=(0, 0, 0), width=LINE_WIDTH)
            
            elif maze.cells[row][col].symbol=='o' and maze.cells[row+1][col].symbol=='o':
                draw.line((cell_size*col+cell_size/2, cell_size*row+cell_size/2, cell_size*col+cell_size/2, cell_size*(row+1)+cell_size/2), fill=(0, 255, 0), width=LINE_WIDTH)
            
            if maze.cells[row][col].walls['E']: 
                draw.line((cell_size*(col+1), cell_size*row, cell_size*(col+1), cell_size*(row+1)), fill=(0, 0, 0), width=LINE_WIDTH)

            elif col != size-1 and maze.cells[row][col].symbol=='o' and maze.cells[row][col+1].symbol=='o':
                draw.line((cell_size*col+cell_size/2, cell_size*row+cell_size/2, cell_size*(col+1)+cell_size/2, cell_size*row+cell_size/2), fill=(0, 255, 0), width=LINE_WIDTH)

            if maze.cells[row][col].symbol=='*': 
                draw.rectangle((cell_size*(col+1/2)-cell_size/6, cell_size*(row+1/2)-cell_size/6, cell_size*(col+1/2)+cell_size/6, cell_size*(row+1/2)+cell_size/6), fill=(255, 255, 0), width=LINE_WIDTH)

    img.show()
    img.save("TEST.jpg")