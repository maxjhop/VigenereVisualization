import sys, pygame as pg
from pygame.draw import line

pg.init()
screen_size = 850, 850
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None, 30)
pg.display.set_caption('Table')
letters = ['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
# letter_grid = [letters.append(letters.pop(0)) for i in range(26)]
letter_grid = []
for i in range (26):
    letters.append(letters.pop(0))
    new_letters = letters.copy()
    letter_grid.append(new_letters)
# print(letter_grid)



class Table:
    def __init__(self):
        self.screen = pg.Surface(screen_size)

        self.save = pg.Surface(screen_size)

        self.cells = []
        self.letters = []

        self.edgeRowLetters = []
        self.edgeColLetters = []
        
        self.draw_background()
        self.draw_letters()
        self.draw_edge_row()
        self.draw_edge_col()
        self.save.blit(self.screen, (0, 0))
        return None

    def draw_background(self):
        self.screen.fill(pg.Color("white"))
        pg.draw.rect(self.screen, pg.Color("black"), pg.Rect(40,40,780,780),3)
        i = 1
        while (i * 30) < 810:
            line_width = 3 
            pg.draw.line(self.screen, pg.Color("black"), pg.Vector2((i * 30)+40, 40), pg.Vector2((i*30) +40, 820), line_width)
            pg.draw.line(self.screen, pg.Color("black"), pg.Vector2(40, (i * 30)+40), pg.Vector2(820, (i*30) +40), line_width)
            i += 1
        return None

    def draw_letters(self):
        row = 0
        offset = 50
        while row < 26:
            col = 0
            while col < 26:
                output = letter_grid[row][col]
                # print(str(output))
                tempRect = pg.Rect((col*30 + 42), (row * 30 + 42), 27, 27)
                pg.draw.rect(self.screen, (255, 255, 255), tempRect)
                self.cells.append(tempRect)
                n_text = font.render(str(output), True, pg.Color('black'))
                curpos = pg.Vector2((col*30 + offset - 2), (row * 30 + offset))
                self.screen.blit(n_text, curpos)
                self.letters.append((n_text, curpos))
                col += 1
            row += 1
        return None
    
    def draw_edge_row(self):
        edge_row = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        row = 0
        offset = 50
        while row < 26:
            output = edge_row[row]
            n_text = font.render(str(output), True, pg.Color('black'))
            pp = pg.Vector2(20, (row * 30 + offset))
            self.screen.blit(n_text, pp)
            self.edgeRowLetters.append((n_text, pp))
            row += 1
        return None

    def draw_edge_col(self):
        edge_col = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        col = 0
        offset = 50
        while col < 26:
            output = edge_col[col]
            n_text = font.render(str(output), True, pg.Color('black'))
            pp = pg.Vector2((col * 30 + offset), 20)
            self.screen.blit(n_text, pg.Vector2((col * 30 + offset), 20))
            self.edgeColLetters.append((n_text, pp))
            col += 1
        return None

    def highlightRow(self, row):
        offset = row * 26
        tempRect = pg.Rect(self.cells[0].left - 30, self.cells[row*26].top, 27, 27)
        pg.draw.rect(self.screen, (0, 180, 255), tempRect)
        self.screen.blit(self.edgeRowLetters[row][0], self.edgeRowLetters[row][1])
        for i in range(26):
            pg.draw.rect(self.screen, (0, 180, 255), self.cells[offset + i])
            self.screen.blit(self.letters[offset+i][0], self.letters[offset+i][1])
        return None

    def highlightCol(self, col):
        tempRect = pg.Rect(self.cells[col].left, self.cells[0].top - 30, 27, 27)
        pg.draw.rect(self.screen, (255, 255, 0), tempRect)
        self.screen.blit(self.edgeColLetters[col][0], self.edgeColLetters[col][1])
        for i in range(26):
            pos = i*26 + col
            pg.draw.rect(self.screen, (255, 255, 0), self.cells[pos])
            self.screen.blit(self.letters[pos][0], self.letters[pos][1])
        return None

    def fill_cell(self, row, col):
        index = row*26 + col
        pg.draw.rect(self.screen, (0, 255, 0), self.cells[index])
        self.screen.blit(self.letters[index][0], self.letters[index][1])
        return None

    def display(self, row, column):
        self.screen.blit(self.save, (0, 0))
        self.highlightRow(row)
        self.highlightCol(column)
        self.fill_cell(row, column)
        return None

def main():
    table = Table()
    table.display(10, 10)
    while True:
        screen.blit(table.screen, (0, 0))
        events = pg.event.get()
        pressed_keys = pg.key.get_pressed()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
        pg.display.update()

