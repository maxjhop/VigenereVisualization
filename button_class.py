import pygame

class button():

    def __init__(self, y1, text, click_funct, x1=5, x2=150, y2=30, textOffsetx = 5, textOffsety = 5):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.textOffsetx = textOffsetx
        self.textOffsety = textOffsety
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
        screen.blit(self.text, (self.x1 + self.textOffsetx, self.y1 + self.textOffsety))

    def hover(self, mouse):
        if self.x1 <= mouse[0] <= (self.x1 + self.x2) and self.y1 <= mouse[1] <= (self.y1 + self.y2):
            return True
        else:
            return False

    def click(self):
        self.click_funct()