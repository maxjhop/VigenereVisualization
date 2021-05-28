"""
This is the main project file for the Vigenere Cipher Visualization
Authors: Joshua Fawcett, Max Hopkins, Meghan Riehl, Yuyao Zhuge

Citations:
Starter code for basic pygame window was pulled from:
https://www.geeksforgeeks.org/creating-start-menu-in-pygame/

Inspiration for class setup/scene managers:
https://nerdparadise.com/programming/pygame/part7
"""
import pygame
import sys
from SceneManager import *


class MainMenu(SceneManager):
    def __init__(self):
        SceneManager.__init__(self)
        # white color
        self.color = (255, 255, 255)

        # light shade of the button
        self.color_light = (170, 170, 170)

        # dark shade of the button
        self.color_dark = (100, 100, 100)

        # stores the width of the
        # screen into a variable
        self.width = 720

        # stores the height of the
        # screen into a variable
        self.height = 720

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.input_smallfont = pygame.font.SysFont('Corbel', 24)

        # rendering a text written in
        # this font
        self.encrypt = self.smallfont.render('encrypt', True, self.color)
        self.decrypt = self.smallfont.render('decrypt', True, self.color)
        self.message = self.smallfont.render("message", True, self.color_dark)
        self.key = self.smallfont.render("key", True, self.color_dark)
        self.title = self.smallfont.render("Vigenere Visualization Tool", True, self.color_dark)

        self.encrypt_rect = pygame.Rect(self.width / 2, self.height / 1.5, 140, 40)
        self.decrypt_rect = pygame.Rect(self.width / 4, self.height / 1.5, 140, 40)
        self.message_rect = pygame.Rect(self.width / 3.5, self.height / 4.2, 300, 40)
        self.key_rect = pygame.Rect(self.width / 3.5, self.height / 2.5, 300, 40)

        self.message_color = self.color
        self.key_color = self.color
        self.message_active = False
        self.key_active = False
        self.message_text = ''
        self.key_text = ''

    def Input(self, events, pressed_keys, mouse):
        for ev in events:
            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the Encryption
                # button the game is terminated
                if self.width / 2 <= mouse[0] <= self.width / 2 + 140 and self.height / 1.5 <= mouse[1] <= self.height / 1.5 + 40:
                    #pygame.quit()
                    self.SwitchToScene(ButtonScene())

                if self.width / 4 <= mouse[0] <= self.width / 4 + 140 and self.height / 1.5 <= mouse[1] <= self.height / 1.5 + 40:
                    #pygame.quit()
                    self.SwitchToScene(ButtonScene())

                if self.message_rect.collidepoint(ev.pos):
                    self.message_active = True
                    self.message_color = self.color_light
                    self.key_color = self.color
                    self.key_active = False

                if self.key_rect.collidepoint(ev.pos):
                    self.key_active = True
                    self.key_color = self.color_light
                    self.message_color = self.color
                    self.message_active = False

            if ev.type == pygame.KEYDOWN:

                if self.message_active:
                    if ev.key == pygame.K_BACKSPACE:
                        self.message_text = self.message_text[:-1]
                    else:
                        self.message_text += ev.unicode
                elif self.key_active:
                    if ev.key == pygame.K_BACKSPACE:
                        self.key_text = self.key_text[:-1]
                    else:
                        self.key_text += ev.unicode

    def Render(self, screen, mouse):
        # fills the screen with a color
        screen.fill((255, 255, 165))

        pygame.draw.rect

        # if mouse is hovered over encrypt it
        # changes to lighter shade
        if self.width / 2 <= mouse[0] <= self.width / 2 + 140 and self.height / 1.5 <= mouse[1] <= self.height / 1.5 + 40:
            pygame.draw.rect(screen, self.color_light, self.encrypt_rect)

        else:
            pygame.draw.rect(screen, self.color_dark, self.encrypt_rect)

        # if mouse is hovered over decrypt it
        # changes to lighter shade
        if self.width / 4 <= mouse[0] <= self.width / 4 + 140 and self.height / 1.5 <= mouse[1] <= self.height / 1.5 + 40:
            pygame.draw.rect(screen, self.color_light, self.decrypt_rect)

        else:
            pygame.draw.rect(screen, self.color_dark, self.decrypt_rect)

        message_input = self.input_smallfont.render(self.message_text, True, self.color_dark)
        key_input = self.input_smallfont.render(self.key_text, True, self.color_dark)

        pygame.draw.rect(screen, self.message_color, self.message_rect)
        pygame.draw.rect(screen, self.key_color, self.key_rect)

        # superimposing text onto our buttons
        screen.blit(self.encrypt, (self.width / 2 + 10, self.height / 1.5))
        screen.blit(self.decrypt, (self.width / 4 + 10, self.height / 1.5))

        screen.blit(self.message, (self.width / 2.5, self.height / 3.5))
        screen.blit(self.key, (self.width / 2.2, self.height / 2.2))
        screen.blit(self.title, (self.width / 4, self.height / 8))
        screen.blit(message_input, (self.message_rect.x + 10, self.message_rect.y + 10))
        screen.blit(key_input, (self.key_rect.x + 10, self.key_rect.y + 10))


FPS = 30

def main():

    # initializing the constructor
    pygame.init()
    scene = MainMenu()

    fpsClock = pygame.time.Clock()

    # screen resolution
    res = (1100, 800)

    # opens up a window
    screen = pygame.display.set_mode(res, pygame.RESIZABLE)

    active_scene = scene

    cursize = res

    while True:
        events = pygame.event.get()
        pressed_keys = pygame.key.get_pressed()
        for ev in events:

            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.VIDEORESIZE:
                cursize = ev.size

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        active_scene.Input(events, pressed_keys, mouse)
        active_scene.Render(screen, mouse)
        active_scene.update(screen, cursize)

        active_scene = active_scene.scene

        # updates the frames of the game
        pygame.display.update()

        fpsClock.tick(FPS)









if __name__ == "__main__":
    main()
