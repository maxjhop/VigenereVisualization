import pygame


class SceneManager:
    def __init__(self):
        self.scene = self

    def Input(self, events, pressed_keys, mouse):
        print("Input not overridden")

    def Render(self, screen, mouse):
        print("Render not overriden")

    def SwitchToScene(self, next_scene):
        self.scene = next_scene

    def Terminate(self):
        self.SwitchToScene(None)


class button():

    def __init__(self, y1, text, click_funct, x1=5, x2=200, y2=40):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.text = text
        self.click_funct = click_funct

    def draw(self, screen):

        # light shade of the button
        color_light = (170, 170, 170)

        # dark shade of the button
        color_dark = (100, 100, 100)

        if self.hover(pygame.mouse.get_pos()):
            # print(self.text, self.x1, self.x2, self.y1, self.y2)
            pygame.draw.rect(screen, color_light, [self.x1, self.y1, self.x2, self.y2])
        else:
            # print(self.text, self.x1, self.x2, self.y1, self.y2)
            pygame.draw.rect(screen, color_dark, [self.x1, self.y1, self.x2, self.y2])
        screen.blit(self.text, (self.x1 + 5, self.y1 + 5))

    def hover(self, mouse):
        if self.x1 <= mouse[0] <= (self.x1 + self.x2) and self.y1 <= mouse[1] <= (self.y1 + self.y2):
            return True
        else:
            return False

    def click(self):
        self.click_funct()


class ButtonScene(SceneManager):
    def __init__(self):
        SceneManager.__init__(self)

        # white color
        self.color = (255, 255, 255)

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 35)

        # rendering a text written in this font
        self.menu = self.smallfont.render('Main Menu', True, self.color)
        self.play = self.smallfont.render('Play', True, self.color)
        self.pause = self.smallfont.render('Pause', True, self.color)
        self.forw = self.smallfont.render('Step Forward', True, self.color)
        self.back = self.smallfont.render('Step Back', True, self.color)
        self.up = self.smallfont.render('Speed Up', True, self.color)
        self.down = self.smallfont.render('Slow Down', True, self.color)
        self.res = self.smallfont.render('Restart', True, self.color)

        # buttons and their locations
        menu_button = button(5, self.menu, lambda: self.SwitchToScene(MainMenu()))
        play_button = button(50, self.play, lambda: print("play"))
        pause_button = button(95, self.pause, lambda: print("pause"))
        forw_button = button(140, self.forw, lambda: print("forward"))
        back_button = button(185, self.back, lambda: print("back"))
        up_button = button(230, self.up, lambda: print("up"))
        down_button = button(275, self.down, lambda: print("dpwn"))
        res_button = button(320, self.res, lambda: print("res"))

        self.buttons = [menu_button, play_button, pause_button, forw_button, back_button, up_button, down_button,
                        res_button]
        """
        while True:

            # stores the (x,y) coordinates into
            # the variable as a tuple
            mouse = pygame.mouse.get_pos()

            # fills the screen with a color
            screen.fill((50, 100, 0))
        """

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
        screen.fill((255, 255, 165))
        # drawing buttons
        for i in self.buttons:
            i.draw(screen)

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
        self.validCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

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
                        if ev.unicode in self.validCharacters:
                            self.message_text += ev.unicode

                elif self.key_active:
                    if ev.key == pygame.K_BACKSPACE:
                        self.key_text = self.key_text[:-1]
                    else:
                        if ev.unicode in self.validCharacters:
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