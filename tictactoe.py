from random import choice
class Board:
    BLANK_SPACE = " "
    def __init__(self, size) -> None:
        self.size = size
        self.__grid = [[Board.BLANK_SPACE for _ in range(size)] for _ in range(size)]
        self.slotsFilled = 0
        
    def update(self, symbol, row, col):
        print("You chose to place a {} at point ({} , {})".format(symbol, row, col))
        if not 0 <= row < self.size or not 0 <= col < self.size:
            print("Invalid move. Row and Column must be {} and {}".format(0, self.size - 1))
            return False
        if self.__grid[row][col] != Board.BLANK_SPACE:
            print("Invalid move. This space is already occupied.")
            return False
        
        self.__grid[row][col] = symbol
        self.slotsFilled += 1
        return True
    
    
    def getPossibleMoves(self):
        possibleMoves = []
        for i in range(self.size):
            for j in range(self.size):
                if self.__grid[i][j] == Board.BLANK_SPACE:
                    possibleMoves.append((i, j))
                    
        return possibleMoves
    def getBoard(self):
        gridCopy = [[self.__grid[row][col] for col in range(self.size)] for row in range(self.size)]
        return gridCopy
        
    def isGameOver(self):
        def checkRows(rows):
            for row in rows:
                if len(set(row)) == 1:
                    if row[0] != Board.BLANK_SPACE:
                        print("Player {} Wins!".format(row[0]))
                        return True
            return False
        
        #check rows
        if checkRows(self.__grid):
            return True
        #check columns
        columns = [*zip(*self.__grid)]
        if checkRows(columns):
            return True
        #check diagonals
        lrDiagonal = [self.__grid[i][i] for i in range(self.size)]
        rlDiagonal = [self.__grid[i][self.size - 1 - i] for i in range(self.size)]
        
        if checkRows([lrDiagonal, rlDiagonal]):
            return True
        
        #check draw
        if self.slotsFilled == self.size * self.size:
            print("Game is a draw!")
            return True
        
        return False
        
    def __repr__(self) -> str:
        # number of slots + number of dividers
        spaces = self.size + (self.size - 1)
        output = ""
        for printRowNum in range(spaces):
            rowOutput = ""
            if printRowNum % 2 == 0: # even rows have slots
                rowOutput += " "
                row = self.__grid[printRowNum // 2]
                for i in range(spaces):
                    if i % 2 == 0:
                        rowOutput +=  row[i // 2]
                    else:
                        rowOutput += " | "
            else: # odd rows are dividers
                rowOutput = " - +" * (self.size - 1) + " -"
            
            output += "\n" + rowOutput    
        return(output)
                        
        
    def __str__(self) -> str:
        return self.__repr__()

class TicTacToe:
    def __init__(self, size) -> None:
        self.board = Board(size)
        self.player = 1
        
    def makeMove(self, symbol, x, y):
        return self.board.update(symbol, x, y)
    
    
    def makeRandomMove(self, symbol):
        possibleMoves = self.board.getPossibleMoves()
        row, col = choice(possibleMoves)
        self.board.update(symbol, row, col)
        return
        
    
            
        
        
    