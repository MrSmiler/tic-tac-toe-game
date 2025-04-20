from typing import List
from tic_tac_toe_game.token import Token
from tic_tac_toe_game.pos import Pos
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Board:
    _board_rows: ClassVar[int] = 3
    _board_cols: ClassVar[int] = 3

    tokens: List[Token]

    def __init__(self):
        self.tokens = [Token.NONE] * 9
    
    def calc_index(self, pos: Pos) -> int:
        array_pos_x = pos.x - 1
        array_pos_y = pos.y - 1
        index: int = (array_pos_x * self._board_rows) + array_pos_y
        return index

    def set_token(self, pos: Pos, token: Token):
        index: int = self.calc_index(pos)
        self.tokens[index] = token

    def get_token(self, pos: Pos) -> Token:
        index: int = self.calc_index(pos)
        return self.tokens[index]
