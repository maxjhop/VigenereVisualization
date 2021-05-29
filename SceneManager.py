import pygame
from Cipher import Encrypt, Decrypt
from table import *
from button_class import button

class SceneManager:
    def __init__(self):
        self.scene = self

    def Input(self, events, pressed_keys, mouse):
        print("Input not overridden")

    def Render(self, screen, mouse):
        print("Render not overriden")

    def update(self, screen, cursize):
        return None

    def SwitchToScene(self, next_scene):
        self.scene = next_scene

    def Terminate(self):
        self.SwitchToScene(None)



class ButtonScene(SceneManager):
    def __init__(self, message, key, result, steps, mode):
        SceneManager.__init__(self)

        print("BUTTON SCENE INIT")
        self.table = Table()
        self.result = result
        self.steps = steps
        self.mode = mode

        print("Result: {}".format(self.result))

        self.pace = 5
        self.updateSpeed = (30 / self.pace) * 5

        self.paused = False # Used to pause the game

        self.mainSurfaceSize = (0, 0) # Hold the size of the main Surface. Updated in self.update
        self.mainDisplay = pygame.Surface((1, 1)) # Holds the actual main display. Random initial value will be overwritten by self.update

        self.inst = steps
        self.ind = 0
        
        self.timer = 0

        # white color
        self.color = (255, 255, 255)
        self.color_dark = (100, 100, 100)

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 25)

        self.message = self.smallfont.render(message, True, self.color_dark)
        self.key = self.smallfont.render(key, True, self.color_dark)
        self.result = self.smallfont.render(result, True, self.color_dark)

        # rendering a text written in this font
        self.menu = self.smallfont.render('Go Back', True, self.color)
        self.play = self.smallfont.render('Play', True, self.color)
        self.pause = self.smallfont.render('Pause', True, self.color)
        self.forw = self.smallfont.render('Step Forward', True, self.color)
        self.back = self.smallfont.render('Step Back', True, self.color)
        self.up = self.smallfont.render('Speed Up', True, self.color)
        self.down = self.smallfont.render('Slow Down', True, self.color)
        self.res = self.smallfont.render('Restart', True, self.color)

        # buttons and their locations
        play_button = button(5, self.play, lambda: self.togglePause(False))
        pause_button = button(40, self.pause, lambda: self.togglePause(True))
        forw_button = button(75, self.forw, lambda: self.stepForward())
        back_button = button(110, self.back, lambda: self.stepBack())
        up_button = button(145, self.up, lambda: self.speedUp())
        down_button = button(180, self.down, lambda: self.slowDown())
        res_button = button(215, self.res, lambda: self.restart())
        menu_button = button(250, self.menu, lambda: self.SwitchToScene(MainMenu()))

        self.buttons = [menu_button, play_button, pause_button, forw_button, back_button, up_button, down_button,
                        res_button]

        self.messageText = self.smallfont.render(f"message: ", True, self.color_dark)
        self.keyText = self.smallfont.render(f"key: ", True, self.color_dark)
        self.resultText = self.smallfont.render(f"result: ", True, self.color_dark)


        """
        while True:

            # stores the (x,y) coordinates into
            # the variable as a tuple
            mouse = pygame.mouse.get_pos()

            # fills the screen with a color
            screen.fill((50, 100, 0))
        """

    # Updates the self.updateSpeed variable so the self.update() function makes update
    # to the board at the appropriate rate
    def updatePace(self):
        self.updateSpeed = (30 // self.pace) * 5
        return None

    # This function makes the animation play slower. It is called on the 'slow down'
    # button presses by the user
    def slowDown(self):
        if (self.pace > 1): # Minimum pace is 1

            # decrement the current pace
            self.pace -= 1

            # update the 'self.updateSpeed' variable with this function call. Having
            # a separate function may be unecessary for this but it works. 
            self.updatePace()
        return None

    # This function makes the animation play faster. It is called on the 'speed up'
    # button presses by the user
    def speedUp(self):
        if (self.pace < 10): # Max pace is 10

            # increment the current pace
            self.pace += 1

            # update the 'self.updateSpeed' variable with this function call. Having
            # a separate function may be unecessary for this but it works. 
            self.updatePace()
        return None

    # This function displays the previous step in the animation. It can only
    # be called if the animation is currently paused. It is called on the 'step back'
    # button presses by the user.
    def stepBack(self):
        if (self.paused): # if the animation is currently paused

            # since self.ind generally points to the next step to be shown, the index needs to be
            # decremented by 2 in order to get the previous step. 
            self.ind = (self.ind - 2) % len(self.inst)

            # display the previous step in the animation
            self.displayBoard(self.ind)

            # increment the index in order to point to the next step to be played
            self.ind = (self.ind + 1) % len(self.inst)
        return None

    # This function displays the next sequential step in the animation. It can only
    # be called if the animation is currently paused. It is called on the 'step forward'
    # button presses by the user.
    def stepForward(self):
        if (self.paused): # if the animation is currently paused

            self.displayBoard(self.ind) # display the next step in the animation
            
            self.ind = (self.ind + 1) % len(self.inst) # increment the index
        return None

    # This function stops the current animation process and starts it over from the
    # first step. It is called on the 'restart' button presses by the user
    def restart(self):
        # pause the animation so it can't continue to play while it is being reset
        self.paused = True

        # Clear the table of any highlights with the table.refresh method
        self.table.refresh()

        # Call self.displayBoard to show the very first step in the animation
        self.displayBoard(0)

        # Reset the current instruction index
        self.ind = 0

        # Could possibly have something like "self.paused = False" if we want the animation
        # to start playing automatically after it has been reset. For now the animation stays paused
        # after resetting and the user has to click 'play' in order to resume the visualization
        return None

    # Toggles the value of the self.pause variable. This is called on the
    # 'pause'/'play' button presses by the user. A value of true pauses the visualization,
    # and a value of false resumes/plays the animation. 
    def togglePause(self, value):
        self.paused = value

    def Input(self, events, pressed_keys, mouse):
        for ev in events:
            """
            if ev.type == pygame.QUIT:
                pygame.quit()
            """
            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on a
                # button the game does the thing
                for i in self.buttons:
                    if i.hover(mouse):
                        i.click()

    def Render(self, screen, mouse):
        #screen.fill((255, 255, 165))
        # drawing buttons
        for i in self.buttons:
            i.draw(screen)

        screen.blit(self.messageText, (5, 285))
        screen.blit(self.message, (5, 305))
        screen.blit(self.keyText, (5, 345))
        screen.blit(self.key, (5, 365))
        screen.blit(self.resultText, (5, 405))
        screen.blit(self.result, (5, 425))

    # This function handles all functionality related to updating the table display for the scene.
    # The argument 'index' refers to an index into the instruction list, so that the correct
    # rows and columns get highlighted
    def displayBoard(self, index):
        # Fill the screen with a yellowish background. Probably not the best to completely refill
        # the background on every update. It might be better to fill the background on initialization
        # in order to cover the previous scene. But this works for now.
        self.mainDisplay.fill((255, 255, 165))

        # Redraw the buttons and message/keyword/result every update because they are covered by the
        # previous line which fills the entire screen. 
        self.Render(self.mainDisplay, None)

        # Change table position based on screen size. If main screen size changes, the table will align itself
        # to the very right edge of the screen to make as much room for the buttons and message/keyword/result text
        # as possible. Not sure what happens when screen size is smaller than the table size 
        x = self.mainBoardSize[0] - 850
        
        if (self.mode == 0): # if current mode is encryption
            # Call table.displayEncrypt
            self.table.displayEncrypt(self.inst[index][1], self.inst[index][0])
        else: # if current mode is decryption
            # Call table.displayDecrypt
            self.table.displayDecrypt(self.inst[index][1], self.inst[index][0])

        # blit (copy) the table onto the main button scene display at the correct position
        self.mainDisplay.blit(self.table.screen, (x, 10))
        return None

    # This function is called once per game loop in the main.py file. It adds functionality
    # for updating the screen at a certain pace
    def update(self, board, size):
        self.mainBoardSize = size
        self.mainDisplay = board
        x = self.mainBoardSize[0] - 850
        self.mainDisplay.fill((255, 255, 165))
        self.mainDisplay.blit(self.table.screen, (x, 10))
        self.Render(self.mainDisplay, None)
        if (not self.paused): # if the game is paused, the board should not update

            if (self.timer == 0): # every time the timer == 0, the board updates

                # Call the display board funtion which handles all of the functionality
                # for actually displaying the updates to the board
                self.displayBoard(self.ind)

                # Increment the instruction index. Modulo for wrap around, so the animation
                # plays on repeat
                self.ind = (self.ind + 1) % len(self.inst)

                # We could possibly include a feature that pauses the animation when we have reached the end,
                # so that it is clear that the end of the process has been reached
                
            # Increment the timer using modulo, so whenever (timer + 1) == updateSpeed,
            # the result of modulo division will be 0, and the board will update
            self.timer = (self.timer + 1) % self.updateSpeed
        return None

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





        self.message_color = self.color
        self.key_color = self.color
        self.message_active = False
        self.key_active = False
        self.message_text = ''
        self.key_text = ''

        self.menu = self.smallfont.render('Back to Main Menu', True, self.color)


        self.validCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

    def Input(self, events, pressed_keys, mouse):
        for ev in events:
            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                for i in self.buttons:
                    if i.hover(mouse):
                        i.click()

                # if the mouse is clicked on the Encryption
                # button the game is terminated
                if self.encrypt_rect.collidepoint(ev.pos):
                    #pygame.quit()
                    result = Encrypt(self.message_text, self.key_text)
                    if (result is None):
                        print("ERROR CANNOT ENCRYPT NOTHING!")
                        return None
                    self.SwitchToScene(ButtonScene(result[2], result[3], result[0], result[1], 0))

                if self.decrypt_rect.collidepoint(ev.pos):
                    #pygame.quit()
                    result = Decrypt(self.message_text, self.key_text)
                    if (result is None):
                        print("ERROR CANNOT DECRYPT NOTHING!")
                        return None
                    self.SwitchToScene(ButtonScene(result[2], result[3], result[0], result[1], 1))

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
                    elif ev.unicode in self.validCharacters and len(self.message_text) <= 19:
                        self.message_text += ev.unicode



                elif self.key_active:
                    if ev.key == pygame.K_BACKSPACE:
                        self.key_text = self.key_text[:-1]
                    elif ev.unicode in self.validCharacters and len(self.key_text) <= 19:
                        self.key_text += ev.unicode

    def Render(self, screen, mouse):
        # fills the screen with a color
        screen.fill((255, 255, 165))

        pygame.draw.rect

        self.encrypt_rect = pygame.Rect(self.width / 2 + 50, self.height / 1.7, 140, 40)
        self.decrypt_rect = pygame.Rect(self.width / 2 - 200, self.height / 1.7, 140, 40)
        self.message_rect = pygame.Rect(self.width / 2 - 150, self.height / 4.2, 300, 40)
        self.key_rect = pygame.Rect(self.width / 2 - 150, self.height / 2.5, 300, 40)
        menu_button = button(self.height / 1.3, self.menu, lambda: self.SwitchToScene(StartMenu()), self.width / 2 - 140,
                             280, 40)

        self.buttons = [menu_button]

        for i in self.buttons:
            i.draw(screen)

        # if mouse is hovered over encrypt it
        # changes to lighter shade
        if self.width / 2 + 50 <= mouse[0] <= self.width / 2 + 50 + 140 and self.height / 1.7 <= mouse[1] <= self.height / 1.7 + 40:
            pygame.draw.rect(screen, self.color_light, self.encrypt_rect)

        else:
            pygame.draw.rect(screen, self.color_dark, self.encrypt_rect)

        # if mouse is hovered over decrypt it
        # changes to lighter shade
        if self.width / 2 - 200 <= mouse[0] <= self.width / 2 - 200 + 140 and self.height / 1.7 <= mouse[1] <= self.height / 1.7 + 40:
            pygame.draw.rect(screen, self.color_light, self.decrypt_rect)

        else:
            pygame.draw.rect(screen, self.color_dark, self.decrypt_rect)

        message_input = self.input_smallfont.render(self.message_text, True, self.color_dark)
        key_input = self.input_smallfont.render(self.key_text, True, self.color_dark)

        pygame.draw.rect(screen, self.message_color, self.message_rect)
        pygame.draw.rect(screen, self.key_color, self.key_rect)

        # superimposing text onto our buttons
        screen.blit(self.encrypt, (self.encrypt_rect.x + 10, self.encrypt_rect.y))
        screen.blit(self.decrypt, (self.decrypt_rect.x + 10, self.decrypt_rect.y))

        screen.blit(self.message, (self.width / 2 - 60, self.height / 3.5))
        screen.blit(self.key, (self.width / 2 - 30, self.height / 2.2))
        screen.blit(self.title, (self.width / 2 - 200, self.height / 8))
        screen.blit(message_input, (self.message_rect.x + 10, self.message_rect.y + 10))
        screen.blit(key_input, (self.key_rect.x + 10, self.key_rect.y + 10))

    def update(self, board, size):
        self.width = size[0]
        self.height = size[1]

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
        self.buttons = []


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

        menu_button = button(self.height / 4.2, self.menu, lambda: self.SwitchToScene(MainMenu()), self.width / 2 - 140,
                             250, 40)
        info_button = button(self.height / 2.7, self.info, lambda: self.SwitchToScene(InfoMenu()), self.width / 2 - 140,
                             250, 40, 100)
        quit_button = button(self.height / 2, self.quit, lambda: pygame.quit(), self.width / 2 - 140, 250, 40, 100)
        self.buttons = [menu_button, info_button, quit_button]

        for i in self.buttons:
            i.draw(screen)
        screen.blit(self.title, (self.width / 2 - 200, self.height / 8))

    def update(self, screen, cursize):
        self.width = cursize[0]
        self.height = cursize[1]

class InfoMenu(SceneManager):
    def __init__(self):
        SceneManager.__init__(self)
        print("Information")

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
        self.about = self.smallfont.render('About Ciphers', True, self.color)
        self.use = self.smallfont.render('About This Tool', True, self.color)
        self.menu = self.smallfont.render("Go Back", True, self.color)
        self.information = self.smallfont.render("Information", True, self.color_dark)





    def Input(self, events, pressed_keys, mouse):
        for ev in events:
            """
            if ev.type == pygame.QUIT:
                pygame.quit()
            """
            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on a
                # button the game does the thing
                for i in self.buttons:
                    if i.hover(mouse):
                        i.click()

    def Render(self, screen, mouse):
        # fills the screen with a color
        screen.fill((255, 255, 165))
        # buttons and their locations/functions
        about_button = button(self.height / 4.7, self.about, lambda: self.SwitchToScene(AboutCi_1()),
                              self.width / 2 - 140,
                              250, 40, 30)
        use_button = button(self.height / 2.8, self.use, lambda: self.SwitchToScene(Uses_1()), self.width / 2 - 140,
                            250, 40, 20)

        menu_button = button(self.height / 2, self.menu, lambda: self.SwitchToScene(StartMenu()),
                             self.width / 2 - 140,
                             250, 40, 70)

        self.buttons = [menu_button, about_button, use_button]

        for i in self.buttons:
            i.draw(screen)

        #Menu title
        screen.blit(self.information, (self.width / 2 - 100, self.height / 8))

    def update(self, board, size):
        self.width = size[0]
        self.height = size[1]

class Uses_1(SceneManager):
    def __init__(self):
        SceneManager.__init__(self)
        print("Information")

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

        self.x2 = 75

        self.y2 = 30

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.input_smallfont = pygame.font.SysFont('Corbel', 24)

        # rendering a text written in
        # this font
        self.next = self.smallfont.render('Next', True, self.color)
        self.menu = self.smallfont.render("Main Menu", True, self.color)
        self.title = self.smallfont.render("Using this tool", True, self.color_dark)




    def Input(self, events, pressed_keys, mouse):
        for ev in events:
            """
            if ev.type == pygame.QUIT:
                pygame.quit()
            """
            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on a
                # button the game does the thing
                for i in self.buttons:
                    if i.hover(mouse):
                        i.click()

    def Render(self, screen, mouse):
        # fills the screen with a color
        screen.fill((255, 255, 165))
        # buttons and their locations/functions
        menu_button = button(self.height / 1.1, self.menu, lambda: self.SwitchToScene(StartMenu()), self.width / 2 + 350,
                             170, 40)
        next_button = button(self.height / 1.1, self.next, lambda: self.SwitchToScene(Uses_2()),
                             self.width / 2 - 500, 80, 40)

        self.buttons = [menu_button, next_button]

        for i in self.buttons:
            i.draw(screen)

        #Title
        screen.blit(self.title, (self.width / 2 - 100, self.height / 30))

        #Information

    def update(self, board, size):
        self.width = size[0]
        self.height = size[1]

class Uses_2(SceneManager):
    def __init__(self):
        SceneManager.__init__(self)
        print("Information")

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

        self.x2 = 75

        self.y2 = 30

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.input_smallfont = pygame.font.SysFont('Corbel', 24)

        # rendering a text written in
        # this font
        self.back = self.smallfont.render('Back', True, self.color)
        self.menu = self.smallfont.render("Main Menu", True, self.color)
        self.next = self.smallfont.render("Next", True, self.color)
        self.title = self.smallfont.render("Using this tool2", True, self.color_dark)


        # buttons and their locations/functions
        menu_button = button(self.height - 20, self.menu, lambda: self.SwitchToScene(StartMenu()), x1 = 20)
        back_button = button(self.height - 20, self.next, lambda: self.SwitchToScene(Uses_1()), x1 = self.width - 20 - self.x2)

        self.buttons = [menu_button, back_button]

    def Input(self, events, pressed_keys, mouse):
        for ev in events:
            """
            if ev.type == pygame.QUIT:
                pygame.quit()
            """
            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on a
                # button the game does the thing
                for i in self.buttons:
                    if i.hover(mouse):
                        i.click()

    def Render(self, screen, mouse):
        # fills the screen with a color
        screen.fill((255, 255, 165))

        for i in self.buttons:
            i.draw(screen)

        #Title
        screen.blit(self.title, (self.width / 2.5, self.height / 3.5))

        #Information

    def update(self, board, size):
        return None


class AboutCi_1(SceneManager):
    def __init__(self):
        SceneManager.__init__(self)
        print("Information")

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

        self.x2 = 75

        self.y2 = 30

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.input_smallfont = pygame.font.SysFont('Corbel', 24)

        # rendering a text written in
        # this font
        self.next = self.smallfont.render('Next (Vigenere Cipher)', True, self.color)
        self.menu = self.smallfont.render("Main Menu", True, self.color)
        self.ciphers = self.smallfont.render("Ciphers", True, self.color_dark)


        # buttons and their locations/functions
        menu_button = button(self.height - 20, self.menu, lambda: self.SwitchToScene(StartMenu()), x1 = 20)
        next_button = button(self.height - 20, self.next, lambda: self.SwitchToScene(AboutCi_2()), x1 = self.width - 20 - self.x2)

        self.buttons = [menu_button, next_button]

    def Input(self, events, pressed_keys, mouse):
        for ev in events:
            """
            if ev.type == pygame.QUIT:
                pygame.quit()
            """
            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on a
                # button the game does the thing
                for i in self.buttons:
                    if i.hover(mouse):
                        i.click()

    def Render(self, screen, mouse):
        # fills the screen with a color
        screen.fill((255, 255, 165))

        for i in self.buttons:
            i.draw(screen)

        #Title
        screen.blit(self.ciphers, (self.width / 2.5, self.height / 3.5))

        #Information

    def update(self, board, size):
        return None


class AboutCi_2(SceneManager):
    def __init__(self):
        SceneManager.__init__(self)
        print("Information")

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

        self.x2 = 75

        self.y2 = 30

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.input_smallfont = pygame.font.SysFont('Corbel', 24)

        # rendering a text written in
        # this font
        self.back = self.smallfont.render('Back', True, self.color)
        self.menu = self.smallfont.render("Main Menu", True, self.color)
        self.title = self.smallfont.render("The Vigenere Cipher", True, self.color_dark)
        self.next = self.smallfont.render('Next', True, self.color)


        # buttons and their locations/functions
        menu_button = button(self.height - 20, self.menu, lambda: self.SwitchToScene(StartMenu()), x1 = 20)
        back_button = button(self.height - 20, self.next, lambda: self.SwitchToScene(AboutCi_1()), x1 = self.width - 20 - self.x2)

        self.buttons = [menu_button, back_button]

    def Input(self, events, pressed_keys, mouse):
        for ev in events:
            """
            if ev.type == pygame.QUIT:
                pygame.quit()
            """
            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on a
                # button the game does the thing
                for i in self.buttons:
                    if i.hover(mouse):
                        i.click()

    def Render(self, screen, mouse):
        # fills the screen with a color
        screen.fill((255, 255, 165))

        for i in self.buttons:
            i.draw(screen)

        #Title
        screen.blit(self.title, (self.width / 2.5, self.height / 3.5))

        #Information

    def update(self, board, size):
        return None
