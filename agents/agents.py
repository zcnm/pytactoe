from random import choice


class BaseAgent:
    def __init__(self, symbol, opponentSymbol):
        self.symbol = symbol
        self.opponentSymbol = opponentSymbol
    
    def getPossibleMoves(self, board):
        n = len(board)
        possibleMoves = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == " ":
                    possibleMoves.append((i, j))
        return possibleMoves
    
    def move(self, board):
        pass 
    
class RandomAgent(BaseAgent):
    def __init__(self, symbol, opponentSymbol):
        super().__init__(symbol, opponentSymbol)
        
    def move(self, board):
        possibleMoves = self.getPossibleMoves(board)
        return choice(possibleMoves)
    
class HumanAgent(BaseAgent):
    def __init__(self, symbol, opponentSymbol):
        super().__init__(symbol, opponentSymbol)
        
    def move(self, board):
        possibleMoves = self.getPossibleMoves(board)
        while True:
            print("Enter coordinates x y:")
            line = input()
            try:
                x, y = map(int, line.split())
                if (x, y) in possibleMoves:
                    return (x, y)
                else:
                    print("Error: invalid coordinates")
                    print("That position is either occupied or does not exist.")
            except: 
                print("Error: invalid format")
                print("two numbers, x y are required.")

class MiniMaxAgent(BaseAgent):
    
    def __init__(self, symbol, opponentSymbol):
        super().__init__(symbol, opponentSymbol)
        self.maxDepth = 10
        
    def move(self, board):
        n = len(board)
        possibleMoves = self.getPossibleMoves(board)
        bestMove = possibleMoves[0]
        bestValue = -10
        newBoard = [[board[row][col] for col in range(n)] for row in range(n)]
        for move in possibleMoves:
            x, y = move
            newBoard[x][y] = self.symbol
            value = self.minimax(newBoard, self.maxDepth, False)
            newBoard[x][y] = " "
            if value > bestValue:
                bestValue = value 
                bestMove = move 
            print(move, value)
        
        return bestMove
    
    def calculateHeuristic(self, board, depth):
        score = 1/(self.maxDepth - depth+ 0.001)
        winner = self.isGameOver(board, returnWinner = True)[0]
        if winner is None:
            return 0
        elif winner == self.symbol:
            return score + 1
        else:
            return -1 - score
    def minimax(self, board, depth, maximisingPlayer):
        n = len(board)
        if depth == 0 or self.isGameOver(board):
            return self.calculateHeuristic(board, depth)
        possibleMoves = self.getPossibleMoves(board)
        newBoard = [[board[row][col] for col in range(n)] for row in range(n)]
        if maximisingPlayer:
            value = -10
            for move in possibleMoves:
                x, y = move
                newBoard[x][y] = self.symbol
                value = max(value, self.minimax(newBoard, depth - 1, False))   
                
                newBoard[x][y] = " "
        else:
            value = 10
            for move in possibleMoves:
                x, y = move
                newBoard[x][y] = self.opponentSymbol
                value = min(value, self.minimax(newBoard, depth - 1, True))
                newBoard[x][y] = " "
        return value
            
        
    def isGameOver(self, board, returnWinner = False):
        
        n = len(board)
        winner = [None]
        def checkRows(rows):
            for row in rows:
                if len(set(row)) == 1:
                    if row[0] != " ":
                        winner[0] = row[0]
                        return True
            return False
        
        #check rows
        if checkRows(board):
            if returnWinner:
                return winner
            return True
        #check columns
        columns = [*zip(*board)]
        if checkRows(columns):
            if returnWinner:
                return winner
            return True
        #check diagonals
        lrDiagonal = [board[i][i] for i in range(n)]
        rlDiagonal = [board[i][n - 1 - i] for i in range(n)]
        
        if checkRows([lrDiagonal, rlDiagonal]):
            if returnWinner:
                return winner
            return True
        
        #check draw
        for row in board:
            for cell in row:
                if cell == " ":
                    return False
        
        if returnWinner:
            return [None]
        return True
    

class NegaMaxAgent(BaseAgent):
    
    def __init__(self, symbol, opponentSymbol):
        super().__init__(symbol, opponentSymbol)
        self.maxDepth = 10
        
    def move(self, board):
        n = len(board)
        possibleMoves = self.getPossibleMoves(board)
        bestMove = possibleMoves[0]
        bestValue = -10 
        newBoard = [[board[row][col] for col in range(n)] for row in range(n)]
        for move in possibleMoves:
            x, y = move
            newBoard[x][y] = self.symbol
            value = self.negamax(newBoard, self.maxDepth, -1)
            newBoard[x][y] = " "
            if value > bestValue:
                bestValue = value 
                bestMove = move 
            print(move, value)
        
        return bestMove
    
    def calculateHeuristic(self, board):
        winner = self.isGameOver(board, returnWinner = True)[0]
        if winner is None:
            return 0
        elif winner == self.symbol:
            return 1
        else:
            return -1
    def negamax(self, board, depth, colour):
        n = len(board)
        if depth == 0 or self.isGameOver(board):
            return colour * self.calculateHeuristic(board)
        possibleMoves = self.getPossibleMoves(board)
        newBoard = [[board[row][col] for col in range(n)] for row in range(n)]
        value = -10
        for move in possibleMoves:
            x, y = move
            if colour == 1:
                newBoard[x][y] = self.symbol
            else:
                newBoard[x][y] = self.opponentSymbol
            value = max(value, -1 * self.negamax(newBoard, depth - 1, -1 * colour))
            newBoard[x][y] = " "
        return value
        
    def isGameOver(self, board, returnWinner = False):
        
        n = len(board)
        winner = [None]
        def checkRows(rows):
            for row in rows:
                if len(set(row)) == 1:
                    if row[0] != " ":
                        winner[0] = row[0]
                        return True
            return False
        
        #check rows
        if checkRows(board):
            if returnWinner:
                return winner
            return True
        #check columns
        columns = [*zip(*board)]
        if checkRows(columns):
            if returnWinner:
                return winner
            return True
        #check diagonals
        lrDiagonal = [board[i][i] for i in range(n)]
        rlDiagonal = [board[i][n - 1 - i] for i in range(n)]
        
        if checkRows([lrDiagonal, rlDiagonal]):
            if returnWinner:
                return winner
            return True
        
        #check draw
        for row in board:
            for cell in row:
                if cell == " ":
                    return False
        
        if returnWinner:
            return [None]
        return True
