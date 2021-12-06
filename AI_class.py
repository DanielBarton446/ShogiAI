import python_shogi.shogi as ps
import evaluator as evlt
import material_consts as mc
import alpha_beta as ab
import generators as gens
import itertools
import random

def AI_game(board: ps.Board,player1,depth = 3):
    while(board.is_game_over() == False):
        if(player1 == False):
            moves = board.generate_legal_moves()
            length = sum(1 for _ in moves)
            moves = board.generate_legal_moves()
            index = random.randint(0,length - 1)
            move = next(itertools.islice(moves,index,None)).usi();
            board.push_usi(move)
            print("board after player 2 move: " + str(move))
            print(board)
            print()
            AI_game(board,True)
        else:
            move = ab.finale_alpha_beta(board,depth,True,float('-inf'), float('inf'),gens.generate_legal_attacking_moves, evlt.count_material)[0]
            board.push_usi(move)
            print("afer player 1 move: " + str(move))
            print(board)
            print()
            AI_game(board,False)

board = ps.Board()
AI_game(board,True,2)