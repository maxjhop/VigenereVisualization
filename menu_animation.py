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

# rendering a text written in
# this font
menu = smallfont.render('Main Menu', True, color)
play = smallfont.render('Play', True, color)
pause = smallfont.render('Pause', True, color)
forw = smallfont.render('Step Forward', True, color)
back = smallfont.render('Step Back', True, color)
up = smallfont.render('Speed Up', True, color)
down = smallfont.render('Slow Down', True, color)
res = smallfont.render('Restart', True, color)

# buttons and their locations
options = (menu, play, pause, forw, back, up, down, res)
names = ("menu", "play", "pause", "forw", "back", "up", "down", "res")
locY = (5, 50, 95, 140, 185, 230, 275, 320)

#checks if mouse is over a button: bool
def hover(location):
    if 5 <= mouse[0] <= 205:
        for i in locY:
            if i <= mouse[1] <= i + 40:
                return True, names[locY.index(i)]
    
    return False, None


while True:

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # fills the screen with a color
    screen.fill((60, 0, 0))

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on a
            # button the game does the thing
            button = hover(mouse)[1]
            if button == "menu":
                pygame.quit()

            elif button == "play":
                pass

            elif button == "pause":
                pass

            elif button == "for":
                pass

            elif button == "back":
                pass

            elif button == "up":
                pass

            elif button == "down":
                pass

            elif button == "res":
                pass



    #drawing buttons, lighter shade if mouse hovering over one
    for i in range(len(options)):
        if hover(mouse)[0]:
            pygame.draw.rect(screen, color_light, [5, locY[i], 200, 40])

        else:
            pygame.draw.rect(screen, color_dark, [5, locY[i], 200, 40])

        # superimposing the text onto buttons
        screen.blit(options[i], (10, locY[i] + 5))

    # updates the frames of the game
    pygame.display.update()
