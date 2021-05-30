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


class StartMenu(SceneManager):
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
        self.width = 1100

        # stores the height of the
        # screen into a variable
        self.height = 800

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.input_smallfont = pygame.font.SysFont('Corbel', 24)

        # rendering a text written in
        # this font
        self.title = self.smallfont.render("Vigenere Visualization Tool", True, self.color_dark)
        self.menu = self.smallfont.render('Visualization Tool', True, self.color)
        self.info = self.smallfont.render('Info', True, self.color)
        self.quit = self.smallfont.render('Quit', True, self.color)

        menu_button = button(self.height / 4.2, self.menu, lambda: self.SwitchToScene(MainMenu()), self.width / 2 - 140, 250, 40)
        info_button = button(self.height / 2.7, self.info, lambda: print("info"), self.width / 2 - 140, 250, 40, 100)
        quit_button = button(self.height / 2, self.quit, lambda : pygame.quit(), self.width / 2 - 140, 250, 40, 100)

        self.buttons = [menu_button, info_button, quit_button]

    def Input(self, events, pressed_keys, mouse):
        for ev in events:
            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                for i in self.buttons:
                    if i.hover(mouse):
                        i.click()

    def Render(self, screen, mouse):
        # fills the screen with a color
        screen.fill((255, 255, 165))

        pygame.draw.rect

        for i in self.buttons:
            i.draw(screen)
        screen.blit(self.title, (self.width / 2 - 200, self.height / 8))



FPS = 30

def main():

    # initializing the constructor
    pygame.init()
    scene = StartMenu()

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
        #active_scene.update(screen, cursize)

        active_scene = active_scene.scene

        # updates the frames of the game
        pygame.display.update()

        fpsClock.tick(FPS)









if __name__ == "__main__":
    main()
