import pygame
from screen import *
from colour import *

def rectangle(colour, x, y, width, length):
  pygame.draw.rect(screen, colour, (x, y, width, length))