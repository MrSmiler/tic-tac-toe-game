from tic_tac_toe_game.board import Board
from tic_tac_toe_game.token import Token
from tic_tac_toe_game.pos import Pos

def test_set_single_token():

    board = Board()
    
    pos: Pos = Pos(1, 1)

    board.set_token(pos, Token.X)

    assert board.get_token(pos) == Token.X

def test_set_single_token():

    pass
