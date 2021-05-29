import sys, pygame as pg
from pygame import *
from pygame import key
import time
from Cipher import *
from pygame.draw import line 

pg.init()
#set total screen size
screen_size = 600, 300
#display screen
screen = pg.display.set_mode(screen_size)
#set font size later on
font = pg.font.SysFont(None, 40)
#set title
pg.display.set_caption('Text')

class Text_And_Highlight:
    def __init__(self) -> None:
        self.screen = pg.Surface(screen_size)
        self.save = pg.Surface(screen_size)
        self.screen.fill((255, 255, 165))
        self.save.blit(self.screen, (0,0))

        self.indices = []

    def refresh(self):
        self.screen.blit(self.save, (0,0))
        
    def write_letter(self, plain_text, key, cipher_text):
        #line_width is the width of the dividing line
        line_width = 3
        #the initial x-axis starting point
        xpos = 20
        # xpos + x_offset is the x-axis starting point of the message and line
        x_offset = 150
        # y_offset is the distance between each row
        y_offset = 24
        # the distance between each letter
        letter_distance = 21
        string1 = "Plaintext:"
        string2 = "Key:"
        string3 = "Ciphertext:"

        #First row
        #the initial y-axis starting point
        ypos = 0
        n_text1 = font.render(str(string1), True, pg.Color('black'))
        pp = pg.Vector2(xpos, ypos)
        self.screen.blit(n_text1, pp)
        ypos += 32
        for i in range(len(plain_text)):
            output = plain_text[i]
            n_text = font.render(str(output), True, pg.Color('black'))
            pp = pg.Vector2((i * letter_distance + xpos), ypos)
            self.screen.blit(n_text, pp)
        pg.draw.line(self.screen, pg.Color("black"), pg.Vector2(xpos,ypos+y_offset), pg.Vector2(i*(letter_distance)+xpos+20,ypos+y_offset),line_width)
        
        #Second row
        ypos += 50
        n_text2= font.render(str(string2), True, pg.Color('black'))
        pp = pg.Vector2(xpos, ypos)
        self.screen.blit(n_text2, pp)
        ypos += 32
        key_index = 0
        for j in range(len(plain_text)):
            if (plain_text[j] != " "):
                index = key_index % len(key)
                output = key[index]
                self.indices.append(j)
                key_index += 1
            else :
                output = " "
            n_text = font.render(str(output), True, pg.Color('black'))
            pp = pg.Vector2((j * letter_distance + xpos), ypos)
            self.screen.blit(n_text, pp)
        pg.draw.line(self.screen, pg.Color("black"), pg.Vector2(xpos,ypos+y_offset), pg.Vector2(j*(letter_distance)+xpos+20,ypos+y_offset),line_width)
        
        #Third row
        ypos += 50
        n_text3 = font.render(str(string3), True, pg.Color('black'))
        pp = pg.Vector2(xpos, ypos)
        ypos += 32
        self.screen.blit(n_text3, pp) 
        for k in range(len(cipher_text)):
            output = cipher_text[k]
            n_text = font.render(str(output), True, pg.Color('black'))
            pp = pg.Vector2((k * letter_distance + xpos), ypos)
            self.screen.blit(n_text, pp)
        pg.draw.line(self.screen, pg.Color("black"), pg.Vector2(xpos,ypos+y_offset), pg.Vector2(k*(letter_distance)+xpos+20,ypos+y_offset),line_width)

    def highlight(self, ind, mode):
        self.refresh()

        index = self.indices[ind]

        if (mode == 0):
            color = (255, 255, 0)
        else:
            color = (255, 80, 80)
        # the starting x-axis point of the highlight
        offset = 170
        #width of the highlight grid
        width = 20
        #height of the highlight grid
        height = 30
        #distance between each highlight grid
        distance = 21
        #draw three grid each time in each three rows
        pg.draw.rect(self.screen, color, pg.Rect((index*distance + 20),30, width, height))
        pg.draw.rect(self.screen, (0, 180, 255), pg.Rect((index*distance + 20),112, width, height))
        pg.draw.rect(self.screen, (0, 255, 0), pg.Rect((index*distance + 20),194, width, height))

def main():
    text = Text_And_Highlight()
    input_plain_text = "Really Long Message"
    plain_text = input_plain_text.upper()
    input_key = "sch"
    key = input_key.upper()
    second = 1
    cipher = Encrypt(plain_text, key)

    while True:
        screen.blit(text.screen,(0,0))
        events = pg.event.get()

        for i in range(len(plain_text)):
            # game_loop(plain_text, key,i)
            for event in events:
                if event.type == pg.QUIT: sys.exit()
            #screen.fill(pg.Color("white"))
            screen.blit(text.screen, (0, 0))
            text.highlight(i)
            text.write_letter(cipher[2],cipher[3],cipher[0])
            time.sleep(second)
            pg.display.update()
        
            
    
if __name__ == '__main__':
    main()
