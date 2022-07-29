import pygame
from visual import *

running = True

FPS = 60
clock = pygame.time.Clock()

answer_display = ""
user_input = ""

intake = False

while running:
  clock.tick(FPS)
  
  calculator()
  number_and_symbols()

  #mouse position
  for event in pygame.event.get():
    pos = pygame.mouse.get_pos()
    button = pygame.mouse.get_pressed()
    mx=pos[0]
    my=pos[1]
    print(mx, my, button)

  #original rectangle(the button "0")
  button_pos_x1, button_pos_x2 = 8, 61
  button_pos_y1, button_pos_y2 = 359, 407

  #first line
  if mx > button_pos_x1 and mx < button_pos_x2 and my > button_pos_y1 and my < button_pos_y2 and button[0] == 1 and intake == False:
    user_input += "0"
    print("0")
  elif mx > button_pos_x1+63 and mx < button_pos_x2+63 and my > button_pos_y1 and my < button_pos_y2 and button[0] == 1 and intake == False:
    user_input += "."
    print(".")
  elif mx > button_pos_x1+63*2 and mx < button_pos_x2+63*2 and my > button_pos_y1 and my < button_pos_y2 and button[0] == 1 and intake == False:
    user_input += "("
    print("(")
  elif mx > button_pos_x1+63*3 and mx < button_pos_x2+63*3 and my > button_pos_y1 and my < button_pos_y2 and button[0] == 1 and intake == False:
    user_input += ")"
    print(")")
  elif mx > button_pos_x1+63*4 and mx < button_pos_x2+63*4 and my > button_pos_y1 and my < button_pos_y2 and button[0] == 1 and intake == False:
    #replace the symbol to display better looking one to the user
    if "×" in user_input:
      try:
        answer_display = str(eval(user_input.replace("×", "*")))
      except:
        answer_display = "ERROR"
    elif "÷" in user_input:
      try:
        answer_display = str(eval(user_input.replace("÷", "/")))
      #to test whether it is a integer
        decimal = answer_display.find(".")
        if float(answer_display) == int(answer_display[:decimal]):
          #if true, change to integer
          answer_display = str(int(answer_display[:decimal]))
      except:
        answer_display = "ERROR"
    else:
      #to test if the equation is valid
      try:
        answer_display = str(eval(user_input))
      except:
        answer_display = "ERROR"
    user_input = ""
    print("=")
  #second line
  if mx > button_pos_x1 and mx < button_pos_x2 and my > button_pos_y1-63 and my < button_pos_y2-63 and button[0] == 1 and intake == False:
    user_input += "1"
    print("1")
  elif mx > button_pos_x1+63 and mx < button_pos_x2+63 and my > button_pos_y1-63 and my < button_pos_y2-63 and button[0] == 1 and intake == False:
    user_input += "2"
    print("2")
  elif mx > button_pos_x1+63*2 and mx < button_pos_x2+63*2 and my > button_pos_y1-63 and my < button_pos_y2-63 and button[0] == 1 and intake == False:
    user_input += "3"
    print("3")
  elif mx > button_pos_x1+63*3 and mx < button_pos_x2+63*3 and my > button_pos_y1-63 and my < button_pos_y2-63 and button[0] == 1 and intake == False:
    user_input += "+"
    print("+")
  elif mx > button_pos_x1+63*4 and mx < button_pos_x2+63*4 and my > button_pos_y1-63 and my < button_pos_y2-63 and button[0] == 1 and intake == False:
    user_input += "-"
    print("-")
  #third line
  if mx > button_pos_x1 and mx < button_pos_x2 and my > button_pos_y1-63*2 and my < button_pos_y2-63*2 and button[0] == 1 and intake == False:
    user_input += "4"
    print("4")
  elif mx > button_pos_x1+63 and mx < button_pos_x2+63 and my > button_pos_y1-63*2 and my < button_pos_y2-63*2 and button[0] == 1 and intake == False:
    user_input += "5"
    print("5")
  elif mx > button_pos_x1+63*2 and mx < button_pos_x2+63*2 and my > button_pos_y1-63*2 and my < button_pos_y2-63*2 and button[0] == 1 and intake == False:
    user_input += "6"
    print("6")
  elif mx > button_pos_x1+63*3 and mx < button_pos_x2+63*3 and my > button_pos_y1-63*2 and my < button_pos_y2-63*2 and button[0] == 1 and intake == False:
    user_input += "×"
    print("×")
  elif mx > button_pos_x1+63*4 and mx < button_pos_x2+63*4 and my > button_pos_y1-63*2 and my < button_pos_y2-63*2 and button[0] == 1 and intake == False:
    user_input += "÷"
    print("÷")
  #fourth line
  if mx > button_pos_x1 and mx < button_pos_x2 and my > button_pos_y1-63*3 and my < button_pos_y2-63*3 and button[0] == 1 and intake == False:
    user_input += "7"
    print("7")
  elif mx > button_pos_x1+63 and mx < button_pos_x2+63 and my > button_pos_y1-63*3 and my < button_pos_y2-63*3 and button[0] == 1 and intake == False:
    user_input += "8"
    print("8")
  elif mx > button_pos_x1+63*2 and mx < button_pos_x2+63*2 and my > button_pos_y1-63*3 and my < button_pos_y2-63*3 and button[0] == 1 and intake == False:
    user_input += "9"
    print("9")
  elif mx > button_pos_x1+63*3 and mx < button_pos_x2+63*3 and my > button_pos_y1-63*3 and my < button_pos_y2-63*3 and button[0] == 1 and intake == False:
    user_input = user_input[:-1]
    print("del")
  elif mx > button_pos_x1+63*4 and mx < button_pos_x2+63*4 and my > button_pos_y1-63*3 and my < button_pos_y2-63*3 and button[0] == 1 and intake == False:
    answer_display = ""
    user_input = ""
    print("AC")
    
  #one input per click
  if button[0] == 1:
    intake = True
  else:
    intake = False

  #print input
  answer = font.render(answer_display, True, black)
  screen.blit(answer, (10, 70))
  input = font.render(user_input, True, black)
  screen.blit(input, (10, 130))
  pygame.display.update()