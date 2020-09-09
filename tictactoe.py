
class TicTacToe():

    EMPTY_VALUE = "_"
    TEAMS = ["X", "O"]
    WIN_OPTIONS = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    def __init__(self):
        self.board = [[TicTacToe.EMPTY_VALUE] * 3 for _ in range(3)]

    def get(self, coords):
        return self.board[coords[0]][coords[1]]

    def make_move(self, value, coords):
        self.board[coords[0]][coords[1]] = value
        self.pretty_print()

    def ask_for_move(self, team):
        row = input("Row? (1/2/3): ")
        col = input("Column? (1/2/3): ")
        print()
        self.make_move(team, (int(row)-1, int(col)-1))

    def robot_move(self, team):
        print("The opponent is moving...")
        for y in range(3):
            for x in range(3):
                if self.get((y, x)) == TicTacToe.EMPTY_VALUE:
                    self.make_move(team, (y, x))
                    return

    def is_over(self):
        for row in TicTacToe.WIN_OPTIONS:
            if self.get(row[0]) == self.get(row[1]) == self.get(row[2]):
                team = self.get(row[0])
                if team != TicTacToe.EMPTY_VALUE:
                    return team

    def pretty_print(self):
        for row in self.board:
            print([item.upper() for item in row])
        print()

    def main_loop(self):
        print("***** Welcome to Tic Tac Toe, fool! *****")
        human_team = input("Do you want Xs or Os? (x/o): ")
        robot_team = "X" if human_team == "o" else "O"
        print("You've chosen {0}s".format(human_team))
        print()
        self.pretty_print()

        while True:
            self.ask_for_move(human_team)
            self.robot_move(robot_team)
            winner = self.is_over()

            if winner == robot_team:
                print("You lost!")
                return
            elif winner == human_team:
                print("You won!")
                return


#Test
testBoard = TicTacToe()
testBoard.main_loop()
# testBoard.pretty_print()
# testBoard.make_move('X', (0, 1))
# testBoard.pretty_print()
