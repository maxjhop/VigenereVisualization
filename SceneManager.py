import pygame
from Cipher import Encrypt, Decrypt
from table import *
from button_class import button
from TextHighlight import *

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
        self.displayText = Text_And_Highlight()
        self.result = result
        self.steps = steps
        self.mode = mode

        self.message = message
        self.key = key
        self.result = result

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
        #dark grey
        self.color_dark = (100, 100, 100)
        #Green colors for play button
        self.light_green = (0, 204, 0)
        self.dark_green =(0, 102, 0)

        #Red colors for paused button
        self.light_red = (255, 102, 102)
        self.dark_red = (153, 0, 0)

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 25)
        self.font = pg.font.SysFont("FreeSans", 28, bold=True)


        #self.message = self.smallfont.render(message, True, self.color_dark)
        #self.key = self.smallfont.render(key, True, self.color_dark)
        #self.result = self.smallfont.render(result, True, self.color_dark)

        # rendering a text written in this font
        self.menu = self.smallfont.render('Go Back', True, self.color)
        self.play = self.smallfont.render('Playing', True, self.color)
        self.pause = self.smallfont.render('Paused', True, self.color)
        self.forw = self.smallfont.render('Step Forward', True, self.color)
        self.back = self.smallfont.render('Step Back', True, self.color)
        self.up = self.smallfont.render('Speed Up', True, self.color)
        self.down = self.smallfont.render('Slow Down', True, self.color)
        self.res = self.smallfont.render('Restart', True, self.color)
        self.encryptText = self.font.render('Encrypting', True, self.color_dark)
        self.decryptText = self.font.render('Decrypting', True, self.color_dark)
        self.PlayPause = self.play




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
    def togglePause(self):
        if self.paused:
            self.PlayPause = self.play
            self.paused = False
        else:
            self.paused = True
            self.PlayPause = self.pause

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
        # buttons and their locations
        if self.paused:
            play_button = button(40, self.PlayPause, lambda: self.togglePause(), color_light=self.light_red,
                                 color_dark=self.dark_red)
        else:
            play_button = button(40, self.PlayPause, lambda: self.togglePause(), color_light=self.light_green,
                                 color_dark=self.dark_green)

        forw_button = button(75, self.forw, lambda: self.stepForward())
        back_button = button(110, self.back, lambda: self.stepBack())
        up_button = button(145, self.up, lambda: self.speedUp())
        down_button = button(180, self.down, lambda: self.slowDown())
        res_button = button(215, self.res, lambda: self.restart())
        menu_button = button(250, self.menu, lambda: self.SwitchToScene(MainMenu()))

        self.buttons = [menu_button, play_button, forw_button, back_button, up_button, down_button,
                        res_button]

        self.mainDisplay.blit(self.displayText.screen, (0, 500))
        self.displayText.write_letter(self.message.upper(), self.key.upper(), self.result.upper())
        
        for i in self.buttons:
            i.draw(screen)


        if self.mode == 0:
            screen.blit(self.encryptText, (5, 5))
        elif self.mode == 1:
            screen.blit(self.decryptText, (5, 5))

        #screen.blit(self.messageText, (5, 285))
        #screen.blit(self.message, (5, 305))
        #screen.blit(self.keyText, (5, 345))
        #screen.blit(self.key, (5, 365))
        #screen.blit(self.resultText, (5, 405))
        #screen.blit(self.result, (5, 425))

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
        x = (self.mainBoardSize[0] / 2) - 300
        
        if (self.mode == 0): # if current mode is encryption
            # Call table.displayEncrypt
            self.table.displayEncrypt(self.inst[index][1], self.inst[index][0])
        else: # if current mode is decryption
            # Call table.displayDecrypt
            self.table.displayDecrypt(self.inst[index][1], self.inst[index][0])

        self.displayText.highlight(index, self.mode)

        # blit (copy) the table onto the main button scene display at the correct position
        self.mainDisplay.blit(self.table.screen, (x, 10))
        return None

    # This function is called once per game loop in the main.py file. It adds functionality
    # for updating the screen at a certain pace
    def update(self, board, size):
        self.mainBoardSize = size
        self.mainDisplay = board
        x = (self.mainBoardSize[0] / 2) - 300
        self.mainDisplay.fill((255, 255, 165))

        self.Render(self.mainDisplay, None)
        self.mainDisplay.blit(self.table.screen, (x, 10))
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

        # Dark red for error message
        self.color_darkred = (55, 0, 0)

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
        self.error_message = self.smallfont.render("Error: please input a valid key/message", True, self.color_darkred)

        # Error boolean
        self.error = False





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
                        self.error = True
                        print("ERROR CANNOT ENCRYPT NOTHING!")
                        return None
                    self.SwitchToScene(ButtonScene(result[2], result[3], result[0], result[1], 0))

                if self.decrypt_rect.collidepoint(ev.pos):
                    #pygame.quit()
                    result = Decrypt(self.message_text, self.key_text)
                    if (result is None):
                        self.error = True
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
        if self.error:
            screen.blit(self.error_message, (self.width / 2 - 275, self.height / 1.5))

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
        self.importantfont = pygame.font.SysFont('Corbel', 45, bold=True)
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.input_smallfont = pygame.font.SysFont('Corbel', 24)

        # rendering a text written in
        # this font
        self.title = self.smallfont.render("Vigenere Visualization Tool", True, self.color_dark)
        self.menu = self.smallfont.render('Visualization Tool', True, self.color)
        self.info = self.smallfont.render('Info', True, self.color)
        self.quit = self.smallfont.render('Quit', True, self.color)
        self.important = self.importantfont.render("Best used in fullscreen!", True, self.color_dark)
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
        screen.blit(self.important, (self.width / 2 - 225, self.height / 1.5))

    def update(self, screen, cursize):
        self.width = cursize[0]
        self.height = cursize[1]

class InfoMenu(SceneManager):
    def __init__(self):
        SceneManager.__init__(self)
        #print("Information")

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
        about_button = button(self.height / 4.7, self.about, lambda: self.SwitchToScene(About()),
                              self.width / 2 - 140,
                              250, 40, 30)
        use_button = button(self.height / 2.8, self.use, lambda: self.SwitchToScene(Use()), self.width / 2 - 140,
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

class Use(SceneManager):
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
        self.titlefont = pygame.font.SysFont('Corbel', 50, bold = True)
        self.heading = pygame.font.SysFont('Corbel', 35, bold = True)
        self.input_smallfont = pygame.font.SysFont('Corbel', 24)

        # rendering button and title text
        self.menu = self.smallfont.render("Main Menu", True, self.color)
        self.other = self.smallfont.render("Cipher Information", True, self.color)
        self.title = self.titlefont.render("Using this tool", True, self.color_dark)

        # rendering information text
        self.text1 = self.smallfont.render("This tool is a visualization of the Vigenere cipher, it can encrypt and decrypt short messages when ", True, self.color_dark)
        self.text2 = self.smallfont.render("given a key. It is meant to be a learning/ teaching tool to better understand how the Vigenere cipher works,", True, self.color_dark)
        self.text3 = self.smallfont.render("not a robust encryption/decryption software that can break encryptions", True, self.color_dark)

        self.sub1 = self.heading.render("How to use this tool", True, self.color_dark)
        self.ins1 = self.smallfont.render("1. From the Main Menu, click on 'Visualization Tool'", True, self.color_dark)
        self.ins2 = self.smallfont.render("2. Input the text you want encrypted or decryped in the 'message' box", True, self.color_dark)
        self.ins3 = self.smallfont.render("3. Input the key you want or need used to either encrypty or decrypt the text in the 'key' box", True, self.color_dark)
        self.ins4 = self.smallfont.render("4. Click on either 'encrypt' or 'decrypt' to process the text", True, self.color_dark)

        self.sub2 = self.heading.render("Controls", True, self.color_dark)

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
        other_button = button(self.height / 1.1, self.other, lambda: self.SwitchToScene(About()),
                             self.width / 2 - 500, 270, 40)

        self.buttons = [menu_button, other_button]

        for i in self.buttons:
            i.draw(screen)

        #Title
        screen.blit(self.title, (self.width / 2 - 150, self.height / 30))

        #Information
        screen.blit(self.text1, (self.width / 2 - 625, 120))
        screen.blit(self.text2, (self.width / 2 - 725, 170))
        screen.blit(self.text3, (self.width / 2 - 725, 220))

        screen.blit(self.sub1, (75, 300))
        screen.blit(self.ins1, (150, 350))
        screen.blit(self.ins2, (150, 400))
        screen.blit(self.ins3, (150, 450))
        screen.blit(self.ins4, (150, 500))

        screen.blit(self.sub2, (75, 580))

    def update(self, board, size):
        self.width = size[0]
        self.height = size[1]


class About(SceneManager):
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
        self.smallerfont = pygame.font.SysFont('Corbel', 30)
        self.titlefont = pygame.font.SysFont('Corbel', 40, bold = True)
        self.heading = pygame.font.SysFont('Corbel', 35, bold = True)
        self.input_smallfont = pygame.font.SysFont('Corbel', 24)

        # rendering button and title text
        self.menu = self.smallfont.render("Main Menu", True, self.color)
        self.other = self.smallfont.render("Tool Information", True, self.color)
        self.title = self.titlefont.render("Some information on Ciphers", True, self.color_dark)

        #rendering information text
        self.sub1 = self.heading.render("What is a cipher?", True, self.color_dark)
        self.text1 = self.smallfont.render("A cipher is a system in which plain text is encoded via transposition or subsititution according to", True, self.color_dark)
        self.text2 = self.smallfont.render("predetermined system. Some betterknown examples are the Caesar cipher, Enigma code, Morse code, ", True, self.color_dark)
        self.text3 = self.smallfont.render("and even smoke signals. This tool is a visualization of the vigenere cipher.", True, self.color_dark)

        self.sub2 = self.heading.render("The Vigenere Cipher", True, self.color_dark)
        self.txt1 = self.smallerfont.render("First descriped in 1553 it remained unbroken for three centries and gained the title 'le chiffre indechiffrable'", True, self.color_dark)
        self.txt2 = self.smallerfont.render("or 'the indecipherable cipher'. The Vigenere cipher uses two alphabets, one for the text to be altered and", True, self.color_dark)
        self.txt3 = self.smallerfont.render("another for the keyword. These two alphabets form a grid of letters, shifting to the left every row/column.", True, self.color_dark)
        self.txt4 = self.smallerfont.render("The colums are for the text and rows for the keyword. The first letter of each are highlighted and the resulting", True, self.color_dark)
        self.txt5 = self.smallerfont.render("encrypted letter is found in the grid. While for decryption the key letter row is highlighted and the encrypted", True, self.color_dark)
        self.txt6 = self.smallerfont.render("letter will find the plain text column. Keywords are repeated until they reach the lenght necessary to encrypt", True, self.color_dark)
        self.txt7 = self.smallerfont.render("the entire message. For example the keyword 'one' would be 'oneoneoneo' for the plain text 'everything'", True, self.color_dark)

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
        other_button = button(self.height / 1.1, self.other, lambda: self.SwitchToScene(Use()),
                             self.width / 2 - 500, 240, 40)   

        self.buttons = [menu_button, other_button]

        for i in self.buttons:
            i.draw(screen)

        #Title
        screen.blit(self.title, (self.width / 2 - 200, self.height / 30))

        #Information

        screen.blit(self.sub1, (75, 120))
        screen.blit(self.text1, (self.width / 2 - 625, 170))
        screen.blit(self.text2, (self.width / 2 - 725, 220))
        screen.blit(self.text3, (self.width / 2 - 725, 270))

        screen.blit(self.sub2, (75, 350))
        screen.blit(self.txt1, (self.width / 2 - 650, 400))
        screen.blit(self.txt2, (self.width / 2 - 700, 450))
        screen.blit(self.txt3, (self.width / 2 - 700, 500))
        screen.blit(self.txt4, (self.width / 2 - 700, 550))
        screen.blit(self.txt5, (self.width / 2 - 700, 600))
        screen.blit(self.txt6, (self.width / 2 - 700, 650))
        screen.blit(self.txt7, (self.width / 2 - 700, 700))

    def update(self, board, size):
        self.width = size[0]
        self.height = size[1]
