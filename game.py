import python_shogi.shogi as ps
import evaluator as evlt
import material_consts as mc
import alpha_beta as ab
import generators as gens
import itertools
import random

def AI_game(board: ps.Board,player1,depth = 3, record_game = False):
    while(board.is_game_over() == False):
        if(player1 == False):
            moves = board.generate_legal_moves()
            length = sum(1 for _ in moves)
            moves = board.generate_legal_moves()
            index = random.randint(0,length - 1)
            move = next(itertools.islice(moves,index,None)).usi()
            board.push_usi(move)
            print("board after player 2 move: " + str(move))
            print(board)
            print()
            AI_game(board,True)
        else:
            gen = gens.generate_qualifying_moves
            move,_ = ab.finale_alpha_beta(board,depth,True,float('-inf'), float('inf'), gen, evlt.evaluator)
            print(move)
            board.push_usi(move)
            print("afer player 1 move: " + str(move))
            print(board)
            print()
            AI_game(board,False)
    if record_game:
        file_name = 'savegame'
        extension = '.txt'
        num = 0
        while(True):
            try: 
                with open(file_name + str(num) + extension) as fl:
                    num+=1
                print("File exists")
            except IOError:
                with open(file_name + str(num) + extension, 'w') as f:
                    for mv in board.move_stack:
                        f.write(mv.usi() + '\n')
                break
                

def main():
    board = ps.Board()
    AI_game(board,True,3,True)

if __name__ == "__main__":
    main()
