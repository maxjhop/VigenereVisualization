"""
All of the buttons available during animation
"""
import pygame
import sys


# initializing the constructor
pygame.init()

# screen resolution
res = (720, 720)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in this font
menu = smallfont.render('Main Menu', True, color)
play = smallfont.render('Play', True, color)
pause = smallfont.render('Pause', True, color)
forw = smallfont.render('Step Forward', True, color)
back = smallfont.render('Step Back', True, color)
up = smallfont.render('Speed Up', True, color)
down = smallfont.render('Slow Down', True, color)
res = smallfont.render('Restart', True, color)


class button():
    
    def __init__(self, y1, text, x1 = 5, x2 = 200, y2 = 40):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.text = text

    def draw(self):
        if self.hover(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, color_light, [self.x1, self.y1, self.x2, self.y2])
        else:
            pygame.draw.rect(screen, color_dark, [self.x1, self.y1, self.x2, self.y2])
        screen.blit(self.text, (self.x1 + 5, self.y1 + 5))

    def hover(self, mouse):
        if self.x1 <= mouse[0] <= self.x2 and self.y1 <= mouse[1] <= self.y2:
            print(mouse)
            print("Hover True")
            return True
        
        else:
            print(mouse)
            print("False")
            return False


# buttons and their locations
menu_button = button(5, menu)
play_button = button(50, play)
pause_button = button(95, pause)
forw_button = button(140, forw)
back_button = button(185, back)
up_button = button(230, up)
down_button = button(275, down)
res_button = button(320, res)

buttons = [menu_button, play_button, pause_button, forw_button, back_button, up_button, down_button, res_button]

while True:

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # fills the screen with a color
    screen.fill((50, 100, 0))

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on a
            # button the game does the thing
            pass

    #drawing buttons
    for i in buttons:
        i.draw()

    # updates the frames of the game
    pygame.display.update()
