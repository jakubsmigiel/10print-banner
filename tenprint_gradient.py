import tenprint
import random

def get_rgb_from_int(color):
    r = (color>>16) & 255
    g = (color>>8) & 255
    b = color & 255
    return (r,g,b)

def get_gradient(color1, color2, between):
    new_color = []
    for p1, p2 in zip(color1, color2):
        new_color.append(int(p1*between + p2*(1-between)))
    return tuple(new_color)

def get_palette_rgb_from_palette_int(palette_raw):
    return [
        get_rgb_from_int(c) for c in 
            palette_raw
    ]


def generate_gradiented_10print(width, height, cellsize, margin, palette):
    image = tenprint.make_image(width, height, cellsize, margin)
    pixels = image.load()

    width_px = image.size[0]
    height_px = image.size[1]

    bg_gradient = palette[0:2]
    fg_gradient = palette[2:4]

    for x in range(width_px):
        for y in range(height_px):
            if pixels[x,y] == tenprint.bgcolor:
                pixels[x,y] = get_gradient(bg_gradient[0], bg_gradient[1], y/height_px)
            if pixels[x,y] == tenprint.fgcolor:
                pixels[x,y] = get_gradient(fg_gradient[0], fg_gradient[1], y/height_px)

    return image

def get_random_palette(palettes):
    palette_index, palette_rotations = random.choice(tuple(enumerate(palettes)))
    palette_rotation, palette = random.choice(tuple(enumerate(palette_rotations)))
    return palette_index, palette_rotation, get_palette_rgb_from_palette_int(palette)
