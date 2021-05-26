import sys, pygame as pg
from pygame.draw import line
import time

pg.init()
screen_size = 1150, 825
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None, 30)
pg.display.set_caption('Table')
letters = ['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
letter_grid = []
for i in range (26):
    letters.append(letters.pop(0))
    new_letters = letters.copy()
    letter_grid.append(new_letters)

def draw_background():
    screen.fill(pg.Color("white"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(40,40,780,780),3)
    i = 1
    while (i * 30) < 810:
        line_width = 3 
        pg.draw.line(screen, pg.Color("black"), pg.Vector2((i * 30)+40, 40), pg.Vector2((i*30) +40, 820), line_width)
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(40, (i * 30)+40), pg.Vector2(820, (i*30) +40), line_width)

        i += 1

def draw_and_highlight_letters(plain_text, key):
    letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    row = 0
    offset = 50
    width = 25
    height = 25
    while row < 26:
        col = 0
        while col < 26:
            if (plain_text == letter_list[col]):
                pg.draw.rect(screen, pg.Color("yellow"), pg.Rect((col * 30 + offset - 2) - 5, (row * 30 + offset) - 5, width, height))
            if (key == letter_list[row]):
                pg.draw.rect(screen, pg.Color("yellow"), pg.Rect((col*30 + offset -2)-5, (row*30 + offset)-5, width, height))
            if (plain_text == letter_list[col]) and (key == letter_list[row]):
                pg.draw.rect(screen, pg.Color("orange"), pg.Rect((col*30 + offset -2)-5, (row*30 + offset)-5, width, height))
            output = letter_grid[row][col]
            n_text = font.render(str(output), True, pg.Color('black'))
            screen.blit(n_text, pg.Vector2((col*30 + offset - 2), (row * 30 + offset)))
            col += 1
        row += 1

def draw_edge_row():
    edge_row = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    row = 0
    offset = 50
    while row < 26:
        output = edge_row[row]
        n_text = font.render(str(output), True, pg.Color('black'))
        screen.blit(n_text, pg.Vector2(20, (row * 30 + offset)))
        row += 1

def draw_edge_col():
    edge_col = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    col = 0
    offset = 50
    while col < 26:
        output = edge_col[col]
        n_text = font.render(str(output), True, pg.Color('black'))
        screen.blit(n_text, pg.Vector2((col * 30 + offset), 20))
        col += 1

def game_loop(plain_text,key):
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.KEYDOWN:
                pg.quit()
                sys.exit()
    draw_background()
    draw_and_highlight_letters(plain_text,key)
    draw_edge_row()
    draw_edge_col()
    pg.display.flip()

while 1:
    plain_text = 'HELLO WORLD'
    key = "HGOEN KSHFB"
    pause = 2
    for i in range(len(plain_text)):
        if i == ' ':
            time.sleep(pause)
        game_loop(plain_text[i], key[i])
        time.sleep(pause)
