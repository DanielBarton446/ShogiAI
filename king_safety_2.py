import unittest
import python_shogi.shogi as ps
import evaluator as evlt
import material_consts as mc
import alpha_beta as ab
import generators as gens
import math


def shogi_notation(positions):
    shogi_array = []
    my_dict = {
        "0": "a", "1": "b", "2": "c", "3": "d", "4": "e", "5": "f", "6": "g", "7": "h", "8": "i"
    }
    for st in positions:
        number = str(int(st[1]) + 1)
        letter = my_dict[st[0]]
        shogi_array.append(number + letter)
    return shogi_array
    

def find_adjacent(piece_position,r):
    row = math.floor(piece_position / 9)
    column = piece_position % 9
    adjacent = []
    for i in range(1,r + 1):    
        forward =  column + (1 * i); backward = column - (1 * i); r = row + ( 1 * i); l = row - (1 * i) 
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
    return shogi_notation(adjacent)

print(find_adjacent(4,4))