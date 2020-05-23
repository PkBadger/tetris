import pygame
from board import Board
from piece import I, O, J, L, T, S, Z
import random


pygame.display.set_caption('tetris')

WHITE = (255,255,255)
BLUE = (0,0,255)

class GUI:
    def __init__(self):
        self.height = 600
        self.width = 600
        self.blockSize = 25
        self.boardX = 40
        self.boardY = 40
        self.boardWidth = self.blockSize * 10
        self.boardHeight = self.blockSize * 20
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.tetrisBoard = Board()
        self.piece = None

    def drawSquare(self,square, x, y):
        pixelX = (x + square[0]) * self.blockSize + self.boardX
        pixelY = (y - square[1]) * self.blockSize + self.boardY
        square = pygame.draw.rect(self.window, BLUE, (pixelX, pixelY, self.blockSize, self.blockSize))
        pygame.display.update(square)

    def drawBoardSquare(self, x, y):
        pixelX = x * self.blockSize + self.boardX
        pixelY = y * self.blockSize + self.boardY
        square = pygame.draw.rect(self.window, BLUE, (pixelX, pixelY, self.blockSize, self.blockSize))
        pygame.display.update(square)

    def drawPiece(self):
        body = self.piece.getBody()
        x = self.tetrisBoard.pieceX
        y = self.tetrisBoard.pieceY 
        for square in body:
            self.drawSquare(square, x, y)

    def drawBoard(self):
        for x in range(10):
            for y in range(20):
                if(self.tetrisBoard.matrix[x][y]):
                    self.drawBoardSquare(x,y)


    def run(self):
        run =  True
        pause = False
        speed = 15
        time_elapsed_since_last_action = 0
        while run:
            
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.tetrisBoard.rotate(self.piece)
                    if event.key == pygame.K_LEFT:
                        self.tetrisBoard.moveLeft(self.piece)
                    if event.key == pygame.K_RIGHT:
                        self.tetrisBoard.moveRight(self.piece)
                    if event.key == pygame.K_z:
                        pause = not pause
                        if(pause):
                            print(self.tetrisBoard.columnHeight)
                    if event.key == pygame.K_DOWN:
                        speed = 3
                    #if event.key == pygame.K_SPACE:
                    #    speed = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        speed = 15
                        #self.tetrisBoard.moveRight(self.piece)
                    #if event.key == pygame.K_RIGHT:
                    #    location += 1
            self.window.fill((0,0,0))
            time_elapsed_since_last_action += 1

            if(not self.piece):
                self.piece = random.choice([I, O, J, L, T, S, Z])()
                self.tetrisBoard.setCurrentPiece(self.piece)
            
            boardRect = pygame.draw.rect(self.window,WHITE,(self.boardX,self.boardY,self.boardWidth,self.boardHeight), 2)
            self.drawPiece()
            self.drawBoard()

            if time_elapsed_since_last_action > speed and not pause:
                self.tetrisBoard.fall()
                time_elapsed_since_last_action = 0 # reset it to 0 so you can count again
                if(self.tetrisBoard.isTerminal(self.piece)):
                    #print('IS TEEMINAL')
                    self.tetrisBoard.place(self.piece)
                    self.piece = None

            pygame.display.update(boardRect)

            if(self.tetrisBoard.isGameOver()):
                run = False
    

tetris = GUI()


tetris.run()

    