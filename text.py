import pygame
from colours import *

font = pygame.font.SysFont("Cosmic Sans MS", 40)

font_display = []

font_display.append(font.render("0", True, black))
font_display.append(font.render(".", True, black))
font_display.append(font.render("(", True, black))
font_display.append(font.render(")", True, black))
font_display.append(font.render("=", True, black))

for i in range(1, 10):
  font_display.append(font.render(str(i), True, black))

font_display.insert(8, font.render("+", True, black))
font_display.insert(9, font.render("-", True, black))
font_display.insert(13, font.render("×", True, black))
font_display.insert(14, font.render("÷", True, black))
font_display.insert(18, font.render("del", True, black))
font_display.insert(19, font.render("AC", True, black))