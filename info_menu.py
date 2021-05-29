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
        self.menu = self.smallfont.render("Main Menu", True, self.color_dark)

        # storing the x1 value so buttons will be center screen
        midX = self.width - self.x2/2

        # buttons and their locations/functions
        menu_button = button(self.height/2 - self.y2*1.5 +5, self.menu, lambda: self.SwitchToScene(MainMenu()), x1 = midX)
        about_button = button(self.height/2 - self.y2/2, self.about, lambda: self.SwitchToScene(AboutCi_1()), x1 = midX)
        use_button = button(self.height/2 + self.y2*1.5 +5, self.use, lambda: self.SwitchToScene(Uses_1()), x1 = midX)

        self.buttons(menu_button, about_button, use_button)

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

        #Menu title
        screen.blit("Information", (self.width / 2.5, self.height / 3.5))

    def update(self, board, size):
        return None

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

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.input_smallfont = pygame.font.SysFont('Corbel', 24)

        # rendering a text written in
        # this font
        self.next = self.smallfont.render('Next (Controls)', True, self.color)
        self.menu = self.smallfont.render("Main Menu", True, self.color_dark)


        # buttons and their locations/functions
        menu_button = button(self.height - 20, self.menu, lambda: self.SwitchToScene(MainMenu()), x1 = 20)
        next_button = button(self.height - 20, self.next, lambda: self.SwitchToScene(Uses_2()), x1 = self.width - 20 - self.x2)

        self.buttons(menu_button, next_button)

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
        screen.blit("Using This Tool", (self.width / 2.5, self.height / 3.5))

        #Information

    def update(self, board, size):
        return None

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

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.input_smallfont = pygame.font.SysFont('Corbel', 24)

        # rendering a text written in
        # this font
        self.back = self.smallfont.render('Back', True, self.color)
        self.menu = self.smallfont.render("Main Menu", True, self.color_dark)


        # buttons and their locations/functions
        menu_button = button(self.height - 20, self.menu, lambda: self.SwitchToScene(MainMenu()), x1 = 20)
        back_button = button(self.height - 20, self.next, lambda: self.SwitchToScene(Uses_1()), x1 = self.width - 20 - self.x2)

        self.buttons(menu_button, back_button)

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
        screen.blit("Using This Tool", (self.width / 2.5, self.height / 3.5))

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

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.input_smallfont = pygame.font.SysFont('Corbel', 24)

        # rendering a text written in
        # this font
        self.next = self.smallfont.render('Next (Vigenere Cipher)', True, self.color)
        self.menu = self.smallfont.render("Main Menu", True, self.color_dark)


        # buttons and their locations/functions
        menu_button = button(self.height - 20, self.menu, lambda: self.SwitchToScene(MainMenu()), x1 = 20)
        next_button = button(self.height - 20, self.next, lambda: self.SwitchToScene(Uses_2()), x1 = self.width - 20 - self.x2)

        self.buttons(menu_button, next_button)

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
        screen.blit("Ciphers", (self.width / 2.5, self.height / 3.5))

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

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.input_smallfont = pygame.font.SysFont('Corbel', 24)

        # rendering a text written in
        # this font
        self.back = self.smallfont.render('Back', True, self.color)
        self.menu = self.smallfont.render("Main Menu", True, self.color_dark)


        # buttons and their locations/functions
        menu_button = button(self.height - 20, self.menu, lambda: self.SwitchToScene(MainMenu()), x1 = 20)
        back_button = button(self.height - 20, self.next, lambda: self.SwitchToScene(Uses_1()), x1 = self.width - 20 - self.x2)

        self.buttons(menu_button, back_button)

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
        screen.blit("The Vigenere Cipher", (self.width / 2.5, self.height / 3.5))

        #Information

    def update(self, board, size):
        return None