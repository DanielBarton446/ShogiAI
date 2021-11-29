import python_shogi.shogi as ps
import evaluator as evlt
import material_consts as mc
import random

def alpha_beta(board : ps.Board,depth, maximizingplayer, alpha, beta):
    if (depth == 0 or board.is_game_over()):
        return [None,evlt.evaluator(board)]
    elif(maximizingplayer):
        max_value = float('-inf')
        best_move = ""
        moves = board.generate_legal_moves()
        for move in moves:
            current_move = move.usi()
            board.push_usi(current_move)
            evl = alpha_beta(board, depth-1, False,alpha,beta)
            if (evl[1] > max_value):
                best_move = current_move
                max_value = evl[1]            
            board.pop()
            alpha = max(alpha,evl[1])
            if beta <= alpha:
                break

        return [best_move, max_value]
    else:
        min_value = float('inf')
        best_move = ""
        moves = board.generate_legal_moves()
        for move in moves:
            current_move = move.usi()
            board.push_usi(current_move)
            evl = alpha_beta(board, depth-1,True,alpha,beta)
            if (evl[1] < min_value):
                min_value = evl[1]
                best_move = current_move
            board.pop()
            beta = min(beta,evl[1])
            if beta <= alpha:
                break
        return [best_move,min_value]
