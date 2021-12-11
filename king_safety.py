import unittest
import python_shogi.shogi as ps
import evaluator as evlt
import material_consts as mc
import alpha_beta as ab
import generators as gens
import math

def find_adjacent(piece_position,r):
    adjacent = []
    level_zero = []
    for i in range(1, r + 1):
        right = piece_position + (i * 1)
        left = piece_position - (i * 1)
        if (right >= 0 and right <= 80):
            level_zero.append(right)
        if (left >= 0 and left <= 80):
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

def number_convert(num):
    my_dict = {
    0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f",6:"g",7:"h",8: "i"
    }
    letter = my_dict[math.floor(num / 9)] 
    number = abs((num % 9) - 9)
    return str(number) + letter
    

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
            type_value = 1.00
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "S"):
            type_value = 6.40
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "B"):
            type_value = 8.90
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "L"):
            type_value = 4.30
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "G"):
            type_value = 6.90
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "R"):
            type_value = 10.40
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "N"):
            type_value = 4.50
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "P+"):
            type_value = 4.20
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "N+"):
            type_value = 6.40
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "S+"):
            type_value = 6.70
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "B+"):
            type_value = 11.50
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "L+"):
            type_value = 6.30
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
        if (piece_type== "R+"):
            type_value = 13.00
            over_all_value = type_value * individual_attackers[attacker]
            valueOfAttacks += over_all_value
    print(attackingPiecesCount)
    print(valueOfAttacks)
    attackWeight = {1:0,2:50,3:75,4:88,5:94,6:97,7:99,
    }
    return valueOfAttacks * attackWeight[attackingPiecesCount] / 100

board = ps.Board("lnsgkgsnl/1r5b1/pp1pppppp/2p6/6N2/2L6/PPPPPPPPP/1B5R1/LNSGKGS2 b - 1")
print(king_zone(board,gens.generate_attacking_moves,4,2))

