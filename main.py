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

def main():

    # initializing the constructor
    pygame.init()
    scene = MainMenu()

    # screen resolution
    res = (720, 720)

    # opens up a window
    screen = pygame.display.set_mode(res)

    active_scene = scene

    while True:
        events = pygame.event.get()
        pressed_keys = pygame.key.get_pressed()
        for ev in events:

            if ev.type == pygame.QUIT:
                pygame.quit()
            elif ev.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        active_scene.Input(events, pressed_keys, mouse)
        active_scene.Render(screen, mouse)

        active_scene = active_scene.scene

        # updates the frames of the game
        pygame.display.update()



if __name__ == "__main__":
    main()
