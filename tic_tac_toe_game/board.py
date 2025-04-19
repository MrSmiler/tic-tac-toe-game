from typing import List
from tic_tac_toe_game.token import Token
from tic_tac_toe_game.pos import Pos

class Board:
    tokens: List[Token]

    def __init__(self):

        self.tokens = [Token.NONE] * 9

    
    def set_token(self, pos: Pos, token: Token):
        pass

    def get_token(self, pos: Pos) -> Token:
        return Token.X
