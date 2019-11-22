#!/usr/bin/env python

from PIL import Image
import numpy as np
from colorama import Fore, Back, Style
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filePath", help="file path")
parser.add_argument("-i","--invert", help="invert the result", action="store_true")
parser.add_argument("-t", "--threshold", help="rgb threshold", type=int, default=110)

characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
args = parser.parse_args()
filePath = args.filePath
isInvert=args.invert
rgb_threshold = args.threshold

def getColor(R, G, B):
    r = 1 if R > 110 else 0
    g = 1 if G > 110 else 0
    b = 1 if B > 110 else 0
    if (r, g, b) == (0, 0, 0):
        return Fore.BLACK
    elif (r, g, b) == (1, 1, 1):
        return Fore.WHITE
    elif (r, g, b) == (0, 0, 1):
        return Fore.BLUE
    elif (r, g, b) == (0, 1, 0):
        return Fore.GREEN
    elif (r, g, b) == (1, 0, 0):
        return Fore.RED
    elif (r, g, b) == (0, 1, 1):
        return Fore.CYAN
    elif (r, g, b) == (1, 0, 1):
        return Fore.MAGENTA
    else:
        return Fore.YELLOW


def getCharacters(brightness, invert=False):
    index =  int(brightness / 255 * (len(characters) - 1))
    index = index if invert == False else len(characters) - 1 - index
    return characters[index]

im = Image.open(filePath)
print(im.format, im.size, im.mode)
base_width = 100
base_height = int(base_width / im.size[0] * im.size[1])

im = im.resize((base_width, base_height), Image.ANTIALIAS)
print(im.format, im.size, im.mode)
im.save("haha.jpg")
temp = np.asarray(im)
print('Iteratin though pixel')

for x in range(temp.shape[0]):
    for y in range(temp.shape[1]):
        averageRgb = (int(temp[x][y][0]) + int(temp[x][y][1]) + int(temp[x][y][2])) / 3
        color = getColor(temp[x][y][0], temp[x][y][1], temp[x][y][2])
        print(color + getCharacters(averageRgb, isInvert), end="")
        print(color + getCharacters(averageRgb, isInvert), end="")
        print(color + getCharacters(averageRgb, isInvert), end="")
    print('\n')


