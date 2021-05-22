"""
This is the main project file for the Vigenere Cipher Visualization
Authors: Joshua Fawcett, Max Hopkins, Meghan Riehl, Yuyao Zhuge

Citations:
Starter code for basic pygame window was pulled from:
https://www.geeksforgeeks.org/creating-start-menu-in-pygame/
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
input_smallfont = pygame.font.SysFont('Corbel', 24)

# rendering a text written in
# this font
encrypt = smallfont.render('encrypt', True, color)
decrypt = smallfont.render('decrypt', True, color)
message = smallfont.render("message", True, color_dark)
key = smallfont.render("key", True, color_dark)
title = smallfont.render("Vigenere Visualization Tool", True, color_dark)

encrypt_rect = pygame.Rect(width / 2, height / 1.5, 140, 40)
decrypt_rect = pygame.Rect(width / 4, height / 1.5, 140, 40)
message_rect = pygame.Rect(width / 3.5, height / 4.2, 300, 40)
key_rect = pygame.Rect(width / 3.5, height / 2.5, 300, 40)

message_color = color
key_color = color
message_active = False
key_active = False
message_text = ''
key_text = ''

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 1.5 <= mouse[1] <= height / 1.5 + 40:
                pygame.quit()

            if width / 4 <= mouse[0] <= width / 4 + 140 and height / 1.5 <= mouse[1] <= height / 1.5 + 40:
                pygame.quit()

            if message_rect.collidepoint(ev.pos):
                message_active = True
                message_color = color_light
                key_color = color
                key_active = False

            if key_rect.collidepoint(ev.pos):
                key_active = True
                key_color = color_light
                message_color = color
                message_active = False

        if ev.type == pygame.KEYDOWN:


            if message_active:
                if ev.key == pygame.K_BACKSPACE:
                    message_text = message_text[:-1]
                else:
                    message_text += ev.unicode
            elif key_active:
                if ev.key == pygame.K_BACKSPACE:
                    key_text = key_text[:-1]
                else:
                    key_text += ev.unicode



    # fills the screen with a color
    screen.fill((255,255,165))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    pygame.draw.rect

    # if mouse is hovered over encrypt it
    # changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 1.5 <= mouse[1] <= height / 1.5 + 40:
        pygame.draw.rect(screen, color_light, encrypt_rect)

    else:
        pygame.draw.rect(screen, color_dark, encrypt_rect)

    # if mouse is hovered over decrypt it
    # changes to lighter shade
    if width / 4 <= mouse[0] <= width / 4 + 140 and height / 1.5 <= mouse[1] <= height / 1.5 + 40:
        pygame.draw.rect(screen, color_light, decrypt_rect)

    else:
        pygame.draw.rect(screen, color_dark, decrypt_rect)

    message_input = input_smallfont.render(message_text, True, color_dark)
    key_input = input_smallfont.render(key_text, True, color_dark)

    pygame.draw.rect(screen, message_color, message_rect)
    pygame.draw.rect(screen, key_color, key_rect)

    # superimposing text onto our buttons
    screen.blit(encrypt, (width / 2+ 10 , height / 1.5))
    screen.blit(decrypt, (width / 4+ 10 , height / 1.5))
    screen.blit(message, (width / 2.5 , height / 3.5))
    screen.blit(key, (width / 2.2, height / 2.2))
    screen.blit(title, (width / 4, height / 8))
    screen.blit(message_input, (message_rect.x +10, message_rect.y +10))
    screen.blit(key_input, (key_rect.x +10, key_rect.y +10))

    # updates the frames of the game
    pygame.display.update()
