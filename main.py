import numpy


class ConnectFour:
    def __init__(self):
        self._field = self.createField()
        self._winner = False

    def coreLoop(self):
        self.renderField()
        while True:
            self.getMove(1)
            self.renderField()
            if self._winner:
                print(f"Player {self._winner} wins the game.")
                return
            self.getMove(2)
            self.renderField()
            if self._winner:
                print(f"Player {self._winner} wins the game.")
                return

    def renderField(self):
        print(self._field)

    def getMove(self, player: int()):
        while True:
            move = int(input(f"Player {player} Move:"))
            if move not in range(1, 8):
                print("Illegal Move, press 1 through 7")
                continue
            if self._throwStone(move-1, player):
                return
            else:
                print(f"Illegal Move, row {move} is full. Choose another row.")

    def _throwStone(self, column: int(), player: int()):
        if self._field[0, column] != 0:
            return False
        for i in range(6):
            if self._field[i, column] == 0:
                continue
            elif self._field[i, column] > 0:
                self._field[i - 1, column] = player
                self._checkVictory(i - 1, column)
                return True
        self._field[5, column] = player
        self._checkVictory(5, column)
        return True

    def _checkVictory(self, lastmove: int(), column):
        player = self._field[lastmove, column]
        self._countToFour(self._field[:, column], player)
        self._countToFour(self._field[lastmove, :], player)
        self._countAllDiagonals(player)

    def _countAllDiagonals(self, player):
        a=self._field
        diags = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
        diags.extend(a.diagonal(i) for i in range(a.shape[1] - 1, -a.shape[0], -1))
        for n in diags:
            if len(n) > 3:
                self._countToFour(n, player)

    def _countToFour(self, array, player):
        count = 0
        for i in array:
            if i == player:
                count+=1
                if count == 4:
                    self._winner=player
            if i != player:
                count=0

    def createField(self):
        return numpy.zeros((6,7))

    def createPlayers(self):
        pass
        # TODO: Every player has a colour.
        # TODO: Every player has 21 pieces of their colour.
        # TODO: There are two players.


if __name__ == '__main__':
    game = ConnectFour()
    game.coreLoop()

