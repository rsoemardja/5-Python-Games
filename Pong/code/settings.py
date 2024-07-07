import pygame
from os.path import join

# Screen settings
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
SIZE = {'paddle': (40,100), 'ball': (30,30)}
SPEED = {'player': 500, 'opponent': 250, 'ball': 450}
COLORS = {
    'paddle': '#ee322c',
    'paddle shadow': '#b12521',
    'ball': '#f7f7f7',
    'ball shadow': '#bfbfbf',
    'background': '#002633',
}