import sys, pygame as pg
from pygame import *
from pygame import key
import time
from Cipher import *
from pygame.draw import line 

pg.init()
#set total screen size
screen_size = 1100, 800
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
        self.save.blit(self.screen, (0,0))
        self.screen.fill(pg.Color("white"))

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
        y_offset = 22
        # the distance between each letter
        letter_distance = 21
        string1 = "Plaintext: "
        string2 = "Key: "
        string3 = "Ciphertext: "

        #First row
        #the initial y-axis starting point
        ypos = 500
        n_text1 = font.render(str(string1), True, pg.Color('black'))
        pp = pg.Vector2(xpos, ypos)
        screen.blit(n_text1, pp)       
        for i in range(len(plain_text)):
            output = plain_text[i]
            n_text = font.render(str(output), True, pg.Color('black'))
            pp = pg.Vector2((i * letter_distance + xpos+x_offset), ypos)
            screen.blit(n_text, pp)
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(xpos+x_offset,ypos+y_offset), pg.Vector2(i*(letter_distance)+xpos+x_offset+20,ypos+y_offset),line_width)
        
        #Second row
        ypos = 532
        n_text2= font.render(str(string2), True, pg.Color('black'))
        pp = pg.Vector2(xpos, ypos)
        screen.blit(n_text2, pp) 
        for j in range(len(plain_text)):
            index = j % len(key)
            output = key[index]
            n_text = font.render(str(output), True, pg.Color('black'))
            pp = pg.Vector2((j * letter_distance + xpos+x_offset), ypos)
            screen.blit(n_text, pp)
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(xpos+x_offset,ypos+y_offset), pg.Vector2(j*(letter_distance)+xpos+x_offset+20,ypos+y_offset),line_width)
        
        #Third row
        ypos = 564
        n_text3 = font.render(str(string3), True, pg.Color('black'))
        pp = pg.Vector2(xpos, ypos)
        screen.blit(n_text3, pp) 
        for k in range(len(cipher_text)):
            output = cipher_text[k]
            n_text = font.render(str(output), True, pg.Color('black'))
            pp = pg.Vector2((k * letter_distance + xpos+x_offset), ypos)
            screen.blit(n_text, pp)
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(xpos+x_offset,ypos+y_offset), pg.Vector2(k*(letter_distance)+xpos+x_offset+20,ypos+y_offset),line_width)

    def highlight(self, index):
        # the starting x-axis point of the highlight
        offset = 170
        #width of the highlight grid
        width = 20
        #height of the highlight grid
        height = 30
        #distance between each highlight grid
        distance = 21
        #draw three grid each time in each three rows
        pg.draw.rect(screen, pg.Color("yellow"), pg.Rect((index*distance + offset),500, width, height))
        pg.draw.rect(screen, pg.Color("yellow"), pg.Rect((index*distance + offset),530, width, height))
        pg.draw.rect(screen, pg.Color("orange"), pg.Rect((index*distance + offset),560, width, height))

def main():
    text = Text_And_Highlight()
    input_plain_text = "Helloworld"
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
            screen.fill(pg.Color("white"))
            text.highlight(i)
            text.write_letter(cipher[2],cipher[3],cipher[0])
            time.sleep(second)
            pg.display.update()
        
            
    
if __name__ == '__main__':
    main()

