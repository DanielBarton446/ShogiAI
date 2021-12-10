import unittest
import python_shogi.shogi as ps
import evaluator as evlt
import material_consts as mc
import alpha_beta as ab
import generators as gens
import math

def detect_edge_case(letter_position):
    if(int(letter_position[0]) == 1):
        return "right_edge_case"
    elif(int(letter_position[0]) == 9):
        return "left_edge_case"
    else:
        return "not_edge_case"
    
def find_letter_position(position):
    my_dict = {
        0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i"
    }
    letter_value = my_dict[math.floor(position/9)]
    number_value = (position % 9) + 1
    return (str(number_value) + letter_value)



def find_adjacent(position):
    edge_case = detect_edge_case(find_letter_position(position))
    right = position - 1; left = position + 1; front = position - 9; back = position + 9
    top_right = position - 9 - 1; top_left = position - 9 + 1
    bottom_right = position + 9 - 1; bottom_left = position + 9 + 1
    number_array = []
    print(edge_case)
    if (edge_case == "left_edge_case"):
        number_positions = [right,front,back,top_right,bottom_right,]
    elif (edge_case == "right_edge_case"):
        number_positions = [left,front,back,top_left,bottom_left]
    else:
        number_positions = [right,left,front,back,top_right,top_left,bottom_right,bottom_left]
    letter_positions = []
    for number_position in number_positions:
        try:
            letter_position = find_letter_position(number_position)
            letter_positions.append(letter_position)
        except:
            pass
    return letter_positions
        
board = ps.Board()
print(board)
print(find_adjacent(0))
    
    