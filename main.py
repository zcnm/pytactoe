import sys
from tictactoe import TicTacToe
import agents.agents


def play(players, game):
    while True:
        for player in players:
            print(game.board)
            print("Player {}'s turn.".format(player.symbol))
            board = game.board.getBoard()
            x, y = player.move(board)
            if not game.makeMove(player.symbol, x, y):
                game.makeRandomMove(player.symbol)

            if game.board.isGameOver():
                print(game.board)
                return


def main():
    players = [agents.agents.NegaMaxAgent("X", "O"), agents.agents.NegaMaxAgent("O", "X")]
    game = TicTacToe(3)
    play(players, game)


if __name__ == "__main__":
    main()
