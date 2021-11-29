import python_shogi.shogi as ps
import alpha_beta as ab
import material_consts as mc
import random

def alpha_beta(board : ps.Board,depth, maximizingplayer, alpha, beta):
    if (depth == 0 or board.is_game_over()):
        return [None,ab.evaluator(board)];
    elif(maximizingplayer):
        max_value = float('-inf');
        best_move = "";
        moves = board.generate_legal_moves();
        for move in moves:
            current_move = move.usi();
            board.push_usi(current_move);
            eval = alpha_beta(board, depth-1, False,alpha,beta);
            if (eval[1] > max_value):
                best_move = current_move;
                max_value = eval[1];            
            board.pop();
            alpha = max(alpha,eval[1]);
            if beta <= alpha:
                break;

        return [best_move, max_value];
    else:
        min_value = float('inf');
        best_move = "";
        moves = board.generate_legal_moves();
        for move in moves:
            current_move = move.usi();
            board.push_usi(current_move);
            eval = alpha_beta(board, depth-1,True,alpha,beta);
            if (eval[1] < min_value):
                min_value = eval[1];
                best_move = current_move;
            board.pop();
            beta = min(beta,eval[1])
            if beta <= alpha:
                break;
        return [best_move,min_value];



board = ps.Board();
print(alpha_beta(board,3,True, float('-inf'), float('inf')));