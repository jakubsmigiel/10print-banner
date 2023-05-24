from PIL import Image, ImageDraw
import random

bgcolor = (255,255,255)
fgcolor = (0,0,0)

def draw_slash(d, x, y, cellsize, flip, thickness=0.16):
    if flip:
        slash = [
            (x+cellsize*(1-thickness), y),
            (x+cellsize, y),
            (x+cellsize, y+cellsize*thickness),
            (x+cellsize*thickness, y+cellsize),
            (x, y+cellsize),
            (x, y+cellsize*(1-thickness))
        ]
    else:
        slash = [
            (x, y),
            (x+cellsize*thickness, y),
            (x+cellsize, y+cellsize*(1-thickness)),
            (x+cellsize, y+cellsize),
            (x+cellsize*(1-thickness), y+cellsize),
            (x, y+cellsize*thickness)
        ]
    d.polygon(slash, fill=fgcolor)

def make_image(width, height, cellsize_px, margin=0):
    image = Image.new("RGB", (int(cellsize_px*margin + width*(cellsize_px*(1+margin))), int(cellsize_px*margin + height*(cellsize_px*(1+margin)))), bgcolor)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw_slash(draw, cellsize_px*margin + x*(cellsize_px+margin*cellsize_px), cellsize_px*margin + y*(cellsize_px+margin*cellsize_px), cellsize_px, random.random() > 0.5)
    return image

