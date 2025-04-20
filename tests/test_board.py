from tic_tac_toe_game.board import Board
from tic_tac_toe_game.token import Token
from tic_tac_toe_game.pos import Pos


class TestBoard():

    board = Board()

    def test_set_single_token(self):

        pos: Pos = Pos(1, 1)

        self.board.set_token(pos, Token.X)

        assert self.board.get_token(pos) == Token.X

    def test_multiple_token(self):
        pos1: Pos = Pos(1, 1)
        pos2: Pos = Pos(2, 2)
        pos3: Pos = Pos(3, 3)

        self.board.set_token(pos1, Token.X)
        self.board.set_token(pos2, Token.O)
        self.board.set_token(pos3, Token.X)

        assert self.board.get_token(pos1) == Token.X
        assert self.board.get_token(pos2) == Token.O
        assert self.board.get_token(pos3) == Token.X

    def test_pos_out_of_boundary(self):

        pos: Pos = Pos(10, 5)

        self.board.set_token(pos, Token.X)

        assert self.board.get_token(pos) == Token.X
