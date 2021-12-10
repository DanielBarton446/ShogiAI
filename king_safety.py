import unittest
import python_shogi.shogi as ps
import evaluator as evlt
import material_consts as mc
import alpha_beta as ab
import generators as gens
import math


def get_squares(positions):
    shogi_array = []
    for st in positions:
        shogi_array.append(int(st[0]) * 9 + int(st[1]))
    return shogi_array
    

def find_adjacent(piece_position,r):
    row = math.floor(piece_position / 9)
    column = piece_position % 9
    adjacent = []
    for i in range(1,r + 1):    
        forward =  column + (1 * i) 
        backward = column - (1 * i) 
        r = row + ( 1 * i) 
        l = row - (1 * i) 
        if (r >= 0 and r < 9):
            adjacent.append(str(r) + str(column))
        if (l >= 0 and l < 9):
            adjacent.append(str(l) + str(column))
        if (forward >= 0 and forward < 9):
            adjacent.append(str(row) + str(forward))  
        if (backward >= 0 and backward < 9):
            adjacent.append(str(row) + str(backward))       
        if(r >= 0 and r < 9 and forward >= 0 and forward < 9):
            adjacent.append(str(r) + str(forward)) 
        if (l >= 0 and l < 9 and forward >= 0 and forward < 9):
            adjacent.append(str(l) + str(forward)) 
        if (r >= 0 and r < 9 and backward >= 0 and backward):
            adjacent.append(str(r) + str(backward))
        if (l >= 0 and l < 9 and backward >= 0 and backward < 9):
            adjacent.append(str(l) + str(backward))
    return get_squares(adjacent)

