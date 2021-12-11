import unittest
import python_shogi.shogi as ps
import evaluator as evlt
import material_consts as mc
import alpha_beta as ab
import generators as gens
import math
from python_shogi.shogi import Consts

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


def king_zone(board: ps.Board,generator,piece, r):
    attackingPiecesCount = 0 
    valueOfAttacks = 0
    moves = generator(board)
    adjacent = find_adjacent(piece,r)
    individual_attackers = {}
    for move in moves:
        start = str(move)[:2]
        end = str(move)[2:]
        if (letter_convert(end) in adjacent):
            num_start = letter_convert(start)
            if (num_start in individual_attackers):
                individual_attackers[num_start] += 1
            else:
                individual_attackers[num_start] = 1
    attackingPiecesCount = len(individual_attackers)
    for attacker in individual_attackers:
        piece_type = str(board.piece_at(attacker))
        if (piece_type== "P"):
            type_value = mc.ON_BOARD_VALUES[ps.PAWN]
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "S"):
            type_value = mc.ON_BOARD_VALUES[ps.SILVER]
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "B"):
            type_value = mc.ON_BOARD_VALUES[ps.BISHOP]
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "L"):
            type_value = mc.ON_BOARD_VALUES[ps.LANCE]
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "G"):
            type_value = mc.ON_BOARD_VALUES[ps.GOLD]
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "R"):
            type_value = mc.ON_BOARD_VALUES[ps.ROOK]
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "N"):
            type_value = mc.ON_BOARD_VALUES[ps.KNIGHT]
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "P+"):
            type_value = mc.ON_BOARD_VALUES[ps.PROM_PAWN]
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "N+"):
            type_value = mc.ON_BOARD_VALUES[ps.PROM_KNIGHT]
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "S+"):
            type_value = mc.ON_BOARD_VALUES[ps.PROM_SILVER]
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "B+"):
            type_value = mc.ON_BOARD_VALUES[ps.PROM_BISHOP]
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "L+"):
            type_value = mc.ON_BOARD_VALUES[ps.PROM_LANCE]
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "R+"):
            type_value = mc.ON_BOARD_VALUES[ps.PROM_ROOK]
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
    print(attackingPiecesCount)
    print(valueOfAttacks)
    attackWeight = {1:0,2:50,3:75,4:88,5:94,6:97,7:99,
    }
    return valueOfAttacks * attackWeight[attackingPiecesCount] / 100


board = ps.Board("9/9/9/9/9/9/9/9/4K4 b - 1")
adj = find_adjacent(76,9)
adj.sort()
print(adj)
print()
expected_square_indexes = [x for x in range(81)]
print(expected_square_indexes)