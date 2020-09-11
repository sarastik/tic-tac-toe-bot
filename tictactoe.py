from team import HumanTeam, RobotTeam

class TicTacToe:

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

    def __init__(self, player1, player2):
        if not player1 or not player2:
            raise Exception("Not enough players :(")

        self.board = [[TicTacToe.EMPTY_VALUE] * 3 for _ in range(3)]
        self.availableMoves = [(i,j) for i in range(3) for j in range(3)]

        # Player state
        self.player1 = player1
        self.player2 = player2
        self.activePlayer = player1

    def getAvailableMoves(self):
        return self.availableMoves

    def get(self, coords):
        return self.board[coords[0]][coords[1]]

    def _setState_(self, board, availableMoves, activePlayer):
        self.board = board
        self.availableMoves = availableMoves
        self.activePlayer = activePlayer

    def simulateMove(self, coords):
        simulatedGame = TicTacToe(self.player1.getName(), self.player2.getName())
        simulatedGame._setState_(list(self.board), list(self.availableMoves), self.activePlayer)
        simulatedGame.make_move(coords)
        return simulatedGame

    def make_move(self, coords):
        if self._isMoveValid_(coords):
            self.board[coords[0]][coords[1]] = self.activePlayer.getName()
            self.availableMoves.remove((coords[0], coords[1]))
            self.activePlayer.addMoveToHistory((coords[0], coords[1]))
            self.activePlayer = self.player2 if self.activePlayer == self.player1 else self.player1
        else:
            print("That's an invalid move, please try again")

    def ask_for_move(self):
        row, col = self.activePlayer.chooseMove(self)
        print()
        return row, col

    def is_over(self):
        for row in TicTacToe.WIN_OPTIONS:
            if self.get(row[0]) == self.get(row[1]) == self.get(row[2]):
                team = self.get(row[0])
                if team != TicTacToe.EMPTY_VALUE:
                    return team

    def pretty_print(self):
        if self.activePlayer == self.player1:
            print("Your turn!")
        else:
            print("Opponent's turn")
        for row in self.board:
            print([item for item in row])
        print()

    def _isMoveValid_(self, coords):
        return False if self.get(coords) != self.EMPTY_VALUE else True

    def start_game(self):
        self.pretty_print()

        while True:
            coords = self.ask_for_move()
            self.make_move(coords)
            self.pretty_print()
            winner = self.is_over()

            if winner == self.player2.getName():
                print("You lost!")
                break
            elif winner == self.player1.getName():
                print("You won!")
                break

if __name__ == "__main__":
    print("***** Welcome to Tic Tac Toe, fool! *****")
    human_team_name = input("Do you want Xs or Os? (x/o): ").upper()
    while True:
        if human_team_name.upper() == "X" or human_team_name.upper() == "O":
            break
        else:
            human_team_name = input("Invalid team name, you must either select 'X' or 'O': ").upper()
    robot_team_name = "X" if human_team_name == "O" else "O"
    
    print("You've chosen {0}s".format(human_team_name))
    print()
    TicTacToe(HumanTeam(human_team_name), RobotTeam(robot_team_name)).start_game()

