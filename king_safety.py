import python_shogi.shogi as ps
from python_shogi.shogi import Consts
import evaluator as evlt
import math

levels  = {
    1: (8,0),
    2: (17,9),
    3: (26,18),
    4: (35,27),
    5: (44,36),
    6: (53,45),
    7: (62,54),
    8: (71,63),
    9: (80,72)
}

def find_level(num):
    low_range = 0
    high_range = 8
    for i in range(1,10):
        if (num >= low_range and num <= high_range):
            return i
        else:
            low_range += 9
            high_range += 9
            
def on_level(num,level):
    if (find_level(num) == level):
        return True
    else:
        return False

    
def find_adjacent(piece_position,r):
    adjacent = []
    level_zero = []
    for i in range(1, r + 1):
        right = piece_position - (i * 1)
        left = piece_position + (i * 1)
        if (on_level(right,find_level(piece_position))):
            level_zero.append(right)
        if (on_level(left,find_level(piece_position))):
            level_zero.append(left)
    level_zero.append(piece_position)
    adjacent += level_zero
    for i in range(1, r + 1):
        new_level = []
        for k in range(len(level_zero)):
            current_piece = level_zero[k] + (i * 9)
            if (current_piece >= 0 and current_piece <= 80):
                new_level.append(current_piece)
        adjacent += new_level
    for i in range(1, r + 1):
        new_level = []
        for k in range(len(level_zero)):
            current_piece = level_zero[k] - (i * 9)
            if (current_piece >= 0 and current_piece <= 80):
                new_level.append(current_piece)
        adjacent += new_level
    adjacent.remove(piece_position)
    return adjacent
            

def letter_convert(st):
    my_dict = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6,"h":7, "i":8
    }
    letter = my_dict[st[1]] * 9
    number = abs(int(st[0]) - 9)
    value = letter + number
    return value

def king_safety(board : ps.Board, radius):
    valueOfAttacks = 0

    attacking_moves = board.legal_moves

    adjacent_squares = find_adjacent(board.king_squares[not board.turn], radius)

    attacking_from_squares = set()
    
    attack_value = {
        Consts.PAWN  : 5, Consts.LANCE: 20, Consts.KNIGHT: 20,
        Consts.SILVER: 40, Consts.GOLD : 40, 
        Consts.BISHOP: 80, Consts.ROOK : 80,

        # Promoted Pieces
        # Note -- promoted gold does not exist.

        Consts.PROM_PAWN  : 40, Consts.PROM_LANCE: 40, 
        Consts.PROM_KNIGHT: 40, 
        Consts.PROM_SILVER: 40, 
        Consts.PROM_BISHOP: 90, Consts.PROM_ROOK: 90
        }

    attackWeight = {
                    0 : 0 , 1 : 0 , 2 : 50, 3 : 75, 
                    4 : 88, 5 : 94, 6 : 97, 7 : 99,
                   }

    for mv in attacking_moves:
        # For some reason, mv.from_square can be None.
        if mv.from_square is not None and \
           mv.to_square in adjacent_squares and \
           board.piece_at(mv.from_square).piece_type is not ps.KING:
            # for each to_square attacked, we add to our valueOfAttacks
            valueOfAttacks += attack_value[board.piece_at(mv.from_square).piece_type]
            attacking_from_squares.add(mv.from_square)

    if len(attacking_from_squares) > 7:
        return round(valueOfAttacks / 100 * attackWeight[7] / 100, evlt.sig_figs)
    else:
        return round(valueOfAttacks / 100 * attackWeight[len(attacking_from_squares)] / 100, evlt.sig_figs)
