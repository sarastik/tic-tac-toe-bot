import random

class HumanTeam:
    def __init__(self, name):
        self.name = name
        self.moveHistory = []

    def getName(self):
        return self.name

    def getMoveHistory(self):
        return self.moveHistory

    def addMoveToHistory(self, move):
        self.moveHistory.append(move)

    def chooseMove(self, _):
        print("Where would you like to move?")
        row = input("Row? (1/2/3): ")
        col = input("Column? (1/2/3): ")
        return int(row) - 1, int(col) - 1
        

class RobotTeam:
    def __init__(self, name):
        self.name = name
        self.moveHistory = []

    def getName(self):
        return self.name

    def getMoveHistory(self):
        return self.moveHistory
    
    def addMoveToHistory(self, move):
        self.moveHistory.append(move)
    
    # TODO: Implement minimax here
    def chooseMove(self, board):
        for y in range(3):
            for x in range(3):
                if board.get((y, x)) == board.EMPTY_VALUE:
                    return y, x