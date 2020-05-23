import copy

def findIndex(lst, value):
    try:
        idx = lst.index(value)
    except ValueError:
        idx = -1
    return idx

class Board:
    def __init__(self):
        self.matrix = [[False for _ in range(20)] for _ in range(10)]#[[False] * 20] * 10
        self.width = 10
        self.height = 20
        self.pieceX = None
        self.pieceY = None
        self.columnHeight = [0 for _ in range(10)]
        self.columnWidth = [0 for _ in range(20)]
        self.maxHeight = 0

    def place(self, piece):
        skirt = piece.getSkirt()
        heights = [0] * 4
        #print(self.pieceY )
        for square in piece.getBody():
            x = self.pieceX + square[0]
            y = self.pieceY - square[1] - 1
            self.matrix[x][y] = True
            heights[square[0]] = 20 - y
            self.columnWidth[y] += 1
        print(heights)
        for index in range(len(skirt)):
            sk = skirt[index]
            columnIndex = self.pieceX + index
            self.columnHeight[columnIndex] = heights[index]
            if self.columnHeight[columnIndex] > self.maxHeight:
                self.maxHeight = self.columnHeight[columnIndex]

        #print(self.columnHeight)
        self.clearRows()

    
    def clearRows(self):
        check = True
        while(check):
            check = False
            for index in range(20):
                width = self.getRowWidth(index)
                if(width >= 10): 
                    self.clearRow(index)
                    check = True
                    break

    def populateColumnHeight(self, row):
        index = findIndex(row, True)
        print(row)
        print(index)

        return 0 if index == -1 else 20 - index  

    def clearRow(self, index):
        self.maxHeight = 0

        columnWidthCP = self.columnWidth.copy()

        for i in range(1, 20):
            if(i <= index):
                columnWidthCP[i] = self.columnWidth[i - 1]


        columnWidthCP[0] = 0

        self.columnWidth = columnWidthCP.copy()

        matrixCP = copy.deepcopy(self.matrix)#self.matrix.copy()

        for i in range(10):
            for k in range(20):
                 if(k <= index):
                     matrixCP[i][k] = self.matrix[i][k - 1]

        for i in range(10):
            matrixCP[i][0] = False
            self.columnHeight[i] = self.populateColumnHeight(matrixCP[i])
            if(self.columnHeight[i] > self.maxHeight):
                self.maxHeight = self.columnHeight[i]

        self.matrix = matrixCP.copy()
        for m in self.matrix: print(m)
        print(index)
        print(self.columnWidth)
        print(self.columnHeight)


    def getRowWidth(self, y):
        return self.columnWidth[y]

    def getColumnHeight(self, x):
        return 20 - self.columnHeight[x]

    def getMaximumHeight(self):
        pass

    def dropHeight(self,piece, x):
        pass

    def isTerminal(self, piece):
        skirt = piece.getSkirt()
        for index in range(len(skirt)):
            height = self.getColumnHeight(self.pieceX + index)
            if (height == self.pieceY - skirt[index]): return True

        return False


    def setCurrentPiece(self, piece):
        self.pieceX = 3
        self.pieceY = piece.getHeight() - 1

    def rotate(self, piece):
        piece.rotate()
        width = piece.getWidth()
        if (self.pieceX + width > 10): self.pieceX = 10 - width

    def moveLeft(self, piece):
        if(self.pieceX == 0): return
        if(self.matrix[self.pieceX - 1][self.pieceY]): return
        self.pieceX -= 1

    def moveRight(self, piece):
        if(self.pieceX == (10 - piece.getWidth())): return
        if(self.matrix[self.pieceX + 1][self.pieceY]): return
        self.pieceX += 1

    def fall(self):
        self.pieceY +=1

    def isGameOver(self):
        return True if self.maxHeight >= 20 else False
    

    