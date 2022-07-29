import pygame
from screen import *
from shapes import *
from colours import *
from text import *

def calculator():
  screen.fill(gray)
  #display screen
  rectangle(white, 8, 8, 305, 150)

  #buttons
  x_start = 8
  x = x_start
  y = 170
  for a in range(4):
    for b in range(5):
      rectangle(white, x, y, 53, 48)
      #next rectangle's x position
      x += 63
    x = x_start
    #next rectangle's y position
    y += 63
  pygame.display.update()

def number_and_symbols():
  x_start = 25
  x = x_start
  y = 375
  n = 0
  for a in range(4):
    for b in range(5):
      #move del and AC back
      if n == 18:
        x -= 17
      elif n == 19:
        x -= 3
      screen.blit(font_display[n], (x, y))
      #next font_display x position
      x += 65
      n += 1
    x = x_start
    #next font_display y position
    y -= 65
  pygame.display.update()