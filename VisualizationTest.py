import pygame
from pygame import *

from Cipher import *

pygame.init()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

FPS = 30 # Frames per second

BOXSIZE = 20 # Size of a cell/box in the table
BOARDSIZE = 26 # Number of rows/cols in the table

# Display class, writes the plaintext, keyword, and result string and manages any highlighting of specific letters
class Display:
    def __init__(self):
        self.surface = Surface((200, 200))
        self.save = Surface((200, 200))
        self.surface.fill((255, 255, 255))
        self.font = pygame.font.SysFont('Corbel', 16)
        self.plainText = []
        self.keyWord = []
        self.Result = []
        self.curHighlight = 0
        return None

    def write(self, text, mType): # text = current text to be written to screen, mType = what is being written (plaintext = 0, keyword = 1, result = 2)
        xpos = 5
        ypos = 0

        if mType == 0:
            ypos = 5
            for i in range(len(text)): # writes plaintext to the surface
                if text[i] != " ":
                    tempRect = pygame.Rect(xpos, ypos, 15, 15)
                    pygame.draw.rect(self.surface, (255, 255, 255), tempRect)
                    letterSurf = self.font.render(text[i], True, (0, 0, 0))
                    self.plainText.append((text[i], tempRect))
                    self.surface.blit(letterSurf, tempRect.topleft)
                    xpos += 15 + 1
        elif mType == 1: # Writes repeating keyword to the surface
            ypos = 25
            for i in range(len(self.plainText)):
                index = i % len(text)
                if text[index] != " ":
                    tempRect = pygame.Rect(xpos, ypos, 15, 15)
                    pygame.draw.rect(self.surface, (255, 255, 255), tempRect)
                    letterSurf = self.font.render(text[index], True, (0, 0, 0))
                    self.keyWord.append((text[index], tempRect))
                    self.surface.blit(letterSurf, tempRect.topleft)
                    xpos += 15 + 1
        else: # Writes result string to the surface
            ypos = 45
            for i in range(len(text)):
                if text[i] != " ":
                    tempRect = pygame.Rect(xpos, ypos, 15, 15)
                    pygame.draw.rect(self.surface, (255, 255, 255), tempRect)
                    letterSurf = self.font.render(text[i], True, (0, 0, 0))
                    self.Result.append((text[i], tempRect))
                    self.surface.blit(letterSurf, tempRect.topleft)
                    xpos += 15 + 1
        return None

    def highlightLetter(self, pos, mode): # Highlight a letter at the specified position
        # Unhighlight the currently highlighted text in the plain text
        pygame.draw.rect(self.surface, (255, 255, 255), self.plainText[self.curHighlight][1])
        tempSurf = self.font.render(self.plainText[self.curHighlight][0], True, (0, 0, 0))
        self.surface.blit(tempSurf, self.plainText[self.curHighlight][1].topleft)

        # Unhighlight the currently highlighted text in the keyword
        pygame.draw.rect(self.surface, (255, 255, 255), self.keyWord[self.curHighlight][1])
        tempSurf = self.font.render(self.keyWord[self.curHighlight][0], True, (0, 0, 0))
        self.surface.blit(tempSurf, self.keyWord[self.curHighlight][1].topleft)

        # Unhighlight the currently highlighted text in the result
        pygame.draw.rect(self.surface, (255, 255, 255), self.Result[self.curHighlight][1])
        tempSurf = self.font.render(self.Result[self.curHighlight][0], True, (0, 0, 0))
        self.surface.blit(tempSurf, self.Result[self.curHighlight][1].topleft)

        if (mode == 1): # if decrypt the plaintext is highlighted red
            pygame.draw.rect(self.surface, (255, 0, 0), self.plainText[pos][1])
            tempSurf = self.font.render(self.plainText[pos][0], True, (0, 0, 0))
            self.surface.blit(tempSurf, self.plainText[pos][1].topleft)
        else: # if encrypt the plaintext is highlighted yellow
            pygame.draw.rect(self.surface, (180, 180, 0), self.plainText[pos][1])
            tempSurf = self.font.render(self.plainText[pos][0], True, (0, 0, 0))
            self.surface.blit(tempSurf, self.plainText[pos][1].topleft)

        # highlight the current keyword letter with blue
        pygame.draw.rect(self.surface, (0, 180, 255), self.keyWord[pos][1])
        tempSurf = self.font.render(self.keyWord[pos][0], True, (0, 0, 0))
        self.surface.blit(tempSurf, self.keyWord[pos][1].topleft)

        # highlight the current result letter with green
        pygame.draw.rect(self.surface, (0, 255, 0), self.Result[pos][1])
        tempSurf = self.font.render(self.Result[pos][0], True, (0, 0, 0))
        self.surface.blit(tempSurf, self.Result[pos][1].topleft)
        self.curHighlight = pos

    def displayText(self, board):
        board.blit(self.surface, (0, 0)) # blit the text to the specified board

# Vis class, creates the table of letters and manages things like highlighting rows/columns and specific cells in the table
class Vis:
    def __init__(self, surf): # init
        self.font = pygame.font.SysFont('Corbel', 14)
        self.Board = surf # Surface object holding the table with the current highlights 
        self.save = Surface((800, 600)) # surface object holding a save of the table before highlights
    
        self.lettersBG = [] # Holds a list of rect objects that represent the white backgrounds for each letter in the table
        self.letters = [] # hold the surface objects for each letter written
        coordX = 1 # x coordinte of the current box
        coordY = 1 # y coordinate of the current box

        offset = 0 # offset into alphabet. Used to 'rotate' alphabet for each new row
        pygame.draw.rect(self.Board, (0, 0, 0), (0, 0, 547, 547)) # black background for the table
        for i in range(BOARDSIZE):
            for i in range(BOARDSIZE):
                index = (i + offset) % 26 # current index into alphabet
                tempRect = pygame.Rect(coordX, coordY, BOXSIZE, BOXSIZE) # draw a rect with height,width of BOXSIZE. this will be the white background for a letter
                self.lettersBG.append(tempRect) # append white box to the rect list
                pygame.draw.rect(self.Board, (255, 255, 255), tempRect) # Draw the rect to the table surface
                letterSurf = self.font.render(alphabet[index], True, (0, 0, 0)) # write the current letter in the box
                self.letters.append(letterSurf) # append the letter to the letter list
                temp = letterSurf.get_rect(center=(0, 0)) # Tried using this to center the letter in the white box. Didnt really work, oh well
                self.Board.blit(letterSurf, (coordX, coordY)) # Blit the letter onto the table surface
                coordX += BOXSIZE + 1 # increment the current coordinate. There should be a 1 pixel gap between each white box to make black lines between cells/boxes
            offset += 1
            coordY += BOXSIZE + 1
            coordX = 1

        self.rows = [] # Hold a list of rect objects that cover an entire row
        coordX = 0
        coordY = 0
        for i in range(BOARDSIZE): # Create 26 of these so theres 1 to cover each row. These will be used to highlight specific rows
            tempRect = pygame.Rect(coordX, coordY, BOXSIZE, BOXSIZE * 26 + 26)#Boxsize * 26 + 26. The row will be BOXSIZE*26 units wide, not counting the 1 pixel gap between each cell.
            self.rows.append(tempRect)
            coordX += BOXSIZE + 1

        self.cols = [] # Hold a list of rect objects that cover an entire column
        coordX = 0
        coordY = 0
        for i in range(BOARDSIZE): # Create 26 of these so theres 1 to cover each column. These will be used to highlight specific column
            tempRect = pygame.Rect(coordX, coordY, BOXSIZE * 26 + 26, BOXSIZE) #Boxsize * 26 + 26. The column will be BOXSIZE*26 units tsll, not counting the 1 pixel gap between each cell. 
            self.cols.append(tempRect)
            coordY += BOXSIZE + 1

        self.save.blit(self.Board, (0, 0)) # blit (save) the clean table onto the 'save' surface object

        return None

    def getSurf(self): # return the surface object that has the table written on it. Used to blit with main surface to draw table 
        return self.Board

    def highlightRow(self, row): # highlight a row
        s = Surface((self.rows[row].width, self.rows[row].height)) # temporary surface with the size of a single row
        s.set_alpha(160) # set the alpha value of the tehmp surface
        s.fill((180, 180, 0)) # Fill the entire surface with yellowish color
        self.Board.blit(s, (self.rows[row].left, self.rows[row].top)) # blit the surface in the correct position to cover the current row

    def highlightCol(self, row): # highlight a column 
        s = Surface((self.cols[row].width, self.cols[row].height)) # temporary surface with the size of a single column
        s.set_alpha(160) # set the alpha value of the tehmp surface
        s.fill((0, 180, 255)) # Fill the entire surface with blueish color
        self.Board.blit(s, (self.cols[row].left, self.cols[row].top))# blit the surface in the correct position to cover the current column

    def fillBox(self, pos, col): # Highlight a specific box in the table
        r = self.lettersBG[pos] # get the rect at the specified position
        pygame.draw.rect(self.Board, col, r) # redraw the rect with color 'col'
        self.Board.blit(self.letters[pos], (r.left, r.top)) # Rewrite the letter in the current cell to cover the rect

    # This function highlights a row, column and specific box in the table. 
    def fill(self, row, col, mode, pos=0):
        self.resetBoard() # Erase the current highlight
        self.highlightCol(col) # highlight the specified column
        self.highlightRow(row) # highlight the specified row
        if (mode == 0): # if encrypt then fill the cell at the intersection between the highlighted row and column with green
            index = row + (26*col)
            self.fillBox(index, (0, 255, 0))
        else: # if decrypt fill the cell at the intersection between the highlighted row and column with red, and fill the letter at the top of the current column with green
            index = row + (26*col)
            self.fillBox(index, (255, 0, 0))
            self.fillBox(pos, (0, 255, 0))

    def resetBoard(self):
        self.Board.blit(self.save, (0, 0)) # blit the clean table onto the current table

class pacing:
    def __init__(self, pace, board, fps, states, d, mode = 0):
        self.pace = pace # not really needed here, could be used later to update pace
        self.board = board # board to make changes to 
        self.counter = 0 # Pacing counter
        self.fps = fps * pace # FPS counter, determines how many times the board updates per second
        self.states = states # list of indices for colummns/rows in table ((1, 2), (20, 15), etc..)
        self.index = 0 # current index into self.states
        self.len = len(self.states) # length of self.states
        self.mode = mode # mode: 0 for encrypt, 1 for decrypt
        self.d = d # Display object for writing/highlighting plaintext, keyword, and result

        self.displayText = Display()

    def update(self):
        # If counter == 0 then update the board with the next state in visualization
        if (self.counter == 0):
            # Fill the correct box in the table
            self.board.fill(self.states[self.index][0], self.states[self.index][1], self.mode, self.states[self.index][2])
            # Highlight the correct plaintext, keyword, and result letters
            self.d.highlightLetter(self.index, self.mode)
            # increment index using modulo for wrap around
            self.index = (self.index + 1) % self.len
            
        # increment counter for every call. (When self.counter +1) == self.fps, then the next board update will happen
        self.counter = (self.counter + 1) % self.fps

def main():
    # main display surface
    DISPLAYSURF = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Board")

    # set the fps clock. Used for pacing
    fpsClock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 128)
    BLACK = (0, 0, 0)
    ALPHAYELLOW = (180, 180, 0, 0)

    DISPLAYSURF.fill(WHITE)

    #Encrypt or decrypt here. retVal hold all the information returned from the encryption/decryption process

    retVal = Encrypt("Hello World", "BACON") # comment this out when decrypting
    #retVal = Decrypt("Ienzb Xotzq", "BACON") # comment this out when encrypting

    # list of indices return from encrypt/decrypt. The instructions are used to highlight rows and columns on the board
    instructions = retVal[1]

    # Create a display object for displaying and highlighting the plaintext, keyword, and result
    d = Display()

    # Create a Vis object which basically creates/manages the table
    b = Vis(DISPLAYSURF.convert_alpha())

    #""" This code is for visualizing encryption. Comment this out when decrypting
    c = pacing(2, b, FPS, instructions, d, 0)
    d.write(retVal[2], 0)
    d.write(retVal[3], 1)
    d.write(retVal[0], 2)
    #"""

    """ This code is for visualizing decryption. Comment this out when encrypting
    c = pacing(2, b, FPS, instructions, d, 1) # create pacing object

    # Write the plaintext, keyword, and result to the display 
    d.write(retVal[2], 0)
    d.write(retVal[3], 1)
    d.write(retVal[0], 2)
    #"""

    # after writing stuff to the display object, this needs to be called to blit the information over to the main display surface
    d.displayText(DISPLAYSURF)
    while True:
        c.update() #pacing module update method
        d.displayText(DISPLAYSURF) # Blit display object writing onto display surface
        DISPLAYSURF.blit(b.getSurf(), (250, 30)) # Blit table onto main display surface

        events = pygame.event.get()
        pressed_keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update() #update main display

        """ From the book: The Clock object’s tick() method should be called at the very end of the game loop, after the
            call to pygame.display.update(). The length of the pause is calculated based on how
            long it has been since the previous call to tick(), which would have taken place at the end of
            the previous iteration of the game loop. (The first time the tick() method is called, it doesn’t
            pause at all.)
        """

        fpsClock.tick(FPS) # fps clock tick
    return

main()
